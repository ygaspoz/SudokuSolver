import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 1. Read and preprocess image
image = cv2.imread("img.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 2. Find the largest contour (the Sudoku grid)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = max(contours, key=cv2.contourArea)
peri = cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

# 3. Warp the grid to a square
if len(approx) == 4:
    pts = approx.reshape(4, 2)
    # Order points: top-left, top-right, bottom-right, bottom-left
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    (tl, tr, br, bl) = rect
    width = height = 450
    dst = np.array([[0,0],[width-1,0],[width-1,height-1],[0,height-1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(image, M, (width, height))
else:
    raise Exception("Could not find Sudoku grid.")

# 4. Divide into 9x9 cells and extract digits
cell_w, cell_h = width // 9, height // 9
digits = []
for y in range(9):
    row = []
    for x in range(9):
        x1, y1 = x * cell_w, y * cell_h
        cell = warp[y1:y1+cell_h, x1:x1+cell_w]
        cell_gray = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
        # Adaptive thresholding for better contrast
        cell_thresh = cv2.adaptiveThreshold(cell_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY_INV, 11, 2)
        # Remove borders
        margin = 8
        cell_thresh = cell_thresh[margin:-margin, margin:-margin]
        # Resize for better OCR
        cell_resized = cv2.resize(cell_thresh, (64, 64), interpolation=cv2.INTER_LINEAR)
        # Optional: Morphological operations to enhance digit
        kernel = np.ones((2,2), np.uint8)
        cell_processed = cv2.dilate(cell_resized, kernel, iterations=1)
        cv2.imshow("Sudoku", cell_processed)
        cv2.waitKey(0)

        # OCR
        text = pytesseract.image_to_string(cell_processed, config="--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789")
        digit = text.strip()
        row.append(digit if digit.isdigit() else ' ')
    digits.append(row)

for y in range(9):
    for x in range(9):
        digit = digits[y][x]
        if digit != ' ':
            # Calculate center of the cell
            center_x = x * cell_w + cell_w // 2
            center_y = y * cell_h + cell_h // 2
            cv2.putText(
                warp,
                str(digit),
                (center_x - 10, center_y + 10),  # Offset for better centering
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 0, 255),
                2,
                cv2.LINE_AA
            )

cv2.imshow('Detected Digits', warp)
cv2.waitKey(0)
cv2.destroyAllWindows()