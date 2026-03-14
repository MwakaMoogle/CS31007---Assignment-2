import pytest
from quiz_system import *

class TestFileManager:
    def test_save_to_file(self, tmp_path):
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

        for question in questions:
            quiz_round.add_question(question)

        quiz.add_rounds(quiz_round)

        fm = FileManager()
        tmp_dir = tmp_path / "tmp_dir"
        tmp_dir.mkdir()
        tmp_file = tmp_dir / "test_save_file.json"
        fm.save_quizzes_to_file([quiz], tmp_file)

        assert tmp_file.read_text() == """{"quizzes": [{"quiz_title": "Test Quiz", "quiz_author": "John Pork", "rounds": [{"round_title": "Geography", "questions": [{"question_type": "MultipleChoice", "question_text": "What is the capital of France", "correct_answer": "Paris", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "MultipleChoice", "question_text": "What is the capital of England", "correct_answer": "London", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "MultipleChoice", "question_text": "What is the capital of Germany", "correct_answer": "Berlin", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "MultipleChoice", "question_text": "What is the capital of Spain", "correct_answer": "Madrid", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "Text", "question_text": "What is the capital of Japan", "correct_answer": "Tokyo", "scoring_strategy": "StandardScore"}]}]}]}"""

    
    def test_load_from_file(self, tmp_path):
        fm = FileManager()
        tmp_dir = tmp_path / "tmp_dir"
        tmp_dir.mkdir()
        tmp_file = tmp_dir / "test_load_file.json"
        tmp_file.write_text("""{"quizzes": [{"quiz_title": "Test Quiz", "quiz_author": "John Pork", "rounds": [{"round_title": "Geography", "questions": [{"question_type": "MultipleChoice", "question_text": "What is the capital of France", "correct_answer": "Paris", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "MultipleChoice", "question_text": "What is the capital of England", "correct_answer": "London", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "MultipleChoice", "question_text": "What is the capital of Germany", "correct_answer": "Berlin", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "MultipleChoice", "question_text": "What is the capital of Spain", "correct_answer": "Madrid", "possible_answers": ["London", "Paris", "Berlin", "Madrid"], "scoring_strategy": "StandardScore"}, {"question_type": "Text", "question_text": "What is the capital of Japan", "correct_answer": "Tokyo", "scoring_strategy": "StandardScore"}]}]}]}""")

        quizzes = fm.load_quizzes_from_file(tmp_file)

        assert isinstance(quizzes, list)


