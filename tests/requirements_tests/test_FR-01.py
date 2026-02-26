# FR-01: System must allow user to create different questions with different formats

# Test1.1: Create a question default question object
def test_create_default_question():
    from question import Question
    q = Question()
    assert q.questionText == ""
    assert q.questionAnswer == Answer()
    assert q.scoringStrategy == "default"

