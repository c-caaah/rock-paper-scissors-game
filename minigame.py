from random import choice

comp_victories = 0
player_victories = 0

def Option_player():
    choose_player = input("Choose Rock, Paper or Scissors: ")
    if choose_player in ["Scissors", "SCISSORS", "scissors"]:
        choose_player = "Scissors"
    elif choose_player in ["Rock", "ROCK", "rock"]:
        choose_player = "Rock"
    elif choose_player = ["Paper", "PAPER", "paper"]:
        choose_player = "Paper"