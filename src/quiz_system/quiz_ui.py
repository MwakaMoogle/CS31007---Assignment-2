from .quiz import Quiz
from .round import Round
from .team import Team
from .game_session import GameSession
from .question_factory import QuestionFactory
from .i_scoring_strategy import BonusScore, PenaltyScore, HardScore
from .question import *
from.file_manager import *

class QuizUI:
    """
    Class handling UI of the quiz system
    """

    def __init__(self):
        """
        Constructor for QuizUI class
        """
        self.fm = FileManager()
        self.factory = QuestionFactory()
        self.quiz: Quiz
        self.game_session: GameSession
        self.HEADING_SIZE = 80


    def __print_heading(self, heading: str):
        print("\n" + "="*self.HEADING_SIZE)
        num_chars_in_heading = 0
        for c in heading:
            num_chars_in_heading += 1

        num_spaces_each_side = round((self.HEADING_SIZE - num_chars_in_heading) / 2) if num_chars_in_heading < self.HEADING_SIZE else 0
        print(" " * num_spaces_each_side + heading)
        print("="*self.HEADING_SIZE + "\n")


    def __create_quiz(self):
        """
        Asks user for title and author of quiz, then creates new quiz object
        """
        title = input("Enter your quiz title: ")
        author = input("Enter the quiz author: ")
        self.quiz = Quiz(title, author)
        
    def __create_text_question(self, question_type, text, answer, scoring):
        """
        Creates a question with the "Text" type

        :param question_type: The type of question
        :param text: The text of the question, i.e. "What is the capital of France?"
        :param answer: Answer to the question
        :param scoring: The IScoringStrategy child class to use, i.e. StandardScore, BonusScore etc...

        :returns: created question
        """
        question = self.factory.create_question(
                q_type=question_type,
                question_text=text,
                correct_answer=answer,
                scoring_strategy=scoring
                )
        return question

    def __create_multiplechoice_question(self, question_type, text, answer, scoring, possible_answers):
        """
        Creates a question with the "MultipleChoice" type

        :param question_type: The type of question
        :param text: The text of the question, i.e. "What is the capital of France?"
        :param answer: Answer to the question
        :param scoring: The IScoringStrategy child class to use, i.e. StandardScore, BonusScore etc...
        :param possible_answers: The possible answers for the multiple choice question

        :returns: created question
        """
        question = self.factory.create_question(
                q_type=question_type,
                question_text=text,
                correct_answer=answer,
                scoring_strategy=scoring,
                possible_answers=possible_answers
                )
        return question

    def __ask_user_for_scoring_strategy(self):
        """
        Asks the user which scoring strategy they want to use for a question

        :returns: The scoring strategy to use
        """
        scoring = IScoringStrategy
        print("Please select a scoring strategy from the following")
        choice = int(input("1. Standard Score (1 point)\n2. Hard Score (5 points)\n3. Penalty Score (2 for correct, -1 for incorrect)\n4. Bonus Score (10 points)\nEnter here: "))
        while choice < 1 or choice > 4:
            print("Please enter a number from 1 to 4.")
            choice = int(input("1. Standard Score (1 point)\n2. Hard Score (5 points)\n3. Penalt Score (2 for correct, -1 for incorrect)\n4. Bonus Score (10 points)\nEnter here: "))
        
        if choice == 1:
            scoring = StandardScore()
        elif choice == 2:
            scoring = HardScore()
        elif choice == 3: 
            scoring = PenaltyScore()
        elif choice == 4:
            scoring = BonusScore()
        else:
            print("Unkown error has occured")
            exit()
        
        return scoring

    def __ask_user_for_possible_answers(self):
        """
        Asks the user for possible answers, for a multiple choice question

        :returns: list of possible answers
        """
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
        """
        asks the user questions about creating rounds, then creates them 

        :returns: The newly created rounds
        """
        rounds = []
        num_rounds = int(input("How many rounds would you like to create?: "))

        for i in range(num_rounds):
            print(f"Round: {i + 1}")
            round_name = input(f"Enter round name {i+1}: ")
            r = Round(round_name)

            num_questions = int(input("How many questions do you want in this round?: "))

            for q in range(num_questions):
                question = None
                print(f"\nQuestion: {q + 1}")
                choice = int(input("1. Create a Text Question\n2. Create Multiplechoice Question\nEnter here: "))
                while choice < 1 or choice > 2:
                    print("Please choose between option '1' and '2'") 
                    choice = int(input("1. Create a Text Question\n2. Create Multiplechoice Question\nEner here: "))
                
                text = input("Enter the question text here: ")
                answer = input("Enter the answer to the question here: ")

                if choice == 1:
                    scoring =  self.__ask_user_for_scoring_strategy()
                    question = self.__create_text_question("Text", text, answer, scoring)
                elif choice == 2:
                    scoring =  self.__ask_user_for_scoring_strategy()
                    possible_answers = self.__ask_user_for_possible_answers()
                    question = self.__create_multiplechoice_question("MultipleChoice", text, answer, scoring, possible_answers)
                    
                else:
                    print("Unknown errror has occured")
                    exit()

                r.add_question(question)

            rounds.append(r)

        return rounds

    def __create_teams(self):
        """
        Asks the user to enter team information

        :returns: List of teams
        """
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
        choice = int(input(f"Enter here ({num_min}-{num_max}): "))
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
        """
        Loads an array of quizzes from a JSON file, iteretes through them,
        and allows the user to select one of them.
        """
        
        filename = input("Enter the filename to load from (press Enter for 'test.json'): ")
        if not filename.strip():
            filename = "test.json"

        try:
            quiz_array = self.fm.load_quizzes_from_file(filename)
        except FileNotFoundError:
            print(f"\n[Error]COuld not find a file name '{filename}'.")
            return None
        except Exception as e:
            print(f"\n[Error] An unexpected error occured while loading: {e}")
            return None

        if isinstance(quiz_array, TypeError):
            print(f"[Error] the JSON file is incorrectly formatted.")
            return None
        
        if not quiz_array or len(quiz_array) == 0:
            print(f"\n[Error] No quizes foundin '{filename}'.")
            return None
        
        self.__print_heading("AVAILABLE QUIZZES")
        for i, q in enumerate(quiz_array):
            print(f"{i + 1}.{q.get_title()} (Author: {q.get_author()}")

        print("="*self.HEADING_SIZE)
        print("\nWhich quiz would you like to load?")

        choice = self.__get_user_choice(1, len(quiz_array))

        self.quiz = quiz_array[choice -1]

        print(f"n>>> Successfully loaded=: '{self.quiz.get_title()}'! <<<")

    def __save_quiz(self):
        """
        Saves the current active quiz to a JSON file.
        Safely appends to the exsiting files or updates the quiz if it already exists
        """

        if not hasattr(self, 'quiz') or self.quiz is None:
            print("\n[Error] No active quiz to save. please create or load a quiz first.")
            return

        filename = input("Enter the filename to save to (press Enterfor'test.json'): ")
        if not filename.strip():
            filename = "test.json"

        existing_quizzes = []
        try:
            loaded_data = self.fm.load_quizzes_from_file(filename)
            if not isinstance(loaded_data, TypeError) and loaded_data is not None:
                existing_quizzes = loaded_data
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"\n[Warning] Could not read exsting file. ({e})")

        quizzes_to_save = []
        for q in existing_quizzes:
            if q.get_title() != self.quiz.get_title():
                quizzes_to_save.append(q)
                
        quizzes_to_save.append(self.quiz)

        try:
            self.fm.save_quizzes_to_file(quizzes_to_save, filename)
            print(f"\n>>> Successfully saved '{self.quiz.get_title()}' to '{filename}'! <<<")
        except Exception as e:
            print(f"\n[Error] An error occurred while saving: {e}")




    def __play_quiz_as_host(self):
        """
        Excecute the main game loop: reading questions, taking team answers,
        and updating the GameSession leaderboard.
        """

        if not hasattr(self, 'quiz') or self.quiz is None:
            print("\n[Error] No quiz loaded. Please create or load a quiz first.")
            return

        print(f"\n>>> Starting Quiz: '{self.quiz.get_title()}' by {self.quiz.get_author()}")
        teams = self.__create_teams()
        if not teams:
            print("\n[Error] You need at least one to team to play!")
            return
        
        self.game_session = GameSession(self.quiz, teams)
        self.game_session.start_session()
        
        # Main loop
        rounds = self.quiz.get_rounds()
        for round_index, r in enumerate(rounds):
            
            self.__print_heading(f"ROUND {round_index + 1}: {r.get_title()}")
            
            questions = r.get_questions()
            if len(questions) > 0 and isinstance(questions[0], list):
                questions = questions[0]

            if not questions:
                print("This roudn has no questions.")
                continue

            print("--- Questions ---")
            for q_num, question in enumerate(questions, start=1):
                print(f"\nQ{q_num}: ", end="")
                question.display()
                input("(Press Enter for the next question...)")
            
            self.__print_heading("SCORING PHASE")
            
            for team in teams:
                print(f"\nGrading answers for Team: {team.get_name()}")
                answers = []

                for q_num, question in enumerate(questions, start=1):
                    correct_ans = question.get_correct_answer()

                    ans = input(f"Did they get Q{q_num} correct? [Answer was: '{correct_ans}'] (y/n): ")

                    if ans.strip().lower() == "y":
                        answers.append(True)
                    else:
                        answers.append(False)

                    self.game_session.calculate_team_score(team, round_index, answers)


            print("\n--- End of Round Leader Board ---")
            self.game_session.display_leaderboard()

            if round_index < len(rounds) - 1:
                input("\nPress Enter to start the next round")

        self.__print_heading("FINAL RESULTS")
        self.game_session.display_leaderboard()
        print(f"\nCongratulations to our winners! Thanks for playing.")           
    
    def __play_quiz_as_player(self):
        """
        Executes the game loop for a single player (Jamie's Persona).
        The system automatically checks the user's typed answers against the correct answers
        and provides instant visual feedback.
        """
        
        if not hasattr(self, 'quiz') or self.quiz is None:
            print("\n[Error] No quiz loaded. Please create or load a quiz first.")
            return

        self.__print_heading(f"SOLO MODE: '{self.quiz.get_title()}' by {self.quiz.get_author()}")
        
        player_name = input("Enter your player name: ")
        if not player_name.strip():
            player_name = "Player 1"
        player = Team(player_name)

        self.game_session = GameSession(self.quiz, [player])
        self.game_session.start_session()
        
        # Main loop
        rounds = self.quiz.get_rounds()
        for round_index, r in enumerate(rounds):
            self.__print_heading(f"ROUND {round_index + 1}: {r.get_title()}")

            questions = r.get_questions()
            if len(questions) > 0 and isinstance(questions[0], list):
                questions = questions[0] 

            if not questions:
                print("This round has no questions.")
                continue

            answers = [] 

            for q_num, question in enumerate(questions, start=1):
                print(f"\nQ{q_num}: ", end="")
                question.display()
            
                user_answer = input("\nYour Answer: ")
                
                correct_answer = str(question.get_correct_answer()).strip().lower()
                user_answer_clean = str(user_answer).strip().lower()
                
                is_correct = (user_answer_clean == correct_answer)
                answers.append(is_correct)

                if is_correct:
                    print("Correct! Great job!")

                else:
                    print(f"Incorrect! The right answer was: '{question.get_correct_answer()}'")

                input("(Press Enter to continue...)")
            
            self.game_session.calculate_team_score(player, round_index, answers)

            print(f"\n--- End of Round {round_index + 1} ---")
            print(f"Your Current Score: {player.get_score()} points")
            
            if round_index < len(rounds) - 1:
                input("\nPress Enter to start the next round...")

        self.__print_heading("FINAL RESULTS")
        print(f"Well played, {player.get_name()}!")
        print(f"Final Score: {player.get_score()} points")


    def __main_menu(self):
        self.__print_heading("Quiz System 1.0")
        print("1. New Quiz")
        print("2. Load Quiz")
        print("3. Save Quiz")
        print("4. Play Quiz (Host Mode - Multiple Teams)")
        print("5. Play Quiz (Solo Mode - Interactive)")
        print("6. Exit Program")
        
        choice = self.__get_user_choice(1, 6) 
        
        if choice == 1:
            self.__initialise_quiz()
        elif choice == 2:
            self.__load_quiz()
        elif choice == 3:
            self.__save_quiz()
        elif choice == 4:
            self.__play_quiz_as_host()  
        elif choice == 5:
            self.__play_quiz_as_player() 
        elif choice == 6:
            print("Thanks for using the program!!!")
            exit()
        else: 
            print("Unknown Error has Occurred")

    def run_quiz(self):
        """
        Public entry point for the Quiz Management System.
        Keeps the application running in a continuous loop until the user exits.
        """
        self.__print_heading("Welcome to the Quiz Management System")

        while True:
            try:
                self.__main_menu()
            except KeyboardInterrupt:
                print("\n\nExiting program.")
                exit()
            except Exception as e:
                print(f"\n[Fatal Error] An unexpected error occurred: {e}")
                print("Returning to the main menu\n")
