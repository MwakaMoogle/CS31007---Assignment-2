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
        assert isinstance(question, MultipleChoiceQuestion), "Factory did not return a MultipleChoiceQuestion"
        assert question.text == "What is the capital of France?", "Question text was not set correctly"
        assert question.correctAnswer == "Paris", "Correct answer was not set correctly"

    def test_factory_creates_text_question(self):
        """
        Tests that requestion a "Text" question return the correct object.
        """
        factory = QuestionFactory()

        # Create the question object and popluate it 
        question = factory.createQuestion(
                type = "Text",
                text = "What is 5 + 5?",
                answer = "10"
                )

        # Assert
        assert isinstance(question, MultipleChoiceQuestion), "Factory did not return a TextQuestion"
        assert question.text == "Whatis 5 + 5?", "Question text was not set correctly"
        assert question.correctAnswer == "10", "Correct answer was not set correctly"

    def test_factory_raises_an_error_for_invalid_type(self):
        """
        Tests that requesting an invalid question object type raises an errror
        """

        factory = QuestionFactory()

        # Create a question object and populate it
        question = factory.createQuestion()
