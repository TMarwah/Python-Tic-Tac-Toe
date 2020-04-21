#global var



#array of empty board values
board = ["*","*","*",
        "*","*","*",
        "*","*","*",]
#game still going
game_going = True

#winner?
winner = None

#whos turn
current_player = "X"
def show_board():
  #display rows of the board by array location
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
  #show starting board
  show_board()
  while game_going:

    turn_manager(current_player)
    check_gameover()

    switch_player()
  #game end
  if winner == "X" or winner =="O":
    print(winner + " has won the game!")
  elif winner == None:
    print("The game ended in a tie.")

def turn_manager(player):

  pos = input("Choose a location using 1-9:")
  #account for array value starting on 0
  pos = int(pos)-1

  board[pos] = "X"
  show_board()

def check_gameover():
  check_win()
  check_tie()

def check_win():
  #check row
  #check column
  #check diagonal
  return

def check_tie():
  
  return

def switch_player():

  return

play_game()