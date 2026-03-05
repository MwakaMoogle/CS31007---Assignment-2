import pytest
from quiz_system import QuestionFactory, Round

class TestRounds:
    def test_adding_question_to_round(self):
        factory = QuestionFactory()
        question = factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of France",
                answer="Paris",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                )
        round = Round(
                title="Geography"
               )
        num_questions_in_round = len(round.questions)
        round.addQuestion(question)

        assert question in round.questions
        assert len(round.questions) == num_questions_in_round + 1

    def test_adding_multiple_questions_to_round(self):
        factory = QuestionFactory()
        questions = [
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of France",
                answer="Paris",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of England",
                answer="London",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Germany",
                answer="Berlin",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Spain",
                answer="Madrid",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="Written",
                text="What is the capital of Japan",
                answer="Tokyo"
                )
                ]
        round = Round(
                title="Geography"
               )

        for question in questions:
            round.addQuestion(question)
                
        for question in questions:
            assert question in round.questions

        assert len(round.questions) == len(questions)

    def test_removing_question_from_round(self):
        factory = QuestionFactory()
        questions = [
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of France",
                answer="Paris",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of England",
                answer="London",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Germany",
                answer="Berlin",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Spain",
                answer="Madrid",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="Written",
                text="What is the capital of Japan",
                answer="Tokyo"
                )
                ]
        round = Round(
                title="Geography"
               )

        for question in questions:
            round.addQuestion(question)
                
        removed_question = round.remove_question(question_number=1)

        assert removed_question.title == "What is the capital of France"

        assert len(round.questions) == len(questions) - 1

    def test_getting_question_based_on_position(self):
        factory = QuestionFactory()
        questions = [
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of France",
                answer="Paris",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of England",
                answer="London",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Germany",
                answer="Berlin",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Spain",
                answer="Madrid",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="Written",
                text="What is the capital of Japan",
                answer="Tokyo"
                )
                ]
        round = Round(
                title="Geography"
               )

        for question in questions:
            round.addQuestion(question)
            
        q = round.get_question(position=1)

        assert q.text == "What is the capital of France"

    def test_get_err_index(self):
        factory = QuestionFactory()
        questions = [
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of France",
                answer="Paris",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of England",
                answer="London",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Germany",
                answer="Berlin",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="MultipleChoice",
                text="What is the capital of Spain",
                answer="Madrid",
                possibleAnswers = ["London", "Paris", "Berlin", "Madrid"]
                ),
                factory.createQuestion(
                qType="Written",
                text="What is the capital of Japan",
                answer="Tokyo"
                )
                ]
        round = Round(
                title="Geography"
               )

        for question in questions:
            round.addQuestion(question)

        with pytest.raises(IndexError, match="Question not in Round"):
            q = round.get_question(position=6)


