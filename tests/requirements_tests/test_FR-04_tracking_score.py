import pytest
from quiz_system import Team, GameSession, Quiz

class TestTeamTracking:



    def test_add_points_1(self):
            team = Team("Team A")
            team.addPoints(1)

            assert team.currentScore == 1, "currentScore was not increased by 1"

        
    def test_add_points_with_float_raises_exception(self):
            team = Team("Team A")

            with pytest.raises((TypeError, ValueError)):
                team.addPoints(0.5)

        
    def test_add_points_minus_1(self):
            team = Team("Team A")
            team.addPoints(-1)

            assert team.currentScore == 0, "currentScore should be 0 after adding -1"

    
    def test_add_points_increases_5(self):
            team = Team("Team A")
            team.addPoints(5)

            assert team.currentScore == 5, "currentScore was not increased by 5"

        
    def test_get_score_returns_expected_total(self):
            team = Team("Team A")
            team.addPoints(5)

            assert team.getScore() == 5, "getScore() did not return the expected total"

    
    def test_reset_score_to_0(self):
            team = Team("Team A")
            team.addPoints(5)
            team.resetScore()

            assert team.currentScore == 0, "resetScore() did not reset currentScore to 0"

#Wasn't too sure if we would need this or not 

    def test_add_0_points_leaves_score_unchanged(self):
            team = Team("Team A")
            team.addPoints(5)
            team.addPoints(0)

            assert team.currentScore == 5, "Adding 0 points should not change currentScore"


class TestGameSessionScoreTracking:


    def test_create_game_session_with_dummy_teams_and_scores(self):
            quiz = Quiz("Test Quiz", "Author")
            team_a = Team("Team A")
            team_b = Team("Team B")

            team_a.addPoints(3)
            team_b.addPoints(7)

            session = GameSession(quiz, [team_a, team_b], 0)

            assert session.currentQuiz == quiz, "GameSession did not store the Quiz correctly"

            assert len(session.participatingTeams) == 2, "GameSession did not store the teams correctly"

            assert session.participatingTeams[0].getScore() == 3, "Team A score not stored correctly"

            assert session.participatingTeams[1].getScore() == 7, "Team B score not stored correctly"

    
    def test_enter_score_updates_specific_team_score(self):
            quiz = Quiz("Test Quiz", "Author")
            team_a = Team("Team A")
            team_b = Team("Team B")
            session = GameSession(quiz, [team_a, team_b], 0)

            session.enterScore(team_b, 5)

            assert team_a.getScore() == 0, "Wrong team score was modified"

            assert team_b.getScore() == 5, "Desired team score was not updated correctly"

    def test_enter_score_for_team_not_in_game_session(self):
            quiz = Quiz("Test Quiz", "Author")
            team_a = Team("Team A")
            missing_team = Team("Missing Team")
            session = GameSession(quiz, [team_a], 0)

            with pytest.raises(Exception):
                session.enterScore(missing_team, 5)