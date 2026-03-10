class GameSession:
    
    def __init__(self, current_quiz, participating_teams, current_round_index):
        self.current_quiz = current_quiz
        self.participating_teams = participating_teams 
        self.current_round_index = current_round_index

    def start_session(self):
        self.current_round_index = 0 

    def enter_score(self, team, points):
        if team not in self.participating_teams:
            raise ValueError("This team is not in this session")
        
        team.add_points(points)

    def get_leaderboard(self):
        return sorted(
            self.participating_teams, 
            key=lambda team: team.get_score(), 
            reverse=True )
    
    def display_leaderboard(self):
        leaderboard = self.get_leaderboard()

        for i, team in enumerate(leaderboard, start=1):
            print(f"{i}. {team.team_name} - {team.get_score()}")
