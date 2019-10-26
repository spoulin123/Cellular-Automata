# Renderer options
# Window
window_title = "Cellular Automata"
window_width = 1000
window_height = 1000
# Grid
grid_start_x = 50
grid_start_y = 50
grid_length_x = 900
grid_length_y = 900
grid_line_color = (95, 95, 95)  # 5f5f5f
grid_line_width = 1
border_line_color = (150, 150, 150)
border_line_width = 2
block_width = 9


# Renderer class
class Renderer:

    # Class info
    __author__ = "Hykilpikonna"
    __version__ = "0.0.0 (2019-10-26)"

    # Constructor
    def __init__(self, pygame):
        self.pygame = pygame

        # Initialize pygame
        self.pygame.display.set_caption(window_title)
        self.window = pygame.display.set_mode((window_width, window_height))

    # Draw grid lines
    def draw_grid(self):

        # Draw border lines
        self.pygame.draw.rect(self.window, border_line_color,
                              (grid_start_x - border_line_width, grid_start_y, border_line_width, grid_length_y))

        # Loop through all x values in the grid
        for x in range(grid_start_x, grid_start_x + grid_length_x):

            # Every gap between blocks
            if x % (block_width + grid_line_width) == 0:

                # Calculate box position
                position = (x + block_width, grid_start_y, grid_line_width, grid_length_x)

                # Draw a line
                self.pygame.draw.rect(self.window, grid_line_color, position)

        # Loop through all y values in the grid
        for y in range(grid_start_y, grid_start_y + grid_length_y):

            # Every gap between blocks
            if y % (block_width + grid_line_width) == 0:

                # Calculate box position
                position = (grid_start_x, y + block_width, grid_length_y, grid_line_width)

                # Draw a line
                self.pygame.draw.rect(self.window, grid_line_color, position)




