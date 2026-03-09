class GameSession:
    
    def _init_(self, current_quiz, participating_teams, current_round_index):
        self.current_quiz = current_quiz
        self.participating_teams = participating_teams 
        self.current_round_index = current_round_index

    def startSession(self):
        self.current_round_index = 0 

    def enterScore(self, team, points):
        if team not in self.participating_teams:
            raise ValueError("This team is not in this session")
        
        team.addPoints(points)

    def getLeaderboard(self):
        return sorted(
            self.participating_teams, 
            key=lambda team: team.getScore(), 
            reverse=True )
    
    def displayLeaderboard(self):
        leaderboard = self.getLeaderboard()

        for i, team in enumerate(leaderboard, start=1):
            print(f"{i}. {team.teamName} - {team.getScore()}")
