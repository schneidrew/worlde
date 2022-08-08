

def get_complete_colours(guess:str, goal_word:str):

    guess, goal_word = guess.strip().upper(), goal_word.strip().upper()
    assert len(guess) == len(goal_word), "the two words must be of the same length"

    colours = ["neutral"]*len(guess)

    char_dict = get_char_dict(guess, goal_word)

    for char, dict_ in char_dict.items():
        counter = 0
        if not dict_['goal']:
            for index in dict_['guess']:
                colours[index] = 'incorrect'
        else:
            for index in dict_['guess']:
                if index in dict_['goal']:
                    colours[index] = 'correct'
                    counter += 1
                else:
                    pass
            for index in dict_['guess']:
                if index not in dict_['goal']:
                    if counter < len(dict_['goal']):
                        colours[index] = 'partial'
                        counter += 1
                    else:
                        colours[index] = 'incorrect'

    assert "neutral" not in colours, "None of the colours can remain neutral"
    return colours


def get_char_dict(guess:str, goal:str):
    char_dict = {}
    for i, char in enumerate(guess):
        temp_dict = {}
        temp_dict['guess'] = [i for i, c in enumerate(guess) if c == char]
        temp_dict['goal'] = [i for i, c in enumerate(goal) if c == char]
        char_dict[char] = temp_dict
    return char_dict


if __name__ == "__main__":

    guess = "syssa"
    goal_word = "masty"
    get_complete_colours(guess, goal_word)
