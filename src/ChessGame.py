"""
Main driver file.

"""

import pygame as pyg
from GameState import GameState

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def input_images():
    """
    Loads Chess piece images.

    """
    # Importing pieces
    # Expensive operation
    # Only done once
    pieces = ["bp", "bR", "bN", "bB", "bK", "bQ", "wp", "wR", "wN", "wB", "wK", "wQ"]
    for piece in pieces:
        image_path = piece + ".png"
        IMAGES[piece] = pyg.transform.scale(pyg.image.load(image_path), (SQ_SIZE, SQ_SIZE))


def main():
    pyg.init()