from random import choice

comp_victories = 0
player_victories = 0

def Player_option():
    player_choice = input("Choose Rock, Paper or Scissors: ")
    if player_choice in ["Scissors", "SCISSORS", "scissors"]:
        player_choice = "Scissors"
    elif player_choice in ["Rock", "ROCK", "rock"]:
        player_choice = "Rock"
    elif player_choice in ["Paper", "PAPER", "paper"]:
        player_choice = "Paper"
    else:
        print("Invalid option. Try again")
        Player_option()
    return player_choice


def Comp_option():
    comp_choice = choice(["Rock", "Paper", "Scissors"])
    return comp_choice


while True:

    print("------------")

    comp_choice = Comp_option()
    player_choice = Player_option()

    print("-------------")

    if(player_choice == "Paper") and (comp_choice == "Rock") or (player_choice == "Rock") and (comp_choice == "Scissors") or (player_choice == "Scissors") and (comp_choice == "Paper"):
        #player wins the game

        print(f"The player choose {player_choice} and the machine choose {comp_choice}. Game result: You Win! \o/")
        player_victories += 1

        #player tie the game with the machine
    elif player_choice == comp_choice:
        print(f"The player choose {player_choice} and the machine choose {comp_choice}. Game result: Game´s tied")

    else :
        #player lost the game
        print(f"The player choose {player_choice} and the machine choose {comp_choice}. Game result: You lost! :( The machine is better than you ;)")
        comp_victories += 1

    print("-------------")

    print(f"Player Victories: {player_victories}")
    print(f"Computer Victories: {comp_victories}")

    print("-------------")

    player_choice = input("Do you want to play again? (y/n): ")
    if player_choice in ["yes", "YES", "Yes", "y", "Y"]:
        pass
    elif player_choice in ["no", "NO", "No", "n", "N"]:
        break
    else:
        break