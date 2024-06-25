import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def play_craps():
    die1, die2 = roll_dice()
    roll_sum = die1 + die2
    print(f"You rolled: {die1} + {die2} = {roll_sum}")

    if roll_sum == 7 or roll_sum == 11:
        print("You win!")
    elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
        print("Craps! You lose.")
    else:
        point = roll_sum
        print(f"Point set to {point}")

        while True:
            die1, die2 = roll_dice()
            roll_sum = die1 + die2
            print(f"You rolled: {die1} + {die2} = {roll_sum}")

            if roll_sum == point:
                print("You made point! You win!")
                break
            elif roll_sum == 7:
                print("You rolled a 7. You lose.")
                break

play_craps()
