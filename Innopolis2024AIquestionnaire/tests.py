from .classes import TextTest
from .utils import get_file_descriptor
from typing import TextIO

class SANQuestionnaire(TextTest):
    def __init__(self, seed: int = 0, file: TextIO = get_file_descriptor('data/SAN.json')) -> None:
        super().__init__(seed, file, lambda a: int(a))

    def _score_cycle(self, total: dict, answers: list, data: list, note: str) -> None:
        for answer, question in zip(answers, data):
            if answer is not None:
                total[question['key']["*"]['emotion']] += (((answer - 4) * question['key']["*"]['weight']) + 4) / 10
        self.results[note] = total
