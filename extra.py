print("Here are some directions to help you out")
print("press A to add items to list")
print("press B to insert items to list")
print("press C to remove items from list")
print("press D to search list")
print("E to see all your items on your lsit")
print("press F to change existing items on your list ")
print("press G to undo your last change")

list = []
undo_list=[]


while True:
    start = input("Please enter a letter to start! ")

    # ADD TO LIST-A
    if start == "A":
        undo_list=list.copy()
        stuff = int(input("How many items would you like? "))
        for _ in range(stuff):
            task = input("List your items here! ")
            list.append(task)
            print(list)

    # INSERT ITEM-B
    elif start == "B":
        undo_list = list.copy()

        print("To insert values, you must address them by index.")
        print("Your first value is 0, your second value is 1, and so on.")

        add = int(input("Which position would you like to insert at? "))
        new_item = input("What item would you like to insert? ")

        if add < 0 or add > len(list):
            print("Invalid index!")
        else:
            list.insert(add, new_item)
            print("Item inserted!")
            print(list)

    # REMOVE ITEMS-C
    elif start == "C":
        undo_list = list.copy()

        print("To remove values, you must address them by index.")
        print("Your first value is 0, your second value is 1, and so on.")

        remove = int(input("Which position would you like to remove? "))

        if remove < 0 or remove >= len(list):
            print("Invalid index!")
        else:
            removed_item = list.pop(remove)
            print(f"Removed {removed_item}.")
            print(list)
 #SEARCH=D
    elif start=="D":
        print("To insert values, you must address them by index.")
        print("Your first value is 0, your second value is 1, and so on.")
        search=(int(input("What index you like to search for?")))
        if search < 0 or search >= len(list):
           print('Index not ofund!')
        else:
            print(f"At this index, you have written:{list[search]}")
    # #ASK MR. FORSYTH
    elif start=="E":
        print("Here is your current list!")
        print(list)

    elif start=="F":
        undo_list = list.copy()
        print("To insert values, you must address them by index.")
        print("Your first value is 0, your second value is 1, and so on.")
        change=(int(input("What index would you like to replace?")))

        if change < 0 or change >= len(list):
            print("Invalid index!")
        else:
            new_value = input("Enter the new value: ")
            list[change] = new_value
            print("Item changed!")
            print(list)
#UNDO LAST CHANGE

    elif start == "G":
        list = undo_list.copy()
        print("Undo successful!")
        print(list)
