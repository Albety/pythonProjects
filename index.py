import tkinter

window = tkinter.Tk()
window.title("Mile to km Converter")
window.minsize(width=200, height=200)

def convert():
    new_text = int(float(input.get())*1.6)
    label3.config(text= new_text)

input = tkinter.Entry(width=7)
input.grid(row=0, column=1)

label1 = tkinter.Label(text="Miles")
label1.grid(row=0, column=2)

label2 = tkinter.Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = tkinter.Label(text=0)
label3.grid(row=1, column=1)

label4 = tkinter.Label(text="Km")
label4.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)





window.mainloop()
