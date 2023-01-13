import pygame
import time
import scipy
import numpy as np
import win32api
import win32con
import keyboard
from scipy import signal
import pyautogui


# @Earth : Numpy Grid
# @Earth.compute() : Compute neighbors count through 2d convolution
# @Earth.update() : Update every cell of the board
class Earth:
    def __init__(self, width, height, scale, density):
        self.earthColumns = int(width/scale)
        self.earthRows = int(height/scale)

        # 1: Living cell, 0: Dead cell
        # Density can be set in __main__
        self.Entity = np.random.choice([1, 0], self.earthColumns*self.earthRows, p=[
                                       cellDensity/100, 1-cellDensity/100]).reshape(self.earthColumns, self.earthRows)
        self.draw()

    # Compute neighbors by comparing every cell with a 3*3 ones matrix
    def compute(self):
        counts = scipy.signal.convolve2d(self.Entity, comparison, mode='same')
        self.update(counts, displayNeighborsText)

    # Update every cell of the board
    def update(self, counts, displayText):
        # Iterate through the whole board
        for x in range(len(counts)):
            for y in range(len(counts[0])):

                # Rule 1: if a cell is living and is surrounded by 2 or 3 living cells, it survives
                if self.Entity[x][y] == 1:
                    if counts[x][y] == 2 or counts[x][y] == 3:
                        pass
                    else:
                        self.Entity[x][y] = 0

                # Rule 2: if a cell is dead and is surrounded by 3 living cells, it comes back to life
                elif self.Entity[x][y] == 0:
                    if counts[x][y] == 3:
                        self.Entity[x][y] = 1

                # If no rule is respected, the cell is dead upon the next iteration

                # If the boolean is set to true in __main_, display the number of neighbors in real time
                if displayText:
                    font = pygame.font.SysFont('arial', 10)
                    text = font.render(str(counts[x][y]), False, (50, 50, 50))
                    monitorDisplay.blit(text, (x*cellSize, y*cellSize))
        self.draw()

    def draw(self):
        # Iterate through the whole board
        for x in range(len(self.Entity)):
            for y in range(len(self.Entity[0])):
                # pygame.draw.rect takes a rect as an argument: (posX, posY, width, height)
                rect = [x * cellSize, y * cellSize, cellSize, cellSize]
                # Draws a cell on the display, blue if the cell is living, black if the cell is dead
                if self.Entity[x][y] == 1:
                    pygame.draw.rect(monitorDisplay, (14, 72, 143), rect)
                else:
                    pygame.draw.rect(monitorDisplay, (0, 0, 0), rect)
                    pygame.draw.rect(monitorDisplay, (5, 5, 5), rect, 1)
        pygame.display.update()

    def reroll(self):
        self.Entity = np.random.choice([1, 0], self.earthColumns * self.earthRows,
                                       p=[cellDensity / 100, 1 - cellDensity / 100]).reshape(self.earthColumns,
                                                                                             self.earthRows)
        self.draw()

    def clear(self):
        self.Entity = np.random.choice([1, 0], self.earthColumns * self.earthRows,
                                       p=[0, 1]).reshape(self.earthColumns, self.earthRows)
        self.draw()


if __name__ == '__main__':

    # Useful parameters to edit your simulation
    # @cellSize: sets the width and height of each cell in pixels
    # @cellDensity: gives the percentage used for the distribution of initial living cells
    # @displayNeighborsText: display the amount of neighbors in real time
    cellSize = 10
    cellDensity = 20
    displayNeighborsText = False

    gameStarted = False

    # Comparison matrix for the 2d convolution
    comparison = np.ones((3, 3))
    # The center cell is set to zero so the current cell doesn't count itself as a neighbor
    comparison[1][1] = 0

    pygame.init()
    pygame.display.set_caption("Conway's Game of Life")
    monitorSpecs = pygame.display.Info()
    # Sets the size of the window according to the screen resolution
    monitorDisplay = pygame.display.set_mode(
        [monitorSpecs.current_w, monitorSpecs.current_h])

    # Create the grid object
    Earth = Earth(width=monitorSpecs.current_w,
                  height=monitorSpecs.current_h, scale=cellSize, density=cellDensity)
    # Default click state: released
    state_left = win32api.GetKeyState(0x01)

    Earth.clear()

    while True:
        if not gameStarted:
            time.sleep(0.01)
            pygame.event.get()
            font = pygame.font.SysFont('arial', 20)
            space = font.render(
                'Press <SPACE> to start the game', False, (180, 180, 180))
            spacePos = (monitorSpecs.current_w * 0.05,
                        monitorSpecs.current_h*0.01)
            enter = font.render(
                'Press <ENTER> to generate random seed', False, (180, 180, 180))
            enterPos = (monitorSpecs.current_w * 0.05,
                        monitorSpecs.current_h * 0.04)
            click = font.render(
                'Press <LEFTCLICK> to add a cell', False, (180, 180, 180))
            clickPos = (monitorSpecs.current_w * 0.05,
                        monitorSpecs.current_h * 0.07)
            clear = font.render(
                'Press <RETURN> to clear the grid', False, (180, 180, 180))
            clearPos = (monitorSpecs.current_w * 0.05,
                        monitorSpecs.current_h * 0.1)
            monitorDisplay.blit(space, spacePos)
            monitorDisplay.blit(enter, enterPos)
            monitorDisplay.blit(click, clickPos)
            monitorDisplay.blit(clear, clearPos)

            if keyboard.is_pressed('ENTER'):
                Earth.reroll()
                time.sleep(0.3)

            if keyboard.is_pressed('BACKSPACE'):
                Earth.clear()
            # Current click state
            key = win32api.GetKeyState(0x01)
            if key != state_left:  # Button state changed
                state_left = key
                if key < 0:
                    Earth.Entity[int(pyautogui.position().x/cellSize)
                                 ][int(pyautogui.position().y/cellSize)] = 1
                    Earth.draw()
            if keyboard.is_pressed('SPACE'):
                while keyboard.is_pressed('SPACE'):
                    time.sleep(0.01)
                gameStarted = not gameStarted
            pygame.display.update()

        if gameStarted:
            time.sleep(0.01)
            pygame.event.get()
            Earth.compute()
            font = pygame.font.SysFont('arial', 20)
            space = font.render(
                'Press <SPACE> to pause the game', False, (180, 180, 180))
            spacePos = (monitorSpecs.current_w * 0.05,
                        monitorSpecs.current_h * 0.01)
            monitorDisplay.blit(space, spacePos)
            pygame.display.update()
            if keyboard.is_pressed('SPACE'):
                while keyboard.is_pressed('SPACE'):
                    time.sleep(0.01)
                gameStarted = not gameStarted
