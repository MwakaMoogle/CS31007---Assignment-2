from abc import ABC, abstractmethod

class IScoringStrategy(ABC):

    @abstractmethod
    def executeScoring(self, isCorrect: bool) -> int:
        """
        Define how points are awarded
        """
        pass

class StandardScore(IScoringStrategy):
    
    def executeScoring(self, isCorrect: bool) -> int:
        if isCorrect:
            return 1
        else: 
            return 0
    
class HardScore(IScoringStrategy):

    def executeScoring(self, isCorrect: bool) -> int:
        if isCorrect:
            return 5
        else:
            return 0

class PenaltyScore(IScoringStrategy):

    
    def executeScoring(self, isCorrect: bool) -> int:
        if isCorrect:
            return 2
        else:
            return -1

class BonusScore(IScoringStrategy):
    
    def executeScoring(self, isCorrect: bool) -> int:
        if isCorrect:
            return 10
        else:
            return 0



