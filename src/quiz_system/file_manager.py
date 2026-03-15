import json
from .quiz import Quiz
from .round import Round
from .question_factory import *
from .i_scoring_strategy import StandardScore, HardScore, PenaltyScore, BonusScore

class FileManager:
    """
    Class to manage saving/loading quizzes to/from a file
    """

    def __init__(self):
        """
        Empty Constructor for FileManager
        """
        pass

    def __open_file(self, filename, mode):
        """
        Helper function to open a file

        :param filename: location of file being opened
        :param mode: mode in which file is being opened (e.g. "r" for read, "w" for write)

        :returns: file object
        """
        try:
            file = open(filename, mode)
            return file
        except Exception as e:
            print(f"Error opening file: {e}")
            return None
        


    def __close_file(self, file):
        """
        Helper function to close a file

        :param file: file object being closed
        """
        try:
            file.close()
        except Exception as e:
            print(f"Error closing file: {e}")
    
    def __read_file(self, file):
        """
        Helper function to read a file

        :param file: file object being read from

        :returns: data read from file
        """
        try:
            data = file.read()
            return data
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    def __write_file_json(self, file, data): 
        """
        Helper function to write json data to a file

        :param file: file object being written to
        :param data: data being written to file
        """
        try:
            json_data = json.dumps(data)
            file.write(json_data)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def load_quizzes_from_file(self, filename):
        """
        Loads quiz from json file.
        File must be in the following format:

        {
            "quizzes": [
            {
                "quiz_title": "Quiz 1",
                "quiz_author": "John Pork",
                "rounds": [
                    {
                        "round_title": "Geography",
                        "questions": [
                            {
                                "question_type": "Text",
                                "question_text": "What is the capital of France",
                                "correct_answer": "Paris",
                                "scoring_strategy": "StandardScore"
                            },
                            {
                                "question_type": "MultipleChoice",
                                "question_text": "What is the capital of Japan",
                                "correct_answer": "Tokyo"
                                "possible_answers": [
                                    "Kyoto",
                                    "Lijang",
                                    "Tokyo",
                                    "Hanamura"
                                ],
                                "scoring_strategy": "BonusScore"
                            },
                        ]
                    },
                    {
                        "round_title": "Maths",
                        "questions": [
                            {
                                "question_type": "Text",
                                "question_text": "What is the 2+2",
                                "correct_answer": "4",
                                "scoring_strategy": "PenaltyScore"
                            },
                            {
                                "question_type": "MultipleChoice",
                                "question_text": "What is the 3-1",
                                "correct_answer": "2"
                                "possible_answers": [
                                    "2",
                                    "4",
                                    "3",
                                    "1"
                                ],
                                "scoring_strategy": "StandardScore"
                            },
                        ]
                    }
                ]
            },
            ]
        }

        :param filename: the location of the file being read from

        :returns: List of loaded quizzes
        """
        file = self.__open_file(filename, "r")
        if file is None:
            return []

        data = None
        try:
            data_str = self.__read_file(file)
        finally:
            self.__close_file(file)

        if data_str is None:
            return []

        data = json.loads(data_str)
        if "quizzes" not in data:
            return TypeError("Incorrect JSON format")
        
        quizzes_dict_list = data["quizzes"]

        quizzes_quiz = []
        for i, quiz_dict in enumerate(quizzes_dict_list):
            quizzes_quiz.append(Quiz(quiz_dict["quiz_title"], quiz_dict["quiz_author"]))

            quiz_rounds = []
            for j,  r in enumerate(quiz_dict["rounds"]):
                quiz_rounds.append(Round(r["round_title"]))

                round_questions = []
                for k, q in enumerate(r["questions"]):
                    factory = QuestionFactory()
                    strategy_str = q.get("scoring_strategy", "StandardScore")
                    
                    if strategy_str == "HardScore":
                        scoring_obj = HardScore()
                    elif strategy_str == "PenaltyScore":
                        scoring_obj = PenaltyScore()
                    elif strategy_str == "BonusScore":
                        scoring_obj = BonusScore()
                    else:
                        scoring_obj = StandardScore()
                    
                    if "possible_answers" in q:
                        round_questions.append(factory.create_question(
                            q_type = q["question_type"],
                            question_text = q["question_text"],
                            correct_answer = q["correct_answer"],
                            scoring_strategy = scoring_obj, 
                            possible_answers = q["possible_answers"]
                            ))
                    else:
                        round_questions.append(factory.create_question(
                            q_type = q["question_type"],
                            question_text = q["question_text"],
                            correct_answer = q["correct_answer"],
                            scoring_strategy = scoring_obj
                            ))
                    
                for question_obj in round_questions:
                    quiz_rounds[j].add_question(question_obj)

            quizzes_quiz[i].add_rounds(quiz_rounds)

        return quizzes_quiz
    
    def save_quizzes_to_file(self, quizzes, filename):
        """
        saves list of quizzes to file

        :param quizzes: list of quizzes to be saved
        :param filename: location of file being written to
        """
        json_data = {
            "quizzes": []
        }
        for quiz in quizzes:
            rounds = []
            for r in quiz.get_rounds():
                questions = []
                for _, question in enumerate(r.get_questions()):
                    if hasattr(question, "get_possible_answers"):
                        questions.append(
                            {
                                "question_type": question.get_type(),
                                "question_text": question.get_question_text(),
                                "correct_answer": question.get_correct_answer(),
                                "possible_answers" : question.get_possible_answers(),
                                "scoring_strategy": question.get_scoring_strategy_str()
                            }
                        )
                    else:
                        questions.append(
                            {
                                "question_type": question.get_type(),
                                "question_text": question.get_question_text(),
                                "correct_answer": question.get_correct_answer(),
                                "scoring_strategy": question.get_scoring_strategy_str()
                            }
                        )
                rounds.append(
                    {
                        "round_title": r.get_title(),
                        "questions": questions
                    }
                )
            json_data["quizzes"].append(
                {
                    "quiz_title": quiz.get_title(),
                    "quiz_author": quiz.get_author(),
                    "rounds": rounds
                }
            )
        file = self.__open_file(filename, "w")
        if file is None:
            return

        try:
            self.__write_file_json(file, json_data)
        finally:
            self.__close_file(file)
