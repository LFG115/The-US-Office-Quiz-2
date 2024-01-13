
import os


def begin():
    """
    The begining of the game starts with a breife summary of why amd what
    its about then tells you the rules, and ask's your name.
    """
    print("\n\n")
    print(" *WELCOME TO THE US OFFICE QUIZ!* \n\n")

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


def question_one():
    """
    Displays the first question.
    Player must answer the questions to continue
    and then gives a score.
    """
    score = 0

    #Question 1
    q1 = input("What item did Jim put in jelly ?")


def question_two():
    """
    Displays the second question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 2
    q2 = input("Bob Vance has a business, what is it called ?")


def question_three():
    """
    Displays the third question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 3
    q3 = input("What department is Kevin located in ?")


def question_four():
    """
    Displays the fourth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 4
    q4 = input("Who is the assistant to the reginal Manager ?")


def question_five():
    """
    Displays the fith question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 5
    q5 = input("What is Jim's nickname according to Andy ?")


def question_six():
    """
    Displays the sixth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 6
    q6 = input("Where is Dunder Mifflin located ?")


def question_seven():
    """
    Displays the seventh question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 7
    q7 = input("What is the receptionist name ?")


def question_eight():
    """
    Displays the eighth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 8
    q8 = input("Who works in HR ?")


def question_nine():
    """
    Displays the ninth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 9
    q9 = input("What has Michael Scott said before ?")


def question_ten():
    """
    Displays the tenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 10
    q10 = input("Who wins the "'Rear of the Year'" award ? (according to Michael)")


def question_eleven():
    """
    Displays the eleventh question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 11
    q11 = input("Who is Jan’s assistant ?")


def question_tweleve():
    """
    Displays the twelveth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 12
    q12 = input("In the "'Booze Cruise'" episode who breaks up on the boat ?")


def question_thirteen():
    """
    Displays the thirteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 13
    q13 = input("What's Pam's favourite flavour of yogurt ?")


def question_fourteen():
    """
    Displays the fourteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 14
    q14 = input("Who started the fire ?")


def question_fifteen():
    """
    Displays the fifteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 15
    q15 = input("Who is the final couple we see getting married ?")


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