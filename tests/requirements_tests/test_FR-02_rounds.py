import pytest
from quiz_system import QuestionFactory, Round

class TestRounds:
    def test_adding_question_to_quiz_round(self):
        factory = QuestionFactory()
        question = factory.create_question(
                q_type="MultipleChoice",
                question_text="What is the capital of France",
                correct_answer="Paris",
                possible_answers = ["London", "Paris", "Berlin", "Madrid"]
                )
        quiz_round = Round(
                category_title="Geography"
               )
        num_questions_in_quiz_round = len(quiz_round.questions)
        quiz_round.add_question(question)

        assert question in quiz_round.questions
        assert len(quiz_round.questions) == num_questions_in_quiz_round + 1

    def test_adding_multiple_questions_to_quiz_round(self):
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
                
        for question in questions:
            assert question in quiz_round.questions

        assert len(quiz_round.questions) == len(questions)

    def test_removing_question_from_quiz_round(self):
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

        #TODO Need to chek the correct question has been removed form the Question object array.
        delete_question = quiz_round.get_question(2)
        quiz_round.remove_question(2)

        assert len(quiz_round.questions) == len(questions) - 1 

    def test_getting_question_based_on_index(self):
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
            
        q = quiz_round.get_question(index=0)

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

        with pytest.raises(IndexError, match="Enter a question that exists"):
            q = quiz_round.get_question(index=6)


