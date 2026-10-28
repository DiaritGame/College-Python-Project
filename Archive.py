# # with open("data/test", "r", encoding="utf-8") as file:
# #     print(file.readline())
# #     print(file.readline())
# #     print(file.readline())
# #
# # with open("data/test", "r", encoding="utf-8") as file:
# #     lines = file.readlines()
# #
# # print(lines)
# #
# # #data/test
#
# # with open("data/test", "r", encoding="utf-8") as file:
# #     for line in file:
# #         print(line.strip())
#
# # with open("data/test", "w", encoding="utf-8") as file:
# #     file.write("Первая строка\n")
# #     file.write("Вторая строка\n")
#
# # lines = ["Привет\n", "Как дела?\n", "Пока\n"]
# #
# # with open("data/test", "w", encoding="utf-8") as file:
# #     file.writelines(lines)
#
#
# path = "data/logs.txt"
# count = 0
#
# with open(path, "r", encoding="utf-8") as file:
#     for string in file:
#         if 'Error' in string:
#             print(string, end="")
#             count += 1
#
# print(count)

# path = "data/score"
# # summ = 0
# # counts = 0
# # lst = []
# # with open(path, "r", encoding="utf-8") as file:
# #     for string in file:
# #         string = string.strip()
# #         if string == "":
# #             continue
# #         lst = string.split(";")
# #         if lst[1].isdigit():
# #             counts += 1
# #             summ += int(lst[1])
# #         if lst[1] == "5":
# #             print(lst[0])
# # if counts > 0:
# #     print(f"Средняя оценка: {summ / counts}")

