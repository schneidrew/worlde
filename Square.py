import pygame as pg


class Square(pg.sprite.Sprite):

    def __init__(self, x_:int, y_:int, char:str, dims:tuple, font_size:int):
        super().__init__()

        self.font = pg.font.Font(None, font_size)
        self.x = x_
        self.y = y_
        self.char = char
        self.status = "neutral"
        self.rotate = 1

        self.image = self.font.render(self.char, False, (64, 64, 64))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.background = pg.Rect(*dims)
        self.background.center = (self.x, self.y)

        self.shake_timer_pos = 0
        self.shake_time_neg = 0

        self.last_drawn = False

        self.colours = {

            "neutral": {
                "order": 0,
                "border": (200, 200, 200),
                "background": (252, 252, 252)
            },

            "progress": {
                "order": 1,
                "border": (101, 157, 181),
                "background": (252, 252, 252)
            },

            "incorrect": {
                "order": 3,
                "border": (200, 200, 200),
                "background": (200, 200, 200)
            },

            "partial": {
                "order": 2,
                "border": (250, 222, 132),
                "background": (250, 222, 132)
            },

            "correct": {
                "order": 3,
                "border": (145, 227, 179),
                "background": (145, 227, 179)
            }
        }

        self.set_colours_status()

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

    def set_status(self, status:str):
        assert status in self.colours.keys(), f"Status must be in: {self.colours.keys()}"
        if self.colours[status]['order'] > self.colours[self.status]['order']:
            self.status = status
            self.set_colours_status()

    def set_border_colour(self, colour:tuple):
        self.border_colour = colour

    def set_background_colour(self, colour:tuple):
        self.background_colour = colour

    def set_colours_status(self):
        self.border_colour = self.colours[self.status]['border']
        self.background_colour = self.colours[self.status]['background']

    def get_border_colour(self):
        return self.border_colour

    def get_background_colour(self):
        return self.background_colour

    def set_shake_timer(self, time_:int):
        assert time_ >= 0, f"Time variable must be greater than 0. Supplied value is: {time_}"

        if (self.shake_timer_pos == 0) & (self.shake_time_neg == 0):
            self.shake_timer_pos = time_
            self.shake_time_neg = time_
        else:
            pass

    def shake_update(self, dir:int = 1):

        if self.shake_timer_pos > 0:
            self.x += 2*dir
            self.shake_timer_pos -= 1
        elif self.shake_time_neg > 0:
            self.x -= 2*dir
            self.shake_time_neg -= 1

    def draw(self, surface):

        self.shake_update()
        self.background.center = (self.x, self.y)
        self.rect.center = (self.x, self.y)

        pg.draw.rect(surface, self.background_colour, self.background)
        pg.draw.rect(surface, self.border_colour, self.background, 2)

        surface.blit(self.image, self.rect)
        return

    def update(self):

        return
