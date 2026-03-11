class Round:
    def __init__(self, category_title):
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

    def get_questions(self):
        return self.questions
    
    def remove_question(self, index):
       pass 
        
