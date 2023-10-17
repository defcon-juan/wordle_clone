# wrdyl.py

import pathlib
import random
from string import ascii_letters

WORDLIST = pathlib.Path("wordlist.txt")

words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf-8").split("\n")
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
]

word = random.choice(words)


for guess_num in range(1, 7):
    guess = input("Guess a word: ").upper()
    if guess == word:
        print("Correct")
        break
    # using set comprehension to organise letters
    # newSet= { expression for element in  iterable if condition}

    # Description of the syntax:

    # The iterable may be any iterable object or data structure in Python from which we have to use the elements to create the new set.
    # The condition is a conditional expression using
    # The element denotes the element from the iterable that has to be included in the set.
    # The expression can be any mathematical expression derived from the element.
    # newSet is the name of the new set which has to be created from the elements of the iterable.

    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }

    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))
    print("\n")
else:
    print(f"The word was {word}")
