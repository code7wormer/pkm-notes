import os
from datetime import datetime
import shutil
import time

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
    openmenu={}
    notepath='notes'
    for filename in os.listdir(notepath):
        if filename.endswith('.md'):
            file_path=os.path.join(notepath,filename)
            with open(file_path,"r", encoding='utf-8') as f:
                first_line = f.readline().strip()
                if file_path not in openmenu.values():
                    openmenu[first_line]=file_path
    titlelist=list(openmenu.keys())
    for i in range(1,len(titlelist)+1):\
        print(i,f"-> {titlelist[i-1]}")
    x = int(input("Enter file to open: "))
    width = shutil.get_terminal_size().columns
    with open(openmenu[titlelist[x-1]], "r", encoding='utf-8') as f:
        print("\n",'#'*width,"\n")
        content = f.read()
        print(content)
    print("\n", '#' * width, "\n")
    y=input()



