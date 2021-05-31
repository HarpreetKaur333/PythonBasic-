# Final Exam Question 3 Harpreet Kaur(student id: 2031314)

class Question:
    def __init__(self, question, answerKey, correctAnswer, points):
        self.question = question
        self.answerKey = answerKey
        self.correctAnswer = correctAnswer
        self.points = points


questions = [
    # Question    #answer keys   #answer  #points
    Question("What’s the capital of Canada? " + "\n" + "(a) Ottawa " + "\n" + "(b) BritishColumbia " + "\n" +
             "(c) Quebec \n\n", ["a", "b", "c"], "a", 2),

    Question("How many time zones are there in Canada?" + "\n" + "(a) 6 " + "\n" + "(b) many " + "\n" + "(c) 11 \n\n",
             ["a", "b", "c"], "a", 2),

    Question("Name the longest river in the world?" + "\n" + "(a) Lena River " + "\n" + "(b) The Nile " + "\n" +
             "(c) Congo \n\n", ["a", "b", "c"], "b", 2),

    Question(
        "How many days does it take for the Earth to orbit the Sun?" + "\n" + "(a) 520" + "\n" + "(b) the sun" + "\n"
        + "(c) 365 \n\n", ["a", "b", "c"], "c", 2)]


def runQuestion(questions):
    score = 0

    for questionNo in questions:

        userAnswer = input(questionNo.question)

        rightAnswer = False

        while rightAnswer is False:
            if userAnswer not in questionNo.answerKey:
                rightAnswer = False
                print("Invalid option, Select a valid option: ")
                userAnswer = input(questionNo.question)

            else:
                rightAnswer = True

            if userAnswer == questionNo.correctAnswer:
                score += questionNo.points
                print("Correct!" + "\n\n")

            else:
                print("Nope wrong answer!! The Correct Answer is: " + str(questionNo.correctAnswer) + "\n\n")

    print("You are  score is: " + str(score) + "/" + str(sum(questionPoints.points for questionPoints in questions)))


runQuestion(questions)
