import pygame
from renderer import Renderer

# Initialize pygame
pygame.init()

# Create pygame window
window = pygame.display.set_mode((1000, 1000))

# Create renderer
renderer = Renderer(pygame, window)

# Frame operations
running = True
while running:
    # Delay
    pygame.time.delay(10)

    # Loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.update()

# Quit
pygame.quit()
