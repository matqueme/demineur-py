import pygame


class Sprites():
    def __init__(self):
        self.filename = './sprites.png'
        PIXEL = 17

        DIGIT_X = 14
        DIGIT_Y = 24

        SMILEY = 25
        sprite_sheet = pygame.image.load(self.filename).convert_alpha()

        self.bloc_full = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 0, 50)
        self.bloc_empty = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 17, 50)
        self.bloc_flag = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 34, 50)
        self.bloc_interrogation = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 51, 50)
        self.bloc_mine = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 85, 50)
        self.bloc_mine_explode = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 102, 50)
        self.bloc_number_1 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 0, 67)
        self.bloc_number_2 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 17, 67)
        self.bloc_number_3 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 34, 67)
        self.bloc_number_4 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 51, 67)
        self.bloc_number_5 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 68, 67)
        self.bloc_number_6 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 85, 67)
        self.bloc_number_7 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 102, 67)
        self.bloc_number_8 = self.get_image(
            sprite_sheet, PIXEL, PIXEL, 119, 67)

        self.digit_1 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 0, 0)
        self.digit_2 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 14, 0)
        self.digit_3 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 28, 0)
        self.digit_4 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 42, 0)
        self.digit_5 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 56, 0)
        self.digit_6 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 70, 0)
        self.digit_7 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 84, 0)
        self.digit_8 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 98, 0)
        self.digit_9 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 112, 0)
        self.digit_0 = self.get_image(
            sprite_sheet, DIGIT_X, DIGIT_Y, 126, 0)

        self.smiley_happy = self.get_image(
            sprite_sheet, SMILEY, SMILEY, 1, 25)
        self.smiley_happy_click = self.get_image(
            sprite_sheet, SMILEY, SMILEY, 28, 25)
        self.smiley_shock = self.get_image(
            sprite_sheet, SMILEY, SMILEY, 55, 25)
        self.smiley_win = self.get_image(
            sprite_sheet, SMILEY, SMILEY, 82, 25)
        self.smiley_lose = self.get_image(
            sprite_sheet, SMILEY, SMILEY, 109, 25)

    def get_image(self, sheet, width, height, pos_x_image, pos_y_image):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (pos_x_image,
                   pos_y_image, width, height))
        return image

    def printNumber(self, i, nb_bombes):
        if nb_bombes[i] == '1':
            digit = self.digit_1
        elif nb_bombes[i] == '2':
            digit = self.digit_2
        elif nb_bombes[i] == '3':
            digit = self.digit_3
        elif nb_bombes[i] == '4':
            digit = self.digit_4
        elif nb_bombes[i] == '5':
            digit = self.digit_5
        elif nb_bombes[i] == '6':
            digit = self.digit_6
        elif nb_bombes[i] == '7':
            digit = self.digit_7
        elif nb_bombes[i] == '8':
            digit = self.digit_8
        elif nb_bombes[i] == '9':
            digit = self.digit_9
        elif nb_bombes[i] == '0':
            digit = self.digit_0
        return digit

    def getbloc_full(self): return self.bloc_full
    def getbloc_empty(self): return self.bloc_empty
    def getbloc_flag(self): return self.bloc_flag
    def getbloc_interrogation(self): return self.bloc_interrogation
    def getbloc_mine(self): return self.bloc_mine
    def getbloc_mine_explode(self): return self.bloc_mine_explode
    def getbloc_number_1(self): return self.bloc_number_1
    def getbloc_number_2(self): return self.bloc_number_2
    def getbloc_number_3(self): return self.bloc_number_3
    def getbloc_number_4(self): return self.bloc_number_4
    def getbloc_number_5(self): return self.bloc_number_5
    def getbloc_number_6(self): return self.bloc_number_6
    def getbloc_number_7(self): return self.bloc_number_7
    def getbloc_number_8(self): return self.bloc_number_8
    def getdigit_1(self): return self.digit_1
    def getdigit_2(self): return self.digit_2
    def getdigit_3(self): return self.digit_3
    def getdigit_4(self): return self.digit_4
    def getdigit_5(self): return self.digit_5
    def getdigit_6(self): return self.digit_6
    def getdigit_7(self): return self.digit_7
    def getdigit_8(self): return self.digit_8
    def getdigit_9(self): return self.digit_9
    def getdigit_0(self): return self.digit_0
    def getsmiley_happy(self): return self.smiley_happy
    def getsmiley_happy_click(self): return self.smiley_happy_click
    def getsmiley_shock(self): return self.smiley_shock
    def getsmiley_win(self): return self.smiley_win
    def getsmiley_lose(self): return self.smiley_lose
