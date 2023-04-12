class QuizBrain:
    # TODO: Construct the quiz model:

    def __init__(self, question_bank, category):
        self.question_list = question_bank
        self.num = 0
        self.score = 0
        self.category = category

    # TODO: Check if you reach the end of the question list:
    def still_has_questions(self):
        return self.num < len(self.question_list)


    # TODO: Input the current question:
    def curr_question(self):
        current_question = self.question_list[self.num]
        self.num += 1
        user_answer = input(f"Q.{self.num} from {self.category}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # TODO: check if the answer is correct:
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.num}")
        print("\n")
