class Team:
    """
    Class containing methods and variables relating to teams
    """

    def __init__(self, team_name: str):
        """
        Constructor for Team class

        :param team_name: name of team
        """
        self.team_name = team_name
        self.current_score = 0

    def add_points(self, points):
        """
        Adds points to team score

        :param points: how many points to add to the team
        """
        if not isinstance(points, int):
            raise TypeError("points must be an integer")

        self.current_score += points

    def get_score(self):
        """
        :returns: Current score of team
        """
        return self.current_score

    def reset_score(self):
        """
        Resets score to zero
        """
        self.current_score = 0

    def get_name(self):
        """
        :returns: Team name
        """
        return self.team_name
