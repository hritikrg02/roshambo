"""
file: roshambo.py
description: the game of rock paper scissors
language: python3
author: Hritik "Ricky" Gupta
"""

from random import randint as r

VALUES = {"rock": 0, 'r': 0, "scissors": 1, "s": 1, "paper": 2, "p": 2}

def game(human_p, ai_p):
    """
    implements the mechanics of rock paper scissors,
    0 beats 1, 1 beats 2, 2 beats 0
    :param human_p: int
    :param ai_p: int
    :return: True if human_p wins, False if ai_p wins, None otherwise
    """
    if human_p == ai_p:
        return None
    elif (human_p == 0 and ai_p == 1)\
            or (human_p == 1 and ai_p == 2)\
            or (human_p == 2 and ai_p == 0):
        return True
    return False

def ai_player():
    """
    randomly picks an option out of the three
    :return: int, either 0, 1, or 2; str, either rock, paper, or scissors respectively
    """
    play_int = r(0, 2)
    play_str = ""
    if play_int == 0:
        play_str = "rock"
    elif play_int == 1:
        play_str = "scissors"
    elif play_int == 2:
        play_str = "paper"
    return play_int, play_str


def main():
    """
    plays a game of rock paper scissors
    :return:
    """
    while True:
        print("", end="\n")
        human = VALUES[input("rock, paper, or scissors? ").lower()]
        ai_int, ai_str = ai_player()
        result = game(human, ai_int)
        print("opponent played", ai_str)
        if result:
            print("game won!")
        elif result is False:
            print("game lost...")
        else:
            print("it's a tie! ")

        again = input("would you like to play again (y/n)? ")
        if again.lower() == "no" or again == "n":
            break
    print("Thanks for playing!")

if __name__ == '__main__':
    main()
