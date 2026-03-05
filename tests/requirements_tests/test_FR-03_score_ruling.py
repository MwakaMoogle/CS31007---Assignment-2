import pytest
from quiz_system import StandardScore, HardScore, PenaltyScore 

class TestingScoringStratagey:
    
    #Test for allowing different scoring rules for different question types

    def test_standard_correct_1(self):
        strategy = StandardScore()
        assert strategy.executeScoring(
            isCorrect= True, difficulty = "Standard") ==1

    def test_standard_incorrect_0(self):
        strategy = StandardScore()
        assert strategy.executeScoring(
            isCorrect = False, difficulty = "Standard") ==0

    def test_hard_correct_5(self):
        strategy = HardScore()
        assert strategy.executeScoring(
            isCorrect = True, difficulty = "Hard") ==5

    def test_hard_incorrect_0(self):
        strategy = HardScore()
        assert strategy.executeScoring(
            isCOrrect = False, difficulty = "Hard") ==0
    
    def test_penalty_incorrect_negative_one(self):
        strategy = PenaltyScore()
        assert strategy.executeScoring(
            isCorrect = False, difficulty = "penalty") == -1

     # Im stuck : I will figure out later
    def test_invalid_type_raise_error(self):()