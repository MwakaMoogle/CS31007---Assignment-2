import pytest
from quiz_system import Team, GameSession, Quiz

class TestDisplayLeaderboard:
    def test_displaying_empty_leaderboard(self, capsys):
        quiz = Quiz("Test Quiz", "Author")
        session = GameSession(quiz, [], 0)
        session.display_leaderboard()
        captured = capsys.readouterr()

        assert captured.out == ""

    def test_displaying_normal_leaderboard(self, capsys):
        quiz = Quiz("Test Quiz", "Author")
        team_a = Team("Team A")
        team_b = Team("Team B")
        team_c = Team("Team C")
        team_a.add_points(5)
        team_b.add_points(6)
        team_c.add_points(4)
        session = GameSession(quiz, [team_a, team_b, team_c], 0)

        session.display_leaderboard()
        captured = capsys.readouterr()

        assert captured.out == "1. Team B - 6\n2. Team A - 5\n3. Team C - 4\n"

    def test_displaying_drawing__non_winning_teams(self, capsys):
        quiz = Quiz("Test Quiz", "Author")
        team_a = Team("Team A")
        team_b = Team("Team B")
        team_c = Team("Team C")
        team_a.add_points(5)
        team_b.add_points(6)
        team_c.add_points(5)
        session = GameSession(quiz, [team_a, team_b, team_c], 0)

        session.display_leaderboard()
        captured = capsys.readouterr()

        assert captured.out == "1. Team B - 6\n2. Team A - 5\n3. Team C - 5\n"

    def test_displaying_drawing__non_winning_teams(self, capsys):
        quiz = Quiz("Test Quiz", "Author")
        team_a = Team("Team A")
        team_b = Team("Team B")
        team_c = Team("Team C")
        team_a.add_points(5)
        team_b.add_points(6)
        team_c.add_points(6)
        session = GameSession(quiz, [team_a, team_b, team_c], 0)

        session.display_leaderboard()
        captured = capsys.readouterr()

        assert captured.out == "1. Team B - 6\n2. Team C - 6\n3. Team A - 5\n"


