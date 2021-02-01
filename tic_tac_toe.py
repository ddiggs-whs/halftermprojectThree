import random
empty_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
test_board1 = [['X','O','X'],[' ','X',' '],['O','O','X']]
test_board2 = [['O','X',''],['X','',' '],[' ',' ',' ']]
board_ids = [['00','01','02'],['10','11','12'],['20','21','22 ']]
def print_board(board):
  print(board[0][0]+'|'+board[0][1]+'|'+board[0][2])
  print('-----')
  print(board[1][0]+'|'+board[1][1]+'|'+board[1][2])
  print('-----')
  print(board[2][0]+'|'+board[2][1]+'|'+board[2][2])

def whose_turn(board):
  """
  A function that looks at an array and determines whose turn it is to go
  Should select X on an empty board, X on test board 1, O on test board 2
  inputs: board-> an array defining a board
  outputs: 'X' or 'O'
  """
  raise NotImplementedError

def is_valid(board, selection):
  """
  A function that checks is a space on the board is empty
  inputs: board-> an array defining a board
  selection-> a position in the array, given as a string
  outputs: True or False
  """

def next_play(board, selection, active_player):
  """
  A function that replaces a selection on the board with the active player
  inputs: board-> an array defining a board
  selection-> a position in the array, given as a string
  active_player-> 'X' or 'O'
  ouputs: a board that has been edited
  """

def win_check(board):
  """
  a function that checks if a game is over
  inputs: board-> an array defining a board
  outputs: game_over-> True if a winner or the board is full
  winner-> 'X' or 'O' if they win, None if no one won
  """

x_winner_count = 0
o_winner_count = 0
current_board = empty_board
while x_winner_count + o_winner_count < 5:
  #continues playing game until 5 games have been won
  active_player = whose_turn(current_board)
  if active_player == 'X':
    #if the player is X, the human picks a square
    while True:
      selection = input('Type the board id number of where you would like to play')
      valid = is_valid(current_board, selection)
      if valid:
        break
      else:
        print('NOT A VALID MOVE, please select a valid move')
    # run this line print_board(board_ids) to see the locations
  elif active_player == 'O':
    #if the player is O, the computer takes a turn
    selection = None
    while True:
      #The computer picks a random available square
      row = random.randint(0,2)
      col = random.randint(0,2)
      if current_board[row][col] == ' ':
        selection = str(row) + str(col)
        break
  current_board = next_play(current_board, selection, active_player)
  print_board(current_board)
  game_over, winner = win_check(current_board)
  if game_over == None:
    continue
  elif winner == 'X':
    x_winner_count += 0
    current_board = empty_board
  elif winner =='Y':
    y_winner_count += 1
    current_board = empty_board


