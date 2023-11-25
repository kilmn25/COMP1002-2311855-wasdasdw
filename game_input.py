def game_input(game_board): # THIS IS TASK 2
  coordinate = {"x": 0, "y": 0}
  print("\"a1\" or \"A1\" - coordinate format\nexit - return to main menu")
  
  while True:
    print("===================================================")
    player_input = input("💬 Coordinate: ")

    if player_input == "exit":
        return player_input

    if len(player_input) < 2:
        print("⚠ The input is not in the format of \"a1\" or \"A1\". Please enter valid coordinate.")
        continue

    if ord(player_input[0]) < 95:
      coordinate["x"] = ord(player_input[0]) - 65
    else:
      coordinate["x"] = ord(player_input[0]) - 97

    if not player_input[1:].isdigit():
        print("⚠ The input is not in the format of \"a1\" or \"A1\". Please enter valid coordinate.")
        continue

    coordinate["y"] = int(player_input[1:]) - 1
    
    if not (0 <= coordinate["x"] < len(game_board) and 0 <= coordinate["y"] < len(game_board)):
        print("⚠ The coordinates are outside the play area. Please enter valid coordinate.")
        continue
    if game_board[coordinate["y"]][coordinate["x"]] != "🟨":
        print("⚠ The spot is already taken. Please enter a valid coordinate.")
        continue
    
    return coordinate









