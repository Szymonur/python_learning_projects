numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     new_list.append(n+1)
#     print(new_list) #  [2, 3, 4]

# new_list = [new_item for item in list]

new_list = [number + 1 for number in numbers]  # [2, 3, 4]

name = "Szymon"
name_list = [letter for letter in name]
print(name_list)

range_list = [i*2 for i in range(1, 5)]
print(range_list)

names = ["Jan", "Ola", "Alan", "xyz"]
names_list = [name.upper() for name in names if name != "xyz" and len(name) < 4]
print(names_list)


