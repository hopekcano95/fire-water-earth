This game is a simple text-based implementation of "Rock, Paper, Scissors" with a twist, using the elements Fire, Water, and Earth. Here's a breakdown of how it works:

Objective: The player competes against the computer by choosing one of three elements: Fire, Water, or Earth. Each element has a specific interaction with the others:
Fire beats Earth
Earth beats Water
Water beats Fire

Gameplay Loop:
The game displays the current score (wins, losses, ties).
The player is prompted to enter their move (F for Fire, W for Water, E for Earth, or Q to quit).
If the player enters an invalid option, they are prompted to try again.
The game then waits for a moment, counts down from 3, and reveals the computer's random choice.

Scoring:
The game compares the player's choice to the computer's choice to determine the outcome:
If both choices are the same, it's a tie.
If the player's choice beats the computer's choice, the player wins.
If the computer's choice beats the player's choice, the player loses.
End of Game: The player can quit the game at any time by entering 'Q', which will terminate the program.
