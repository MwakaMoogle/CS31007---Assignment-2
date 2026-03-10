class GameSession:
    
    def _init_(self, current_quiz, participating_teams, current_round_index):
        self.current_quiz = current_quiz
        self.participating_teams = participating_teams 
        self.current_round_index = current_round_index

    def start_session(self):
        self.current_round_index = 0 

    def enter_score(self, team, points):
        if team not in self.participating_teams:
            raise ValueError("This team is not in this session")
        
        team.addPoints(points)

    def get_leaderboard(self):
        return sorted(
            self.participating_teams, 
            key=lambda team: team.getScore(), 
            reverse=True )
    
    def displayLeaderboard(self):
        leaderboard = self.get_leaderboard()

        for i, team in enumerate(leaderboard, start=1):
            print(f"{i}. {team.teamName} - {team.get_score()}")
