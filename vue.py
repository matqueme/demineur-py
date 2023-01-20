import pygame
from pygame.locals import *
from sprites_sheet import sprites_sheet
from modele import Generation


class Vue():
    def __init__(self):

        # Taille du tableau de jeu
        longeur = 16
        largeur = 16

        NB_MINES = 40

        SCREEN_WIDTH = longeur*17
        SCREEN_HEIGHT = largeur*17

        background = (255, 255, 255)

        filename = './sprites.png'

        LEFT = 1
        RIGHT = 3

        PIXEL = 17

        DIGIT_X = 14
        DIGIT_Y = 24

        def grille():
            PERDU = 0
            self.arrayHide = []
            genere = True
            pygame.init()
            window = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption('Demineur')
            pygame.display.flip()
            run = True

            sprite_sheet = pygame.image.load(filename).convert_alpha()
            # On recupére tous les différents sprites
            bloc_full = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 0, 50)
            bloc_empty = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 17, 50)
            bloc_flag = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 34, 50)
            bloc_interrogation = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 51, 50)
            bloc_mine = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 85, 50)
            bloc_mine_explode = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 102, 50)
            bloc_number_1 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 0, 67)
            bloc_number_2 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 17, 67)
            bloc_number_3 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 34, 67)
            bloc_number_4 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 51, 67)
            bloc_number_5 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 68, 67)
            bloc_number_6 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 85, 67)
            bloc_number_7 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 102, 67)
            bloc_number_8 = sprites_sheet.get_image(
                sprite_sheet, PIXEL, PIXEL, 119, 67)

            digit_1 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 0, 0)
            digit_2 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 14, 0)

            window.fill(background)

            # On affiche le tableau
            for i in range(longeur):
                for y in range(largeur):
                    window.blit(bloc_full, (17*i, 17*y))

            while run:

                # event during game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        quit()

                    if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                        # Set the x, y postions of the mouse click
                        x, y = event.pos
                        pos_x, pos_y = int(x / 17), int(y / 17)
                        while genere:
                            demineur = Generation(
                                longeur, largeur, NB_MINES, pos_x, pos_y)
                            genere = False
                        if PERDU == 0:
                            arrayHide = demineur.deleteCase(pos_x, pos_y)
                        # print(arrayHide)

                        for i in range(len(arrayHide)):
                            for y in range(len(arrayHide)):
                                if arrayHide[y][i] != '*':
                                    if arrayHide[y][i] == 'B':
                                        for g in range(len(demineur.array)):
                                            for w in range(len(demineur.array)):
                                                if demineur.array[w][g] == 'b':
                                                    window.blit(
                                                        bloc_mine, (g*17, w*17))
                                        window.blit(
                                            bloc_mine_explode, (i*17, y*17))
                                        PERDU = 1

                                    if arrayHide[y][i] == '0':
                                        window.blit(
                                            bloc_empty, (i*17, y*17))
                                    if arrayHide[y][i] == '1':
                                        window.blit(
                                            bloc_number_1, (i*17, y*17))
                                    if arrayHide[y][i] == '2':
                                        window.blit(
                                            bloc_number_2, (i*17, y*17))
                                    if arrayHide[y][i] == '3':
                                        window.blit(
                                            bloc_number_3, (i*17, y*17))
                                    if arrayHide[y][i] == '4':
                                        window.blit(
                                            bloc_number_4, (i*17, y*17))
                                    if arrayHide[y][i] == '5':
                                        window.blit(
                                            bloc_number_5, (i*17, y*17))
                                    if arrayHide[y][i] == '6':
                                        window.blit(
                                            bloc_number_6, (i*17, y*17))
                                    if arrayHide[y][i] == '7':
                                        window.blit(
                                            bloc_number_7, (i*17, y*17))
                                    if arrayHide[y][i] == '8':
                                        window.blit(
                                            bloc_number_8, (i*17, y*17))
                                    if arrayHide[y][i] == 'F':
                                        window.blit(
                                            bloc_flag, (int(i*17), int(y*17)))
                    if PERDU == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                            # Set the x, y postions of the mouse click
                            x, y = event.pos
                            pos_x, pos_y = int(x / 17), int(y / 17)
                            if not genere:
                                arrayHide = demineur.setFlagorInt(pos_x, pos_y)
                                for i in range(len(arrayHide)):
                                    for y in range(len(arrayHide)):
                                        if arrayHide[y][i] == 'F':
                                            window.blit(
                                                bloc_flag, (int(i*17), int(y*17)))
                                        if arrayHide[y][i] == 'I':
                                            window.blit(
                                                bloc_interrogation, (int(i*17), int(y*17)))
                                        if arrayHide[y][i] == '*':
                                            window.blit(
                                                bloc_full, (int(i*17), int(y*17)))
                            # il faut verifier avec le tableau qu'il s'agit d'une case plein
                            #window.blit(bloc_flag, (int(pos_x*17), int(pos_y*17)))
                        if not genere:
                            cur = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()
                            # demineur.timestmp()
                            if click[0] == True:
                                dem = demineur.getArrayHide()
                                if dem[int(cur[1] / 17)][int(cur[0] / 17)] == '*':
                                    for i in range(len(dem)):
                                        for j in range(len(dem)):
                                            if dem[j][i] == '*':
                                                window.blit(
                                                    bloc_full, (i*17, j*17))
                                    window.blit(
                                        bloc_empty, (int(cur[0] / 17)*17, int(cur[1] / 17)*17))
                                else:
                                    for i in range(len(dem)):
                                        for j in range(len(dem)):
                                            if dem[j][i] == '*':
                                                window.blit(
                                                    bloc_full, (i*17, j*17))
                pygame.display.update()
            return

        grille()


Vue()
