import pygame as pg


class Square(pg.sprite.Sprite):

    def __init__(self, guess:int, letter:int):
        super().__init__()

        self.font = pg.font.Font(None, 50)
        self.dimension = 30
        self.x = (letter)*70 + 90
        self.y = (guess)*70 + 90
        self.char = ""

        self.image = self.font.render(self.char, False, (64, 64, 64))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.background = pg.Rect(0,0, 60, 60)
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

    def change_colours(self, **kwargs):
        for key, value in kwargs.items():
            if key.upper().strip() == 'BORDER':
                self.border_colour = value
            elif key.upper().strip() == 'BACKGROUND':
                self.background_colour = value
            else:
                print(f"no colour change could be made for {key}")

    def draw(self, surface):

        pg.draw.rect(surface, self.background_colour, self.background)
        pg.draw.rect(surface, self.border_colour, self.background, 2)

        surface.blit(self.image, self.rect)
        return

    def update(self):

        return
