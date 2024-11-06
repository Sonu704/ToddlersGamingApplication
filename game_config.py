import os
import pygame

IMAGE_SIZE = 128
# defining the image size
SCREEN_SIZE = 650
# defining the screen size
NUM_TILES_SIDE = 5
# NUM_TILES_SIDE = 4


NUM_TILES_TOTAL = 20
# NUM_TILES_TOTAL = 16

# total tiles in the game

MARGIN = 5
# margin between one image and another

ASSET_DIR = 'assets'
# defining the assset directory

ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
# list comprehension to access all the files

# assert len(ASSET_FILES) == 10
# assert len(ASSET_FILES) == 8
# just to check wether all the 8 files of our program are there or not



