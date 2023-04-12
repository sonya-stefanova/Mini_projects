from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# TODO: Reach the question and the answer from the list of dictionaries and loop through it:
for current_dict_item in question_data:
    text = current_dict_item["question"]
    answer = current_dict_item["correct_answer"]
    category = current_dict_item["category"]

    # TODO: Create every new question as an object and add it in a list of objects that could be processed:
    new_question = Question(text, answer)
    question_bank.append(new_question)

# TODO: Create the quiz class that declares the actions that must be followed in connection with every object in the list
quiz = QuizBrain(question_bank, category)

# while quiz.still_has_questions(): # Till the end of the list of questions, print the question
#     quiz.curr_question()

i=0
while i<len(question_bank):
    quiz.curr_question()
    i+=1


# TODO: Print the final results:
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.num}")
