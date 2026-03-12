from .quiz import Quiz
from .round import Round
from .team import Team
from .game_session import GameSession
from .question_factory import QuestionFactory
from .i_scoring_strategy import PenaltyScore, HardScore
from .question import *

class QuizUI:
    def create_quiz():
        title = input("Enter your quiz title")
        author = input("Enter the quiz author")
        quiz = Quiz(title, author)
        return quiz

    def create_rounds(factory):
        rounds = []
        num_rounds = int(input("How many rounds would you like to create?"))

        for i in range(num_rounds):
            round_name = input(f"Enter round name {i+1}:")
            r = Round(round_name)

            num_questions = int(input("How many questions do you want in this round?"))

            for q in range(num_questions):

                q_type = input("Question type (MultipleChoice/Text): ")
                question_text = input("Question text: ")
                correct_answer = input("Correct answer: ")

                scoring = input("Scoring (Standard/Penalty/Hard): ")

                strategy = None
                if scoring.lower() == "penalty":
                    strategy = PenaltyScore()
                elif scoring.lower() == "hard":
                    strategy = HardScore()

                if q_type == "MultipleChoice":

                    possible_answers = []
                    num_options = int(input("How many options? "))

                    for i in range(num_options):
                        option = input(f"Option {i+1}: ")
                        possible_answers.append(option)

                    question = factory.create_question(
                        q_type="MultipleChoice",
                        question_text=question_text,
                        correct_answer=correct_answer,
                        possible_answers=possible_answers,
                        scoring_strategy=strategy
                    )

                else:

                    question = factory.create_question(
                        q_type="Text",
                        question_text=question_text,
                        correct_answer=correct_answer,
                        scoring_strategy=strategy
                    )

                r.add_question(question)

            rounds.append(r)

        return rounds

    def create_teams():
        teams = []

        num_teams = int(input("How many teams? "))

        for i in range(num_teams):
            name = input(f"Team {i+1} name: ")
            teams.append(Team(name))

        return teams

    def play_quiz(session, rounds, teams):

        for round_index, r in enumerate(rounds):

            print("\n====================")
            print(f"ROUND: {r.get_name()}")
            print("====================\n")

            for question in r.get_questions():
                question.display()

            for team in teams:

                print(f"\nAnswers for {team.get_name()}")

                answers = []

                for question in r.get_questions():

                    ans = input("Correct? (y/n): ")

                    if ans.lower() == "y":
                        answers.append(True)
                    else:
                        answers.append(False)

                session.calculate_team_score(team, round_index, answers)

            session.display_leaderboard()



