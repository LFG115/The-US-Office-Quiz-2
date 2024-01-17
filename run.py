import time
import os


def clear():
    """
    Function to clear the terminal when called.
    """
    os.system("clear")


def print_by_letter(output_str):
    """
    Function to read the text to the user and simplify user experience
    """
    for char in output_str:
        print(char, end='', flush=True)
        time.sleep(.03)


def correct_answer(score):
    """
    Displays the correct answer message and adds
    1 to the score.
    """
    score += 1
    print("Correct! Well Done!")
    print("Score : ", score)
    print("\n")
    return score


def wrong_answer(correct_answer, score):
    """
    Displays the incorrect answer message along with correct answer,
    while displaying previous score result.
    """
    print("Wrong Unlucky! The answer is " + correct_answer)
    print("Score: ", score)
    print("\n")


def home():
    """
    The begining of the game starts with a breife summary of why and what
    its about then tells you the rules, and ask's your name.
    """
    output_str = '''
    \n\n
     ** * WELCOME TO THE US OFFICE QUIZ! * ** \n

    This show has brought plenty of laughter and joy to our screens.
    It's easy to say the show has been nothing but spectacular!\n
    The main reason I picked The US Office is because it got me through some
    difficult times during the pandemic.
    and is a great mood improver!

    Rules: 15 Questions, 15 Points are up for grabs.\n
    Please answer using keys '1', '2', '3', '4' and 1 question '5'\n
    Try not to cheat and good luck!\n
    I do hope you enjoy.\n
    '''
    print_by_letter(output_str)
    player_name = input("Enter your name: ")
    print("\n")
    input(f"If your ready {player_name}\nPress the Enter Key To Begin Quiz...")
    question_one()

    while True:
        """
        The play again option will redirect a 'yes'
        to question 1 of the quiz, a 'no' to the home screen.
        """
        play_again_response = input("Would you like to play again?\
        ( yes / no ): ").lower()
        if play_again_response == "yes":
            clear()
            question_one()
        elif play_again_response == "no":
            print("\n\n\n")
            print("Thanks for playing!\n")
            print("Redirecting you to the Home Screen...\n")
            home()
            break
        else:
            print("Please enter yes or no")


def question_one():
    """
    Displays the first question.
    Player must answer the questions to continue
    and then gives a score.
    """
    print("\n")
    score = 0

    # Question 1
    q1 = input("Q1: What item did Jim put in jelly ? \
    \n\n1. Mug \n\n2. Stapler \n\n3. Pen \n\n4. Calculator \n\nAnswer: ")
    if q1 in ['1', '2', '3', '4']:
        if int(q1) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("2. Stapler", score)
    else:
        print("Incorrect entry, Try again, Please enter '1', '2', '3', '4'")
        print("\n")
        question_one()
    question_two(score)


