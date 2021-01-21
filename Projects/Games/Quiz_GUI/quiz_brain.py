import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        format_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {format_text}."
        # answer = input(f"Q.{self.question_number}. {format_text}. (True/False)?: ")
        # self.check_answer(answer, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        correct_answer = self.current_question.answer
        if answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
