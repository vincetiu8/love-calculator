def love_calc(names, search_letters):
    present_letters: list[int] = [0 for _ in range(len(search_letters))]
    for i in (names):
        for index, j in enumerate(search_letters):
            if i == j:
                present_letters[index] += 1

    repeats: int = 0
    while len(present_letters) > 2:
        temp_list = []
        for i in range(len(present_letters) - 1):
            temp_string = str(present_letters[i] + present_letters[i + 1])
            for char in temp_string:
                temp_list.append(int(char))
        present_letters = temp_list
        repeats += 1
        if repeats > 20:
            return 0

    return present_letters[0] * 10 + present_letters[1]


# def everything():
#     scores = {}
#     partners = {}
#     high_names_score = 0
#     lines = []
#
#     for name1 in names:
#         high_score = 0
#         high_names = []
#         for name2 in names:
#             score = love_calc(name1, name2, "LOVES".lower())
#             lines.append(name1 + " " + name2 + " " + str(score) + "\n")
#             scores_data[score] += 1
#             if score > high_score:
#                 high_names = [name2]
#                 high_score = score
#             elif score == high_score:
#                 high_names.append(name2)
#         if name1 in high_names:
#             lines.append(name1 + " you are destined to be alone...")
#         else:
#             lines.append(name1 + " most compatible name(s) (" + str(high_score) + "%): " + " ".join(high_names) + "\n")
#         scores[name1] = high_score
#         partners[name1] = high_names
#         high_names_score = max(high_names_score, high_score)
#
#     for score in range(99, 0, -1):
#         people = []
#         for person in scores:
#             if scores[person] == score:
#                 people.append(person + " " + " ".join(partners[person]))
#         if len(people) != 0:
#             lines.append(str(score) + "%" + "\n")
#             for x in people:
#                 lines.append(x + "\n")
#
#     with open(output_file_path, "w+") as output_file:
#         output_file.writelines(lines)
