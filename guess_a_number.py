import random

# the number to guess is a random int between 0 and 100
number = random.randint(0, 100)

correct_guess = False
guess_counter = 0

while not correct_guess:
    # increase guess_counter with each loop
    guess_counter += 1
    # read user guess from input
    guess = int(input("Enter a number between 0 and 100: "))

    if guess == number:
        print("Congratulations!")
        print("You found the correct number!")
        print("You needed {} tries!".format(guess_counter))
        correct_guess = True  # end the loop, game over

    else:
        # if get the direction in which the correct number lies
        if guess < number:
            direction = "higher"
        else:
            direction = "lower"

        # give hint towards correct number, dependent on distance
        if abs(guess - number) < 10:
            print("You're close!")
            print("Just a little bit {}.".format(direction))
        elif abs(guess - number) < 25:
            print("Keep going!")
            print("The number you search is {}.".format(direction))
        else:
            print("Not even close!")
            print("You need to search way {}!".format(direction))


