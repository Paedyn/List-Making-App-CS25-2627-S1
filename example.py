number_to_add = input("How many?")
number_to_add = int(number_to_add)

my_list = []

for _ in range(number_to_add):
    item = input("What to add to list?")
    my_list.append(item)

print(my_list)