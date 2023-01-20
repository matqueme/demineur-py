import pygame
from pygame.locals import *
from sprites_sheet import sprites_sheet
from modele import Generation
import math


class Vue():
    def __init__(self):

        # Taille du tableau de jeu
        longeur = 16
        largeur = 16

        NB_MINES = 40

        HAUTEUR = 50

        SCREEN_WIDTH = longeur*17
        SCREEN_HEIGHT = largeur*17 + HAUTEUR

        background = (192, 192, 192)

        filename = './sprites.png'

        LEFT = 1
        RIGHT = 3

        PIXEL = 17

        DIGIT_X = 14
        DIGIT_Y = 24

        SMILEY = 25

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
            digit_3 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 28, 0)
            digit_4 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 42, 0)
            digit_5 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 56, 0)
            digit_6 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 70, 0)
            digit_7 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 84, 0)
            digit_8 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 98, 0)
            digit_9 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 112, 0)
            digit_0 = sprites_sheet.get_image(
                sprite_sheet, DIGIT_X, DIGIT_Y, 126, 0)

            smiley_happy = sprites_sheet.get_image(
                sprite_sheet, SMILEY, SMILEY, 1, 25)
            smiley_happy_click = sprites_sheet.get_image(
                sprite_sheet, SMILEY, SMILEY, 28, 25)
            smiley_shock = sprites_sheet.get_image(
                sprite_sheet, SMILEY, SMILEY, 55, 25)
            smiley_win = sprites_sheet.get_image(
                sprite_sheet, SMILEY, SMILEY, 82, 25)
            smiley_lose = sprites_sheet.get_image(
                sprite_sheet, SMILEY, SMILEY, 109, 25)

            window.fill(background)

            # On affiche le tableau
            for i in range(longeur):
                for y in range(largeur):
                    window.blit(bloc_full, (17*i, 17*y+HAUTEUR))

            window.blit(smiley_happy, ((SCREEN_WIDTH/2) -
                        SMILEY/2, HAUTEUR/2 - SMILEY/2))

            for i in range(3):
                window.blit(digit_1, (SCREEN_WIDTH-i *
                            DIGIT_X, HAUTEUR/2 - DIGIT_Y/2))
            for i in range(3):
                window.blit(
                    digit_0, (i*DIGIT_X, HAUTEUR/2 - DIGIT_Y/2))

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
                        y = y - HAUTEUR
                        pos_x, pos_y = int(x / 17), int(((y) / 17))
                        if y >= 0:
                            while genere:
                                demineur = Generation(
                                    longeur, largeur, NB_MINES, pos_x, pos_y)
                                genere = False
                            if PERDU == 0:
                                arrayHide = demineur.deleteCase(
                                    pos_x, pos_y)
                            # print(arrayHide)

                            for i in range(len(arrayHide)):
                                for y in range(len(arrayHide)):
                                    if arrayHide[y][i] != '*':
                                        if arrayHide[y][i] == 'B':
                                            for g in range(len(demineur.array)):
                                                for w in range(len(demineur.array)):
                                                    if demineur.array[w][g] == 'b':
                                                        window.blit(
                                                            bloc_mine, (g*17, w*17+HAUTEUR))
                                            window.blit(
                                                bloc_mine_explode, (i*17, y*17+HAUTEUR))
                                            PERDU = 1

                                        if arrayHide[y][i] == '0':
                                            window.blit(
                                                bloc_empty, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '1':
                                            window.blit(
                                                bloc_number_1, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '2':
                                            window.blit(
                                                bloc_number_2, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '3':
                                            window.blit(
                                                bloc_number_3, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '4':
                                            window.blit(
                                                bloc_number_4, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '5':
                                            window.blit(
                                                bloc_number_5, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '6':
                                            window.blit(
                                                bloc_number_6, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '7':
                                            window.blit(
                                                bloc_number_7, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == '8':
                                            window.blit(
                                                bloc_number_8, (i*17, y*17+HAUTEUR))
                                        if arrayHide[y][i] == 'F':
                                            window.blit(
                                                bloc_flag, (int(i*17), int(y*17+HAUTEUR)))
                    if PERDU == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
                            # Set the x, y postions of the mouse click
                            x, y = event.pos
                            y = y - HAUTEUR
                            pos_x, pos_y = int(x / 17), int(y / 17)
                            if not genere and y >= 0:
                                arrayHide = demineur.setFlagorInt(pos_x, pos_y)
                                for i in range(len(arrayHide)):
                                    for y in range(len(arrayHide)):
                                        if arrayHide[y][i] == 'F':
                                            window.blit(
                                                bloc_flag, (int(i*17), int(y*17)+HAUTEUR))
                                        if arrayHide[y][i] == 'I':
                                            window.blit(
                                                bloc_interrogation, (int(i*17), int(y*17)+HAUTEUR))
                                        if arrayHide[y][i] == '*':
                                            window.blit(
                                                bloc_full, (int(i*17), int(y*17)+HAUTEUR))
                            # il faut verifier avec le tableau qu'il s'agit d'une case plein
                            #window.blit(bloc_flag, (int(pos_x*17), int(pos_y*17)))
                            nb_bombe = NB_MINES - demineur.getNb_Bombe()

                            nb_bombes = list(str(nb_bombe))

                            for i in range(len(nb_bombes)):
                                if nb_bombes[i] == '1':
                                    digit = digit_1
                                elif nb_bombes[i] == '2':
                                    digit = digit_2
                                elif nb_bombes[i] == '3':
                                    digit = digit_3
                                elif nb_bombes[i] == '4':
                                    digit = digit_4
                                elif nb_bombes[i] == '5':
                                    digit = digit_5
                                elif nb_bombes[i] == '6':
                                    digit = digit_6
                                elif nb_bombes[i] == '7':
                                    digit = digit_7
                                elif nb_bombes[i] == '8':
                                    digit = digit_8
                                elif nb_bombes[i] == '9':
                                    digit = digit_9
                                elif nb_bombes[i] == '0':
                                    digit = digit_0
                                window.blit(
                                    digit, (i*DIGIT_X, HAUTEUR/2 - DIGIT_Y/2))

                        if not genere:
                            cur = pygame.mouse.get_pos()
                            click = pygame.mouse.get_pressed()
                            # demineur.timestmp()
                            if click[0] == True and cur[1]-HAUTEUR >= 0:
                                y = cur[1]-HAUTEUR
                                dem = demineur.getArrayHide()
                                if dem[int((y) / 17)][int((cur[0] / 17))] == '*':
                                    for i in range(len(dem)):
                                        for j in range(len(dem)):
                                            if dem[j][i] == '*':
                                                window.blit(
                                                    bloc_full, (i*17, j*17+HAUTEUR))
                                    window.blit(
                                        bloc_empty, (int(cur[0] / 17)*17, math.floor(y/17)*17+HAUTEUR))
                                else:
                                    for i in range(len(dem)):
                                        for j in range(len(dem)):
                                            if dem[j][i] == '*':
                                                window.blit(
                                                    bloc_full, (i*17, j*17+HAUTEUR))
                    else:
                        window.blit(smiley_lose, ((SCREEN_WIDTH/2) -
                                                  SMILEY/2, HAUTEUR/2 - SMILEY/2))
                pygame.display.update()
            return

        grille()


Vue()
