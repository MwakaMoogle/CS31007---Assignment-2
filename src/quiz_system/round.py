class Round:
    def _init_(self, categoryTitle):
        self.categoryTitle = categoryTitle
        self.questions = []

        def addQuestion(self, question):
                self.questions = self.questions + [question]

        def getQuestion(self, index):
            if not isinstance(index, int):
                 raise TypeError("The index must be an integer")
            if index < 0 or index>=len(self.questions):
                 raise IndexError("Enter a question that exists")
            

            return self.questions[index]