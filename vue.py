import pygame
from pygame.locals import *
from sprites import Sprites
from modele import Generation
import math


class Vue():
    def __init__(self):

        # Taille du tableau de jeu
        self.longueur = 16
        self.largeur = 16

        self.nb_mines = 40

        self.hauteur = 50
        self.bordure = 12

        self.screen_width = self.largeur*16 + 2*self.bordure
        self.screen_height = self.longueur * 16 + self.hauteur + self.bordure

        self.background = (192, 192, 192)
        self.colorWhite = (255, 255, 255)
        self.colorGrey = (128, 128, 128)

        self.left = 1
        self.right = 3

        self.digit_x = 13
        self.digit_y = 23

        self.smiley = 25

        self.start_ticks = 0
        self.seconds = 0
        self.demineur = 0
        self.nb_bombes = 0
        self.arrayHide = []

        self.win = False
        self.lose = False

        self.genere = True
        self.run = True

        pygame.init()
        self.window = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption('Démineur')
        pygame.display.set_icon(pygame.image.load('./icon.png'))
        pygame.display.flip()

        self.window.fill(self.background)
        self.sprite = Sprites()
        self.affiche_bordure()
        self.grille()

    def affiche_bordure(self):
        pygame.draw.rect(self.window, self.colorWhite,
                         pygame.Rect(0, 0, self.screen_width, 2))

        pygame.draw.rect(self.window, self.colorGrey,
                         pygame.Rect(self.bordure, 10, self.screen_width - 2*self.bordure, 2))

        pygame.draw.rect(self.window, self.colorWhite,
                         pygame.Rect(self.bordure-2, self.hauteur-self.bordure, self.screen_width - 2*self.bordure+2, 2))

        pygame.draw.rect(self.window, self.colorGrey,
                         pygame.Rect(self.bordure, self.hauteur-2, self.screen_width - 2*self.bordure, 2))

        pygame.draw.rect(self.window, self.colorWhite,
                         pygame.Rect(10, self.screen_height - self.bordure, self.screen_width - 2 * self.bordure + 4, 2))

        pygame.draw.rect(self.window, self.colorGrey,
                         pygame.Rect(0, self.screen_height - 2, self.screen_width, 2))

        # self.longueur
        pygame.draw.rect(self.window, self.colorWhite,
                         pygame.Rect(0, 0, 2, self.screen_height))

        pygame.draw.rect(self.window, self.colorGrey,
                         pygame.Rect(10, self.hauteur-2, 2, self.screen_height - self.hauteur - self.bordure + 2))

        pygame.draw.rect(self.window, self.colorWhite,
                         pygame.Rect(self.screen_width - self.bordure, self.hauteur-2,  2, self.screen_height - self.hauteur - self.bordure + 2))

        pygame.draw.rect(self.window, self.colorGrey,
                         pygame.Rect(self.screen_width - 2, 0,  2, self.screen_height))

        pygame.draw.rect(self.window, self.colorWhite,
                         pygame.Rect(self.screen_width - self.bordure, 10,  2, self.hauteur - 2*self.bordure + 4))

        pygame.draw.rect(self.window, self.colorGrey,
                         pygame.Rect(10, 10,  2, self.hauteur - 2*self.bordure + 2))

    def grille(self):
        # On affiche le tableau
        for i in range(self.largeur):
            for y in range(self.longueur):
                self.window.blit(self.sprite.getbloc_full(),
                                 (16*i+self.bordure, 16*y+self.hauteur))

        self.window.blit(self.sprite.getsmiley_happy(), ((self.screen_width/2) -
                                                         self.smiley/2, self.hauteur/2 - self.smiley/2))

        for i in range(3):
            self.window.blit(self.sprite.getdigit_0(),
                             (self.screen_width - (i * self.digit_x) - self.digit_x - self.bordure, self.hauteur/2 - self.digit_y/2))

        # Calcul le nombre de bombes restantes
        self.nb_bombes = list(str(self.nb_mines))
        for i in range(3-len(self.nb_bombes)):
            self.nb_bombes.insert(0, '0')
        # Affiche le nombre de bombes restantes
        for i in range(len(self.nb_bombes)):
            self.window.blit(
                self.sprite.printNumber(i, self.nb_bombes), (i*self.digit_x + self.bordure, self.hauteur/2 - self.digit_y/2))

        while self.run:
            # event during game
            for event in pygame.event.get():
                # timer tout les secondes
                if not self.genere and self.lose == False and self.win == False:
                    self.seconds = (pygame.time.get_ticks() -
                                    self.start_ticks)/1000
                    nb_sec = list(str(math.floor(self.seconds)))
                    for i in range(3-len(nb_sec)):
                        nb_sec.insert(0, '0')
                    for i in range(len(nb_sec)):
                        self.window.blit(self.sprite.printNumber(i, nb_sec),
                                         (self.screen_width - (i * self.digit_x) - self.digit_x - self.bordure, self.hauteur/2 - self.digit_y/2))
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self.left:
                    x, y = event.pos
                    y -= self.hauteur
                    x -= self.bordure
                    # affiche le shock si on est dans le jeux
                    if self.lose == False and self.win == False:
                        if y >= 0:
                            self.window.blit(self.sprite.getsmiley_shock(), ((self.screen_width/2) -
                                                                             self.smiley/2, self.hauteur/2 - self.smiley/2))
                        # si on est dans le menu affiche le btnclick si on click dessus
                        elif x + self.bordure < (self.screen_width/2) + self.smiley/2 and x + self.bordure > (self.screen_width/2) - self.smiley/2 and y + self.hauteur < (self.hauteur/2) + self.smiley/2 and y + self.hauteur > (self.hauteur/2) - self.smiley/2:
                            self.window.blit(self.sprite.getsmiley_happy_click(), ((self.screen_width/2) -
                                                                                   self.smiley/2, self.hauteur/2 - self.smiley/2))
                    elif self.win == False:
                        self.window.blit(self.sprite.getsmiley_lose(), ((self.screen_width/2) -
                                                                        self.smiley/2, self.hauteur/2 - self.smiley/2))

                elif event.type == pygame.MOUSEBUTTONUP and event.button == self.left:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    y -= self.hauteur
                    x -= self.bordure
                    pos_x, pos_y = int(x / 16), int(y / 16)

                    # si on est dans le jeu
                    if y >= 0:

                        while self.genere:
                            self.demineur = Generation(
                                self.longueur, self.largeur, self.nb_mines, pos_x, pos_y)
                            self.genere = False
                            self.start_ticks = pygame.time.get_ticks()
                        if self.lose == False and self.win == False:
                            arrayHide = self.demineur.deleteCase(
                                pos_x, pos_y)

                        # Victoire
                        if self.demineur.getWin() == self.nb_mines:
                            self.win = True
                            self.window.blit(self.sprite.getsmiley_self.win(), ((self.screen_width/2) -
                                                                                self.smiley/2, self.hauteur/2 - self.smiley/2))

                        for i in range(len(arrayHide[0])):
                            for y in range(len(arrayHide)):
                                if arrayHide[y][i] != '*':
                                    # Si on perd
                                    if arrayHide[y][i] == 'B':
                                        for g in range(len(self.demineur.array[0])):
                                            for w in range(len(self.demineur.array)):
                                                if self.demineur.array[w][g] == 'b':
                                                    self.window.blit(
                                                        self.sprite.getbloc_mine(), (g*16+self.bordure, w*16+self.hauteur))
                                        self.window.blit(
                                            self.sprite.getbloc_mine_explode(), (i*16+self.bordure, y*16+self.hauteur))
                                        self.window.blit(self.sprite.getsmiley_lose(), ((self.screen_width/2) -
                                                                                        self.smiley/2, self.hauteur/2 - self.smiley/2))
                                        self.lose = True
                                    # affiche les autres numéro qui sont pas une bombes
                                    else:
                                        self.window.blit(
                                            eval(self.sprite.returnSprite(arrayHide[y][i])), (i*16+self.bordure, y*16+self.hauteur))
                    elif x + self.bordure < (self.screen_width/2) + self.smiley/2 and x + self.bordure > (self.screen_width/2) - self.smiley/2 and y + self.hauteur < (self.hauteur/2) + self.smiley/2 and y + self.hauteur > (self.hauteur/2) - self.smiley/2:
                        self.genere = True
                        self.lose = False
                        self.win = False
                        # Affiche un tableau de bloc plein
                        for i in range(self.largeur):
                            for y in range(self.longueur):
                                self.window.blit(self.sprite.getbloc_full(),
                                                 (16*i+self.bordure, 16*y+self.hauteur))
                        # Calcul le nombre de bombes restantes
                        self.nb_bombes = list(str(self.nb_mines))
                        for i in range(3-len(self.nb_bombes)):
                            self.nb_bombes.insert(0, '0')
                        # Affiche le nombre de bombes restantes
                        for i in range(len(self.nb_bombes)):
                            self.window.blit(
                                self.sprite.printNumber(i, self.nb_bombes), (i*self.digit_x + self.bordure, self.hauteur/2 - self.digit_y/2))

                    # Réaffiche le bon self.smiley
                    if self.lose == False and self.win == False:
                        self.window.blit(self.sprite.getsmiley_happy(), ((self.screen_width/2) -
                                                                         self.smiley/2, self.hauteur/2 - self.smiley/2))

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == self.right and self.lose == False and self.win == False:
                    # Set the x, y postions of the mouse click
                    x, y = event.pos
                    y -= self.hauteur
                    x -= self.bordure
                    pos_x, pos_y = int(x / 16), int(y / 16)
                    if not self.genere and y >= 0:
                        arrayHide = self.demineur.setFlagorInt(
                            pos_x, pos_y, self.nb_mines)
                        for i in range(len(arrayHide[0])):
                            for y in range(len(arrayHide)):
                                if arrayHide[y][i] == 'F':
                                    self.window.blit(
                                        self.sprite.getbloc_flag(), (int(i*16)+self.bordure, int(y*16)+self.hauteur))
                                if arrayHide[y][i] == 'I':
                                    self.window.blit(
                                        self.sprite.getbloc_interrogation(), (int(i*16)+self.bordure, int(y*16)+self.hauteur))
                                if arrayHide[y][i] == '*':
                                    self.window.blit(
                                        self.sprite.getbloc_full(), (int(i*16)+self.bordure, int(y*16)+self.hauteur))

                        # Calcul le nombre de bombes restantes
                        nb_bombe = self.nb_mines - self.demineur.getNb_Bombe()
                        self.nb_bombes = list(str(nb_bombe))
                        for i in range(3-len(self.nb_bombes)):
                            self.nb_bombes.insert(0, '0')
                 # Affiche le nombre de bombes restantes
                    for i in range(len(self.nb_bombes)):
                        self.window.blit(
                            self.sprite.printNumber(i, self.nb_bombes), (i*self.digit_x + self.bordure, self.hauteur/2 - self.digit_y/2))

                # Pour actualiser le click long
                if not self.genere and self.lose == False and self.win == False:
                    click = pygame.mouse.get_pressed()
                    # self.demineur.timestmp()
                    if click[0] == True:
                        cur = pygame.mouse.get_pos()
                        if cur[1]-self.hauteur >= 0:
                            y = cur[1]-self.hauteur
                            x = cur[0]-self.bordure
                            dem = self.demineur.getArrayHide()
                            if dem[int(y / 16)][int((x / 16))] == '*':
                                for i in range(len(dem[0])):
                                    for j in range(len(dem)):
                                        if dem[j][i] == '*':
                                            self.window.blit(
                                                self.sprite.getbloc_full(), (i*16+self.bordure, j*16+self.hauteur))
                                self.window.blit(
                                    self.sprite.getbloc_empty(), (int(x / 16)*16+self.bordure, math.floor(y/16)*16+self.hauteur))
                            else:
                                for i in range(len(dem[0])):
                                    for j in range(len(dem)):
                                        if dem[j][i] == '*':
                                            self.window.blit(
                                                self.sprite.getbloc_full(), (i*16+self.bordure, j*16+self.hauteur))
            pygame.display.update()
        return


Vue()
