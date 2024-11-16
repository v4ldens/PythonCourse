# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    ...  # TODO считать содержимое csv файла

    with open(INPUT_FILENAME) as input_f:

        reader = csv.reader(input_f)

        dict1 = dict()
        dict2 = dict()
        dict3 = dict()
        dict4 = dict()

        s = list()

        for row in reader:

            s.append(row)

        for i in range(len(s[0])):

            dict1[s[0][i]] = s[1][i]
            dict2[s[0][i]] = s[2][i]
            dict3[s[0][i]] = s[3][i]
            dict4[s[0][i]] = s[4][i]

        l = list()

        l.append(dict1)
        l.append(dict2)
        l.append(dict3)
        l.append(dict4)

        with open(OUTPUT_FILENAME, 'w') as f:

            json.dump(l, f, indent = 4)



    ...  # TODO Сериализовать в файл с отступами равными 4




if __name__ == '__main__':

    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, 'r') as output_f:
        for line in output_f:
            print(line, end="")
