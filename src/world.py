# Notes:
# It could be useful to make a seperate Point class for added clarity, orginization
# Eventually update World so that it is initiated with a neighborhood type,
# set of rules and a set of graphics for values
# differentiate Moore getActivePoints and von Neuman getActivePoints
# Save and load functions only save points, not rules or size

# (DONE) getNumNeighbors needs to be updated for different states

# (DONE) processing speed could be significantly sped up if getActivePoints
# only checked in the vicinity of the last set of active points

# (DONE) above method reuqires that active_points be updated when points are spawned after initialization
# 	(namely spawn_points)

# creating a blank grid every single iteration is extremely innefficient
#		potential fix: create a list of points to update along with their
#		new values, clear grid, set grid to values

# __init__ with points only spawns state 1s


class World:
    # Empty world
    def __init__(self, name, w, h, states, rules, graphics):
        grid = World.make_blank_grid(w, h)
        self.name = name
        self.grid = grid
        self.w = w
        self.h = h
        self.rules = rules
        self.states = states
        self.graphics = graphics
        self.active_points = []

    # World with living cells at points
    def __init__(self, name, w, h, states, rules, graphics, points):
        grid = World.make_blank_grid(w, h)
        self.grid = grid
        self.name = name
        self.w = w
        self.h = h
        self.rules = rules
        self.states = states
        self.graphics = graphics
        self.active_points = []
        for value in points:
            for point in points[value]:
                grid[point[0]][point[1]] = value
                self.active_points.append(point)
        self.update_active_points()

    def make_blank_grid(w, h):
        grid = []
        for x in range(w):
            row = []
            for y in range(h):
                row.append(0)
            grid.append(row)
        return grid

    def update_active_points(self):
        live_points = []
        for point in self.active_points:
            if self.get_point_value(point) != 0:
                live_points.append(point)
        self.active_points = []
        self.add_active_points(live_points)

    def add_active_points(self, points):
        for point in points:
            x, y = point
            for subx in range(-1, 2):
                for suby in range(-1, 2):
                    active_point = ((x + subx) % self.w, (y + suby) % self.h)
                    if active_point not in self.active_points:
                        self.active_points.append(active_point)

    def get_grid(self):
        return self.grid

    def display(self, x1, x2, y1, y2, iter):
        out = ""
        # graphics = {0: " ", 1: "#"}
        for y in range(y2 - 1, y1 - 1, -1):
            for x in range(x1, x2):
                out += str(self.graphics[self.grid[x][y]]) + " "
            out += "\n"
        out += "Iteration: " + str(iter)
        print(out)

    def get_neighbors(self, point):
        x = point[0]
        y = point[1]
        neighbors = {}
        for n in range(0, self.states):
            neighbors[n] = 0
        for subx in range(-1, 2):
            for suby in range(-1, 2):
                current = ((x + subx) % self.w, (y + suby) % self.h)
                if (subx != 0 or suby != 0):
                    neighbors[self.grid[current[0]][current[1]]] += 1
        return neighbors

    def update_point_value(self, point, neighbors):
        status = self.get_point_value(point)
        for rule in self.rules:
            if rule.check(status, neighbors):
                return rule.result
        return status

    def get_point_value(self, point):
        return self.grid[point[0]][point[1]]

    def update_grid(self):
        # grid_new = World.make_blank_grid(self.w, self.h)
        point_values = {}
        self.update_active_points()
        for point in self.active_points:
            point_values[point] = self.update_point_value(point, self.get_neighbors(point))
        self.spawn_points(self.active_points, 0)
        for point in point_values:
            self.grid[point[0]][point[1]] = point_values[point]

    # rename to set_points later
    def spawn_points(self, points, value):
        for point in points:
            self.grid[point[0]][point[1]] = value
        if value != 0:
            self.add_active_points(points)

    def save_world(self, filename):
        f = open(filename, "w+")
        f.write(self.name + "\n")
        f.write(self.rules + "\n")
        for x in range(0, self.w):
            for y in range(0, self.h):
                if self.grid[x][y] == 1:
                    f.write(str(x) + " " + str(y) + "\n")

    def load_world(self, filename):
        points = []
        f = open(filename, "r")
        lines = f.split("\n")
        self.name = lines[0]
        self.rules = lines[1]
        for n in range(2, len(lines)):
            x, y = line.split(" ")
            points.append((x, y))
        self.grid = World.make_blank_grid(self.w, self.h)
        self.spawn_points(points)
