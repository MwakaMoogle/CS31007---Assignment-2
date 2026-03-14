from .quiz import Quiz
from .round import Round
from .team import Team
from .game_session import GameSession
from .question_factory import QuestionFactory
from .i_scoring_strategy import BonusScore, PenaltyScore, HardScore
from .question import *

class QuizUI:

    def __init__(self):
        self.factory = QuestionFactory()
        self.quiz: Quiz
        self.game_session: GameSession

    def __create_quiz(self):
        title = input("Enter your quiz title: ")
        author = input("Enter the quiz author: ")
        self.quiz = Quiz(title, author)
        
    def __create_text_question(self, question_type, text, answer, scoring):
        question = self.factory.create_question(
                q_type=question_type,
                question_text=text,
                correct_answer=answer,
                scoring_strategy=scoring
                )
        return question

    def __create_multiplechoice_question(self, question_type, text, answer, scoring, possible_answers):
        question = self.factory.create_question(
                q_type=question_type,
                question_text=text,
                correct_answer=answer,
                scoring_strategy=scoring,
                possible_answers=possible_answers
                )
        return question

    def __ask_uesr_for_scoring_strategy(self):
        scoring = IScoringStrategy
        print("Please select a scoring strategy from the following")
        choice = int(input("1. Standard Score (1 point)\n2. Hard Score (5 points)\n3. Penalty Score (2 for correct, -1 for incorrect)\n4. Bonus Score (10 points)\nEnter here: "))
        while choice < 1 or choice > 4:
            print("Please enter a number from 1 to 4.")
            choice = int(input("1. Standard Score (1 point)\n2. Hard Score (5 points)\n3. Penalt Score (2 for correct, -1 for incorrect)\n4. Bonus Score (10 points)\nEnter here: "))
        
        if choice == 1:
            scoring = StandardScore
        elif choice == 2:
            scoring = HardScore
        elif choice == 3: 
            scoring = PenaltyScore
        elif choice == 4:
            scoring = BonusScore
        else:
            print("Unkown error has occured")
            exit()
        
        return scoring

    def __ask_user_for_possible_answers(self):
        possible_answers = []
        arr_length = int(input("Please enter how many possible answers you want (max 4): "))
        while arr_length < 2 or arr_length > 4:
            print("Invalid input")
            arr_length = int(input("Please enter how many possible answers you want (max 4): "))
        for i in range(arr_length):
            answer = input("Please enter a possible answer:")
            possible_answers.append(answer)
        
        return possible_answers

        

    def __create_rounds(self):
        rounds = []
        num_rounds = int(input("How many rounds would you like to create?: "))

        for i in range(num_rounds):
            print(f"Round: {i}")
            round_name = input(f"Enter round name {i+1}: ")
            r = Round(round_name)

            num_questions = int(input("How many questions do you want in this round?: "))

            for q in range(num_questions):
                question = None
                print(f"\nQuestion: {q}")
                choice = int(input("1. Create a Text Question\n2. Create Multiplechoice Question\nEnter here: "))
                while choice < 1 or choice > 2:
                    print("Please choose between option '1' and '2'") 
                    choice = int(input("1. Create a Text Question\n2. Create Multiplechoice Question\nEner here: "))
                
                text = input("Enter the question text here: ")
                answer = input("Enter the answer to the question here: ")

                if choice == 1:
                    scoring =  self.__ask_uesr_for_scoring_strategy()
                    question = self.__create_text_question("Text", text, answer, scoring)
                elif choice == 2:
                    scoring =  self.__ask_uesr_for_scoring_strategy()
                    possible_answers = self.__ask_user_for_possible_answers()
                    question = self.__create_multiplechoice_question("MultipleChoice", text, answer, scoring, possible_answers)
                    
                else:
                    print("Unknown errror has occured")
                    exit()

                r.add_question(question)

            rounds.append(r)

        return rounds

    def __create_teams(self):
        teams = []

        num_teams = int(input("How many teams?: "))

        for i in range(num_teams):
            name = input(f"Team {i+1} name: ")
            teams.append(Team(name))

        return teams
    
    # asks the user for a number between, num_min and num_max
    def __get_user_choice(self, num_min, num_max):
        if not isinstance(num_min, int)  or not isinstance(num_max, int):
            raise TypeError("num_min and num_max must be integers")
        choice = int(input(f"Enter here: ({num_min}-{num_max})"))
        while choice < num_min or choice > num_max:
            print(f"Please enter a number between {num_min} and {num_max}")
            choice = int(input(f"Enter here: ({num_min}-{num_max})"))
        return choice
        



    def __initialise_quiz(self):
        print("\n")
        print("Creating New Quiz...")
        self.__create_quiz()
        self.quiz.add_rounds(self.__create_rounds())


        

    def __load_quiz(self):
        pass
        

    def __play_quiz(self):

        text = input("\nEnter the question text here: ")
        answer = input("\nEnter the answer to the question here: ")
        for round_index, r in enumerate(rounds):

            print("\n==========================================================================")
            print(f"                         ROUND: {r.get_title()}                            ")
            print("============================================================================\n")

            for question in r.get_questions():
                question.display()

            for team in teams:

                print(f"\nAnswers for {team.get_name()}")

                answers = []

                for question in r.get_questions():

                    ans = input("Correct? (y/n): ")

                    if ans.lower() == "y":
                        answers.append(True)
                    else:
                        answers.append(False)

                session.calculate_team_score(team, round_index, answers)

            session.display_leaderboard()

    def __main_menu(self):
        print("=================================================================================")
        print("                                Quiz Systme 1.0                                  ")
        print("=================================================================================")
        print("1.New Quiz\n2. Load Quiz\n3.Exit Program")
        choice = self.__get_user_choice(1, 3)
        if choice == 1:
            quiz = self.__initialise_quiz()
        elif choice ==2:
            quiz = self.__load_quiz()
        elif choice == 3:
            print("Thanks for using the program!!!")
            exit()
        else: 
            print("Unkown Error has Occured")



