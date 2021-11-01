def format_cpf(event = None):
    
    text = entry.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue
        if index in [2, 5]: new_text += text[index] + "."
        elif index == 8: new_text += text[index] + "-"
        else: new_text += text[index]


    entry.delete(0, "end")
    entry.insert(0, new_text)

def format_tel(event = None):
    
    text = entry.get().replace("(", "").replace(")","").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue

        if index == 0: new_text += "(" + text[index] 
        elif index == 1: new_text += text[index] + ")"
        elif index == 6: new_text += text[index] + "-"
        else: new_text += text[index]

    entry.delete(0, "end")
    entry.insert(0, new_text)

def format_data(event = None):
    
    text = entry.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue

        if index == 1: new_text +=  text[index] + "/" 
        elif index == 3: new_text += text[index] + "/"
        else: new_text += text[index]

    entry.delete(0, "end")
    entry.insert(0, new_text)

from tkinter import *
screen = Tk()

entry = Entry(screen, font = ("Arial", 20))
entry.bind("<KeyRelease>", format_data)
entry.pack()
screen.mainloop()