print("Welcome to your list!")
print("Here are some directions to help you out")
print("press A to add items to list")
print("press B to insert items to list")
print("press C to remove items from list")
print("press D to search list")
print("E to see all your items on your lsit")
print("press F to change existing items on your list ")
print("press G to undo your last change")

list=[]
start=(input("Please enter a letter to start!"))

#ADD TO LIST
if start=="A":
    stuff = (int(input("How many items would you like?")))
for _ in range(stuff):
    task=(input("List your items here!"))
    list.append(task)
    print(list)

elif start=="B":
        undo_list = list.copy()
        print("To remove values, you must address them by index.")
        print("Your first value is 1, your second value is 2, and so on.")

        remove = int(input("Which position would you like to remove? ")) - 1

        if remove < 0 or remove >= len(list):
            print("Invalid index!")
        else:
            removed_item = list.pop(remove)
            print(f"Removed {removed_item}.")
            print(list)





# elif start=="B":
#     print("To remove values, you must address them by index. Your first value is 0, your second values is 1, and so on.")
#     remove=(input("What would you like to remove"))
# if remove < 0 or remove >= len(list):
#     print("Invalid index!")
#     else:
#     removed = items.pop(remove)
#     print(f"Removed {remove}.")
