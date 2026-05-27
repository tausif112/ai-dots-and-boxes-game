import pygame

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 480

# Colors
LINE_COLOR = (50, 50, 50)
DOT_COLOR = (255, 50, 50)
BACKGROUND = (240, 230, 200)
PLAYER_COLOR = (100, 200, 255)
AI_COLOR = (255, 150, 100)
TEXT_COLOR = (20, 20, 20)

# Sizes
DOT_RADIUS = 10
LINE_WIDTH = 5
GAP = 120

# Grid
ROWS, COLS = 3, 3

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots and Boxes")

# Fonts
font = pygame.font.SysFont("Arial", 22)
big_font = pygame.font.SysFont("Arial", 38, bold=True)