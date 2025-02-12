import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Pygame Window")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Game logic here
    
    # Drawing
    screen.fill(WHITE)  # Fill screen with white background
    
    # Add your drawing code here
    # After screen.fill(WHITE):
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)  # 60 FPS

# Quit Pygame
pygame.quit()