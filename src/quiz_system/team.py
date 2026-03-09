class Team:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.current_score = 0
        self.match_history = []

    def addPoints(self, points):
        if not isinstance(points, int):
            raise TypeError("points must be an integer")
        
        self.current_score += points

        if self.current_score < 0:
            self.current_score = 0

        self.match_history.append(points)


    def getScore(self):
        return self.current_score

    def resetScore(self):
        self.current_score = 0 
