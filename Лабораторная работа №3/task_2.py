# TODO Напишите функцию find_common_participants

def find_common_participants(first, second, separator=','):

    first_group = first.split(separator)
    second_group = second.split(separator)

    union1 = set(first_group)

    repetitive = union1.intersection(second_group)

    return sorted(list(repetitive))




participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

find_common_participants(participants_first_group, participants_second_group, '|')