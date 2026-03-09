from abc import ABC, abstractmethod

class IScoringStrategy(ABC):

    @abstactmethod
    def executeScoring(isCorrect, difficulty):
        """
        Define how points are awarderd
        """
        pass

class StandardScore(IscoringStrategy):
    
    def executeScoring(isCorrect, difficulty):
        if iscorrect:
            return 1
        else: 
            return 0
    
class HardScore(IScoringStrategy):

    def executeScoring(isCorrect, difficulty):
        if isCorrect:
            return 5
        else:
            return 0

class PenaltyScore(IScoringStrategy):
    
    def executeScoring(isCorrect, difficulty):
        if isCorrect:
            return -1
        else:
            return 0

class BonusScore(IScoringStrategy):
    pass



