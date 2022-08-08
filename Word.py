import pygame as pg
from Square import Square


class Word(pg.sprite.Sprite):
    def __init__(self, word_num:int, len_:int=5):
        super().__init__()

        self.char_group = pg.sprite.Group()
        for i in range(1, len_+1):
            x_ = i*70 + 90
            y_ = word_num*70 + 90
            self.char_group.add(Square(x_, y_, "", (0, 0, 60, 60), 40))

        self.char_list = []
        self.word = ""
        self.isComplete = False
        self.inProgress = False

        self.isCorrect = False

        return

    def set_in_progress(self):
        self.inProgress = True
        for char in self.char_group:
            char.set_status("progress")
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
            self.set_complete_char_colour(goal_word)
        return

    def set_complete_char_colour(self, goal_word):

        for index, char in enumerate(self.char_group):

            if char.char in goal_word:
                if goal_word[index] == char.char:
                    char.set_status("correct")
                else:
                    char.set_status("partial")
            else:
                char.set_status("incorrect")

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

    def set_shake_time(self, time_):
        for char in self.char_group:
            char.set_shake_timer(time_)

    def draw_word(self, surface):
        for char in self.char_group:
            char.draw(surface)
        return

    def check_match(self, goal_word:str):

        if goal_word.strip().upper() == self.word.upper().strip():
            self.isCorrect = True
        return

    def update(self):
        self.update_word()

