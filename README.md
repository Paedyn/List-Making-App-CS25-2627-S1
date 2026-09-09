# Extension Activity: List Making App

Create a Python program that allows a user to manage a list entirely through the console. Your program could manage a to-do list, packing list, watch list, shopping list, game collection, reading list, or another type of ordered information you choose.

Your program should demonstrate that you can create, access, modify, search, traverse, copy, and remove data from a Python list. These are the main list operations introduced in the lesson.

This program presents a significant level of challenge, and is intentionally left open-ended. I recommend trying to break this program down into smaller tasks. In terms of help, you can use myself for recommendations.

# AI Assistance With this Task

It would also be appropriate to use AI for a workflow breakdown or a series of steps that might be helpful for breaking down this task. An appropriate prompt might be along the lines of "Without providing any coding assistance, help me break this project down into more manageable subtasks" or "Without providing any coding assistance, where would be a good place to start this task". Regardless of you choose to use AI, an important part of the prompt will be **"without providing any coding assistance"**.

## Requirements

Your program must:

* Start with an **empty list** that will store items entered by the user. 
* Repeatedly display a menu and use `input()` to let the user choose what they want to do.
* Continue running until the user chooses an **Exit** option.
* Include at least **six different commands** that interact with the list:

  1. Allow the user to **add a new item** to the end of the list using `append()`. 
  2. Allow the user to **insert an item at a specific position** using `insert()`. 
  3. Allow the user to **change an existing item** by accessing and reassigning a list index. 
  4. Allow the user to **remove an item** using either `remove()` or `pop()`.  
  5. Include an option to **display every item in the list** using a `for` loop rather than simply printing the entire list.
  6. Include a **search command** that asks the user for an item and uses `in` to report whether that value exists in the list.
* Display the **number of items currently stored** using `len()`.
* When displaying the list, clearly show the position or number of each item so that the user can identify items they may want to edit or remove.
* Prevent the program from intentionally accessing an index that is outside the list. An invalid position should display an appropriate message instead of crashing the program. The lesson demonstrates that an invalid list index causes an `IndexError`. 
* Include an **Undo Last Change** feature:

  * Before changing the list, save its current state using `copy()`.
  * Undo should restore the list to that saved state.
  * The copied list must remain independent of the current list. 
* Display clear messages after actions so the user knows what happened.

## Design Choices

You decide:

* What type of information your program manages.
* What the program and menu options are called.
* How the menu is displayed.
* Whether users enter positions starting from `0` or starting from `1`.
* Which removal method makes the most sense for your program.
* How you organize your conditions and loops.
* Whether you add additional list features beyond the required commands.

Your finished program should feel like a small usable application rather than a collection of unrelated demonstrations.

## Minimum Testing

Before submitting, demonstrate that your program can successfully:

* Add at least **3 items**.
* Insert an item somewhere other than the end.
* Change an existing item.
* Search for an item that exists.
* Search for an item that does not exist.
* Remove an item.
* Display all current items.
* Display the current number of items.
* Undo a change.
* Handle at least one invalid position without crashing.
* Exit normally.

## Grading Checklist

| Criteria                                                                         |  Marks |
| -------------------------------------------------------------------------------- | -----: |
| Program uses an empty list and user input to build its data                      |      2 |
| Menu repeats until the user chooses to exit                                      |      2 |
| User can add items with `append()`                                               |      2 |
| User can insert items with `insert()`                                            |      2 |
| User can modify an existing item using its index                                 |      3 |
| User can remove items from the list                                              |      2 |
| Program traverses and displays the list using a `for` loop                       |      3 |
| Program uses `len()` to report the number of items                               |      2 |
| Program searches the list using `in`                                             |      2 |
| Program handles invalid positions without crashing                               |      3 |
| Undo feature correctly uses `copy()` to preserve an independent previous version |      4 |
| Program provides clear prompts, output, and feedback to the user                 |      2 |
| Program is complete, organized, and functions as one coherent application        |      3 |
| **Total**                                                                        | **30** |
