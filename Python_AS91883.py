#Imports
import random
import math
import time

#Needed Variable
retry = 0

#Quiz
while retry == 0:
    
    #Variables
    level = 0
    score = 0
    run = 0
    settingA = 0
    settingB = 0

    #Maximum Questions
    while settingA == 0:
        try:
            max_questions = int(input("How many questions would you like to answer?\n"))

            if max_questions > 0:
                settingA = 1

            else:
                print("Please enter a value greater than 0.\n")
    
        except ValueError:
            print("Please enter an integer such as 1.\n")

    #Maximum Value of Equations
    while settingB == 0:
        try:
            max_value = int(input("What is the maximum value of the questions that you want to answer?\n"))

            if max_value > 0:
                settingB = 1

            else:
                print("Please enter a value greater than 0.\n")

        except ValueError:
            print("Please enter an integer such as 1.\n")

    max_Q = max_questions
       
    retry = 0

    correct = "Correct! Your current score is {} out of {}. ({}/{})"
    incorrect = "Incorrect, the answer was {}. Your current score is {} out of {}. ({}/{})"

    random_value_1 = random.randrange((max_value * -1), (max_value + 1))
    random_value_2 = random.randrange((max_value * -1), (max_value + 1))
    random_value_3 = random.randrange((max_value * -1), (max_value + 1))
    random_pick = random.randrange(0, 6)
    
    #Game
    while max_questions != 0:
        try:
            #Total Score Value
            true_level = level + 1
        
            random_question = ["What is {} + {} + {}?".format(random_value_1, random_value_2, random_value_3),
                               "What is {} + {} - {}?".format(random_value_1, random_value_2, random_value_3),
                               "What is {} - {} - {}?".format(random_value_1, random_value_2, random_value_3),
                               "What is {} + {} x {}?".format(random_value_1, random_value_2, random_value_3),
                               "What is {} x {} - {}?".format(random_value_1, random_value_2, random_value_3),
                               "What is {} x {} x {}?".format(random_value_1, random_value_2, random_value_3)]
            random_answer = [random_value_1 + random_value_2 + random_value_3,
                             random_value_1 + random_value_2 - random_value_3,
                             random_value_1 - random_value_2 - random_value_3,
                             random_value_1 + random_value_2 * random_value_3,
                             random_value_1 * random_value_2 - random_value_3,
                             random_value_1 * random_value_2 * random_value_3]

            question = "{}. {}\n".format(true_level, random_question[random_pick])
        
            response = int(input(question))

            #Correct Answer
            if response == random_answer[random_pick]:
                score += 1
                level += 1
                print(correct.format(score, true_level, score, max_Q))
                max_questions -= 1
                
                random_value_1 = random.randrange((max_value * -1), (max_value + 1))
                random_value_2 = random.randrange((max_value * -1), (max_value + 1))
                random_value_3 = random.randrange((max_value * -1), (max_value + 1))
                random_pick = random.randrange(0, 6)

            #Incorrect Answer
            else:
                print(incorrect.format(random_answer[random_pick], score, true_level, score, max_Q))
                level += 1
                max_questions -= 1
                
                random_value_1 = random.randrange((max_value * -1), (max_value + 1))
                random_value_2 = random.randrange((max_value * -1), (max_value + 1))
                random_value_3 = random.randrange((max_value * -1), (max_value + 1))
                random_pick = random.randrange(0, 6)

        #Error Prevention
        except ValueError:
            print("Please enter an integer such as 1.\n")

    print("")

    #Restart
    print("")
    while run != 1:
        retry_value = input("Would you like to retry?\n")
        if "y" in retry_value.lower():
            retry = 0
            run = 1
        elif "n" in retry_value.lower():
            retry = 1
            break
        else:
            print("Please answer with Y or N.\n")
