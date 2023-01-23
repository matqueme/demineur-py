import pygame
from pygame.locals import *
from sprites import Sprites
from modele import Generation
import math


class Vue():
    def __init__(self):

        # Taille du tableau de jeu
        LONGUEUR = 16
        LARGEUR = 16

        NB_MINES = 40

        HAUTEUR = 50
        BORDURE = 12

        SCREEN_WIDTH = LARGEUR*16 + 2*BORDURE
        SCREEN_HEIGHT = LONGUEUR * 16 + HAUTEUR + BORDURE

        background = (192, 192, 192)
        colorWhite = (255, 255, 255)
        colorGrey = (128, 128, 128)

        LEFT = 1
        RIGHT = 3

        DIGIT_X = 13
        DIGIT_Y = 23

        SMILEY = 25

        self.start_ticks = 0
        self.seconds = 0

        def grille():
            WIN = False
            PERDU = False
            self.arrayHide = []
            genere = True
            pygame.init()
            window = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption('Demineur')
            pygame.display.set_icon(pygame.image.load('./icon.png'))
            pygame.display.flip()
            run = True
            self.sprite = Sprites()

            window.fill(background)

            # affiche les contours
            # Largeur
            pygame.draw.rect(window, colorWhite,
                             pygame.Rect(0, 0, SCREEN_WIDTH, 2))

            pygame.draw.rect(window, colorGrey,
                             pygame.Rect(BORDURE, 10, SCREEN_WIDTH - 2*BORDURE, 2))

            pygame.draw.rect(window, colorWhite,
                             pygame.Rect(BORDURE-2, HAUTEUR-BORDURE, SCREEN_WIDTH - 2*BORDURE+2, 2))

            pygame.draw.rect(window, colorGrey,
                             pygame.Rect(BORDURE, HAUTEUR-2, SCREEN_WIDTH - 2*BORDURE, 2))

            pygame.draw.rect(window, colorWhite,
                             pygame.Rect(10, SCREEN_HEIGHT - BORDURE, SCREEN_WIDTH - 2 * BORDURE + 4, 2))

            pygame.draw.rect(window, colorGrey,
                             pygame.Rect(0, SCREEN_HEIGHT - 2, SCREEN_WIDTH, 2))

            # Longueur
            pygame.draw.rect(window, colorWhite,
                             pygame.Rect(0, 0, 2, SCREEN_HEIGHT))

            pygame.draw.rect(window, colorGrey,
                             pygame.Rect(10, HAUTEUR-2, 2, SCREEN_HEIGHT - HAUTEUR - BORDURE + 2))

            pygame.draw.rect(window, colorWhite,
                             pygame.Rect(SCREEN_WIDTH - BORDURE, HAUTEUR-2,  2, SCREEN_HEIGHT - HAUTEUR - BORDURE + 2))

            pygame.draw.rect(window, colorGrey,
                             pygame.Rect(SCREEN_WIDTH - 2, 0,  2, SCREEN_HEIGHT))

            pygame.draw.rect(window, colorWhite,
                             pygame.Rect(SCREEN_WIDTH - BORDURE, 10,  2, HAUTEUR - 2*BORDURE + 4))

            pygame.draw.rect(window, colorGrey,
                             pygame.Rect(10, 10,  2, HAUTEUR - 2*BORDURE + 2))

            # On affiche le tableau
            for i in range(LARGEUR):
                for y in range(LONGUEUR):
                    window.blit(self.sprite.getbloc_full(),
                                (16*i+BORDURE, 16*y+HAUTEUR))

            window.blit(self.sprite.getsmiley_happy(), ((SCREEN_WIDTH/2) -
                                                        SMILEY/2, HAUTEUR/2 - SMILEY/2))

            for i in range(3):
                window.blit(self.sprite.getdigit_0(),
                            (SCREEN_WIDTH - (i * DIGIT_X) - DIGIT_X - BORDURE, HAUTEUR/2 - DIGIT_Y/2))

            # Calcul le nombre de bombes restantes
            nb_bombes = list(str(NB_MINES))
            for i in range(3-len(nb_bombes)):
                nb_bombes.insert(0, '0')
            # Affiche le nombre de bombes restantes
            for i in range(len(nb_bombes)):
                window.blit(
                    self.sprite.printNumber(i, nb_bombes), (i*DIGIT_X + BORDURE, HAUTEUR/2 - DIGIT_Y/2))

            while run:
                # event during game
                for event in pygame.event.get():
                    # timer tout les secondes
                    if not genere and PERDU == False and WIN == False:
                        self.seconds = (pygame.time.get_ticks() -
                                        self.start_ticks)/1000
                        nb_sec = list(str(math.floor(self.seconds)))
                        for i in range(3-len(nb_sec)):
                            nb_sec.insert(0, '0')
                        for i in range(len(nb_sec)):
                            window.blit(self.sprite.printNumber(i, nb_sec),
                                        (SCREEN_WIDTH - (i * DIGIT_X) - DIGIT_X - BORDURE, HAUTEUR/2 - DIGIT_Y/2))
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        quit()

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                        x, y = event.pos
                        y -= HAUTEUR
                        x -= BORDURE
                        # affiche le shock si on est dans le jeux
                        if PERDU == False and WIN == False:
                            if y >= 0:
                                window.blit(self.sprite.getsmiley_shock(), ((SCREEN_WIDTH/2) -
                                                                            SMILEY/2, HAUTEUR/2 - SMILEY/2))
                            # si on est dans le menu affiche le btnclick si on click dessus
                            elif x + BORDURE < (SCREEN_WIDTH/2) + SMILEY/2 and x + BORDURE > (SCREEN_WIDTH/2) - SMILEY/2 and y + HAUTEUR < (HAUTEUR/2) + SMILEY/2 and y + HAUTEUR > (HAUTEUR/2) - SMILEY/2:
                                window.blit(self.sprite.getsmiley_happy_click(), ((SCREEN_WIDTH/2) -
                                                                                  SMILEY/2, HAUTEUR/2 - SMILEY/2))
                        elif WIN == False:
                            window.blit(self.sprite.getsmiley_lose(), ((SCREEN_WIDTH/2) -
                                                                       SMILEY/2, HAUTEUR/2 - SMILEY/2))

                    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                        # Set the x, y postions of the mouse click
                        x, y = event.pos
                        y -= HAUTEUR
                        x -= BORDURE
                        pos_x, pos_y = int(x / 16), int(y / 16)

                        # si on est dans le jeu
                        if y >= 0:

                            while genere:
                                demineur = Generation(
                                    LONGUEUR, LARGEUR, NB_MINES, pos_x, pos_y)
                                genere = False
                                self.start_ticks = pygame.time.get_ticks()
                            if PERDU == False and WIN == False:
                                arrayHide = demineur.deleteCase(
                                    pos_x, pos_y)

                            # Victoire
                            if demineur.getWin() == NB_MINES:
                                WIN = True
                                window.blit(self.sprite.getsmiley_win(), ((SCREEN_WIDTH/2) -
                                                                          SMILEY/2, HAUTEUR/2 - SMILEY/2))

                            for i in range(len(arrayHide[0])):
                                for y in range(len(arrayHide)):
                                    if arrayHide[y][i] != '*':
                                        # Si on perd
                                        if arrayHide[y][i] == 'B':
                                            for g in range(len(demineur.array[0])):
                                                for w in range(len(demineur.array)):
                                                    if demineur.array[w][g] == 'b':
                                                        window.blit(
                                                            self.sprite.getbloc_mine(), (g*16+BORDURE, w*16+HAUTEUR))
                                            window.blit(
                                                self.sprite.getbloc_mine_explode(), (i*16+BORDURE, y*16+HAUTEUR))
                                            window.blit(self.sprite.getsmiley_lose(), ((SCREEN_WIDTH/2) -
                                                                                       SMILEY/2, HAUTEUR/2 - SMILEY/2))
                                            PERDU = True
                                        # affiche les autres numéro qui sont pas une bombes
                                        else:
                                            window.blit(
                                                eval(self.sprite.returnSprite(arrayHide[y][i])), (i*16+BORDURE, y*16+HAUTEUR))
                        elif x + BORDURE < (SCREEN_WIDTH/2) + SMILEY/2 and x + BORDURE > (SCREEN_WIDTH/2) - SMILEY/2 and y + HAUTEUR < (HAUTEUR/2) + SMILEY/2 and y + HAUTEUR > (HAUTEUR/2) - SMILEY/2:
                            genere = True
                            PERDU = False
                            WIN = False
                            # Affiche un tableau de bloc plein
                            for i in range(LARGEUR):
                                for y in range(LONGUEUR):
                                    window.blit(self.sprite.getbloc_full(),
                                                (16*i+BORDURE, 16*y+HAUTEUR))
                            # Calcul le nombre de bombes restantes
                            nb_bombes = list(str(NB_MINES))
                            for i in range(3-len(nb_bombes)):
                                nb_bombes.insert(0, '0')
                            # Affiche le nombre de bombes restantes
                            for i in range(len(nb_bombes)):
                                window.blit(
                                    self.sprite.printNumber(i, nb_bombes), (i*DIGIT_X + BORDURE, HAUTEUR/2 - DIGIT_Y/2))

                        # Réaffiche le bon smiley
                        if PERDU == False and WIN == False:
                            window.blit(self.sprite.getsmiley_happy(), ((SCREEN_WIDTH/2) -
                                                                        SMILEY/2, HAUTEUR/2 - SMILEY/2))

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT and PERDU == False and WIN == False:
                        # Set the x, y postions of the mouse click
                        x, y = event.pos
                        y -= HAUTEUR
                        x -= BORDURE
                        pos_x, pos_y = int(x / 16), int(y / 16)
                        if not genere and y >= 0:
                            arrayHide = demineur.setFlagorInt(
                                pos_x, pos_y, NB_MINES)
                            for i in range(len(arrayHide[0])):
                                for y in range(len(arrayHide)):
                                    if arrayHide[y][i] == 'F':
                                        window.blit(
                                            self.sprite.getbloc_flag(), (int(i*16)+BORDURE, int(y*16)+HAUTEUR))
                                    if arrayHide[y][i] == 'I':
                                        window.blit(
                                            self.sprite.getbloc_interrogation(), (int(i*16)+BORDURE, int(y*16)+HAUTEUR))
                                    if arrayHide[y][i] == '*':
                                        window.blit(
                                            self.sprite.getbloc_full(), (int(i*16)+BORDURE, int(y*16)+HAUTEUR))

                            # Calcul le nombre de bombes restantes
                            nb_bombe = NB_MINES - demineur.getNb_Bombe()
                            nb_bombes = list(str(nb_bombe))
                            for i in range(3-len(nb_bombes)):
                                nb_bombes.insert(0, '0')
                     # Affiche le nombre de bombes restantes
                        for i in range(len(nb_bombes)):
                            window.blit(
                                self.sprite.printNumber(i, nb_bombes), (i*DIGIT_X + BORDURE, HAUTEUR/2 - DIGIT_Y/2))

                    # Pour actualiser le click long
                    if not genere and PERDU == False and WIN == False:
                        click = pygame.mouse.get_pressed()
                        # demineur.timestmp()
                        if click[0] == True:
                            cur = pygame.mouse.get_pos()
                            if cur[1]-HAUTEUR >= 0:
                                y = cur[1]-HAUTEUR
                                x = cur[0]-BORDURE
                                dem = demineur.getArrayHide()
                                if dem[int(y / 16)][int((x / 16))] == '*':
                                    for i in range(len(dem[0])):
                                        for j in range(len(dem)):
                                            if dem[j][i] == '*':
                                                window.blit(
                                                    self.sprite.getbloc_full(), (i*16+BORDURE, j*16+HAUTEUR))
                                    window.blit(
                                        self.sprite.getbloc_empty(), (int(x / 16)*16+BORDURE, math.floor(y/16)*16+HAUTEUR))
                                else:
                                    for i in range(len(dem[0])):
                                        for j in range(len(dem)):
                                            if dem[j][i] == '*':
                                                window.blit(
                                                    self.sprite.getbloc_full(), (i*16+BORDURE, j*16+HAUTEUR))
                pygame.display.update()
            return
        grille()


Vue()
