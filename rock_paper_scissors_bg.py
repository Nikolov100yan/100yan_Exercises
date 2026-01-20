# Program implementing the game "Rock, Paper & Scissors"
import sys, random

print("*************************************************************")
print("*************** ИГРА: КАМЪК - НОЖИЦА - ХАРТИЯ ***************")
print("*************************************************************")
print()

wins = 0
ties = 0
losses = 0

# rock = "Rock"
# paper = "Paper"
# scissors = "Scissors"

while True: # the main game loop
    print("*************************************************************")
    print(f"********* Победи: {wins} *** Равенства: {ties} *** Загуби: {losses} **********")
    print("*************************************************************")
    print()
    while True:     # player's prompt loop
        print("*** Въведи своя ход: КАМЪК [к], НОЖИЦА [н] или ХАРТИЯ [х] ***")
        print("*************** За ИЗХОД от играта натисни [и] **************")
        print()

        valid_player_input = {"u", "k", "n", "r"}
        player_move = input()

        if player_move not in valid_player_input:
            print("******************* Невалидна команда *******************")
        else:
            if player_move == "r":
                print("*************************************************************")
                print("*********************** КРАЙ НА ИГРАТА **********************")
                print("*************************************************************")
                sys.exit()
            else:
                break

    # Display what the player chose:
    if player_move == "u":
        print("КАМЪК срещу...")
    elif player_move == "n":
        print("ХАРТИЯ срещу...")
    elif player_move == "k":
        print("НОЖИЦИ срещу")

    # Display what the computer chose:
    random_move = random.randint(1, 3)
    if random_move == 1:
        computer_move = "u"
        print("КАМЪК")
    elif random_move == 2:
        computer_move = "n"
        print("ХАРТИЯ")
    else:
        computer_move = "k"
        print("НОЖИЦИ")

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        ties += 1
        print("Равенство")
    elif ((player_move == "u" and computer_move == "k")
          or (player_move == "n" and computer_move == "u")
          or (player_move == "k" and computer_move == "n")):
        wins += 1
        print("Ти победи :)")
    elif ((player_move == "k" and computer_move == "u")
            or (player_move == "u" and computer_move == "n")
            or (player_move == "n" and computer_move == "k")):
        losses += 1
        print("Ти загуби :(")

