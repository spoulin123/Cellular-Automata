# Renderer options
# Window
WINDOW_TITLE = "Cellular Automata"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
# Grid
GRID_START_X = 50
GRID_START_Y = 50
GRID_LENGTH_X = 900
GRID_LENGTH_Y = 900
GRID_LINE_COLOR = (95, 95, 95)  # 5f5f5f
GRID_LINE_WIDTH = 1
BORDER_COLOR = (150, 150, 150)
BORDER_WIDTH = 2
BLOCK_WIDTH = 9


# Renderer class
class Renderer:

    # Class info
    __author__ = "Hykilpikonna"
    __version__ = "0.0.0 (2019-10-26)"

    # Constructor
    def __init__(self, pygame):
        self.pygame = pygame

        # Initialize pygame
        self.pygame.display.set_caption(WINDOW_TITLE)
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Draw grid lines
    def drawGrid(self):

        # Calculate border line boxes
        rightBox = (GRID_START_X - BORDER_WIDTH, GRID_START_Y, BORDER_WIDTH, GRID_LENGTH_Y)
        leftBox = (GRID_START_X + GRID_LENGTH_X, GRID_START_Y, BORDER_WIDTH, GRID_LENGTH_Y)
        topBox = (GRID_START_X, GRID_START_Y - BORDER_WIDTH, GRID_LENGTH_X, BORDER_WIDTH)
        bottomBox = (GRID_START_X, GRID_START_Y + GRID_LENGTH_Y, GRID_LENGTH_X, BORDER_WIDTH)

        # Draw border lines
        self.pygame.draw.rect(self.window, BORDER_COLOR, rightBox)
        self.pygame.draw.rect(self.window, BORDER_COLOR, leftBox)
        self.pygame.draw.rect(self.window, BORDER_COLOR, topBox)
        self.pygame.draw.rect(self.window, BORDER_COLOR, bottomBox)

        # Loop through all x values in the grid
        for x in range(GRID_START_X, GRID_START_X + GRID_LENGTH_X):

            # Every gap between blocks
            if x % (BLOCK_WIDTH + GRID_LINE_WIDTH) == 0:

                # Calculate box position
                position = (x + BLOCK_WIDTH, GRID_START_Y, GRID_LINE_WIDTH, GRID_LENGTH_X)

                # Draw a line
                self.pygame.draw.rect(self.window, GRID_LINE_COLOR, position)

        # Loop through all y values in the grid
        for y in range(GRID_START_Y, GRID_START_Y + GRID_LENGTH_Y):

            # Every gap between blocks
            if y % (BLOCK_WIDTH + GRID_LINE_WIDTH) == 0:

                # Calculate box position
                position = (GRID_START_X, y + BLOCK_WIDTH, GRID_LENGTH_Y, GRID_LINE_WIDTH)

                # Draw a line
                self.pygame.draw.rect(self.window, GRID_LINE_COLOR, position)


