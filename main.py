from world import World
from rules import Rule, Condition
from presets import ConwayPatterns
import time
import console
console.clear()


rule1 = Rule(1, [Condition(1, "LESS", 2)], 0)			
rule2 = Rule(1, [Condition(1, "GREATER_EQUAL", 2), Condition(1, "LESS", 4)], 1)
rule3 = Rule(1, [Condition(1, "GREATER_EQUAL", 4)], 0)
rule4 = Rule(0, [Condition(1, "EQUAL", 3)], 1)	

conway_rules = [rule1, rule2, rule3, rule4]

populatedWorld = World("Test", 2000, 2000, 2, conway_rules, {0: " ", 1: "#"}, {})
populatedWorld.spawn_points(ConwayPatterns.r_pentomino((10, 10)), 1)
print(populatedWorld.active_points)



i = 0
populatedWorld.display(0, 50, 0, 50, i) 

input()

while True:
	i += 1
	populatedWorld.update_grid()
	console.clear()
	populatedWorld.display(0, 50, 0, 50, i)
	#time.sleep(.1)
