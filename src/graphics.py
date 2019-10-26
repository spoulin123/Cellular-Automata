import pygame
from renderer import Renderer

# Initialize pygame
pygame.init()

# Create renderer
renderer = Renderer(pygame)

# Render initial stuff
renderer.draw_grid()

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
