import pygame
import sys
import time
from SudokuBoard import *

# Global variables for visualization
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Keep track of screen and font to avoid reinitializing
screen = None
font = None


def draw_button(text, x, y, width, height, inactive_color, active_color):
    """Draw a clickable button and return True if clicked"""
    global screen, font

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Check if mouse is over button
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    # Add text to button
    button_text = font.render(text, True, BLACK)
    text_rect = button_text.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(button_text, text_rect)
    return False


def display_interactive_board(board: SudokuBoard, solve_function):
    """Display the board with a Solve button"""
    global screen, font

    if screen is None:
        WIDTH, HEIGHT, CELL_SIZE = initialize_gui(board)
    else:
        WIDTH, HEIGHT = screen.get_size()
        CELL_SIZE = WIDTH // board.dims

    # Button properties
    button_width, button_height = 200, 50
    button_x = (WIDTH - button_width) // 2
    button_y = HEIGHT - button_height - 10

    solving = False

    # Main loop
    running = True
    while running and not solving:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        screen.fill(WHITE)

        # Draw grid
        for i in range(board.dims + 1):
            line_width = 3 if i % board.cell_size == 0 else 1
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), line_width)

        # Draw numbers
        for row in range(board.dims):
            for col in range(board.dims):
                value = board.table[row][col]
                if value != " ":
                    color = BLUE if (row, col) in board.fixed_positions else BLACK
                    text = font.render(str(value), True, color)
                    screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 3,
                                       row * CELL_SIZE + CELL_SIZE // 4))

        # Draw solve button and check if clicked
        if draw_button("Solve Puzzle", button_x, button_y, button_width, button_height, GREEN, (100, 255, 100)):
            solving = True

        pygame.display.flip()

    # If solve button was clicked, start the solving algorithm
    if solving:
        return solve_function(board)

    return False


def initialize_gui(board):
    global screen, font
    # Settings
    WIDTH, HEIGHT = 540, 600
    CELL_SIZE = WIDTH // board.dims
    FONT_SIZE = CELL_SIZE // 2

    # Set up display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Solver")
    font = pygame.font.SysFont(None, FONT_SIZE)
    return WIDTH, HEIGHT, CELL_SIZE


def update_board_display(board, current_pos=None, try_value=None, delay=0.01):
    global screen, font

    if screen is None:
        WIDTH, HEIGHT, CELL_SIZE = initialize_gui(board)
    else:
        WIDTH, HEIGHT = screen.get_size()
        CELL_SIZE = WIDTH // board.dims

    # Handle events to prevent freezing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # Draw grid
    for i in range(board.dims + 1):
        line_width = 3 if i % board.cell_size == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), line_width)

    # Draw numbers
    for row in range(board.dims):
        for col in range(board.dims):
            value = board.table[row][col]
            if value != " ":
                # Determine cell color
                color = BLUE if (row, col) in board.fixed_positions else BLACK

                # Highlight current position
                if current_pos and (row, col) == current_pos:
                    # Draw a yellow background for the current cell
                    pygame.draw.rect(screen, YELLOW,
                                     (col * CELL_SIZE + 1, row * CELL_SIZE + 1,
                                      CELL_SIZE - 2, CELL_SIZE - 2))
                    color = RED  # Make the number red for visibility

                text = font.render(str(value), True, color)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 3,
                                   row * CELL_SIZE + CELL_SIZE // 4))

    # Display status and info
    remaining = board.get_open_positions_num()
    status_text = f"Solving... Open cells: {remaining}"
    if try_value:
        status_text += f" | Trying: {try_value}"
    text = font.render(status_text, True, BLACK)
    screen.blit(text, (10, WIDTH + 20))

    pygame.display.flip()
    time.sleep(delay)  # Add delay to visualize the process


def display_board_gui(board: SudokuBoard, solution=False):
    global screen, font

    if screen is None:
        initialize_gui(board)

    # Main loop for final display
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Draw grid
        WIDTH, HEIGHT = screen.get_size()
        CELL_SIZE = WIDTH // board.dims

        for i in range(board.dims + 1):
            line_width = 3 if i % board.cell_size == 0 else 1
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), line_width)

        # Draw numbers
        for row in range(board.dims):
            for col in range(board.dims):
                value = board.table[row][col]
                if value != " ":
                    color = BLUE if (row, col) in board.fixed_positions else BLACK
                    if solution and (row, col) not in board.fixed_positions:
                        color = GREEN
                    text = font.render(str(value), True, color)
                    screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 3,
                                       row * CELL_SIZE + CELL_SIZE // 4))

        # Display status
        status_text = "Solved!" if solution else f"Open cells: {board.get_open_positions_num()}"
        text = font.render(status_text, True, BLACK)
        screen.blit(text, (10, WIDTH + 20))

        pygame.display.flip()

    pygame.quit()