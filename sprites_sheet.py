import pygame


class sprites_sheet():
    # def __init__(self) -> None:
    #     filename = './sprites.png'
    #     PIXEL = 17

    #     DIGIT_X = 14
    #     DIGIT_Y = 24

    def get_image(sheet, width, height, pos_x_image, pos_y_image):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (pos_x_image,
                   pos_y_image, width, height))
        return image

    # sprite_sheet = pygame.image.load(filename).convert_alpha()
    # self.bloc_full = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 0, 50)
    # self.bloc_empty = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 17, 50)
    # self.bloc_flag = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 34, 50)
    # self.bloc_interrogation = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 51, 50)
    # self.bloc_mine = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 85, 50)
    # self.bloc_mine_explode = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 102, 50)
    # self.bloc_number_1 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 0, 67)
    # self.bloc_number_2 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 17, 67)
    # self.bloc_number_3 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 34, 67)
    # self.bloc_number_4 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 51, 67)
    # self.bloc_number_5 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 68, 67)
    # self.bloc_number_6 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 85, 67)
    # self.bloc_number_7 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 102, 67)
    # self.bloc_number_8 = sprites_sheet.get_image(
    #     sprite_sheet, PIXEL, PIXEL, 119, 67)

    # self.digit_1 = sprites_sheet.get_image(
    #     sprite_sheet, DIGIT_X, DIGIT_Y, 0, 0)
    # self.digit_2 = sprites_sheet.get_image(
    #     sprite_sheet, DIGIT_X, DIGIT_Y, 14, 0)
