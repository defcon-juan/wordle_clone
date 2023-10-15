# rock_paper_scissors_lizard_spock.py

import random
from enum import IntEnum

wins = 0

losses = 0

draws = 0

win_rate_percent = 0


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
    (Choice.Spock, Choice.Scissors): "smashes",
    (Choice.Spock, Choice.Rock): "vapourises",
}


def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        if user_choice == 4:
            print(
                f"\nIt's a draw! Both players chose {user_choice.name}"
            )  # logic for capitalising spocks name

        else:
            print(f"\nIt's a draw! Both players chose {user_choice.name.lower()}")

    else:
        # If the computer choice is a value based on the user_choice key, the user wins
        user_wins = computer_choice in BEATS[user_choice]

        if user_wins:
            # access the messages dictionary with the tuple of user choice and computer choice as a key
            # the value of that key is then used as the verb in the message to the user
            verb = MESSAGES[(user_choice, computer_choice)]
            if computer_choice == 4:
                print(
                    f"\n{user_choice.name} {verb} {computer_choice.name}, you win!"
                )  # logic for capitalising spocks name
            else:
                print(
                    f"\n{user_choice.name} {verb} {computer_choice.name.lower()}, you win!"
                )

        else:
            verb = MESSAGES[(computer_choice, user_choice)]
            if user_choice == 4:
                print(
                    f"\n{computer_choice.name} {verb} {user_choice.name}, you lose!"
                )  # logic for capitalising spocks name
            else:
                print(
                    f"\n{computer_choice.name} {verb} {user_choice.name.lower()}, you lose!"
                )


while True:
    # display the wins, losses, draws and win rate to the user
    print(
        "\n"
        + str(wins)
        + "  Wins ||  "
        + str(losses)
        + "  Losses ||  "
        + str(draws)
        + "  Draws ||  "
        + f"Win rate = {win_rate_percent}%  \n"
    )
    print("Make your throw\n")
    try:
        value = input(f"  Enter a choice ({CHOICES_STR}): ")
        user_choice = Choice(int(value))
    except ValueError:
        print(f"\nYou typed '{value}' which isn't a valid choice.")
        continue

    value = random.randint(0, len(Choice) - 1)
    computer_choice = Choice(value)
    show_winner(user_choice, computer_choice)

    # Logic for wins draws and losses

    if user_choice == computer_choice:
        draws += 1
    else:
        win_condition = computer_choice in BEATS[user_choice]
        if win_condition:
            wins += 1
        else:
            losses += 1
    # calculate win percentage to 2 decimal places

    win_rate_percent = round(((wins / (wins + losses + draws)) * 100), 2)

    again = input("\nWant some more? (y/n): ")
    if again.lower() == "n":
        break

    print()

print("\nGoodbye and thanks for playing!!\n")
