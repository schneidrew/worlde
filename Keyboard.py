import pygame as pg
from square import Square



class Keyboard(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.len = 40
        self.dim = self.len + 6
        self.key_groups = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        self.row_offsets = {0: 0, 1: self.dim/2, 2: self.dim*1.5}


        self.char_group = pg.sprite.Group()
        for row, group_ in enumerate(self.key_groups):
            for num, char_ in enumerate(group_):
                x_ = 90 + num*self.dim + self.row_offsets[row]
                y_ = 625 + row*self.dim
                self.char_group.add(Square(x_, y_, char_, (0, 0, self.len, self.len), 30))

        self.neutral_background = (252, 252, 252)
        self.neutral_border = (200, 200, 200)
        self.progress_border = (101, 157, 181)
        self.correct_background = (145, 227, 179)
        self.partial_background = (250, 222, 132)

        return

    def draw_keyboard(self, surface):
        for char in self.char_group:
            char.draw(surface)
        return

    def update(self):
        self.update_word()

