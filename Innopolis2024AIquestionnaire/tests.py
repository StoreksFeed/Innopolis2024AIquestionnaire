from .classes import TextTest
from .utils import get_file_descriptor
from typing import TextIO

class SANQuestionnaire(TextTest):
    def __init__(self, seed: int = 0, file: TextIO = get_file_descriptor('data/SAN.json')) -> None:
        super().__init__(seed, file, lambda a: int(a))

    def _score_cycle(self, answers: list, factor: int, data: list, note: str) -> None:
        for answer, question in zip(answers, data):
            if answer is not None:
                self.total[question['key']["*"]['emotion']] += (((answer - 4) * question['key']["*"]['weight']) + 4) / (10 * factor)
        self.results[note] = self.total

class MoodQuestionnaire(TextTest):
    def __init__(self, seed: int = 0, file: TextIO = get_file_descriptor('data/MQ.json')) -> None:
        super().__init__(seed, file, lambda a: str(a).lower())
        
    def _score_cycle(self, answers: list, factor: int, data: list, note: str) -> None:
        for answer, question in zip(answers, data):
            if answer in question['key'].keys():
                self.total[question['key'][answer]['emotion']] += 1 / factor
        self.results[note] = self.total

class DESQuestionnaire(TextTest):
    def __init__(self, seed: int = 0, file: TextIO = get_file_descriptor('data/DES.json')) -> None:
        super().__init__(seed, file, lambda a: int(a))
    
    def _score_cycle(self, answers: list, factor: int, data: list, note: str) -> None:
        for answer, question in zip(answers, data):
            if answer is not None:
                self.total[question['key']["*"]['emotion']] += answer / factor
        self.results[note] = self.total

class ETQuestionnaire(TextTest):
    def __init__(self, seed: int = 0, file: TextIO = get_file_descriptor('data/ET.json')) -> None:
        super().__init__(seed, file, lambda a: int(a))
    
    def _score_cycle(self, answers: list, factor: int, data: list, note: str) -> None:
        for answer, question in zip(answers, data):
            if answer is not None:
                self.total[question['key']["*"]['emotion']] += answer / factor
        self.results[note] = self.total
