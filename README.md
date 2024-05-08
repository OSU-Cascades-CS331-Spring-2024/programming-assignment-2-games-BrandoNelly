[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson.
Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.



# Project 2: Othello MinMax Algorithm Agent

## May 7, 2024

## Brandon Nelson 


## CS 331 - Intro to Artificial Intelligence


### Collaborators

Daniel Lounsbury

Kevin Walsh

### 4X4 Game

1. Depth = 5: Player 2 Wins! Player 2 Avg Decision Time:  0.023222875595092774
2. Depth = 3: Player 1 Wins! Player 2 Avg Decision Time:  0.0021685361862182617
3. Depth = 2: Player 2 Wins! Player 2 Avg Decision Time:  0.0009992122650146484
4. Depth = 1: Player 1 Wins!Player 2 Avg Decision Time:  0.000500957171122233


### 8X8 Game

1. Depth = 5: Player 1 Wins! Player 2 Avg Decision Time:  6.267827026049296
               ``` Note: When dealing with a lot of possible move decisions, the speed of decision making became much slower, taking up to 22 seconds to make a decision at the peak. After the decisions started to become fewer and more obvious, agent decision making time sped up drastically, going back to 1 and sub 1 seconds. Something in my min and max function portions of my code could be optimized more to reduce the slowdown during peak decision making time.```

2. Depth = 2: Player 2 Wins! Player 2 Avg Decision Time:  0.012178778648376465

The reason for the agent to take far less time in the 8X8 game to make a move when the depth was set to 1 vs the longest seconds it took when the depth was 5, even when in the middle of there being several valid options is because when the depth is set low the agent doesn't care to look far ahead, it's possible future viable option pool is smaller and it's decision to an "optimal" move is much snappier. The deeper the depth the longer the recursion through the tree will be, possibly increasing the time it takes to make a decision.

The winner of the 4X4 game would be inconsistent in my playthroughs. With the depth set higher the minMax player would win more often, but its decision making was slightly slower than when the depth is set lower. This remains consistent, and with tweaking of the algorithm the ai player should be able to win every time. 


## Sources

Pseudocode found in minimax geeksforgeeks site - (https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)



Artificial Intelligence: A Modern Approach - chapter 5.2 p.150  Pseudocode for minimax search, max and min value functions



