from abc import ABC, abstractmethod
from .i_scoring_strategy import IScoringStrategy, StandardScore


class Question(ABC):
    """
    Parent class for questions
    """

    def __init__(self, question_text: str, correct_answer: str, scoring_strategy: IScoringStrategy | None = None):
        """
        Default constructor for questions

        :param question_text: the words of the question, i.e. "What is the capital of France"
        :param correct_answer: the correct answer to the question
        :param scoring_strategy: the scoring strategy to be used on the question, defaults to StandardScore strategy
        """
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
        # if the question was written with a "?" at the end, use that, else add it
        print(self.question_text +
              ("?" if self.question_text[-1] != "?" else ""))

    def calculateScore(self):
        pass

    def get_question_text(self):
        return self.question_text

    def get_correct_answer(self):
        return self.correct_answer

    def get_scoring_strategy_str(self):
        return self.scoring_strategy.get_str()

    @abstractmethod
    def get_type(self):
        pass


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text: str, correct_answer: str, possible_answers: list[str], scoring_strategy: IScoringStrategy | None = None):
        super().__init__(question_text, correct_answer, scoring_strategy)
        if not isinstance(possible_answers, list):
            raise TypeError("Possible Answers must be of type list[str]")

        self.possible_answers = possible_answers

    def print_possible_answers(self):
        answer_row = ""
        for answer in self.possible_answers:
            answer_row += answer + " "

        answer_row = answer_row.strip()
        print(answer_row)

    def get_possible_answers(self):
        return self.possible_answers

    def get_type(self):
        return "MultipleChoice"

    def display(self):
        super().print_question_text()
        self.print_possible_answers()


class TextQuestion(Question):
    def __init__(self, question_text: str, correct_answer: str, scoring_strategy: IScoringStrategy | None = None):
        super().__init__(question_text, correct_answer, scoring_strategy)

    def display(self):
        super().print_question_text()

    def get_type(self):
        return "Text"
