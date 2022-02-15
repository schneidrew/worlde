import pygame as pg
from square import Square


class Word(pg.sprite.Sprite):
    def __init__(self, word_num:int, len_:int=5):
        super().__init__()

        self.char_group = pg.sprite.Group()
        for i in range(1, len_+1):
            self.char_group.add(Square(word_num, i))

        self.char_list = []
        self.word = ""
        self.isComplete = False
        self.inProgress = False

        self.neutral_background = (252, 252, 252)
        self.neutral_border = (200, 200, 200)
        self.progress_border = (101, 157, 181)
        self.correct_background = (145, 227, 179)
        self.partial_background = (250, 222, 132)

        return

    def set_in_progress(self):
        self.inProgress = True
        for char in self.char_group:
            char.change_colours(border=self.progress_border)
        return

    def check_complete(self):
        if self.inProgress:
            if "" not in self.char_list:
                return True
        return False

    def set_complete(self, goal_word):
        if self.check_complete():
            self.isComplete = True
            self.inProgress = False
            for n, char in enumerate(self.char_group):
                new_colour = self.get_complete_char_colour(char.char, n, goal_word)
                char.change_colours(border=new_colour, background=new_colour)
        return

    def get_complete_char_colour(self, char, index, goal_word):

        if char in goal_word:
            if goal_word[index] == char:
                return self.correct_background
            else:
                return self.partial_background
        else:
            return self.neutral_border

    def update_word(self):
        self.char_list = [sqr.char for sqr in self.char_group]
        self.word = "".join(self.char_list).strip().upper()
        return

    def add_letter(self, letter:str):
        assert len(letter) < 2, f"{letter} is longer than 1 character"
        for char in self.char_group:
            if char.char == "":
                char.change_render(letter)
                break
        return

    def rm_letter(self):
        for char in reversed(self.char_group.sprites()):
            if char.char != "":
                char.change_render("")
                break
        return

    def draw_word(self, surface):
        for char in self.char_group:
            char.draw(surface)
        return

    def check_match(self, goal_word:str):

        if goal_word.strip().upper() == self.word.upper().strip():
            print("Word is a match!")
            return True
        else:
            print("word is not a match!")
            return False

    def update(self):
        self.update_word()

