import pytest
from quiz_system import Team, GameSession, Quiz

class TestParticipantRanking:

    def test_rank_two_teams_with_different_scores(self):
        quiz = Quiz("Test Quiz", "Author")
        team_a = Team("Team A")
        team_b = Team("Team B")
        team_a.addPoints(10)
        team_b.addPoints(5)
        session = GameSession(quiz, [team_a, team_b], 0)
        leaderboard = session.getLeaderboard()

        assert leaderboard == [team_a, team_b], "Ordered list was not returned as [Team A, Team B]"

    def test_rank_two_teams_with_same_score(self):
        quiz = Quiz("Test Quiz", "Author")
        team_a = Team("Team A")
        team_b = Team("Team B")
        team_a.addPoints(5)
        team_b.addPoints(5)
        session = GameSession(quiz, [team_a, team_b], 0)
        leaderboard = session.getLeaderboard()

        assert len(leaderboard) == 2, "Both teams should still appear in the leaderboard"
        assert team_a in leaderboard and team_b in leaderboard, "Both tied teams should be handled cleanly"

    def test_recalculate_rank_after_score_change(self):
        quiz = Quiz("Test Quiz", "Author")
        team_a = Team("Team A")
        team_b = Team("Team B")
        team_a.addPoints(5)
        team_b.addPoints(3)
        session = GameSession(quiz, [team_a, team_b], 0)
        leaderboard = session.getLeaderboard()

        assert leaderboard == [team_a, team_b], "Initial order should be [Team A, Team B]"

        team_b.addPoints(3)
        updated_leaderboard = session.getLeaderboard()

        assert updated_leaderboard == [team_b, team_a], "Leaderboard did not update after score change"

    def test_rank_teams_with_negative_score_present(self):
        quiz = Quiz("Test Quiz", "Author")
        team_a = Team("Team A")
        team_b = Team("Team B")
        team_a.addPoints(5)
        team_b.addPoints(-2)
        session = GameSession(quiz, [team_a, team_b], 0)
        leaderboard = session.getLeaderboard()

        assert leaderboard == [team_a, team_b], "Negative score should appear at the bottom"

    def test_rank_with_zero_participating_teams_returns_empty_list(self):
        quiz = Quiz("Test Quiz", "Author")
        session = GameSession(quiz, [], 0)
        leaderboard = session.getLeaderboard()

        assert leaderboard == [], "Expected an empty list when there are no participating teams"