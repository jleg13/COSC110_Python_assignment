###  Programming Task 2

# RWX Game
## Description:
This program is a game where the player tries to guess a 3 digit randomly
generated number. The player is given clues after each guess,
(W, X or R in different combinations) depending on their
progress of correctly guessing the correct digit and also the correct placing
in the sequence.

The player's score is based on how many attempts it takes to guess all three
digits. 10000 points for correctly guessing in one attempt, reducing by 10%
for each subsequent turn, down to 1000 points.

If the player achieves a high enough score they are asked to enter a name to
be added onto the top 5 high score table. Previous high scores are stored in a
separate high_scores.txt file.


## Installation:
[Python 3](https://www.python.org/downloads/) is a system requirement for this program to run.

The program is stored as a .tgz file so to extract the files copy the file to an empty directory, then from that directory use the following command:
```bash
tar -zxf a3.tgz
```
The zipped file contains three files:
- RWXGame.py
- README.md
- high_scores.txt

## Demo:

[![Run on Repl.it](https://repl.it/badge/github/jleg13/COSC110_Python_assignment)](https://repl.it/github/jleg13/COSC110_Python_assignment)

## Usage:

With the un-zipped files in the working directory, the project can be run using:
```bash
python3 RWXGame.py
```
Or as an executable file:
```bash
./RWXGame.py
```
The following program output demonstrates that the user input value for a guess must be:
- 3 numerical digits
- digits must be unique

The user input for the high score name must be:
- any 3 letters
- a name that doesn't already exist on the list.

The user input for restating the game must be:
- 'y' or 'Y'
- 'n' or 'N'

The output also shows that the user must guess within 23 guesses or game over is called because the score is below 1000.

```

  _______   __          __   __      __
 |   _   |  \  \  /\  /  /   \  \  /  /
 |  |_| _|   \  \/  \/  /     \  \/  /
 |  |\  \     \        /      /  /\  \
 |__| \__\     \__/\__/      /__/  \__\

  ----Welcome to the RWX Game!----

Your aim is to guess the target, consisting
        of 3 digits from 0-9

R | One or more R's means you have a correct character in the right place

W | means all the characters are in your guess are wrong

X | One or more X's means you have a correct character, but in the wrong place

Please enter a guess: hello
Invalid guess! Please enter 3 digits from 0-9
Please enter a guess: 12
Invalid guess! Please enter 3 digits from 0-9
Please enter a guess: 1234
Invalid guess! Please enter 3 digits from 0-9
Please enter a guess: 122
Invalid guess! The 3 digits must be unique
Please enter a guess: 222
Invalid guess! The 3 digits must be unique
Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: RR

Please enter a guess: 125

Your guess, 125, was incorrect
Your current hint is: R

Please enter a guess: 127

Your guess, 127, was incorrect
Your current hint is: R

Please enter a guess: 143

Your guess, 143, was incorrect
Your current hint is: R

Please enter a guess: 523

Your guess, 523, was incorrect
Your current hint is: RR

Please enter a guess: 723

Your guess, 723, was incorrect
Your current hint is: RR

Please enter a guess: 623

Your guess, 623, was incorrect
Your current hint is: RR

Please enter a guess: 823

Congratulations!
823 was the correct answer!
You guessed the correct answer in 8 tries and scored 4782.97 points.

Please enter a 3 character name: 123
Invalid name! Please enter a 3 letter name
Please enter a 3 character name: w
Invalid name! Please enter a 3 letter name
Please enter a 3 character name: wwww
Invalid name! Please enter a 3 letter name
Please enter a 3 character name: nam

____Top Scores____
DAD: 8100.00 points
JLG: 6561.00 points
ERT: 6561.00 points
QUO: 5904.90 points
NAM: 4782.97 points

Would you like to play again (Y/N)? t

Would you like to play again (Y/N)? 6

Would you like to play again (Y/N)? yes

Would you like to play again (Y/N)? y

  _______   __          __   __      __
 |   _   |  \  \  /\  /  /   \  \  /  /
 |  |_| _|   \  \/  \/  /     \  \/  /
 |  |\  \     \        /      /  /\  \
 |__| \__\     \__/\__/      /__/  \__\

  ----Welcome to the RWX Game!----

Your aim is to guess the target, consisting
        of 3 digits from 0-9

R | One or more R's means you have a correct character in the right place

W | means all the characters are in your guess are wrong

X | One or more X's means you have a correct character, but in the wrong place

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 245

Your guess, 245, was incorrect
Your current hint is: R

Please enter a guess: 267

Your guess, 267, was incorrect
Your current hint is: W

Please enter a guess: 358

Your guess, 358, was incorrect
Your current hint is: XX

Please enter a guess: 835

Your guess, 835, was incorrect
Your current hint is: RR

Please enter a guess: 839

Your guess, 839, was incorrect
Your current hint is: R

Please enter a guess: 805

Your guess, 805, was incorrect
Your current hint is: RR

Please enter a guess: 895

Your guess, 895, was incorrect
Your current hint is: RR

Please enter a guess: 875

Your guess, 875, was incorrect
Your current hint is: RR

Please enter a guess: 865

Your guess, 865, was incorrect
Your current hint is: RR

Please enter a guess: 845

Your guess, 845, was incorrect
Your current hint is: RR

Please enter a guess: 835

Your guess, 835, was incorrect
Your current hint is: RR

Please enter a guess: 825

Your guess, 825, was incorrect
Your current hint is: RR

Please enter a guess: 815

Congratulations!
815 was the correct answer!
You guessed the correct answer in 14 tries and scored 2541.87 points.


Would you like to play again (Y/N)? y

  _______   __          __   __      __
 |   _   |  \  \  /\  /  /   \  \  /  /
 |  |_| _|   \  \/  \/  /     \  \/  /
 |  |\  \     \        /      /  /\  \
 |__| \__\     \__/\__/      /__/  \__\

  ----Welcome to the RWX Game!----

Your aim is to guess the target, consisting
        of 3 digits from 0-9

R | One or more R's means you have a correct character in the right place

W | means all the characters are in your guess are wrong

X | One or more X's means you have a correct character, but in the wrong place

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123

Your guess, 123, was incorrect
Your current hint is: X

Please enter a guess: 123
Sorry, the game is now over.
The correct answer was 437, but you didn't guess it in 23 attempts.


Would you like to play again (Y/N)? n

-----Thank you for playing!-----
```

## Support:
Please email jlegresl@une.edu.au if further details are required.

## Contributing:
For major changes, please open an issue first to discuss what you would like to change.
