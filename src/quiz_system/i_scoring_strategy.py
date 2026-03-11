from abc import ABC, abstractmethod

class IScoringStrategy(ABC):

    @abstractmethod
    def execute_scoring(self, isCorrect: bool) -> int:   
        # Check if isCorrect is a boolean
        if not isinstance(isCorrect, bool):
            raise TypeError("isCorrect must be a boolean value")
        """
        Define how points are awarded
        """
        pass

class StandardScore(IScoringStrategy):
    
    def execute_scoring(self, isCorrect: bool) -> int:
        super().execute_scoring(isCorrect)
        if isCorrect:
            return 1
        else: 
            return 0
    
class HardScore(IScoringStrategy):

    def execute_scoring(self, isCorrect: bool) -> int:
        super().execute_scoring(isCorrect)
        if isCorrect:
            return 5
        else:
            return 0

class PenaltyScore(IScoringStrategy):

    
    def execute_scoring(self, isCorrect: bool) -> int:
        super().execute_scoring(isCorrect)
        if isCorrect:
            return 2
        else:
            return -1

class BonusScore(IScoringStrategy):
    
    def execute_scoring(self, isCorrect: bool) -> int:
        super().execute_scoring(isCorrect)
        if isCorrect:
            return 10
        else:
            return 0


