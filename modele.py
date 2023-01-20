import numpy as np
import random
import utils
import time
import math


class Generation:
    def __init__(self, column, row, nbBomb, xClick, yClick):

        self.array = []
        self.column, self.row = column, row
        self.nbBomb = nbBomb
        self.xClick, self.yClick = xClick, yClick
        self.array = np.zeros(shape=(self.column, self.row), dtype=object)
        self.arrayHide = np.full((self.column, self.row), '*', dtype=object)
        self.time = time.time()
        self.lasttime = 0
        self.utils = utils.Utils()

        arrayImposible = self.utils.impossible_array(xClick, yClick)
        # genere des bombes dès que l'on est pas sur une case impossible ou que le il n'y a pas de bombe
        tempNbBomb = 0
        while tempNbBomb != self.nbBomb:
            erreur = 0
            x = random.randint(0, row-1)
            y = random.randint(0, column-1)
            for i in range(len(arrayImposible)):
                if arrayImposible[i] == [x, y]:
                    erreur = 1
            if self.array[y][x] == 'b':
                erreur = 1
            if (erreur == 0):
                self.array[y][x] = 'b'
                tempNbBomb += 1

        # genere les chiffres autour des bombes
        for x in range(len(self.array)):
            for y in range(len(self.array[0])):
                if (self.array[x][y] != 'b'):
                    self.array[x][y] = self.utils.get_adjacent_numbers(
                        self.array, x, y)
        self.deleteCase(self.xClick, self.yClick)

    def deleteCase(self, x, y):

        def add_number(i, j):
            if self.arrayHide[j][i] != 'F':
                self.arrayHide[j][i] = (self.array[j][i])
            if j > 0:
                if self.arrayHide[j-1][i] != 'F':
                    self.arrayHide[j-1][i] = (self.array[j-1][i])
            if i > 0:
                if self.arrayHide[j][i-1] != 'F':
                    self.arrayHide[j][i-1] = (self.array[j][i-1])
            if i < 15:
                if self.arrayHide[j][i+1] != 'F':
                    self.arrayHide[j][i+1] = (self.array[j][i+1])
            if j < 15:
                if self.arrayHide[j+1][i] != 'F':
                    self.arrayHide[j+1][i] = (self.array[j+1][i])
            if i > 0 and j > 0:
                if self.arrayHide[j-1][i-1] != 'F':
                    self.arrayHide[(j-1)][(i-1)] = (self.array[(j-1)][(i-1)])
            if i < 15 and j < 15:
                if self.arrayHide[j+1][i+1] != 'F':
                    self.arrayHide[(j+1)][(i+1)] = (self.array[(j+1)][(i+1)])
            if i > 0 and j < 15:
                if self.arrayHide[j+1][i-1] != 'F':
                    self.arrayHide[(j+1)][(i-1)] = (self.array[(j+1)][(i-1)])
            if i < 15 and j > 0:
                if self.arrayHide[j-1][i+1] != 'F':
                    self.arrayHide[(j-1)][(i+1)] = (self.array[(j-1)][(i+1)])
        if self.arrayHide[y][x] != 'F':
            if (self.array[y][x] == 'b'):
                print("perdu")
                self.arrayHide[y][x] = 'B'
            elif (self.array[y][x] == '0'):
                getZeroTab = [[x, y]]
                index = 0
                while (len(getZeroTab) > index):
                    tabtemp = self.utils.get_adjacent_numbers2(
                        self.array, getZeroTab[index][0], getZeroTab[index][1])
                    for i in range(len(tabtemp)):
                        if tabtemp[i] not in getZeroTab:
                            getZeroTab.append(
                                tabtemp[i])
                    index += 1
                for i in range(len(getZeroTab)):
                    add_number(getZeroTab[i][0], getZeroTab[i][1])
            else:
                self.arrayHide[y][x] = self.array[y][x]
        return self.arrayHide

    def setFlagorInt(self, x, y, nbBombe):
        if self.arrayHide[y][x] == '*' and nbBombe-self.getNb_Bombe() > 0:
            self.arrayHide[y][x] = 'F'
        elif self.arrayHide[y][x] == 'F':
            self.arrayHide[y][x] = 'I'
        elif self.arrayHide[y][x] == 'I':
            self.arrayHide[y][x] = '*'
        return self.arrayHide

    def getArrayHide(self):
        return self.arrayHide

    def getNb_Bombe(self):
        a = (self.arrayHide == 'F').sum()
        return a
    # def timestmp(self):
        # time_stamp = time.time()
        # if math.floor(time_stamp - self.time) > self.lasttime:
        # print(math.floor(time_stamp - self.time))
        # self.lasttime = math.floor(time_stamp - self.time)


'''question :
- Le test autour de chaque nombre avec tout les if c'est bien ?
- Faire un tableau avec la boucle pour les valeurs interditent c'est bien ou autant mettre en statique ?
- On fait la génération dans le __init__ ? '''
