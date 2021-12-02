# cpsc3720_charades

## Table of contents
* [General Info](#general-info)
* [Setup](#setup)
* [How To Play](#how-to-play)

## General Info
This project is simple charades game that was built in Python and implements two APIs.
	
### APIs
Implemented APIs:
* pygame - implements a timer so that each round of the game is limited to 300 milliseconds
* pyspellchecker - checks that the words entered by the playes are spelled correctly. If the users enter a mispelled word, then the word is not added to list of the words that can be played with. If the users enter a correctly word, then the word is added to the list of words that can be played with. 

## Setup
To install Pygame:
```
pip install pygame
```
To install pyspellchecker:
```
pip install pyspellchecker
```
To run this project:
```
python main.py
```
## How To Play
The players should break themselves into two teams. The program will prompt the players to select how many rounds of the charades that they would like to play and enter the words that they would like to play with. Once the users have entered the words that they would like to play with, the program will print one of the words entered by the players. One player will have 300 milliseconds to act out the printed word. If a member of the acting player's team is able to guess the word that they are acting out within 300 milliseconds, then the acting team will recieve one point. The program does not keep score. The players are responsible for keeping score. A member of the opposite team should act out the next word that the program prints out.
