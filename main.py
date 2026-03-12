from quiz_system.quiz_ui import QuizUI
from src.quiz_system import *.py
def main():

    factory = QuestionFactory()

    print("====== QUIZ CREATOR ======")

    quiz = QuizUI.create_quiz()

    rounds = create_rounds(factory)

    for r in rounds:
        quiz.add_round(r)

    teams = create_teams()

    session = GameSession(quiz, teams)

    play_quiz(session, rounds, teams)

    print("\n====== FINAL SCORES ======")

    session.display_leaderboard()


if __name__ == "__main__":
    main()
