# Rockpaperscissorgame
This is a rock, paper and scissor game made using tkinter library in python

Requirements:
- VS code
- Python 3.2
- Library tkinter

Library:
- Import Tkinter and from that import random.
  - Tkinter is used to build graphical user interface (GUI)
  - random is used to select random integers
- Tk() is packed using root

Interface
- root.geometry() is used to set the size of the GUI window.
- root.title() displays the title.

Setup
- Rock, paper and scissor are given indexes 0,1,2 respectively.

Function
- reset() is used to set the options for the player and default state is set as acitve for the three options. The default against player is set as computer.
- disable() results in deactivating the state of the options.
- rock(), paper() and scissor() are used to set the winning, losing and draw options for the game.
- lable() is used to set the properties of the game().
- button() is used to set the buttons for rock, paper and scissor as b1 , b2 and b3 respectively. The parameters for the buttons are initialzed.
- The buttons are packed to hold the value and the positions are set for the same.
- A reset button is created to reset the game after the game is over.
  
