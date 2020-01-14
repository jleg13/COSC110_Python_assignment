#!/usr/bin/env python3

"""RWX Game
This program is a number Guessing game."""

import random
import string
import pickle


def rand_generator(num_str, tar_str):
    """This function generates a random string of digits by recursively
    calling itself until the string is 3 digits long."""
    if len(tar_str) == 3:
        return tar_str
    else:
        rand = random.randint(0, len(num_str)-1)
        new_target_str = tar_str + num_str[rand]
        # slice out the selected digit to ensure unique digits
        num_str_slice = num_str[:rand] + num_str[rand+1:]
        return rand_generator(num_str_slice, new_target_str)


def player_guess(tar_str):
    """This function takes in one parameter, the randomly generated 3 digit
    string. In a while loop the player is promted to make valid guesses until
    they guess correct or the score drops below 1000. The get_hint() function is
    called from within the loop. The function will return the player guess_lst.
    """
    guess_lst = []
    while len(guess_lst) == 0 or guess_lst[-1] != tar_str:
        if len(guess_lst) == 23:  # Points dropped below 1000 on guess 23
            break
        elif len(guess_lst) > 0:
            print("\nYour guess, {0}, was incorrect".format(''.join(guess_lst[-1])))
            hint = get_hint(guess_lst[-1], tar_str)
            print(hint)
        while True:
            num_guess = input("Please enter a guess: ")
            if is_valid_guess(num_guess) is True:
                guess_lst.append(num_guess)
                break
    return guess_lst  # list returned will be between 1 and 23 entries


def is_valid_guess(guess):
    """This function takes one parameter, the input for a guess. A valid guess
    will be 3 unique numerical digits."""
    unique_digits = []
    try:
        assert guess.isdigit()
        assert len(guess) == 3
        for digit in guess:
            if digit in unique_digits:
                return False, print("Invalid guess! The 3 digits must be unique")
            unique_digits.append(digit)
        return True
    except (ValueError, AssertionError):
        return False, print("Invalid guess! Please enter 3 digits from 0-9")


def get_hint(guess, target):
    """This function takes two parameters. The validated 3 digit guess string and
    the the 3 digit target string. Using nested loops the comparison is made,
    composing the appropriate hint depending on the results. A hint is returned.
    """
    hint = []
    for index_i, value_i in enumerate(guess):
        for index_j, value_j in enumerate(target):
            if value_i == value_j and index_i == index_j:
                hint.append('R')
            elif value_i == value_j:
                hint.append('X')
    if len(hint) == 0:
        hint.append('W')
    hint.sort()  # sort the hint list alphabetically
    # .join() creates a string from hint list
    return "Your current hint is: {0}\n".format(''.join(hint))


def calculate_score(guesses, tar_str):
    """This function takes two parameters, a list containing all
    the players guesses and the 3 digit target string. A score is calculated
    and printed to the player. The function returns the float value of the
    points """
    points = 10000
    if len(guesses) == 1:
        print("\n-----TOP SCORE-----\n")
        print("You guessed the correct answer in 1 try and scored 10000 points.\n")
        return points
    elif len(guesses) == 23 and guesses[-1] == tar_str:
        print("Sorry, the game is now over.")
        print(
            "The correct answer was {0}, but your score is below 1000 points.\n".format(tar_str))
        return
    elif len(guesses) == 23:
        print("Sorry, the game is now over.")
        print(
            "The correct answer was {0}, but you didn't guess it in 23 attempts.\n".format(tar_str))
        return
    else:
        print("\nCongratulations!")
        print("{0} was the correct answer!".format(guesses[-1]))
        for i in range(1, len(guesses)):
            points -= (points/100)*10  # reduction in points score of 10% per guess
        print("You guessed the correct answer in {0} tries and scored {1:.2f} points.\n".format(
            len(guesses), points))
        return points


def high_scores(score):
    """This function takes one parameter, the float value of the points received
    by the player. The high_scores.txt file is accessed to get a dictionary of
    highscores. The players score is checked to see if it is high enough to
    make the top 5 list. If it isn't the function exits, if it is the dictionary
    is updated and written to file. """
    if score is None:
        return
    highscores = read_in()  # accesses dictionary of highscores
    if len(highscores) < 5:
        name = add_name(highscores)
        highscores[name.upper()] = score
    else:
        #  'key=' sets the way to sort the values in the min(method).
        #  'key=highscores.get' means the list will be sorted by values of the dictionary.
        lowest = min(highscores, key=highscores.get)
        if highscores[lowest] <= score:
            name = add_name(highscores)
            highscores[name.upper()] = score
            highscores.pop(lowest)
        else:
            return
    top_scores(highscores)
    write_out(highscores)


def read_in():
    """This function opens the file high_scores.txt by unpickling the file. A
    dictionary containing the highscores is returned. If the file is empty an
    empty dictionary is returned"""
    try:
        with open('high_scores.txt', 'rb') as file_in:
            highscores = pickle.load(file_in)
            return highscores
    except EOFError:
        return {}


def write_out(scores):
    """This function takes in one parameter, the updated dictionary of
    highscores. The dictionary is pickled into the highscores file."""
    with open('high_scores.txt', 'wb') as file_out:
        #  Selecting HIGHEST_PROTOCOL can make unpickling faster
        pickle.dump(scores, file_out, protocol=pickle.HIGHEST_PROTOCOL)


def top_scores(scores):
    """This function takes in one parameter, the dictionary of highscores and
    prints out the highscore table"""
    print("\n____Top Scores____")
    #  A list of tuples is created using a list comprehension
    sort_scores = [(value, key) for key, value in scores.items()]
    sort_scores.sort(reverse=True)  # sort tuples by first element
    for value, key in sort_scores:
        print("{0}: {1:.2f} points".format(key, value))


def add_name(high):
    """This function takes in one parameter, the dictionary of highscores. The
    player is asked to enter a valid name (3 characters, that does not already
    exist). The valid 3 character name is returned."""
    while True:
        name = input("Please enter a 3 character name: ")
        try:
            assert len(name) == 3
            assert name.isalpha() is True
            if name.upper() not in high.keys():
                break
        except (AssertionError):
            print("Invalid name! Please enter a 3 letter name")
        else:
            print("Invalid name! Name already exists")
    return name


def play_RWX():
    """This function initiates the game and controls the function calls. It
    generates a random three digit string, allows the player to make guesses,
    calculates a score, checks the high score table and finally asks to play
    again."""
    print("""
  _______   __          __   __      __
 |   _   |  \  \  /\  /  /   \  \  /  /
 |  |_| _|   \  \/  \/  /     \  \/  /
 |  |\  \     \        /      /  /\  \\
 |__| \__\     \__/\__/      /__/  \__\\

  ----Welcome to the RWX Game!----

Your aim is to guess the target, consisting
        of 3 digits from 0-9

R | One or more R's means you have a correct character in the right place

W | means all the characters are in your guess are wrong

X | One or more X's means you have a correct character, but in the wrong place
""")
    # This empty string and 0-9 digit string allows the game to reset if the
    # player selects to play again
    target_str = ""
    digits = string.digits

    target = rand_generator(digits, target_str)
    guess = player_guess(target)
    score = calculate_score(guess, target)
    high_scores(score)
    while True:
        replay = input("\nWould you like to play again (Y/N)? ")
        try:
            assert replay.lower() == 'y' or replay.lower() == 'n'
        except AssertionError:
            print("Invalid Entry! Please enter 'y' or 'n'")
        else:
            break
    if replay.lower() == 'y':
        play_RWX()
    else:
        print("\n-----Thank you for playing!-----\n")


play_RWX()
