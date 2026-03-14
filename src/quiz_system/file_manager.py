import json
from .quiz import Quiz
from .round import Round
from .question_factory import *

class FileManager:
    def __init__(self):
        pass
    
    def load_quizzes_from_file(self, filename):
        """
        Loads quiz from json file.
        File must be in the following format:

        {
            "quizzes": [
            {
                "quiz_title": "Quiz 1",
                "quiz_author"; "John Pork"
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
        """
        data = None
        with open(filename, "r") as file:
            data = json.load(file)
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
                    
                    if "possible_answers" in q:
                        round_questions.append(factory.create_question(
                            q_type = q["question_type"],
                            question_text = q["question_text"],
                            correct_answer = q["correct_answer"],
                            scoring_strategy = q["scoring_strategy"],
                            possible_answers = q["possible_answers"]
                            ))
                    else:
                        round_questions.append(factory.create_question(
                            q_type = q["question_type"],
                            question_text = q["question_text"],
                            correct_answer = q["correct_answer"],
                            scoring_strategy = q["scoring_strategy"]
                            ))
                    
                quiz_rounds[j].add_question(round_questions)

            quizzes_quiz[i].add_rounds(quiz_rounds)

        return quizzes_quiz
    
    def save_quizzes_to_file(self, quizzes, filename):
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
        with open(filename, "w") as file:
            file.write(json.dumps(json_data))
