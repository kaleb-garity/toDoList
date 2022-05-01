"""
Saves to do list in database
Able to add priority to entries
Buttons to add/remove entries
Checkmark for if a due date is relevant
"""

def add_item():
    conn = sqlite3.connect("toDoList.db")
    c = conn.cursor()
    listItem = input("Enter the list item to add: ")
    itemPriority = input("Enter item priority: ")
    itemPriority = int(itemPriority)
    fullItem = [listItem, itemPriority]
    c.execute("INSERT INTO list VALUES (?,?)", fullItem)

    conn.commit()
    conn.close()

def sort_items():
    conn = sqlite3.connect("toDoList.db")
    c = conn.cursor()
    print("\n")
    for row in c.execute("SELECT *, rowid FROM list ORDER BY priority DESC"):
        print(row)
    print("\n")

    conn.close()

def delete_item():
    conn = sqlite3.connect("toDoList.db")
    c = conn.cursor()

    placeholderName = input("Enter the rowid of item to delete: ")
    placeholderName = int(placeholderName)

    c.execute("DELETE FROM list WHERE rowid = (?)", (placeholderName,))

    conn.commit()
    conn.close()

import sqlite3

# db toDoList.db list (list item, priority)

sort_items()
add_item()
sort_items()

