from game_display import *
from game_input import *
from game_new import *
from game_scan import *
import webbrowser

game_board = None
game_won = None
turn_number = 1
current_player = ""

def run_game(): # call this function to start the game
  global turn_number # dont know why this isnt automatically global
  global game_board
  turn_number = 1

  while True: # main game loop
    print("===================================================")
    display_game(game_board)

    if turn_number % 2 == 0: 
      current_player = "⚪"
    else:
      current_player = "⚫"
    
    print(f"Turn number {turn_number}... It is {current_player}'s turn!")
    print("===================================================")

    current_input = game_input(game_board)
    if current_input == "exit":
      print("Game ended...")
      break
    else:
      player_input = current_input

    game_board[int(player_input["y"])][int(player_input["x"])] = current_player

    match game_scan(game_board, turn_number):
      case 1:
        display_game(game_board)
        print("===================================================")
        print("         🏆 THE WINNER IS ⚫ !!! 🏆")
        print("===================================================")
        break
      case 2:
        display_game(game_board)
        print("===================================================")
        print("         🏆 THE WINNER IS ⚪ !!! 🏆")
        print("===================================================")
        break
      case 3:
        display_game(game_board)
        print("===================================================")
        print("         🏆 GAME TIED, NO WINNERS. 🏆")
        print("===================================================")
        break
    
    turn_number += 1
  init()#go back to main menu

def run_draw(): # todo ignore this function
  flag_game = True
  while flag_game: # main game loop
    
    print("===================================================")
    display_game(game_board)

    current_input = game_input(game_board)
    if current_input == "exit":
      print("Game ended...")
      break
    else:
      player_input = current_input

    print("===================================================")
    color = ""
    print("Choose a color:\n1 - 🟥\n2 - 🟧\n3 - 🟨\n4 - 🟩\n5 - 🟦\n6 - 🟪\n7 - 🟫\n8 - ⬛\n9 - ⬜")
    print("exit - go back to main menu")

    while True:
      print("===================================================")
      target = input("💬 Color: ")
      
      match target:
        case "exit":
          flag_game = False
          break
        case "1":
          color = "🟥"
        case "2":
          color = "🟧"
        case "3":
          color = "🟨"
        case "4":
          color = "🟩"
        case "5":
          color = "🟦"
        case "6":
          color = "🟪"
        case "7":
          color = "🟫"
        case "8":
          color = "⬛"
        case "9":
          color = "⬜"
        case _:
          print("⚠ Invalid input! Please only input numbers 1 to 9")
          continue

      game_board[int(player_input["y"])][int(player_input["x"])] = color
      break
  init() #go back to main menu

def init(): # initiation
  global game_board
  print("===================================================\n                 ♟ GOMOKU GAME♟\n       made by COMP1002-2311855-wasdasdw\n===================================================")
  print("1 - PLAY GAME")
  print("2 - OPEN GITHUB (source code)")
  print("3 - EXTRA: DRAWING MODE")
  print("===================================================")
  while True:
    match input("💬 Choice: "):
      case "1":
        game_board = game_new()
        run_game()
        break
      case "2":
        webbrowser.open("https://github.com/kilmn25/COMP1002-2311855-wasdasdw")
        break
      case "3":
        game_board = game_new()
        run_draw()
        break
      case _:
        print("⚠ Invalid input! Please input 1 2 or 3 only!")

init() #start everything




