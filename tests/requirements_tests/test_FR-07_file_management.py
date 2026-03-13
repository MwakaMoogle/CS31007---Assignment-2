import pytest
from quiz_system import *

class TestFileManager:
    def test_save_to_file(self):
        quiz = Quiz("Test Quiz", "John Pork")
        factory = QuestionFactory()
        questions = [
                factory.create_question(
                q_type="MultipleChoice",
                question_text="What is the capital of France",
                correct_answer="Paris",
                possible_answers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.create_question(
                q_type="MultipleChoice",
                question_text="What is the capital of England",
                correct_answer="London",
                possible_answers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.create_question(
                q_type="MultipleChoice",
                question_text="What is the capital of Germany",
                correct_answer="Berlin",
                possible_answers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.create_question(
                q_type="MultipleChoice",
                question_text="What is the capital of Spain",
                correct_answer="Madrid",
                possible_answers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.create_question(
                q_type="Text",
                question_text="What is the capital of Japan",
                correct_answer="Tokyo"
                )
                ]
        quiz_round = Round(
                category_title="Geography"
               )

        quiz_round.add_question(questions)

        quiz.add_rounds(quiz_round)

        fm = FileManager()
        fm.save_quizzes_to_file([quiz], "test_file.json")