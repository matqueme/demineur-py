import pygame
from pygame.locals import *
from sprites import Sprites
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
        colorWhite = (255, 255, 255)
        colorGrey = (80, 80, 80)

        LEFT = 1
        RIGHT = 3

        DIGIT_X = 14
        DIGIT_Y = 24

        SMILEY = 25

        def grille():
            PERDU = False
            self.arrayHide = []
            genere = True
            pygame.init()
            window = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption('Demineur')
            pygame.display.flip()
            run = True
            self.sprite = Sprites()

            window.fill(background)

            pygame.draw.rect(window, colorWhite,
                             pygame.Rect(0, 0, SCREEN_WIDTH, 2))

            pygame.draw.rect(window, colorGrey,
                             pygame.Rect(0, 10, SCREEN_WIDTH, 2))
            # On affiche le tableau
            for i in range(longeur):
                for y in range(largeur):
                    window.blit(self.sprite.getbloc_full(),
                                (17*i, 17*y+HAUTEUR))

            window.blit(self.sprite.getsmiley_happy(), ((SCREEN_WIDTH/2) -
                                                        SMILEY/2, HAUTEUR/2 - SMILEY/2))

            for i in range(3):
                window.blit(self.sprite.getdigit_1(),
                            (SCREEN_WIDTH-i * DIGIT_X, HAUTEUR/2 - DIGIT_Y/2))
            for i in range(3):
                window.blit(
                    self.sprite.getdigit_0(), (i*DIGIT_X, HAUTEUR/2 - DIGIT_Y/2))

            while run:
                # event during game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        quit()

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                        x, y = event.pos
                        y = y - HAUTEUR
                        # affiche le shock si on est dans le jeux
                        if y >= 0:
                            window.blit(self.sprite.getsmiley_shock(), ((SCREEN_WIDTH/2) -
                                                                        SMILEY/2, HAUTEUR/2 - SMILEY/2))
                        # si on est dans le menu affiche le btnclick si on click dessus
                        else:
                            if (x < (SCREEN_WIDTH/2) + SMILEY/2 and x > (SCREEN_WIDTH/2) - SMILEY/2 and y + HAUTEUR < (HAUTEUR/2) + SMILEY/2 and y + HAUTEUR > (HAUTEUR/2) - SMILEY/2):
                                window.blit(self.sprite.getsmiley_happy_click(), ((SCREEN_WIDTH/2) -
                                                                                  SMILEY/2, HAUTEUR/2 - SMILEY/2))

                    if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                        # Set the x, y postions of the mouse click
                        x, y = event.pos
                        y = y - HAUTEUR
                        pos_x, pos_y = int(x / 17), int(((y) / 17))
                        # si on est dans le jeu
                        if y >= 0:
                            while genere:
                                demineur = Generation(
                                    longeur, largeur, NB_MINES, pos_x, pos_y)
                                genere = False
                            if PERDU == False:
                                arrayHide = demineur.deleteCase(
                                    pos_x, pos_y)

                            for i in range(len(arrayHide)):
                                for y in range(len(arrayHide)):
                                    if arrayHide[y][i] != '*':
                                        # Si on perd
                                        if arrayHide[y][i] == 'B':
                                            for g in range(len(demineur.array)):
                                                for w in range(len(demineur.array)):
                                                    if demineur.array[w][g] == 'b':
                                                        window.blit(
                                                            self.sprite.getbloc_mine(), (g*17, w*17+HAUTEUR))
                                            window.blit(
                                                self.sprite.getbloc_mine_explode(), (i*17, y*17+HAUTEUR))
                                            window.blit(self.sprite.getsmiley_lose(), ((SCREEN_WIDTH/2) -
                                                                                       SMILEY/2, HAUTEUR/2 - SMILEY/2))
                                            PERDU = True
                                        # affiche les autres numéro qui sont pas une bombes
                                        else:
                                            window.blit(
                                                eval(self.sprite.returnSprite(arrayHide[y][i])), (i*17, y*17+HAUTEUR))

                        # Réaffiche le bon smiley
                        window.blit(self.sprite.getsmiley_happy(), ((SCREEN_WIDTH/2) -
                                                                    SMILEY/2, HAUTEUR/2 - SMILEY/2))

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT and PERDU == False:
                        # Set the x, y postions of the mouse click
                        x, y = event.pos
                        y = y - HAUTEUR
                        pos_x, pos_y = int(x / 17), int(y / 17)
                        if not genere and y >= 0:
                            arrayHide = demineur.setFlagorInt(
                                pos_x, pos_y, NB_MINES)
                            for i in range(len(arrayHide)):
                                for y in range(len(arrayHide)):
                                    if arrayHide[y][i] == 'F':
                                        window.blit(
                                            self.sprite.getbloc_flag(), (int(i*17), int(y*17)+HAUTEUR))
                                    if arrayHide[y][i] == 'I':
                                        window.blit(
                                            self.sprite.getbloc_interrogation(), (int(i*17), int(y*17)+HAUTEUR))
                                    if arrayHide[y][i] == '*':
                                        window.blit(
                                            self.sprite.getbloc_full(), (int(i*17), int(y*17)+HAUTEUR))

                     # Calcul le nombre de bombes restantes
                        nb_bombe = NB_MINES - demineur.getNb_Bombe()
                        nb_bombes = list(str(nb_bombe))
                        for i in range(3-len(nb_bombes)):
                            nb_bombes.insert(0, '0')
                     # Affiche le nombre de bombes restantes
                        for i in range(len(nb_bombes)):
                            window.blit(
                                self.sprite.printNumber(i, nb_bombes), (i*DIGIT_X, HAUTEUR/2 - DIGIT_Y/2))

                    # Pour actualiser le click long
                    if not genere and PERDU == False:
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
                                                self.sprite.getbloc_full(), (i*17, j*17+HAUTEUR))
                                window.blit(
                                    self.sprite.getbloc_empty(), (int(cur[0] / 17)*17, math.floor(y/17)*17+HAUTEUR))
                            else:
                                for i in range(len(dem)):
                                    for j in range(len(dem)):
                                        if dem[j][i] == '*':
                                            window.blit(
                                                self.sprite.getbloc_full(), (i*17, j*17+HAUTEUR))
                pygame.display.update()
            return
        grille()


Vue()
