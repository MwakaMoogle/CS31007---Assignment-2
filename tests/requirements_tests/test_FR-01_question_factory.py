import pytest
from quiz_system import QuestionFactory, MultipleChoiceQuestion, TextQuestion

class TestQuestionFactory:

    def test_factory_creates_multiple_choice_question(self):
        """
        Tests that requesting a "MultipleChoice" question returns the corret object.
        """
        factory = QuestionFactory()

        # Create the Question object and popluate it
        question = factory.createQuestion(
            type = "MultipleChoice",
            text = "What is the capital of France?",
            answer = "Paris",
            possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
            )

        # Assert
        assert isinstace(question, MultipleChoiceQuestion), "Factory did nor return a MultipleChoiceQuestion"
        assert question.text == "What is the capital of France?", "Question text was not set correctly"
        assert question.correctAnswer == "Paris", "Correct answer was not set correctly"