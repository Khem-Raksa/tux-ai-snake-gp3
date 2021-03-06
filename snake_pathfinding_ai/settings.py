# Dimensions
WIDTH = 412   # Width of game surface
HEIGHT = 412  # Height of game surface
ROWS = 8
SQUARE_SIZE =  HEIGHT // ROWS #Size of one square
GAP_SIZE = 2 # Gap between adjacent squares

# Colors
SURFACE_CLR = (15, 15, 15)
GRID_CLR = (255, 255, 255)
SNAKE_CLR = (50, 255, 50)
TAIL_CLR = (50,255,255)
APPLE_CLR = (0, 0, 255)
HEAD_CLR = (0, 150, 0)
VIRTUAL_SNAKE_CLR = (255, 255, 255)

# Game Settings
FPS = 30  # Frames per second
INITIAL_SNAKE_LENGTH = 3
WAIT_SECONDS_AFTER_WIN = 60  # If snake wins the game, wait for this amount of seconds before restarting
MAX_MOVES_WITHOUT_EATING = ROWS * ROWS * ROWS * 2  # Snake will die after this amount of moves without eating apple
SNAKE_MAX_LENGTH = ROWS * ROWS - INITIAL_SNAKE_LENGTH  # Max number of apples snake can eat

# Variables used in BFS algorithm
GRID = [[i, j] for i in range(ROWS) for j in range(ROWS)]


# Helper functions
def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]],

                 [position[0] - 1, position[1]],

                 [position[0], position[1] + 1],

                 [position[0], position[1] - 1]]
    # neighbors that are in grid             
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors


def distance(pos1, pos2):
    x1, x2 = pos1[0], pos2[0]
    y1, y2 = pos1[1], pos2[1]
    """
    So in a nutshell: 
    Manhattan distance generally works only if the points are arranged in the form of a grid and 
    the problem which we are working on gives more priority to the distance between the points only along with the grids,
     but not the geometric distance.

     e.g our snake moves in x,y not diagonally
    """
    return abs(x2 - x1) + abs(y2 - y1)


# Each position is a tuple because python doesn't allow hashing lists
# Key of dictionary is immutable but list is mutable
ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
