import pytest
from quiz_system import Question, MultipleChoiceQuestion, TextQuestion

class TestQuestion:
    def test_display_question_text(self, capsys):
        q1 = TextQuestion("What is the capital of France", "France", None)
        q1.print_question_text()

        captured1 = capsys.readouterr()
        assert captured1.out == "What is the capital of France?\n"
        
        q2 = TextQuestion("What is the capital of France?", "France", None)
        q2.print_question_text()

        captured2 = capsys.readouterr()
        assert captured2.out == "What is the capital of France?\n"

    def test_print_print_possible_answers(self, capsys):
        q1 = MultipleChoiceQuestion("What is the capital of France", "France", ["London", "Paris", "Madrid", "Tokyo"], None)
        q1.print_possible_answers()
        captured = capsys.readouterr()
        assert captured.out == "London Paris Madrid Tokyo\n"

