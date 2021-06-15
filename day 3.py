# importing library 
from tkinter import *
from tkinter import ttk
window=Tk()

#Declaring Window Title 
window.title("Welcome...Registeration Screen")

#Declaring Window Size
window.Geometry("300*300")

#Declaring window colour 
window.configure(Background="Orange")

#Implementing ten fields 
FirstName=label(window,text="First Name").grid(row = 1,column = 0)
LastName=label(window,text="Last Name").grid(row = 2,column = 0)
Email Id=label(window,text="Email Id").grid(row = 3,column = 0)
Phone No=(window,text="Phone No").grid(row = 4,column = 0)
Date of Birth=(window,text="Date of Birth").grid(row = 5,column = 0)
Educational Qualification=(window,text="Educational Qualification").grid(row = 6,column = 0)
Language = (window,text="Language").grid(row = 7,column = 0)
Address=(window,text="Address").grid(row = 8,column = 0)

First Name=Entry(window).grid(row=1,column=1)
Last Name=Entry(window).grid(row=2,column=1)
Email ID=Entry(window).grid(row=3,column=1)
Phone NO=Entry(window).grid(row=4,column=1)
Date Of Birth=Entry(window).grid(row=5,column=1)
Educational Qualification=Entry(window).grid(row=6,column=1)
Language=Entry(window).grid(row=7,column=1)
Address=Entry(window).grid(row=8,column=1)

var=IntVar()
Radiobutton(window,text="Male",padx=20,Variable=var,value=1).grid(row=9,column=1)
Radiobutton(window,text="Female",padx=30,Variable=var,value=1).grid(row=9,column=2)

#List of Id proof
list of Id proof =["Aadhar Card","Pan Card","Passport","Voter ID card"]

# dropdown menu 
A=StringVar()
dropdown = Optionmenu(window,A,*list of Id proof)
dropdown.config(width=21)
a.set("Select")
dropdown.grid(row=10,column=1)

Button(window,text="Registration form",width=20,bg="blue",fg="White",font=("bold",10).grid(row=0,column=1)
Button(window,text="Submit",width=20,bg="blue",fg="white",font=("bold",10).grid(row=15,column=2)
window.mainloop()



