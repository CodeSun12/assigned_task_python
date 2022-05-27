import os
import glob
# dir_name = 'TextFiles'
#
# try:
#     os.mkdir(dir_name)
#     print("Directory ", dir_name,  " Created ")
# except FileExistsError:
#     print("Directory ", dir_name, " already exists")

user_choice_names = input("Please Tell Us the Names of File \n")
#
for i in range(0, 10):
    with open(f"{user_choice_names} {i}.ini", "w") as file:
        content = file.write(f"{i}")


def change():
    for s in range(0, 10):
        os.rename(f"{user_choice_names}" + " " + f"{s}", f"{s}")


change_name = input('Do you want to change the files name, Type "yes" for changing, Type "no" for no changing ')

if change_name == "yes":
    change()
    for code in range(0, 10):
        first = open(f"{code}.ini", "r")
        my_result = first.read()
        result_file = open("resultFile.txt", "a")
        result_file.write(my_result + "\n")
else:
    print("No Changing")
    for code in range(0, 10):
        path = os.path.abspath(f"{user_choice_names} {code}.ini")
        first = open(f"{path}", "r")
        my_result = first.read()
        result_file = open("resultFile.txt", "a")
        result_file.write(my_result + "\n")

# os.remove("shaki 0")
# os.remove("shaki 1")
# os.remove("shaki 2")
# os.remove("shaki 3")


path = glob.glob('/home/shakeeb/PycharmProjects/assigned_task_python/*.ini')
for file in path:
    os.remove(file)


# first = open("shaki 0", "r")
# one = str(first.read())
# result_file = open("resultFile.txt", "a")
# result_file.write(one + "\n")
# second = open("shaki 1", "r")
# two = str(second.read())
# result_file.write(two)




# my_list = []
# for code in range(0, 3):
#     first = open(f"{user_choice_names} {code}", "r")
#     my_list.append(int(first.read()))
# print(my_list)
#
# result_file = open("resultFile.txt", "w")
# result_file.write(str(my_list))
