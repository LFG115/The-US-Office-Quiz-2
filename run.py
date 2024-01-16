
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
    input("Press Any Key To Begin Quiz...\n")
    question_one()


def question_one():
    """
    Displays the first question.
    Player must answer the questions to continue
    and then gives a score.
    """
    print("\n")
    score = 0

    #Question 1
    q1 = input("Q1: What item did Jim put in jelly ? \
    \n\n1. Mug \n\n2. Stapler \n\n3. Pen \n\n4. Calculator \n\nAnswer:  ")
    if q1 in ['1', '2', '3', '4']:
        if int(q1) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("Stapler", score)
    else:
        print("Please enter '1', '2', '3', '4'")
        question_one()
    question_two(score)


def question_two(score):
    """
    Displays the second question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 2
    q2 = input("Q2: Bob Vance has a business, what is it called ? \
    \n\n1. Vance clean & simple \n\n2. Vance reapir & recovery \n\n3. Vance refrigeration's \n\n4. Vance transportation's \n\nAnswer:  ")
    if q2 in ['1', '2', '3', '4']:
        if int(q2) == 3:
            score = correct_answer(score)
        else:
            wrong_answer("Vance refrigeration's", score)
    else:
        print("Please enter '1', '2', '3', '4'")
        question_two()
    question_three(score)


def question_three(score):
    """
    Displays the third question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 3
    q3 = input("Q3: What department is Kevin located in ? \
    \n\n1. Sales \n\n2. Accounting \n\n3. Customer Services \n\n4. Quality assurance \n\nAnswer:  ")
    if q3 in ['1', '2', '3', '4']:
        if int(q3) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("Accounting", score)
    else:
        print("Please enter '1', '2', '3', '4'")
        question_two()
    question_four()(score)



def question_four(score):
    """
    Displays the fourth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 4
    q4 = input("Q4: Who is the assistant to the reginal Manager ?")


def question_five():
    """
    Displays the fith question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 5
    q5 = input("Q5: What is Jim's nickname according to Andy ?")


def question_six():
    """
    Displays the sixth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 6
    q6 = input("Q6: Where is Dunder Mifflin located ?")


def question_seven():
    """
    Displays the seventh question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 7
    q7 = input("Q7: What is the receptionist name ?")


def question_eight():
    """
    Displays the eighth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 8
    q8 = input("Q8: Who works in HR ?")


def question_nine():
    """
    Displays the ninth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 9
    q9 = input("Q9: What has Michael Scott said before ?")


def question_ten():
    """
    Displays the tenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 10
    q10 = input("Q10: Who wins the "'Rear of the Year'" award ? (according to Michael)")


def question_eleven():
    """
    Displays the eleventh question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 11
    q11 = input("Q11: Who is Jan’s assistant ?")


def question_tweleve():
    """
    Displays the twelveth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 12
    q12 = input("Q12: In the "'Booze Cruise'" episode who breaks up on the boat ?")


def question_thirteen():
    """
    Displays the thirteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 13
    q13 = input("Q13: What's Pam's favourite flavour of yogurt ?")


def question_fourteen():
    """
    Displays the fourteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 14
    q14 = input("Q14: Who started the fire ?")


def question_fifteen():
    """
    Displays the fifteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    #Question 15
    q15 = input("Q15: Who is the final couple we see getting married ?")


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

def clear():
    """
    Function to clear the terminal when called.
    """
    os.system("clear")

begin()