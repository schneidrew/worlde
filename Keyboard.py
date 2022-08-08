import pygame as pg
from Square import Square


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
                y_ = 675 + row*self.dim
                self.char_group.add(Square(x_, y_, char_, (0, 0, self.len, self.len), 24))
        return

    def update_char_status(self, char_:str, new_status:str):
        for char in self.char_group:
            if char.char.upper() == char_.upper():
                char.set_status(new_status)

    def update_colours(self, guess:str, goal_word:str):
        for index, char in enumerate(guess):
            if char in goal_word:
                if goal_word[index] == char:
                    self.update_char_status(char, "correct")
                else:
                    self.update_char_status(char, "partial")
            else:
                self.update_char_status(char, "incorrect")

    def draw_keyboard(self, surface):
        for char in self.char_group:
            char.draw(surface)
        return

    def update(self):
        self.update_word()

