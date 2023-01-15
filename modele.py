import numpy as np
import random


class Generation:
    def __init__(self, column, row, bomb, array, xClick, yClick):

        self.array = array
        self.column, self.row = column, row
        self.bomb = bomb

        self.array = np.zeros(shape=(self.column, self.row), dtype=object)

        # genere un tableau avec toutes les valeurs ou l'on ne peut pas mettre de bombes, cad 3x3 autour de la génération
        def impossible_array(i, j):
            total = [[i, j]]
            if j > 0:
                total.append([i, (j-1)])
            if i > 0:
                total.append([(i-1), j])
            if i < 15:
                total.append([(i+1), j])
            if j < 15:
                total.append([i, (j+1)])
            if i > 0 and j > 0:
                total.append([(i-1), (j-1)])
            if i < 15 and j < 15:
                total.append([(i+1), (j+1)])
            if i > 0 and j < 15:
                total.append([(i-1), (j+1)])
            if i < 15 and j > 0:
                total.append([(i+1), (j-1)])
            return total

        # verifie le nombre de bombe a une coordonnée precise
        def get_adjacent_numbers(grid, i, j):
            total = []
            if j > 0:
                total.append(grid[i, (j-1)])
            if i > 0:
                total.append(grid[(i-1), j])
            if i < 15:
                total.append(grid[(i+1), j])
            if j < 15:
                total.append(grid[i, (j+1)])
            if i > 0 and j > 0:
                total.append(grid[(i-1), (j-1)])
            if i < 15 and j < 15:
                total.append(grid[(i+1), (j+1)])
            if i > 0 and j < 15:
                total.append(grid[(i-1), (j+1)])
            if i < 15 and j > 0:
                total.append(grid[(i+1), (j-1)])
            return str(total.count('b'))

        arrayImposible = impossible_array(xClick, yClick)

        # genere des bombes dès que l'on est pas sur une case impossible ou que le il n'y a pas de bombe
        tempNbBomb = 0
        while tempNbBomb != self.bomb:
            erreur = 0
            x = random.randint(0, row-1)
            y = random.randint(0, column-1)
            for i in range(len(arrayImposible)):
                if arrayImposible[i] == [x, y]:
                    erreur = 1
            if self.array[x][y] == 'b':
                erreur = 1
            if (erreur == 0):
                self.array[x][y] = 'b'
                tempNbBomb += 1

        # genere les chiffres autour des bombes
        for x in range(len(self.array)):
            for y in range(len(self.array[0])):
                if (self.array[x, y] != 'b'):
                    self.array[x, y] = get_adjacent_numbers(self.array, x, y)

        #a = (self.array == 'b').sum()

        print(self.array)


Demineur = Generation(16, 16, 40, [], 0, 0)
