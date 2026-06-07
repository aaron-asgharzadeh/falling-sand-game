# Define grid parameters
CELL_SIZE = 4
GRID_WIDTH = 150
GRID_HEIGHT = 150

# Material IDs
EMPTY = 0
SAND = 1
WATER = 2

# Create 2D grids
grid = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
nextGrid = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
colorGrid = [[(0, 0, 0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
nextColorGrid = [[(0, 0, 0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
