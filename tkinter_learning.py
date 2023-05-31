import tkinter
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=250,height=250)
#buton içinde command kullanırken fonksiyon global en üste yazılmalı, yoksa algılamıyor.
def button_clicked():
    user_input= my_entry.get()
    print(user_input )
#label
my_label = tkinter.Label(text="This is a label.", background="black", foreground="white")
#my_label.config(height=25,width=25)
my_label.grid(row=0,column=0)
#my_label.pack()

#button
my_button = tkinter.Button(text="Button", command=button_clicked)
#my_button.place(x=25, y=25)
#my_button.update()
#print(my_button.winfo_height())
#print(my_button.winfo_width())
my_button.grid(row=2,column=1)
#my_button.pack()

#entry
my_entry = tkinter.Entry(width=20)
my_entry.grid(row=0, column=1)
#my_entry.pack()
window.mainloop()

#place spesifik lokasyon verirken, pack basit lokasyonda, grid ızgara sistemi kullanılırken kullanılır.