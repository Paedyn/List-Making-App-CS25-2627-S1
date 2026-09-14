

    # ask=(int(input("How many things would you like it the list?")))
list = []
print("Hi! You can make a list here! Any type of list, I guess...")#TBD
stuff=(int(input("How many tasks would you like?")))

for i in range(stuff):
    task=(input("List your tasks here!"))
list.append(task)
print(list)