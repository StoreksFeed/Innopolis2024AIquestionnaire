
import os
from typing import TextIO, Generator, Callable

import re

import matplotlib.pyplot as plt
import numpy as np

def get_file_descriptor(filename: str) -> TextIO:
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, filename)
    return open(file_path, 'r', encoding='utf-8')

def normalize_answers(answers: list, regex: str, l: Callable) -> Generator:
    r = re.compile(regex, flags=re.IGNORECASE)
    for answer in answers:
        match = r.match(answer)
        if match is not None:
            yield l(match[0])
        else:
            yield None

def bar_plot(data, emotions, standart = []) -> plt.Figure:
    colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c',
              '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#dea17f', '#b15928']

    plot_data = {emotion: [data[scenario][emotion] for scenario in data.keys()] for emotion in emotions}

    barWidth = 1 / (len(emotions) + 1)

    fig = plt.figure(figsize=(10, 5))
    ax = plt.subplot(111)

    br = np.arange(max(len(i) for i in plot_data.values()))
    for i, emotion in enumerate(emotions):
        plt.bar([x + barWidth * i for x in br], plot_data[emotion], width=barWidth, label=emotion, color=colors[i])

    for i, value in enumerate(standart):
        plt.axhline(y=value, color='black', linestyle='--', label='Норма' if i == 0 else '')

    if 'default' in data:
        plt.axhline(y=sum(data['default'].values()) / len(data['default'].values()), color='black', linestyle='-', label='Среднее по default')

    plt.xlabel('Группы')
    plt.ylabel('Оценка')
    plt.xticks([r + (len(emotions) - 1) * barWidth / 2 for r in range(len(data))], data.keys())

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    return fig
