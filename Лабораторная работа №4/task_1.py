# TODO решите задачу

import json

def task() -> float:

    f = open('input.json', 'r')
    data = json.load(f)

    answer = 0

    for i in range(len(data)):

        answer += float(data[i]["score"]) * float(data[i]["weight"])

    return float("%.3f" % answer)

print(task())
