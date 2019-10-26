# Renderer options
grid_line_color = (200, 200, 200)
grid_line_width = 1
block_width = 50


# Renderer class
class Renderer:

    # Class info
    __author__ = "Hykilpikonna"
    __version__ = "0.0.0 (2019-10-26)"

    # Constructor
    def __init__(self, pygame, window):
        self.pygame = pygame
        self.window = window

    # Draw grid lines
    def draw_lines(self):

        # Loop through all x values in the grid
        for x in range(0, self.window.get_width()):

            # Every gap between blocks
            if x % block_width == 0:
                print('x = ' + str(x))

                # Draw a line
                self.pygame.draw.rect(self.window, grid_line_color, (x, 0, grid_line_width, self.window.get_height()))




