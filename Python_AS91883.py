#Imports
import random
import math
import time

#Needed Variable
retry = 0

#Quiz
while retry == 0:
    
    #Variables
    max_questions = 20
    level = 0
    score = 0
    errorcode = random.randrange(100000, 1000000)
    run = 0

    random_value_1 = random.randrange(0, 31)
    random_value_2 = random.randrange(0, 31)
    random_value_3 = random.randrange(0, 31)
    random_pick = random.randrange(0, 6)

    retry = 0

    correct = "Correct! Your current score is {} out of {}. ({}/20)"
    incorrect = "Incorrect, the answer was {}. Your current score is {} out of {}. ({}/20)"

    while max_questions != 0:
        try:
            #Total Score Value
            true_level = level + 1
        
            random_question = ["What is {} + {} + {}?".format(random_value_1, random_value_2, random_value_3), "What is {} + {} - {}?".format(random_value_1, random_value_2, random_value_3), "What is {} - {} - {}?".format(random_value_1, random_value_2, random_value_3), "What is {} + {} x {}?".format(random_value_1, random_value_2, random_value_3), "What is {} x {} - {}?".format(random_value_1, random_value_2, random_value_3), "What is {} x {} x {}?".format(random_value_1, random_value_2, random_value_3)]
            random_answer = [random_value_1 + random_value_2 + random_value_3, random_value_1 + random_value_2 - random_value_3, random_value_1 - random_value_2 - random_value_3, random_value_1 + random_value_2 * random_value_3, random_value_1 * random_value_2 - random_value_3, random_value_1 * random_value_2 * random_value_3]

            question = "{}. {}\n".format(true_level, random_question[random_pick])
        
            response = int(input(question))

            #Correct Answer
            if response == random_answer[random_pick]:
                score += 1
                level += 1
                print(correct.format(score, true_level, score))
                max_questions -= 1
                random_value_1 = random.randrange(0, 31)
                random_value_2 = random.randrange(0, 31)
                random_value_3 = random.randrange(0, 31)
                random_pick = random.randrange(0, 6)

            #Incorrect Answer
            else:
                print(incorrect.format(random_answer[random_pick], score, true_level, score))
                level += 1
                max_questions -= 1
                random_value_1 = random.randrange(0, 31)
                random_value_2 = random.randrange(0, 31)
                random_value_3 = random.randrange(0, 31)
                random_pick = random.randrange(0, 6)

        #Error Prevention
        except ValueError:
            print("Please enter an integer such as 1.")

    #Different Comments for Score Value
    print("")
    
    if score == 0:
        print("Your score is 0/20. You can definitely do better.")
    elif score > 0 and score < 6:
        print("Your score is {}/20. You could do better.".format(score))
    elif score > 5 and score < 11:
        print("Your score is {}/20. You still can do better.".format(score))
    elif score > 10 and score < 16:
        print("Your score is {}/20. Not bad.".format(score))
    elif score > 15 and score < 20:
        print("Your score is {}/20. Good Job!".format(score))
    elif score == 20:
        print("Your score is 20/20. PERFECT!!!")
    else:
        print("ERROR CODE: {}".format(errorcode))

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
            print("Please answer with Y or N.")
