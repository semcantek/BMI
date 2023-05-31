from tkinter import *
window = Tk()
window.title("Tkinter python")
window.minsize(width=600,height=600)
window.config(pady=10, padx=10)

def buton_clicked():
    userInput = entry.get()
    print(userInput)
    print("***********")
    userText= text.get("1.0", END)
    print(userText)

#label
my_label = Label(text="My label")
my_label.config(fg="white")
my_label.config(bg="black")
my_label.config(padx=20,pady=20)
my_label.pack()
#button
buton = Button(text="Buton1", command=buton_clicked)
buton.pack()

#entry
entry =Entry(width=20)
entry.focus()
entry.pack()
#text
text = Text()
text.config(padx=10,pady=10)
text.config(width=25, height=10)
text.pack()

window.mainloop()