import os
import curses
from datetime import datetime



def create_note():
    notelst=[]
    title=input('Title: ')
    tags=input("Tags (Comma-Separated): ")
    print("Note Content:  [Press Enter Twice To End]\n")
    while True:
        note = input()
        if not note:
            break
        notelst.append(f"{note}\n")


    timestamp=datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename=f"notes/{title}_{timestamp}.md"
    with open(filename, "w") as obj:
        obj.write(f"{title}\n\nTags:{tags}\n\n")
        obj.writelines(notelst)


################################################################
def open_note():
    print("opened a note")
