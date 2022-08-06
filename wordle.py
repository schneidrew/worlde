import pygame as pg
from sys import exit
from word import Word
from Keyboard import Keyboard
from random import choice

word_len = 5
num_tries = 7

legal_words = set()
with open('word_data/word_list') as word_file:
    for word in word_file:
        word = word.strip().upper()
        if len(word) == word_len:
            legal_words.add(word)

answer_words = set()
with open('word_data/answer_list') as answer_file:
    for word in answer_file:
        word = word.strip().upper()
        if len(word) == word_len:
            answer_words.add(word)

goal_word = choice(tuple(answer_words))
print(goal_word)

game_active = True

pg.init()
screen = pg.display.set_mode((600, 800))
screen.fill((252,250,252))
pg.display.set_caption("Wordle-Copy")
clock = pg.time.Clock()


word_group = pg.sprite.Group()
for i in range(1,num_tries):
    word_group.add(Word(i, word_len))

for word_ in word_group:
    word_.draw_word(screen)

kb = Keyboard()
kb.draw_keyboard(screen)

def set_next_in_progress(w_group):
    for w in w_group:
        if not w.inProgress and not w.isComplete:
            w.set_in_progress()
            break
    return w_group


def check_game_active(w_group):
    for w in w_group:
        if w.isComplete:
            if w.isCorrect:
                return False
    return True

set_next_in_progress(word_group)

while True:

    if game_active:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.KEYDOWN:
                key_ = pg.key.name(event.key)
                if key_.upper().isalpha() and len(key_) < 2:
                    for word_ in word_group.sprites():
                        if word_.inProgress:
                            word_.add_letter(key_)
                            word_.draw_word(screen)

                if event.key == pg.K_BACKSPACE or event.key == pg.K_DELETE:
                    for word_ in word_group.sprites():
                        if word_.inProgress:
                            word_.rm_letter()
                            word_.draw_word(screen)

                if event.key == pg.K_RETURN:
                    for word_ in word_group.sprites():
                        if word_.inProgress:
                            if word_.check_complete():
                                if word_.word in legal_words:
                                    word_.set_complete(goal_word)
                                    set_next_in_progress(word_group)
                                    word_.check_match(goal_word)
                                else:
                                    print("Illegal Word")
                                break

        word_group.update()
        for word_ in word_group:
            word_.draw_word(screen)

        game_active = check_game_active(word_group)

    else:
        print(goal_word)
        pg.quit()
        exit()

    pg.display.update()
    clock.tick(60)

