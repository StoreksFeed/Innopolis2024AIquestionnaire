from Innopolis2024AIquestionnaire import SANQuestionnaire, MoodQuestionnaire, DESQuestionnaire, ETQuestionnaire
from Innopolis2024AIquestionnaire import YaGPT
import json
import os

def load_prompts(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def cycle_questionnaires(agent: YaGPT, prompts_path: str, output_path: str, questionnaires: list, n: int):
    emotional_prompts = load_prompts(prompts_path)
    os.makedirs(f'{output_path}/{agent.model}_answers/', exist_ok=True)

    for i in range(n):
        for emotion, emotion_dict in emotional_prompts.items():
            for defininition, defininition_prompt in emotion_dict.items():
                for questionnaire in questionnaires:
                    current = f'{i}_{emotion}_{defininition[0]}_{questionnaire.__class__.__name__}'
                    answers = agent.pass_questionnaire(
                        defininition_prompt, questionnaire)
                    with open(f'{output_path}/{agent.model}_answers/{current}.json', 'w', encoding='utf-8') as f:
                        json.dump(answers, f, ensure_ascii=False)


def construct_plots(agent: YaGPT, prompts_path: str, output_path: str, questionnaires: list, n: int):
    emotional_prompts = load_prompts(prompts_path)
    os.makedirs(f'{output_path}/{agent.model}_plots/', exist_ok=True)

    for emotion, emotion_dict in emotional_prompts.items():
        for questionnaire in questionnaires:
            questionnaire_name = f"{questionnaire.__class__.__name__}"
            for defininition in emotion_dict.keys():
                for i in range(n):
                    current = f'{i}_{emotion}_{defininition[0]}_{questionnaire_name}'
                    with open(f'./{output_path}/{agent.model}_answers/{current}.json', 'r', encoding='utf-8') as f:
                        answers_current = json.load(f)
                    questionnaire.score(
                        answers_current, defininition, first=True if i == 0 else False, factor=3)

            plot_fig = questionnaire.plot(f"{emotion}, {questionnaire_name} ({agent.model})")
            if emotion != 'default':
                plot_fig.savefig(
                    f'{output_path}/{agent.model}_plots/{emotion}_{questionnaire_name}.png')


if __name__ == "__main__":
    API_FOLDER = os.environ['YC_FOLDER_ID']
    API_KEY = os.environ['YC_API_KEY']
    EMOTIONAL_PROMPTS_PATH = 'emotional_prompts.json'
    RESULTS_PATH = './demo_results'

    agent_lite = YaGPT(API_FOLDER, API_KEY, model='yandexgpt-lite')
    agent_pro = YaGPT(API_FOLDER, API_KEY, model='yandexgpt')

    questionnaires = [
        SANQuestionnaire(),
        MoodQuestionnaire(),
        DESQuestionnaire(),
        ETQuestionnaire()
    ]

    for agent in [agent_lite, agent_pro]:
        cycle_questionnaires(agent, EMOTIONAL_PROMPTS_PATH, RESULTS_PATH, questionnaires, 3)
        construct_plots(agent, EMOTIONAL_PROMPTS_PATH, RESULTS_PATH, questionnaires, 3)
