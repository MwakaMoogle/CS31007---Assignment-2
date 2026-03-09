from abc import ABC, abstractmethod
from .i_scoring_strategy import IScoringStrategy
class Question(ABC):
    def __init__(self, question_text: str, correct_answer: str, scoring_strategy: IScoringStrategy):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.scoring_strategy = scoring_strategy

    @abstractmethod
    def display():
        pass

    def print_question_text():
        print(question_text + "?" if question_text[-1] != "?" else "") # if the question was written with a "?" at the end, use that, else add it

    def calculateScore():
        pass

class MultipleChoiceQuestion(Question):
    def __init__(self, question_text: str, correct_answer: str, possible_answers: list[str], scoring_strategy: IScoringStrategy):
        super().__init__(question_text, correct_answer, scoring_strategy)
        self.possible_answers = possible_answers

    def print_possible_answers():
        print(f"+{"-" for answer in possible_answers}")

    def display():
        print_question_text()
        print_possible_answers()


class TextQuestion(Question):
    def __init__(self, question_text: str, correct_answer: str, scoring_strategy: IScoringStrategy):
        super().__init__(question_text, correct_answer, scoring_strategy)

    def display():
        print_question_text()
