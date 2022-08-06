

def get_complete_colours(word:str, goal_word:str):

    assert len(word) == 5, "word must be 5 letters long"
    assert len(goal_word) == 5, "goal word must be 5 letters long"

    col_list = [0,0,0,0,0]
    for i, char in enumerate(word):
        print(goal_word.count(char))

    return


def word_to_dict(text:str):
    text = text.upper()
    temp_dict = {}
    for char in text:
        temp_dict[char] = [i for i, c in enumerate(text) if c == char]

    return temp_dict


if __name__ == "__main__":

    word = "masts"
    goal_word = "sassy"
    get_complete_colours(word, goal_word)
    print(word_to_dict(word))
    print(word_to_dict(goal_word))