def question_two(score):
    """
    Displays the second question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 2
    q2 = input("Q2: Bob Vance has a business, what is it called ? \
    \n\n1. Vance clean & simple \n\n2. Vance reapir & recovery \
    \n\n3. Vance refrigeration's \n\n4. Vance transportation's \n\nAnswer: ")
    if q2 in ['1', '2', '3', '4']:
        if int(q2) == 3:
            score = correct_answer(score)
        else:
            wrong_answer("3. Vance refrigeration's", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_two(score)
    question_three(score)


def question_three(score):
    """
    Displays the third question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 3
    q3 = input("Q3: What department is Kevin located in ? \
    \n\n1. Sales \n\n2. Accounting \n\n3. Customer Services \
    \n\n4. Quality assurance \n\nAnswer: ")
    if q3 in ['1', '2', '3', '4']:
        if int(q3) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("2. Accounting", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_three(score)
    question_four(score)


def question_four(score):
    """
    Displays the fourth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 4
    q4 = input("Q4: Who is the assistant to the reginal Manager ? \
    \n\n1. Jim \n\n2. Kevin \n\n3. Oscar \n\n4. Dwight \n\nAnswer: ")
    if q4 in ['1', '2', '3', '4']:
        if int(q4) == 4:
            score = correct_answer(score)
        else:
            wrong_answer("4. Dwight", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_four(score)
    question_five(score)


def question_five(score):
    """
    Displays the fith question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 5
    q5 = input("Q5: What is Jim's nickname according to Andy ? \
    \n\n1. Tuna \n\n2. Ham \n\n3. Pikle \n\n4. Cream Cheese \n\nAnswer: ")
    if q5 in ['1', '2', '3', '4']:
        if int(q5) == 1:
            score = correct_answer(score)
        else:
            wrong_answer("1. Tuna", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_five(score)
    question_six(score)


def question_six(score):
    """
    Displays the sixth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 6
    q6 = input("Q6: Where is Dunder Mifflin located ? \
    \n\n1. Philadelphia \n\n2. Scranton \
    \n\n3. New York \n\n4. Albany \n\nAnswer: ")
    if q6 in ['1', '2', '3', '4']:
        if int(q6) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("2. Scranton", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_six(score)
    question_seven(score)


def question_seven(score):
    """
    Displays the seventh question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 7
    q7 = input("Q7: What is the receptionist name ? \
    \n\n1. Kelly \n\n2. Meredith \n\n3. Angela \n\n4. Pam \n\nAnswer: ")
    if q7 in ['1', '2', '3', '4']:
        if int(q7) == 4:
            score = correct_answer(score)
        else:
            wrong_answer("4. Pam", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_seven(score)
    question_eight(score)


def question_eight(score):
    """
    Displays the eighth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 8
    q8 = input("Q8: Who works in HR ? \
    \n\n1. Ryan \n\n2. Creed \n\n3. Oscar \n\n4. Toby \n\nAnswer: ")
    if q8 in ['1', '2', '3', '4']:
        if int(q8) == 4:
            score = correct_answer(score)
        else:
            wrong_answer("4. Toby", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_eight(score)
    question_nine(score)


def question_nine(score):
    """
    Displays the ninth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 9
    q9 = input("Q9: What has Michael Scott said before ? \
    \n\n1. 'That's what she said' \n\n2. 'Why always me' \
    \n\n3. 'Beets are life' \n\n4. 'Did I stutter' \n\nAnswer: ")
    if q9 in ['1', '2', '3', '4']:
        if int(q9) == 1:
            score = correct_answer(score)
        else:
            wrong_answer("1. 'That's what she said'", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_nine(score)
    question_ten(score)


def question_ten(score):
    """
    Displays the tenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 10
    q10 = input("""Q10: Who wins the "'Rear of the Year'" award ?
    (according to Michael) \n\n1. Pam \n\n2. Angela \n\n3. Ryan
    \n\n4. Dwight \n\n5. Kelly \n\nAnswer: """)
    if q10 in ['1', '2', '3', '4', '5']:
        if int(q10) == 3:
            score = correct_answer(score)
        else:
            wrong_answer("3. Ryan", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4', '5'")
        print("\n")
        question_ten(score)
    question_eleven(score)


def question_eleven(score):
    """
    Displays the eleventh question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 11
    q11 = input("Q11: Who is Jan’s assistant ? \
    \n\n1. Hunter \n\n2. David \n\n3. Chad \n\n4. James \n\nAnswer: ")
    if q11 in ['1', '2', '3', '4']:
        if int(q11) == 1:
            score = correct_answer(score)
        else:
            wrong_answer("1. Hunter", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_eleven(score)
    question_tweleve(score)


def question_tweleve(score):
    """
    Displays the twelveth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 12
    q12 = input("""Q12: In the "'Booze Cruise'" episode who breaks
    up on the boat ? \n\n1. Pam and Roy \n\n2. Ryan and Kelly
    \n\n3. Jim and Katy \n\nAnswer: """)
    if q12 in ['1', '2', '3']:
        if int(q12) == 3:
            score = correct_answer(score)
        else:
            wrong_answer("3. Jim and Katy", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3'")
        print("\n")
        question_tweleve(score)
    question_thirteen(score)


def question_thirteen(score):
    """
    Displays the thirteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 13
    q13 = input("Q13: What's Pam's favourite flavour of yogurt ?\
    \n\n1. Vanilla \n\n2. Peach \n\n3. Strawberry & kiwi\
    \n\n4. Mixed berry \n\nAnswer:  ")
    if q13 in ['1', '2', '3', '4']:
        if int(q13) == 4:
            score = correct_answer(score)
        else:
            wrong_answer("4. Mixed berry", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_thirteen(score)
    question_fourteen(score)


def question_fourteen(score):
    """
    Displays the fourteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 14
    q14 = input("Q14: Who started the fire ?\
    \n\n1. Jim started the fire! \n\n2. Ryan started the fire! \
    \n\n3. Kevin started the fire! \n\n4. Oscar started the fire! \
    \n\nAnswer: ")
    if q14 in ['1', '2', '3', '4']:
        if int(q14) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("2. Ryan started the fire!", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_fourteen(score)
    question_fifteen(score)


def question_fifteen(score):
    """
    Displays the fifteenth question.
    Player must answer the questions to continue
    and then gives a score.
    """
    # Question 15
    q15 = input("Q15: Who is the final couple we see getting married ? \
    \n\n1. Jim and Pam \n\n2. Dwight and Angela \n\n3. Kelly and Ryan \
    \n\n4. Michael and Holly \n\nAnswer: ")
    if q15 in ['1', '2', '3', '4']:
        if int(q15) == 2:
            score = correct_answer(score)
        else:
            wrong_answer("2. Dwight and Angela", score)
    else:
        print("Incorrect entry, Please enter '1', '2', '3', '4'")
        print("\n")
        question_fifteen(score)
        play_again_response()


home()
