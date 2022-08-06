import pygame as pg


class Square(pg.sprite.Sprite):

    def __init__(self, x_:int, y_:int, char:str, dims:tuple, font_size:int):
        super().__init__()

        self.font = pg.font.Font(None, font_size)
        self.x = x_
        self.y = y_
        self.char = char

        self.image = self.font.render(self.char, False, (64, 64, 64))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.background = pg.Rect(*dims)
        self.background.center = (self.x, self.y)

        self.last_drawn = False

        self.border_colour = (200, 200, 200)
        self.background_colour = (252, 252, 252)

        return

    def change_render(self, text:str):

        if self.char != text.upper():
            self.char = text.upper()
            self.image = self.font.render(self.char, False, (64, 64, 64))
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.last_drawn = True
        else:
            self.last_drawn = False

        return

    def set_border_colour(self, colour:tuple):
        self.border_colour = colour

    def set_background_colour(self, colour:tuple):
        self.background_colour = colour

    def draw(self, surface):

        pg.draw.rect(surface, self.background_colour, self.background)
        pg.draw.rect(surface, self.border_colour, self.background, 2)

        surface.blit(self.image, self.rect)
        return

    def update(self):

        return
