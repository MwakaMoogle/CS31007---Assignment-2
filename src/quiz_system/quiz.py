class Quiz:
    def __init__(self, title, author):
        self.title = title
        self.rounds = []
        self.author = author


    def add_round(self, rounds):
        self.rounds = self.rounds + [rounds] 

    def remove_round(self, index):
        if not isinstance(index, int):
            raise TypeError("index has to be an integer")
        if index < 0 or index >=len(self.rounds):
            raise IndexError("This round is outiside the index range, please choose an existing round")
        
        self.rounds.pop(index)

    def get_total_rounds(self):
        return len(self.rounds)
