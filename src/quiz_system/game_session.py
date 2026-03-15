from .quiz import Quiz
from .team import Team


class GameSession:
    """
    Class for a Game Session, handling a quiz and teams
    """

    def __init__(self, current_quiz: Quiz, participating_teams: list[Team], current_round_index: int = 0):
        """
        Constructor for GameSession class

        :param current_quiz: quiz to be played
        :param participating_teams: list of teams playing the quiz
        :param current_round_index: the round to start on
        """
        if not isinstance(current_quiz, Quiz):
            raise TypeError("currect quiz must be of type Quiz")
        if not isinstance(participating_teams, list):
            raise TypeError("participating teams must be of type list[Team]")

        self.current_quiz = current_quiz
        self.participating_teams = participating_teams
        self.current_round_index = current_round_index

    def start_session(self):
        """
        resets the quiz back to the first round
        """
        self.current_round_index = 0

    def enter_score(self, team, points):
        """
        adds the points for each round to each team

        :param team: The team to add points to
        :param points: the points being added to the team's score
        """
        if team not in self.participating_teams:
            raise ValueError("This team is not in this session")

        team.add_points(points)

    def calculate_team_score(self, team: Team, round_index: int, answer_correct_list: list[bool]):
        """
        calculates a team's score for a round, given a list of correct/incorrect,
        using each question's scoring strategy

        :param team: The team of which a score is being calculated
        :param round_index: The index of the quiz's rounds list, which is being calculated
        :param answer_correct_list: list of boolean for each answer wether they were correct or not
        """
        if not isinstance(team, Team):
            raise TypeError("team must be of type Team")
        if not isinstance(round_index, int):
            raise TypeError("round index must be of type int")
        if not isinstance(answer_correct_list, list):
            raise TypeError("answer correct list must be of type list[bool]")

        for i, question in enumerate(self.current_quiz.get_questions_for_round(round_index)):
            self.enter_score(team, question.scoring_strategy.execute_scoring(
                answer_correct_list[i]))

    def get_leaderboard(self):
        """
        :returns: a sorted leaderboard of teams in the game session
        """
        return sorted(
            self.participating_teams,
            key=lambda team: team.get_score(),
            reverse=True)

    def display_leaderboard(self):
        """
        displays the game session's leaderboard
        """
        leaderboard = self.get_leaderboard()

        for i, team in enumerate(leaderboard, start=1):
            print(f"{i}. {team.team_name} - {team.get_score()}")
