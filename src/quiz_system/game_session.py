from .quiz import Quiz
from .team import Team
class GameSession:
    
    def __init__(self, current_quiz: Quiz, participating_teams: list[Team], current_round_index: int = 0):
        if not isinstance(current_quiz, Quiz):
            raise TypeError("currect quiz must be of type Quiz")
        if not isinstance(participating_teams, list):
            raise TypeError("participating teams must be of type list[Team]")

        self.current_quiz = current_quiz
        self.participating_teams = participating_teams 
        self.current_round_index = current_round_index

    def start_session(self):
        self.current_round_index = 0 

    def enter_score(self, team, points):
        if team not in self.participating_teams:
            raise ValueError("This team is not in this session")
        
        team.add_points(points)

    def calculate_team_score(self, team: Team, round_index: int, answer_correct_list: list[bool]):
        if not isinstance(team, Team):
            raise TypeError("team must be of type Team")
        if not isinstance(round_index, int):
            raise TypeError("round index must be of type int")
        if not isinstance(answer_correct_list, list):
            raise TypeError("answer correct list must be of type list[bool]")

        for i, question in enumerate(self.current_quiz.get_rounds()[round_index].get_questions()):
            self.enter_score(team, question.scoring_strategy.execute_scoring(answer_correct_list[i]))

    def get_leaderboard(self):
        return sorted(
            self.participating_teams, 
            key=lambda team: team.get_score(), 
            reverse=True )
    
    def display_leaderboard(self):
        leaderboard = self.get_leaderboard()

        for i, team in enumerate(leaderboard, start=1):
            print(f"{i}. {team.team_name} - {team.get_score()}")
