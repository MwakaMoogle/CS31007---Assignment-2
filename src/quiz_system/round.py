class Round:
    def _init_(self, category_title):
        self.category_title = category_title
        self.questions = []

        def add_question(self, question):
                self.questions = self.questions + [question]

        def get_question(self, index):
            if not isinstance(index, int):
                 raise TypeError("The index must be an integer")
            if index < 0 or index>=len(self.questions):
                 raise IndexError("Enter a question that exists")
            

            return self.questions[index]
