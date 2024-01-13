
import os


def begin():
    """
    The begining of the game starts with a breife summary of why amd what
    its about then tells you the rules, and ask's your name.
    """
    print(" *WELCOME TO THE US OFFICE QUIZ!* \n\n\n")

    print("This show has brought plenty of laughter and joy to our screens.")
    print("It's easy to say the show has been nothing but spectacular!\n")
    print("As you can tell I am a fan, I hope you enjoy.\n")

    print("Rules: 15 Questions, 18 Points are up for grabs.\n")
    print("Try not to cheat and good luck!\n")
    input("Press Enter Key To Begin Quiz...\n")


def clear():
    """
    Function to clear the terminal when called.
    """
    os.system("clear")


score = 0


def wrong_answer(correct_answer, score):
    """
    Displays the incorrect answer message along with correct answer,
    while displaying previous score result.
    """
    print("Wrong Unlucky! The answer is " + correct_answer)
    print("Score: ", score)
    print("\n")


def correct_answer(score):
    """
    Displays the correct answer message and adds
    1 to the score.
    """
    score += 1
    print("Correct, Well Done!")
    print("Score : ", score)
    print("\n")
    return score

begin()