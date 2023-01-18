import numpy as np
import random
import utils


class Generation:
    def __init__(self, column, row, nbBomb, xClick, yClick):

        self.array = []
        self.column, self.row = column, row
        self.nbBomb = nbBomb
        self.xClick, self.yClick = xClick, yClick
        self.array = np.zeros(shape=(self.column, self.row), dtype=object)
        self.arrayHide = np.full((self.column, self.row), '*', dtype=object)

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
            if self.array[x][y] == 'b':
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
            self.arrayHide[j][i] = (self.array[j][i])
            if j > 0:
                self.arrayHide[j-1][i] = (self.array[j-1][i])
            if i > 0:
                self.arrayHide[j][i-1] = (self.array[j][i-1])
            if i < 15:
                self.arrayHide[j][i+1] = (self.array[j][i+1])
            if j < 15:
                self.arrayHide[j+1][i] = (self.array[j+1][i])
            if i > 0 and j > 0:
                self.arrayHide[(j-1)][(i-1)] = (self.array[(j-1)][(i-1)])
            if i < 15 and j < 15:
                self.arrayHide[(j+1)][(i+1)] = (self.array[(j+1)][(i+1)])
            if i > 0 and j < 15:
                self.arrayHide[(j+1)][(i-1)] = (self.array[(j+1)][(i-1)])
            if i < 15 and j > 0:
                self.arrayHide[(j-1)][(i+1)] = (self.array[(j-1)][(i+1)])

        if (self.array[y][x] == 'b'):
            print("perdu")
        elif (self.array[y][x] == '0'):
            getZeroTab = [[x, y]]
            index = 0
            while (len(getZeroTab) > index):
                tabtemp = self.utils.get_adjacent_numbers(
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


'''question : 
- Le test autour de chaque nombre avec tout les if c'est bien ?
- Faire un tableau avec la boucle pour les valeurs interditent c'est bien ou autant mettre en statique ?
- On fait la génération dans le __init__ ? '''
