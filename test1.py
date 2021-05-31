#Quiz Class
'''
Class: A class is a blueprint for a particular object
it stores the attributes of that object


In this class a quiz has 3 attributes - the question the valid choices and the answer
'''
class Quiz:


    def __init__(self, question, answer_keys, correct_answer, points):
        self.question = question #question to be asked
        self.answer_keys = answer_keys #options for the answer
        self.correct_answer = correct_answer #correct answer
        self.points = points #points for correct answer




#create a list of questions, answers and answer keys
#("\n" will put the text on a new line in the console)
questions = [
    # Question (instance)                                                                                  #answer keys   #answer
    Quiz("What color are apples? (type 'exit' to quit)" + "\n" + "(a) Green/Red" +  "\n" +"(b) 5" + "\n" + "(c) black \n\n", ["a","b","c"],"a", 5),
    Quiz("What color are bananas? (type 'exit' to quit)" + "\n" + "(a) white" +  "\n" +"(b) yellow" + "\n" + "(c) black \n\n", ["a","b","c"], "b", 5),
    Quiz("What color are oranges (type 'exit' to quit)" + "\n" + "(a) houses" +  "\n" +"(b) the sun" + "\n" + "(c) orange \n\n", ["a","b","c"], "c", 5)]




#function to present questions to user
def run_test(questions):
    score = 0 # set base score as zero


    ''' question_no is an aribitrary name given to represent the index of the 
    questions list (this can be anything x,z,e,t etc'''


    for question_no in questions: # call each question and ask user for an answser

        user_answer = input(question_no.question).lower().strip() #call question and take answer


        if user_answer.lower().strip() == 'exit': #if the user types exit convert answer to upper and quit the program
            print('bye!')
            quit()




        ###validate user input###
        #repeat user prompt if answer is not in approved list for that question
        answer_in_scope = False
        while answer_in_scope is False:
            if user_answer not in question_no.answer_keys: # if the user answe is not in the choice list prompt user for another answer
                answer_in_scope = False
                print("Not A valid option, Select a valid option: ")
                user_answer = input(question_no.question).lower().strip()

            else:
                answer_in_scope = True #assign true if the answer is a valid choice to move on

        ###validate answer###
        if (user_answer == question_no.correct_answer):
            score += question_no.points # if correct add points for that question to the score
            print("Correct!" + "\n\n") #identify the answer is correct

        else:
            print("Nope! the correct answer is: " + str(question_no.correct_answer) + "\n\n") #identify the answer is wrong


            #quiz points is the iteration variable - we sum points for the all the questions to get the total points
    print("You're score is: " + str(score) + "/" + str(sum(quiz_points.points for quiz_points in questions))) # calculate the score




#run the quiz
run_test(questions)
