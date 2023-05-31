from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=600,height=600)
window.config(padx=5, pady=5)

def calculate_bmi():
    h = float(height.get())
    w = float(weight.get())
    sonuc = w/h**2
    print(sonuc)
    if sonuc < 18.5:
        print("You are underweight.")
    elif 18.5 < sonuc < 25:
        print("Your weight is normal.")
    elif 25 < sonuc < 29.99:
        print("You are overweight.")
    elif sonuc > 30:
        print("Az ye dana.")
    else:
        print("Please write your height or weight.")

#labels
label1 = Label(text="Weight (kg):")
label1.grid(row=1, column=1)

label2 = Label(text="Height (m):")
label2.grid(row=2, column=1)

label3 = Label()
label3.grid(row=4, column=2)

#entry
height = Entry()
height.grid(row=2, column=2)
weight = Entry()
weight.focus()
weight.grid(row=1, column=2)


#button
calculate = Button(text="Calc",command=calculate_bmi)
calculate.grid(row=3, column=2)


window.mainloop()