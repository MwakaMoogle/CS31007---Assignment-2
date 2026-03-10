import pytest
from quiz_system import QuestionFactory, MultipleChoiceQuestion, TextQuestion

class TestQuestionFactory:

    def test_factory_creates_multiple_choice_question(self):
        """
        Tests that requesting a "MultipleChoice" question returns the corret object.
        """
        factory = QuestionFactory()

        # Create the Question object and popluate it
        question = factory.create_question(
            q_type = "MultipleChoice",
            question_text = "What is the capital of France?",
            correct_answer = "Paris",
            possible_answers = ["London", "Paris", "Berlin", "Madrid"]
            )

        # Assert
        assert isinstance(question, MultipleChoiceQuestion), "Factory did not return a MultipleChoiceQuestion"
        assert question.question_text == "What is the capital of France?", "Question text was not set correctly"
        assert question.correct_answer == "Paris", "Correct answer was not set correctly"

    def test_factory_creates_text_question(self):
        """
        Tests that requestion a "Text" question return the correct object.
        """
        factory = QuestionFactory()

        # Create the question object and popluate it 
        question = factory.create_question(
                q_type = "Text",
                question_text = "What is 5 + 5?",
                correct_answer = "10"
                )

        # Assert
        assert isinstance(question, TextQuestion), "Factory did not return a TextQuestion"
        assert question.question_text == "What is 5 + 5?", "Question text was not set correctly"
        assert question.correct_answer == "10", "Correct answer was not set correctly"

    def test_factory_raises_an_error_for_invalid_type(self):
        """
        Tests that requesting an invalid question object type raises an errror
        """

        factory = QuestionFactory()

        # Create a question object and populate it
        with pytest.raises(ValueError, match="Unknown question type: 'Audio'"):
            question = factory.create_question(
                    q_type = "Audio",
                    question_text = "What song is this?",
                    correct_answer = "SEVEN GOBLINS, Masayoshi Takanaka"
                    )
      
    def test_factory_rejects_empty_text_string(self):
        """
        Tests that creating a question object with the text field empty raises an error
        """
        factory = QuestionFactory()
        
        # Testing an empty string as the input for text
        with pytest.raises(ValueError, match="Question text cannot be empty"):
            factory.create_question(
                q_type = "Text",
                question_text = "", # Empty String
                correct_answer = "10"
                )

        # Testing white space(s) for the text
        with pytest.raises(ValueError, match="Question text cannot be empty"):
            factory.create_question(
                q_type = "Text",
                question_text = "   ", # Empty space
                correct_answer = "10"
                )
        
    def test_factory_rejects_nill_for_an_answer(self):
        """
        Tests that having the answer of the question being nill raises an error
        """
        
        factory = QuestionFactory()

        with pytest.raises(TypeError, match="Answer cannot be None"):
            factory.create_question(
                q_type = "Text",
                question_text = "What is 5 + 5",
                correct_answer = None #Invalid Data Type Requested
                )
