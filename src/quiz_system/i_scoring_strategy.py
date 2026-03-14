from abc import ABC, abstractmethod

class IScoringStrategy(ABC):
    """
    Scoring Strategy Interface
    """
    @abstractmethod
    def execute_scoring(self, is_correct: bool) -> int:   
        """
        Define how points are awarded
        """
        # Check if is_correct is a boolean
        if not isinstance(is_correct, bool):
            raise TypeError("is_correct must be a boolean value")
        
        pass

    @abstractmethod
    def get_str(self):
        pass

class StandardScore(IScoringStrategy):
    """
    Child Class of IScoringStrategy, defining functions related to standard scoring
    """
    def execute_scoring(self, is_correct: bool) -> int:
        """
        Define how points are awarded for standard scoring

        :param is_correct: whether to get the points for a correct or incorrect answer

        :returns: the points for if the answer is correct or not
        """
        super().execute_scoring(is_correct)
        if is_correct:
            return 1
        else: 
            return 0
        
    def get_str(self):
        return "StandardScore"
    
class HardScore(IScoringStrategy):
    """
    Child Class of IScoringStrategy, defining functions related to hard scoring
    """
    def execute_scoring(self, is_correct: bool) -> int:
        """
        Define how points are awarded for hard scoring

        :param is_correct: whether to get the points for a correct or incorrect answer

        :returns: the points for if the answer is correct or not
        """
        super().execute_scoring(is_correct)
        if is_correct:
            return 5
        else:
            return 0
        
    def get_str(self):
        return "HardScore"

class PenaltyScore(IScoringStrategy):
    """
    Child Class of IScoringStrategy, defining functions related to penalty scoring
    """
    def execute_scoring(self, is_correct: bool) -> int:
        """
        Define how points are awarded for penalty scoring

        :param is_correct: whether to get the points for a correct or incorrect answer

        :returns: the points for if the answer is correct or not
        """
        super().execute_scoring(is_correct)
        if is_correct:
            return 2
        else:
            return -1
        
    def get_str(self):
        return "PenaltyScore"

class BonusScore(IScoringStrategy):
    """
    Child Class of IScoringStrategy, defining functions related to bonus scoring
    """
    def execute_scoring(self, is_correct: bool) -> int:
        """
        Define how points are awarded for bonus scoring

        :param is_correct: whether to get the points for a correct or incorrect answer

        :returns: the points for if the answer is correct or not
        """
        super().execute_scoring(is_correct)
        if is_correct:
            return 10
        else:
            return 0
        
    def get_str(self):
        return "BonusScore"


