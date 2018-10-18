'''
Hangman game
'''
import os
import random


def hangman():
    os.path.join("K4446","Users","philllippierce","Documents")
    with open("words_alpha.txt", "r") as f:
        words = f.readlines()
        index = random.randint(0, len(words))
        word = words[index].strip()
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    letters_missed = []
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
            letters_missed.append(char)
        print((" ".join(board)))
        print("Letters missed: {0}".format(" ".join(letters_missed)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win! The word was {0}!".format(word))
            print(" ".join(board))
            win = True
            break
    if win == False:
        print("The word was {0}. Better luck next time".format(word))

hangman()
