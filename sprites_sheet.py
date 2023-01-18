import pygame

class sprites_sheet():
    def get_image(sheet, width, height, pos_x_image, pos_y_image):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (pos_x_image, pos_y_image, width, height))
        return image
