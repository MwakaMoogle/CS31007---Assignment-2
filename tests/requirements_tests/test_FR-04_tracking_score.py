import pytest
from quiz_system import Team, GameSession, Quiz

class TestTeamTracking:



    def test_add_points_1(self):
            team = Team("Team A")
            team.add_points(1)

            assert team.current_score == 1, "current_score was not increased by 1"

        
    def test_add_points_with_float_raises_exception(self):
            team = Team("Team A")

            with pytest.raises((TypeError, ValueError)):
                team.add_points(0.5)

        
    def test_add_points_minus_1(self):
            team = Team("Team A")
            team.add_points(-1)

            assert team.current_score == 0, "current_score should be 0 after adding -1"

    
    def test_add_points_increases_5(self):
            team = Team("Team A")
            team.add_points(5)

            assert team.current_score == 5, "current_score was not increased by 5"

        
    def test_get_score_returns_expected_total(self):
            team = Team("Team A")
            team.add_points(5)

            assert team.getScore() == 5, "getScore() did not return the expected total"

    
    def test_reset_score_to_0(self):
            team = Team("Team A")
            team.add_points(5)
            team.resetScore()

            assert team.current_score == 0, "resetScore() did not reset current_score to 0"

#Wasn't too sure if we would need this or not 

    def test_add_0_points_leaves_score_unchanged(self):
            team = Team("Team A")
            team.add_points(5)
            team.add_points(0)

            assert team.current_score == 5, "Adding 0 points should not change current_score"


class TestGameSessionScoreTracking:


    def test_create_game_session_with_dummy_teams_and_scores(self):
            quiz = Quiz("Test Quiz", "Author")
            team_a = Team("Team A")
            team_b = Team("Team B")

            team_a.add_points(3)
            team_b.add_points(7)

            session = GameSession(quiz, [team_a, team_b], 0)

            assert session.current_quiz == quiz, "GameSession did not store the Quiz correctly"

            assert len(session.participating_teams) == 2, "GameSession did not store the teams correctly"

            assert session.participating_teams[0].getScore() == 3, "Team A score not stored correctly"

            assert session.participating_teams[1].getScore() == 7, "Team B score not stored correctly"

    
    def test_enter_score_updates_specific_team_score(self):
            quiz = Quiz("Test Quiz", "Author")
            team_a = Team("Team A")
            team_b = Team("Team B")
            session = GameSession(quiz, [team_a, team_b], 0)

            session.enter_score(team_b, 5)

            assert team_a.getScore() == 0, "Wrong team score was modified"

            assert team_b.getScore() == 5, "Desired team score was not updated correctly"

    def test_enter_score_for_team_not_in_game_session(self):
            quiz = Quiz("Test Quiz", "Author")
            team_a = Team("Team A")
            missing_team = Team("Missing Team")
            session = GameSession(quiz, [team_a], 0)

            with pytest.raises(Exception):
                session.enter_score(missing_team, 5)