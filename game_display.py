
def display_game(game_board): #print the whole board
  temp_print_target = ""

  # for unit in range(len(game_board)):
  #     temp_print_target += str(unit+1) 
  #     if unit < 9:
  #       temp_print_target += "  "
  #     else:
  #       temp_print_target += " "

  for i in range(65, 65 + len(game_board)):
    temp_print_target += chr(i)
    temp_print_target += "  "

  temp_print_target += "\n" #print on new line

  for row in range(len(game_board)):
    for unit in range(len(game_board[row])):
      temp_print_target += str(game_board[row][unit])
      temp_print_target += " "
    temp_print_target += " " + str(row+1)
    temp_print_target += "\n" #print on new line
  print(temp_print_target)
      

