# TODO Напишите функцию find_common_participants
def find_common_participants(group1_str, group2_str, delimiter=','):
    group1 = set(group1_str.split(delimiter))
    group2 = set(group2_str.split(delimiter))
    common = list(group1.intersection(group2))
    return sorted(common)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(common_participants)
