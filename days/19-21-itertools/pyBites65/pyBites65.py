import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('./', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    actual_words = []
    for potential_word in _get_permutations_draw(draw):
        if potential_word in dictionary:
            actual_words.append(potential_word)
    if len(actual_words) == 1:
        return actual_words[0]
    else:
        return tuple(actual_words)

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw = [letter.lower().strip() for letter in draw]
    no_repeat_perms = []
    num_letters = len(draw)
    for num in range(2,num_letters+1):
        for letters in itertools.permutations(draw, num):
            word = "".join(letters)
            if word not in no_repeat_perms:
                no_repeat_perms.append(word)
    return no_repeat_perms

if __name__ == "__main__":
    print(get_possible_dict_words(["T", "I", "I", "G", "T", "T", "L"]))
