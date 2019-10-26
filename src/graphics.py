import pygame
from renderer import Renderer
from rules import Rule, Condition
from world import World
from presets import ConwayPatterns

# Initialize pygame
pygame.init()

# Create renderer
renderer = Renderer(pygame)

# Render initial stuff
renderer.drawGrid()

# Define rules
conway_rules = [Rule(1, [Condition(1, "LESS", 2)], 0),
                Rule(1, [Condition(1, "GREATER_EQUAL", 2), Condition(1, "LESS", 4)], 1),
                Rule(1, [Condition(1, "GREATER_EQUAL", 4)], 0),
                Rule(0, [Condition(1, "EQUAL", 3)], 1)]

# Create world
world = World("Test", 2000, 2000, 2, conway_rules, {0: " ", 1: "#"}, {})
world.spawn_points(ConwayPatterns.r_pentomino((10, 10)), 1)
print(world.active_points)

# Frame operations
running = True
while running:
    # Delay
    pygame.time.delay(10)

    # Loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update world
    world.update_grid()
    renderer.drawWorld(world)

    # Update display
    pygame.display.update()

# Quit
pygame.quit()
