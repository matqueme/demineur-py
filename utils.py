class Utils:
    # genere un tableau avec toutes les valeurs ou l'on ne peut pas mettre de bombes, cad 3x3 autour de la génération

    def impossible_array(self, i, j):
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

    def get_adjacent_numbers(self, grid, i, j):
        total = []
        if j > 0:
            total.append(grid[i][(j-1)])
        if i > 0:
            total.append(grid[(i-1)][j])
        if i < 15:
            total.append(grid[(i+1)][j])
        if j < 15:
            total.append(grid[i][(j+1)])
        if i > 0 and j > 0:
            total.append(grid[(i-1)][(j-1)])
        if i < 15 and j < 15:
            total.append(grid[(i+1)][(j+1)])
        if i > 0 and j < 15:
            total.append(grid[(i-1)][(j+1)])
        if i < 15 and j > 0:
            total.append(grid[(i+1)][(j-1)])
        return str(total.count('b'))

    def get_adjacent_numbers2(self, grid, i, j):
        total = []
        if j > 0:
            if (grid[j-1][i] == '0'):
                total.append([i, (j-1)])
        if i > 0:
            if (grid[j][i-1] == '0'):
                total.append([i-1, j])
        if i < 15:
            if (grid[j][i+1] == '0'):
                total.append([(i+1), j])
        if j < 15:
            if (grid[j+1][i] == '0'):
                total.append([i, j+1])
        if i > 0 and j > 0:
            if (grid[(j-1)][(i-1)] == '0'):
                total.append([(i-1), (j-1)])
        if i < 15 and j < 15:
            if (grid[(j+1)][(i+1)] == '0'):
                total.append([(i+1), (j+1)])
        if i > 0 and j < 15:
            if (grid[(j+1)][(i-1)] == '0'):
                total.append([(i-1), (j+1)])
        if i < 15 and j > 0:
            if (grid[(j-1)][(i+1)] == '0'):
                total.append([(i+1), (j-1)])
        return total
