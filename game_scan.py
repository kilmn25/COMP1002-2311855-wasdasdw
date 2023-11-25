def game_scan(game_board, turn_number):
  board_size = len(game_board)
  for row in range(board_size):
    for col in range(board_size - 4):  
      if all(game_board[row][col+i] == game_board[row][col] for i in range(5)):
        if game_board[row][col] == "⚫":
          return 1
        elif game_board[row][col] == "⚪":
          return 2

  for col in range(board_size):
    for row in range(board_size - 4): 
      if all(game_board[row+i][col] == game_board[row][col] for i in range(5)):
        if game_board[row][col] == "⚫":
          return 1
        elif game_board[row][col] == "⚪":
          return 2

  for row in range(board_size - 4):
    for col in range(board_size - 4):  
      
      if all(game_board[row+i][col+i] == game_board[row][col] for i in range(5)):
        if game_board[row][col] == "⚫":
          return 1
        elif game_board[row][col] == "⚪":
          return 2

  for row in range(4, board_size):  
    for col in range(board_size - 4): 
     
      if all(game_board[row-i][col+i] == game_board[row][col] for i in range(5)):
        if game_board[row][col] == "⚫":
          return 1
        elif game_board[row][col] == "⚪":
          return 2

  if turn_number>=board_size*board_size:
    return 3
  return 0