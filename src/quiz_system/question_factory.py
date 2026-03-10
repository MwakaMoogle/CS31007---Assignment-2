from .question import *


class QuestionFactory:
    
    _question_types = {
            "Text": TextQuestion,
            "MultipleChoice": MultipleChoiceQuestion
    }

    def create_question(self, qType: str, **kwargs):
        """
        Builds and returns a Question object.
        Expects key arguements like: question_text, correct_answer, scoring_strategy and optionally possible_answers.
        """

        # Check if type exists
        if qType not in self._question_types:
            raise ValueError(f"Unknown question type: '{qType}'")

        # Check for empty question text
        text = kwargs.get("question_text", "")
        if not text or not text.strip():
            raise ValueError("Question text cannot be empty")

        # Check for missing answer
        if kwargs.get("correct_answer") is None:
            raise TypeError("Answer cannot be None")



        question_class = self._question_types[qType]
        return question_class(**kwargs)
