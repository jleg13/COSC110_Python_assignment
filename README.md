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

## Support:
Please email jlegresl@une.edu.au if further details are required.

## Contributing:
For major changes, please open an issue first to discuss what you would like to change.
