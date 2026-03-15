class Quiz:
    """
    Class that handles the quizzes themselves. 
    contains a title, list of rounds and an author.
    """

    def __init__(self, title, author):
        """
        Constructor for Quiz class.

        :param title: title of the quiz
        :param author: author of the quiz
        """
        self.title = title
        self.rounds = []
        self.author = author

    def add_rounds(self, rounds):
        """
        adds rounds to quiz, takes in either one or list of rounds.

        :param rounds: can either be a single round or list of rounds
        """
        if isinstance(rounds, list):
            self.rounds = self.rounds + rounds
        else:
            self.rounds = self.rounds + [rounds]

    def remove_round(self, index):
        """
        removes a specified round from the quiz

        :param index: the index in the rounds[] list to remove
        """
        if not isinstance(index, int):
            raise TypeError("index has to be an integer")
        if index < 0 or index >= len(self.rounds):
            raise IndexError(
                "This round is outiside the index range, please choose an existing round")

        self.rounds.pop(index)

    def get_total_rounds(self):
        """
        :returns: the total number of rounds in the quiz
        """
        return len(self.rounds)

    def get_rounds(self):
        """
        :returns: the list of rounds in the quiz
        """
        return self.rounds

    def get_title(self):
        """
        :returns: the title of the quiz
        """
        return self.title

    def get_author(self):
        """
        :returns: the author of the quiz
        """
        return self.author

    def get_questions_for_round(self, round_index):
        """
        gets questions in a specific round

        :returns: questions from specified round
        """
        return self.rounds[round_index].get_rounds()
