# wrdyl.py

import pathlib
import random
from string import ascii_letters


def main():
    # pre-process - everything before main loop runs
    word = get_random_word()

    # process (main loop)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            break

    # post-process - clean up after main loop
    else:
        game_over(word)


def get_random_word():
    wordlist = pathlib.Path(__file__).parent / "wordlist.txt"

    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]

    return random.choice(words)


def show_guess(guess, word):
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


def game_over(word):
    print(f"THe word was {word}")


if __name__ == "__main__":
    main()
