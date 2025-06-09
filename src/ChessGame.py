"""
Chess Game in Python

Author: Herton Cabral Mabongue
Email: hertoncabral04@gmail.com

Description:
This is my second attempt at creating a chess game. My first attempt was during my
first year of university, where I was restricted to using stddraw for the GUI(not fun).
While it was a valuable learning experience, it wasn’t the most enjoyable due
to the limitations of the library.

For this project, I’ve decided to use Pygame to develop a more engaging and visually
appealing chess game. The game is written in Python and aims to offer a better user
experience, improved functionality, and cleaner code compared to my initial project.

Goals:
- Build a polished graphical interface using Pygame.
- Ensure all chess rules are implemented and validated.
- Design modular, extensible code to support future enhancements.

This project reflects my growth as a developer and my passion for both chess and programming.
"""

# IMPORTS #
import os
# Removing pygame welcome msg
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = str(1)
import pygame as pyg
from GameState import GameState


WIDTH = HEIGHT = 800
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
        image_path = "assets/" + piece + ".png"
        IMAGES[piece] = pyg.transform.scale(pyg.image.load(image_path), (SQ_SIZE, SQ_SIZE))


def main():
    """
       Main application entry point for the engine.
       Initializes pygame and engine classes.

    """
    pyg.init()
    view = pyg.display.set_mode((WIDTH, HEIGHT))
    clock = pyg.time.Clock()
    view.fill(pyg.Color('white'))
    game_state = GameState()
    input_images()
    running = True
    selected_square = ()
    player_clicks = []

    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
            elif event.type == pyg.MOUSEBUTTONDOWN:
                mouse_location = pyg.mouse.get_pos()
                # Mouse location is (x,y) dividing by sq size to get row & col
                column = mouse_location[0] // SQ_SIZE
                row = mouse_location[1] // SQ_SIZE
                if selected_square == (row, column):
                    selected_square = ()
                    player_clicks = []
                else:
                    selected_square = (row, column)
                    player_clicks.append(selected_square)
                if len(player_clicks) == 2:

        draw_game(view, game_state)
        clock.tick(MAX_FPS)
        pyg.display.flip()

def draw_game(view, game_state):
    """
          Draws the board on the canvas.
          Draw pieces from assets page.

       """
    draw_board(view)
    draw_pieces(view, game_state.chess_board)



def draw_board(view):
    """
    Draws the board on the canvas.
    Loops over colors then assigns them to a square.

    """
    colors = [pyg.Color('white'), pyg.Color('grey')]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[(row + column) % 2]
            pyg.draw.rect(view, color, pyg.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
def draw_pieces(view, board):
    """
    Draws the pieces on the board.

    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--": #Empty square
                view.blit(IMAGES[piece], pyg.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()

