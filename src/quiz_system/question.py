from abc import ABC, abstractmethod
from .i_scoring_strategy import IScoringStrategy, StandardScore
class Question(ABC):
    def __init__(self, question_text: str, correct_answer: str, scoring_strategy: IScoringStrategy | None = None):
        self.question_text = question_text
        self.correct_answer = correct_answer
        if scoring_strategy == None:
            self.scoring_strategy = StandardScore()
        else:
            self.scoring_strategy = scoring_strategy

    @abstractmethod
    def display(self):
        pass

    def print_question_text(self):
        print(self.question_text + ("?" if self.question_text[-1] != "?" else "")) # if the question was written with a "?" at the end, use that, else add it

    def calculateScore(self):
        pass

class MultipleChoiceQuestion(Question):
    def __init__(self, question_text: str, correct_answer: str, possible_answers: list[str], scoring_strategy: IScoringStrategy | None = None):
        super().__init__(question_text, correct_answer, scoring_strategy)
        self.possible_answers = possible_answers

    def print_possible_answers(self):
        answer_row = ""
        for answer in self.possible_answers:
            answer_row += answer + " "
            
        answer_row = answer_row.strip()
        print(answer_row)



    def display(self):
        super().print_question_text()
        self.print_possible_answers()


class TextQuestion(Question):
    def __init__(self, question_text: str, correct_answer: str, scoring_strategy: IScoringStrategy | None = None):
        super().__init__(question_text, correct_answer, scoring_strategy)

    def display(self):
        super().print_question_text()
