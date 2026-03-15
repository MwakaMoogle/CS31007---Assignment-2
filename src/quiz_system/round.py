class Round:
    """
    Class handling round information.
    Contains a title for the round as well as a list of questions
    """

    def __init__(self, category_title):
        """
        Constructor for Round class

        :param category_title: the title of the round,
        i.e. "Geography Round"
        """
        self.category_title = category_title
        self.questions = []

    def add_question(self, question):
        """
        adds a question to the round

        :param question: question to be added
        """
        self.questions = self.questions + [question]

    def get_question(self, index):
        """
        gets a question at specified index in questions list

        :param index: index of questions list

        :returns: question at that index
        """
        if not isinstance(index, int):
            raise TypeError("The index must be an integer")
        if index < 0 or index >= len(self.questions):
            raise IndexError("Enter a question that exists")

        return self.questions[index]

    def get_questions(self):
        """
        :returns: round's questions list
        """
        return self.questions

    def remove_question(self, index):
        """
        removes question at specified index

        :param index: index of question to be removed in questions list
        """
        del self.questions[index]

    def get_title(self):
        """
        :returns: title of the round
        """
        return self.category_title
