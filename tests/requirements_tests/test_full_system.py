from quiz_system import *

class TestQuizSystem:
    def test_quiz_system(self, capsys):
        quiz = Quiz("Fun Quiz", "John Pork")
        rounds = [
            Round("Geography"),
            Round("Maths")
        ]
        factory = QuestionFactory()
        geography_questions = [
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
            possible_answers = ["London", "Paris", "Berlin", "Madrid"],
            scoring_strategy=PenaltyScore()
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
            correct_answer="Tokyo",
            scoring_strategy=HardScore()
            )
                ]
        maths_questions = [
            factory.create_question(
            q_type="MultipleChoice",
            question_text="What is 2+2",
            correct_answer="4",
            possible_answers = ["0", "2", "4", "5"],
            scoring_strategy=PenaltyScore()
            ),
            factory.create_question(
            q_type="MultipleChoice",
            question_text="If X+Y=6, and Y=1, What is X?",
            correct_answer="5",
            possible_answers = ["6", "1", "7", "5"]
            ),
            factory.create_question(
            q_type="Text",
            question_text="What comes after 6",
            correct_answer="7"
            ),
            factory.create_question(
            q_type="MultipleChoice",
            question_text="What is 9+10",
            correct_answer="19",
            possible_answers = ["21", "19", "910"],
            scoring_strategy=HardScore()
            ),
            factory.create_question(
            q_type="Text",
            question_text="What is 21/3",
            correct_answer="7",
            scoring_strategy=HardScore()
            )
            ]

        for question in geography_questions:
            rounds[0].add_question(question)

        for question in maths_questions:
            rounds[1].add_question(question)

        for r in rounds:
            quiz.add_round(r)

        teams = [Team("Quizzy Rascals"), Team("Quiztopher Columbus"), Team("Oozma Kappa"), Team("The Oracle")]
        session = GameSession(quiz, teams)

        answers = [
            [
                [True, True, True, True, True],
                [True, False, True, True, True],
                [False, True, False, True, False],
                [True, True, False, False, True]
            ],
            [
                [True, True, True, True, True],
                [False, True, True, False, True],
                [False, False, True, False, False],
                [False, True, False, True, True]
            ]
        ]

        for i,r in enumerate(rounds):
            for question in r.get_questions():
                question.display()

            for j, team in enumerate(teams):
                session.calculate_team_score(team, i, answers[i][j])
            session.display_leaderboard()


        assert teams[0].get_score() == 24
        assert teams[1].get_score() == 13
        assert teams[2].get_score() == 3
        assert teams[3].get_score() == 18
