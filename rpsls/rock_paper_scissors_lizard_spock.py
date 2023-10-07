# RockPaperScissors.py

import random
from enum import IntEnum


class Choice(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


CHOICES = [f"{choice.name}[{choice.value}]" for choice in Choice]
CHOICES_STR = ", ".join(CHOICES)

BEATS = {
    Choice.Rock: [
        Choice.Lizard,
        Choice.Scissors,
    ],
    Choice.Paper: [
        Choice.Spock,
        Choice.Rock,
    ],
    Choice.Scissors: [
        Choice.Lizard,
        Choice.Paper,
    ],
    Choice.Lizard: [
        Choice.Spock,
        Choice.Paper,
    ],
    Choice.Spock: [
        Choice.Scissors,
        Choice.Rock,
    ],
}

MESSAGES = {
    (Choice.Rock, Choice.Scissors): "crushes",
    (Choice.Rock, Choice.Lizard): "crushes",
    (Choice.Lizard, Choice.Spock): "poisons",
    (Choice.Lizard, Choice.Paper): "eats",
    (Choice.Paper, Choice.Spock): "disproves",
    (Choice.Paper, Choice.Rock): "covers",
    (Choice.Scissors, Choice.Paper): "cuts",
    (Choice.Scissors, Choice.Lizard): "decapitates",
    (Choice.Spock, Choice.Spock): "smashes",
    (Choice.Spock, Choice.Rock): "vapourises",
}


def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"It's a tie! Both users chose '{user_choice.name.lower()}'")
    else:
        # Beats[user_choice] is the list of throws that will trigger a win condition for user
        user_wins = computer_choice in BEATS[user_choice]

        if user_wins:
            verb = MESSAGES[(user_choice, computer_choice)]
            if computer_choice == 4:
                print(f"{user_choice.name} {verb} {computer_choice.name}, you win!")
            else:
                print(
                    f"{user_choice.name} {verb} {computer_choice.name.lower()}, you win!"
                )

        else:
            verb = MESSAGES[(computer_choice, user_choice)]
            if user_choice == 4:
                print(f"{computer_choice.name} {verb} {user_choice.name}, you loose!")
            else:
                print(
                    f"{computer_choice.name} {verb} {user_choice.name.lower()}, you loose!"
                )


while True:
    print("Make your throw")
    try:
        value = input(f"  Enter a choice ({CHOICES_STR}): ")
        user_choice = Choice(int(value))
    except ValueError:
        print(f"\nYou typed '{value}' which isn't a valid choice.")
        continue

    value = random.randint(0, len(Choice) - 1)
    computer_choice = Choice(value)
    show_winner(user_choice, computer_choice)

    again = input("\nWant some more? (y/n): ")
    if again.lower() == "n":
        break

    print()

print("\nGoodbye and thanks for playing!!")
