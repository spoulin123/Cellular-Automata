import time

from presets import ConwayPatterns
from rules import Rule, Condition
from world import World

rule1 = Rule(1, [Condition(1, "LESS", 2)], 0)
rule2 = Rule(1, [Condition(1, "GREATER_EQUAL", 2), Condition(1, "LESS", 4)], 1)
rule3 = Rule(1, [Condition(1, "GREATER_EQUAL", 4)], 0)
rule4 = Rule(0, [Condition(1, "EQUAL", 3)], 1)

conway_rules = [rule1, rule2, rule3, rule4]

populatedWorld = World("Test", 2000, 2000, 2, conway_rules, {0: " ", 1: "#"}, {})
populatedWorld.spawn_points(ConwayPatterns.r_pentomino((10, 10)), 1)
print(populatedWorld.active_points)

frameDelay = .1

# Runtime Variables
frameCount = 1

input()

while True:
    # Clear screen
    print("\033[H\033[J")
    # Display the current grid
    populatedWorld.display(0, 50, 0, 50, frameCount)
    # Increment frame count
    frameCount += 1
    # Update grid
    populatedWorld.update_grid()
    # Wait until the next update
    time.sleep(frameDelay)
