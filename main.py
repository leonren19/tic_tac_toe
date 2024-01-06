# 7.10 Tic Tac Toe  
# L Ren
# Mar 5, 2021
# https://repl.it/@LeonRen2/TicTacToe#main.py

# import module
from os import system, name
import random

# global variables
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# functions
def clear_the_screen(): # clears the screen so it starts fresh 
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

def show_the_board(): # this is the original board or the one before it gets redrawn
  clear_the_screen()
  print("________________ Tic Tac Toe ________________")
  show_instructions()
  print("-------------")
  print("| " + "1" + board[0] + "| " + "2" + board[1] + "| " "3" + board[2] + "|")
  print("-------------")
  print("| " + "4" + board[3] + "| " + "5" + board[4] + "| " "6" + board[5] + "|")
  print("-------------")
  print("| " + "7" + board[6] + "| " + "8" + board[7] + "| " "9" + board[8] + "|")
  print("-------------")
  print()
  print("you go first . . .")

def show_instructions(): # explains instructions to the user 
  print()
  print("let's play! you be x's, i'll be o's ")
  print("use these numbers to make a move")

def user_move(): # allows and asks the user where to move 
  pos = input("enter a move (1-9): ")
  pos = int(pos) - 1
  board[pos] = "x"

def computer_move(): # allows the computer to move randomly and when to move
  input("press enter for computer to move: ")
  pos = random.randint(1, 9) - 1;
  while board[pos] != " ": 
    pos = random.randint(1, 9) - 1;
  board[pos] = "o" 

def redraw_the_screen(): # redraws the screen after the user understands the positions on the board
  clear_the_screen()
  print("________________ Tic Tac Toe ________________")
  show_instructions()
  print("-------------")
  print("| " + board[0] + " |" + " " + board[1] + " | " + board[2] + " |")
  print("-------------")
  print("| " + board[3] + " |" + " " + board[4] + " | " + board[5] + " |")
  print("-------------")
  print("| " + board[6] + " |" + " " + board[7] + " | " + board[8] + " |")
  print("-------------")

def check_to_see_if_someone_has_three_in_a_row(): # checks to see if someone has three in a row or who has won 
  if ((board[0] == "x") and (board[1] == "x") and (board[2] == "x")) or ((board[3] == "x") and (board[4] == "x") and (board[5] == "x")) or ((board[6] == "x") and (board[7] == "x") and (board[8] == "x")) or ((board[0] == "x") and (board[3] == "x") and (board[6] == "x")) or ((board[1] == "x") and (board[4] == "x") and (board[7] == "x")) or ((board[2] == "x") and (board[5] == "x") and (board[8] == "x")) or ((board[0] == "x") and (board[4] == "x") and (board[8] == "x")) or ((board[2] == "x") and (board[4] == "x") and (board[6] == "x")): 
    print("x won! game over")
  if ((board[0] == "o") and (board[1] == "o") and (board[2] == "o")) or ((board[3] == "o") and (board[4] == "o") and (board[5] == "o")) or ((board[6] == "o") and (board[7] == "o") and (board[8] == "o")) or ((board[0] == "o") and (board[3] == "o") and (board[6] == "o")) or ((board[1] == "o") and (board[4] == "o") and (board[7] == "o")) or ((board[2] == "o") and (board[5] == "o") and (board[8] == "o")) or ((board[0] == "o") and (board[4] == "o") and (board[8] == "o")) or ((board[2] == "o") and (board[4] == "o") and (board[6] == "o")): 
    print("o won! game over")
  
def play_the_game(): # plays the game using all of the functions under this one function 
  show_the_board()
  while (True):          # always TRUE   CTRL-C
    user_move()   
    redraw_the_screen()
    check_to_see_if_someone_has_three_in_a_row()
    computer_move()
    redraw_the_screen()
    check_to_see_if_someone_has_three_in_a_row()
  
# start here
play_the_game()