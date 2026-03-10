import pytest
from quiz_system import QuestionFactory, Round

class TestRounds:
    def test_adding_question_to_round(self):
        factory = QuestionFactory()
        question = factory.create_question(
                q_type="MultipleChoice",
                question_text="What is the capital of France",
                correct_answer="Paris",
                possible_answers = ["London", "Paris", "Berlin", "Madrid"]
                )
        round = Round(
                category_title="Geography"
               )
        num_questions_in_round = len(round.questions)
        round.add_question(question)

        assert question in round.questions
        assert len(round.questions) == num_questions_in_round + 1

    def test_adding_multiple_questions_to_round(self):
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
                q_type="Written",
                question_text="What is the capital of Japan",
                correct_answer="Tokyo"
                )
                ]
        round = Round(
                category_title="Geography"
               )

        for question in questions:
            round.add_question(question)
                
        for question in questions:
            assert question in round.questions

        assert len(round.questions) == len(questions)

    def test_removing_question_from_round(self):
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
                q_type="Written",
                question_text="What is the capital of Japan",
                correct_answer="Tokyo"
                )
                ]
        round = Round(
                category_title="Geography"
               )

        for question in questions:
            round.add_question(question)
                
        removed_question = round.remove_question(question_number=1)

        assert removed_question.category_title == "What is the capital of France"

        assert len(round.questions) == len(questions) - 1

    def test_getting_question_based_on_position(self):
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
                q_type="Written",
                question_text="What is the capital of Japan",
                correct_answer="Tokyo"
                )
                ]
        round = Round(
                category_title="Geography"
               )

        for question in questions:
            round.add_question(question)
            
        q = round.get_question(position=1)

        assert q.question_text == "What is the capital of France"

    def test_get_err_index(self):
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
                q_type="Written",
                question_text="What is the capital of Japan",
                correct_answer="Tokyo"
                )
                ]
        round = Round(
                category_title="Geography"
               )

        for question in questions:
            round.add_question(question)

        with pytest.raises(IndexError, match="Question not in Round"):
            q = round.get_question(position=6)


