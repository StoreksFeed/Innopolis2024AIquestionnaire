import requests
import time
from .classes import BaseAgent

class YaGPT(BaseAgent):
    def __init__(self, yandex_folder: str, yandex_api_key: str, temp: int = 0.5, model: str = 'yandexgpt-lite'):
        self.folder = yandex_folder
        self.api_key = yandex_api_key
        self.temp = temp
        self.model = model

    def get_prompt(self, system: str, user: str) -> dict:
        messages = []
        if system:
            messages.append({
                "role": "system",
                "text": system
            })

        messages.append({
            "role": "user",
            "text": user
        })

        prompt = {
            "modelUri": f"gpt://{self.folder}/{self.model}",
            "completionOptions": {
                "stream": False,
                "temperature": self.temp,
                "maxTokens": "2000"
            },
            "messages": messages
        }
        return prompt

    def pass_questionnaire(self, emotional_prompt: str, questionnaire):
        answers = []
        for question in questionnaire.sequence():
            url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Api-Key {self.api_key}"
            }

            response = requests.post(url, headers=headers,
                                     json=self.get_prompt(emotional_prompt, questionnaire.intro + question))
            result = response.json()
            answers.append(result['result']['alternatives']
                           [0]['message']['text'])
            time.sleep(1)
        return answers
