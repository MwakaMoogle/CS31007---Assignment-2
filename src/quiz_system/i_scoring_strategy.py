from abc import ABC, abstractmethod

class IScoringStrategy(ABC):

    @abstractmethod
    def executeScoring(self, isCorrect) -> int:
        """
        Define how points are awarded
        """
        pass

class StandardScore(IScoringStrategy):
    
    def __init__(self):
        pass


    def executeScoring(self, isCorrect):
        if isCorrect:
            return 1
        else: 
            return 0
    
class HardScore(IScoringStrategy):

    def __init__(self):
        pass

    def executeScoring(self, isCorrect):
        if isCorrect:
            return 5
        else:
            return 0

class PenaltyScore(IScoringStrategy):

    def __init__(self):
        pass
    
    def executeScoring(self, isCorrect):
        if isCorrect:
            return -1
        else:
            return 0

class BonusScore(IScoringStrategy):
    pass



