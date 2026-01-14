# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, separator=","):

    group1 = participants_first_group.split(separator)
    group2 = participants_second_group.split(separator)

    common = set(group1) & set(group2)

    return sorted(list(common))

participants_first_group = "Иванов Петр,Сидоров Борис"
participants_second_group = "Петров,Сидоров Борис,Смирнов"

common_participants = find_common_participants(
    participants_first_group,
    participants_second_group
)

print("Общие участники:", common_participants)

participants_first_group = "Иванов Петр|Сидоров Борис"
participants_second_group = "Петров|Сидоров Борис|Смирнов"

common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)
print("Общие участники (разделитель |):", common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой
