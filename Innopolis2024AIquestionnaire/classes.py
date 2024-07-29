import random
from typing import TextIO, Iterable, Callable
from json import load
from .utils import bar_plot, normalize_answers

class BaseTest():
    def __init__(self, seed: int = 0, file: TextIO = None, l: Callable = lambda a: a) -> None:
        with file as f:
            json_data = load(f)
            self.data = json_data['data']
            self.emotions = json_data['emotions']
            self.intro = json_data['intro']
            self.standart = json_data['standart']
            self.regex = json_data['regex'] if 'regex' in json_data else '.' 
        self.seed = seed
        self.l = l
        self.results = {}

    def sample(self) -> list:
        random.seed(self.seed)
        return random.sample(self.data, k=len(self.data))
    
    def sequence(self) -> Iterable:
        raise NotImplementedError
    
    def score(self, answers: list, note: str = 'default'):
        data = self.sample()
        total = {emotion: 0 for emotion in self.emotions}
        return self._score_cycle(total,
                                 list(normalize_answers(answers, regex=self.regex, l=self.l)),
                                 data, note)
    
    def _score_cycle(self, *args):
        raise NotImplementedError
    
    def plot(self):
        return bar_plot(self.results, self.emotions, self.standart)


class TextTest(BaseTest):
    def sequence(self) -> Iterable:
        return (i['question'] for i in self.sample())      
    

class ImageTest(BaseTest):
    def sequence(self) -> Iterable:
        return ( (i['image'], i['question']) for i in self.sample())
