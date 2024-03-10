Tic-Tac-Toe Game with AI

Description:
This project implements a Tic-Tac-Toe game featuring a graphical user interface using Python and Pygame. The game includes an AI opponent that uses the Minimax algorithm to make decisions.

Installation:
    Prerequisites:
    Python 3.x
    pip (Python package installer)

    Dependencies:
    This project requires Pygame to run. Install Pygame by running the following command in your terminal or command prompt:


    pip3 install -r requirements.txt
    The requirements.txt file includes a list of necessary Python packages. For this project, it should contain at least:


    pygame>=2.0.0


Running the Game:
Clone or download the project repository to your local machine.
Navigate to the project directory in your terminal or command prompt.
Run the game using Python:

python runner.py
or
python3 runner.py
(depending on the current python version the machine is on)

This command starts the Tic-Tac-Toe game, opening a new window where you can play against the AI.


Gameplay Instructions:

The game window will display a Tic-Tac-Toe board.
Players can choose to play as 'X' or 'O' by clicking on the corresponding button displayed on the screen.
Players make moves by clicking on the cell where they wish to place their mark ('X' or 'O').
The AI opponent will automatically make its move following the player's turn.
The game displays the result (win, lose, or tie) once the game concludes.
A "Play Again" button allows users to restart the game after it ends.


Files Description:

runner.py: Contains the code to run the graphical interface for the game. This file is already implemented and handles user interactions and the game's visual elements.
tictactoe.py: Contains the logic for playing the game, including the AI's decision-making process using the Minimax algorithm. This file requires completion as per the project's objectives.