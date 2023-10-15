# start.py

for guess_num in range(1, 7):
    guess = input("\nGuess a word: ").upper()
    if guess == "SNAKE":
        print("Correct")
        break
    else:
        print("Wrong")
