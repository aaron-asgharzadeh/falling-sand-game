from materials.sand import update_sand
from materials.water import update_water

SAND = 1
WATER = 2

UPDATERS = {SAND: update_sand, WATER: update_water}
