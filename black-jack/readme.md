## BlackJack Project
### Overview
This project is a console-based implementation of the classic Blackjack game. The game allows you to play against a computer dealer, with the goal of having a hand value as close to 21 as possible without exceeding it.

#### How to Play
- You will be dealt two cards initially, and the dealer will also receive two cards, one face up and one face down.
- You can choose to "hit" to receive another card or "stand" to hold your total and end your turn.
- The dealer must continue to take cards until their total is 17 or higher.
- The aim is to have a higher total than the dealer without exceeding 21.

#### House Rules
- The deck is unlimited in size.
- There are no jokers.
- Jack, Queen, and King count as 10 points.
- The Ace can count as 11 or 1 point.
- The list of possible cards is: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards have an equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.

### Project Setup
1. Ensure you have Python installed on your system.
2. Place the following files in the same directory:
    - main.py: The main game logic.
    - art.py: Contains the ASCII art for the game logo.
    - replit.py: Contains the clear() function to clear the console.

#### Instructions
1. Run the game using the command:
```bash
python main.py
```
2. Follow the on-screen prompts to play the game

