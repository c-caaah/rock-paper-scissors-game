from random import choice

comp_victories = 0
player_victories = 0

def 0option_player():
    choose_player = input("Choose Rock, Paper or Scissors: ")
    if choose_player in ["Scissors", "SCISSORS", "scissors"]:
        choose_player = "scissors"
    elif 