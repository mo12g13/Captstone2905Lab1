import random

# A method for guessing the number game


def guest_number():
    number_of_times = 1  # number of tries variable
    # player name for the game
    player_name = input("Please enter your name: ")
    # The random number generator
    random_number = random.randint(1, 50)
    while True:

        # Try and caught the error if the user doesn't enter an integer
        try:
            player_guest = int(input("Please a guess from 1-50"))

        except ValueError:
            # Instruct the user to enter a number
            print("Please enter an integer")
            continue
        # Condition that checks and see if the player guest is equal to the random number
        if player_guest == random_number:
            print("{} you guessed the right number in {} tries!".format(player_name, number_of_times))
            break
        # Condition that checks to see if the player guest is less than random number
        elif player_guest < random_number:
            print("{},  your guest is too low".format(player_name))
        # Condition that checks to see if the player guest is greater than the random number
        elif player_guest > random_number:
            print("{}, your guest is too high".format(player_name))
        number_of_times+=1

if __name__ == '__main__':

    guest_number()



