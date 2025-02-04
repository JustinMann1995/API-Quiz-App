import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """checks if there are still questions in bank"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """grabs next question"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_test = html.unescape(self.current_question.text)
        question = f"Q. {q_test}"
        return question

    def check_answer(self, user_answer):
        """checks for correct answer, if yes adds 1 to score"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


























