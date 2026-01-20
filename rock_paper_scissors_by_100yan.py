# Program implementing the game "Rock - Paper - Scissors"

import sys, random


def main():
    welcome()

    wins = 0
    ties = 0
    losses = 0

    while True:         # the main game loop
        results_tracker(wins, ties, losses)

        while True:     # player prompts loop
            instructions()
            valid_input = {"r", "p", "s", "q"}
            player_move = input()

            if player_move not in valid_input:
                invalid_command()
            else:
                if player_move == "q":
                    game_over()
                    sys.exit()
                else:
                    break

        get_computer_move()


def welcome():
    print_separator()
    print("*************** GAME: ROCK - PAPER - SCISSORS ***************")
    print_separator()
    print()


def print_separator():
    print("*" * 61)


def results_tracker(x, y, z):
    print_separator()
    print(f"********* Wins: {x} *** Ties: {y} *** Losses: {z} **********")
    print_separator()
    print()


def instructions():
    print("*** Enter your move: (r)ock, (p)aper or (s)cissors ***")
    print("**************** For EXIT enter (q)uit ***************")
    print()


def invalid_command():
    print("******************* Invalid command *******************")


def game_over():
    print_separator()
    print("************************* GAME OVER *************************")
    print_separator()


def get_computer_move():
    random_move = random.randint(1, 3)
    if random_move == 1:
        computer_move = "r"
        print("ROCK")
    elif random_move == 2:
        computer_move = "p"
        print("PAPER")
    else:
        computer_move = "k"
        print("SCISSORS")

    return computer_move
