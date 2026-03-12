from src.quiz_system import *
def main():

    ui = QuizUI()

    print("====== QUIZ CREATOR ======")

    quiz = ui.create_quiz()

    rounds = ui.create_rounds()

    quiz.add_rounds(rounds)

    teams = ui.create_teams()

    session = GameSession(quiz, teams)

    ui.play_quiz(session, rounds, teams)

    print("\n====== FINAL SCORES ======")

    session.display_leaderboard()


if __name__ == "__main__":
    main()
