import pytest
from quiz_system import Question, MultipleChoiceQuestion, TextQuestion

class TestQuestion:
    def test_display_question_text(capsys):
        q1 = TextQuestion("What is the capital of France", "France", None)
        captured1 = capsys.readouterr()
        q1.display_question_text()
        assert captured1.out() == "What is the capital of France?\n"
        
        q2 = TextQuestion("What is the capital of France?", "France", None)
        captured2 = capsys.readouterr()
        q2.display_question_text()
        assert captured2.out() == "What is the capital of France?\n"

