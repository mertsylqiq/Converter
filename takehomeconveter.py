from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

root= Tk()
root.title("Converter")
root.geometry("500x400")

def pickoption(e):
    if all_options.get()=="Weight":
        second_options.config(values=weight_options)
        second_options.current(0)
    elif all_options.get()=="Distance":
        second_options.config(values=distance_options)
        second_options.current(0)
    elif all_options.get()=="Temperature":
        second_options.config(values=temp_options)
        second_options.current(0)
def calculations():
    try:
        x=(input1.get())
        if second_options.get()=="Kilograms":
            totalw1=int(x)*1
            output1.delete(0, END)
            output1.insert(0, totalw1)
            totalw2=int(x)*2.20462
            output2.delete(0,END)
            output2.insert(0,totalw2)
            totalw3=int(x)*35.274
            output3.delete(0,END)
            output3.insert(0, totalw3)
            lbl1.config(text="Kilograms")
            lbl2.config(text="Pounds")
            lbl3.config(text="Ounce")
        elif second_options.get()=="Pounds":
            totalw1=int(x)*0.453592
            output1.delete(0, END)
            output1.insert(0,totalw1)
            totalw2=int(x)*1
            output2.delete(0,END)
            output2.insert(0,totalw2)
            totalw3=int(x)*16
            output3.delete(0,END)
            output3.insert(0, totalw3)
            lbl1.config(text="Kilograms")
            lbl2.config(text="Pounds")
            lbl3.config(text="Ounce")
        elif second_options.get()=="Ounce":
            totalw1=int(x)*0.0283495
            output1.delete(0, END)
            output1.insert(0,totalw1)
            totalw2=int(x)*0.0625
            output2.delete(0,END)
            output2.insert(0,totalw2)
            totalw3=int(x)*1
            output3.delete(0,END)
            output3.insert(0,totalw3)
            lbl1.config(text="Kilograms")
            lbl2.config(text="Pounds")
            lbl3.config(text="Ounce")
        elif second_options.get()=="Kilometers":
            totald1=int(x)*1
            output1.delete(0, END)
            output1.insert(0,totald1)
            totald2=int(x)*0.621371
            output2.delete(0,END)
            output2.insert(0,totald2)
            totald3=int(x)*1093.61
            output3.delete(0,END)
            output3.insert(0,totald3)
            lbl1.config(text="Kilometers")
            lbl2.config(text="Miles")
            lbl3.config(text="Yards")
        elif second_options.get()=="Miles":
            totald1=int(x)*1.60934
            output1.delete(0, END)
            output1.insert(0,totald1)
            totald2=int(x)*1
            output2.delete(0,END)
            output2.insert(0,totald2)
            totald3=int(x)*1760
            output3.delete(0,END)
            output3.insert(0,totald3)
            lbl1.config(text="Kilometers")
            lbl2.config(text="Miles")
            lbl3.config(text="Yards")
        elif second_options.get()=="Yards":
            totald1=int(x)*0.0009144
            output1.delete(0, END)
            output1.insert(0,totald1)
            totald2=int(x)*0.000568182
            output2.delete(0,END)
            output2.insert(0,totald2)
            totald3=int(x)*1
            output3.delete(0,END)
            output3.insert(0,totald3)
            lbl1.config(text="Kilometers")
            lbl2.config(text="Miles")
            lbl3.config(text="Yards")
        elif second_options.get()=="Celcius":
            totalt1=int(x)*1
            output1.delete(0, END)
            output1.insert(0,totalt1)
            totalt2=int(x)*33.8
            output2.delete(0,END)
            output2.insert(0,totalt2)
            totalt3=int(x)*274.15
            output3.delete(0,END)
            output3.insert(0,totalt3)
            lbl1.config(text="Celcius")
            lbl2.config(text="Fahrenheit")
            lbl3.config(text="Kelvin")
        elif second_options.get()=="Fahrenheit":
            totalt1=(int(x)- 32) * 5/9 
            output1.delete(0, END)
            output1.insert(0,totalt1)
            totalt2=int(x)*1
            output2.delete(0,END)
            output2.insert(0,totalt2)
            totalt3=int(x)*255.928
            output3.delete(0,END)
            output3.insert(0,totalt3)
            lbl1.config(text="Celcius")
            lbl2.config(text="Fahrenheit")
            lbl3.config(text="Kelvin")
        elif second_options.get()=="Kelvin":
            totalt1=int(x)-273.15
            output1.delete(0, END)
            output1.insert(0,totalt1)
            totalt2=(int(x)-273.15)*9/5+32
            output2.delete(0,END)
            output2.insert(0,totalt2)
            totalt3=int(x)*1
            output3.delete(0,END)
            output3.insert(0,totalt3)
            lbl1.config(text="Celcius")
            lbl2.config(text="Fahrenheit")
            lbl3.config(text="Kelvin")          
    except:
        msg.showinfo("Message", "Please put a integer number")

#List of first options
foptions=[
    "Weight",
    "Distance",
    "Temperature",
]

weight_options=[
    "Kilograms",
    "Pounds",
    "Ounce",
]
distance_options=[
    "Kilometers",
    "Miles",
    "Yards",
]
temp_options=[
    "Celcius",
    "Fahrenheit",
    "Kelvin",
]

#Input
input1= Entry(width=20)
input1.insert(0, " ")
input1.pack()
input1=input1
input1.place(relx=0.35, rely=0.1)

#Option list
all_options=ttk.Combobox(root, values=foptions)
all_options.pack()
all_options.place(relx=0.04, rely=0.1)

#Second list
second_options=ttk.Combobox(root, values=[])
second_options.pack()
second_options.place(relx=0.65, rely=0.1)

#ConvertButton
btnSubmit= Button(text="Convert", width=7, height=1, command=calculations)
btnSubmit.config(font=("Arial", 15))
btnSubmit.pack()
btnSubmit.place(relx=0.4, rely=0.3)

#Outputs
output1=Entry(width = 15)
output1.insert(0," ")
output1.pack()
output1.place(relx=0.04, rely=0.7)

output2=Entry(width = 15)
output2.insert(0," ")
output2.place(relx=0.35, rely=0.7)

output3=Entry(width = 15)
output3.insert(0," ")
output3.place(relx=0.65, rely=0.7)

#Labels

#Lable
lbl1= Label(text=" ", foreground="black")
lbl1.config(font=("Arial", 8))
lbl1.pack()
lbl1.place(relx=0.04, rely=0.6)

lbl2= Label(text=" ", foreground="black")
lbl2.config(font=("Arial", 8))
lbl2.pack()
lbl2.place(relx=0.35, rely=0.6)

lbl3= Label(text=" ", foreground="black")
lbl3.config(font=("Arial", 8))
lbl3.pack()
lbl3.place(relx=0.65, rely=0.6)


#Choosing the second option
all_options.bind("<<ComboboxSelected>>", pickoption)

root.mainloop()