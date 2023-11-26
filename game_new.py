
def game_new():  # creates empty square table of dimensions game_board_sizexgame_board_size

  game_board_size = None  #choose size
  print("===================================================\n1 - 15x15\n2 - 19x19\n===================================================")
  while True:
    size_choice = input("💬 Size: ")
    match size_choice:
      case "1": 
        game_board_size = 15     
        break
      case "2": 
        game_board_size = 19
        break
      case _:
        print("⚠ Invalid input! Please input either 1 or 2 only⚠")   
        print("===================================================")


  #create game_board after valid game_board size is inputted by user
  game_board = []
  for _ in range(game_board_size):
    tempRow = [] #need make brand new each time because add_to_board will change every row when editing one row, since theyre all instanced to the same tempRow
    for _ in range(game_board_size):
      tempRow.append("🟨")
    game_board.append(tempRow)

  return game_board



