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
# Game
COLOR_DEAD = (0, 0, 0)
COLOR_ALIVE = (200, 200, 200)

# Computed Constants
BLOCK_FULL_WIDTH = BLOCK_WIDTH + GRID_LINE_WIDTH
BLOCKS_X = GRID_LENGTH_X // BLOCK_FULL_WIDTH
BLOCKS_Y = GRID_LENGTH_Y // BLOCK_FULL_WIDTH


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
        self.x_offset = 0
        self.y_offset = 0

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
            if x % BLOCK_FULL_WIDTH == 0:

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

    #/**
    # Draw a block
    #
    # @param x (int) X Position of the block
    # @param y (int) Y Position of the block
    # @param color (int, int, int) Color of the block
    #*/
    def drawBlock(self, x, y, color):

        # Calculate positions
        xStart = GRID_START_X + x * BLOCK_FULL_WIDTH
        yStart = GRID_START_Y + y * BLOCK_FULL_WIDTH

        # Draw them
        self.pygame.draw.rect(self.window, color, (xStart, yStart, BLOCK_WIDTH, BLOCK_WIDTH))

    #/**
    # Display a world
    # TODO: Optimize this by rendering specific blocks on change instead of updating the entire thing every frame
    #
    # @param world (World)
    #*/
    def drawWorld(self, world):

        # Get Grid
        grid = world.get_grid()

        # Loop through values
        for y in range(0, BLOCKS_Y):
            for x in range(0, BLOCKS_X):
                self.drawBlock(x, y, self.getBlockColor(grid[x + self.x_offset][y + self.y_offset]))

    # Define callback
    def onBlockUpdate(self, x, y, status):

        # Add the offsets
        #x += self.x_offset
        #y += self.y_offset

        # Check if it is in range
        if (x < 0 + self.x_offset or x > BLOCKS_X + self.x_offset): return
        if (y < 0 + self.y_offset or y > BLOCKS_Y + self.y_offset): return

        # Update block
        self.drawBlock(x - self.x_offset, y - self.y_offset, self.getBlockColor(status))

    # Get alive or dead Color
    def getBlockColor(self, status):
        return COLOR_DEAD if status == 0 else COLOR_ALIVE

    # Update the field
    def updateField(self, x_offset, y_offset):
        self.x_offset += x_offset
        self.y_offset += y_offset

        # Clear screen
        self.clearScreen()

    # Draw everything dead
    def clearScreen(self):
        for y in range(0, BLOCKS_Y):
            for x in range(0, BLOCKS_X):
                self.drawBlock(x, y, self.getBlockColor(0))
