# importing library 
from tkinter import *
from tkinter import ttk
window=Tk()

#Declaring Window Title 
window.title("Welcome...Registration Screen")

#Declaring Window Size
window.geometry('300x300')

#Declaring window colour 
window.configure(background="Orange");

#Implementing ten fields 
FirstName=Label(window,text="First Name").grid(row = 1,column = 0)
LastName=Label(window,text="Last Name").grid(row = 2,column = 0)
Email=Label(window,text="Email Id").grid(row = 3,column = 0)
PhoneNo=Label(window,text="Phone No").grid(row = 4,column = 0)
DateofBirth=Label(window,text="Date of Birth").grid(row = 5,column = 0)
EducationalQualification=Label(window,text="Educational Qualification").grid(row = 6,column = 0)
Language= Label(window,text="Language").grid(row = 7,column = 0)
Address=Label(window,text="Address").grid(row = 8,column = 0)
Gender=Label(window,text="Gender").grid(row = 9,column = 0)
Idproof=Label(window,text="Id proof").grid(row = 10,column = 0)

FirstName=Entry(window).grid(row=1,column=1)
LastName=Entry(window).grid(row=2,column=1)
EmailID=Entry(window).grid(row=3,column=1)
PhoneNO=Entry(window).grid(row=4,column=1)
DateOfBirth=Entry(window).grid(row=5,column=1)
EducationalQualification=Entry(window).grid(row=6,column=1)
Language=Entry(window).grid(row=7,column=1)
Address=Entry(window).grid(row=8,column=1)
Idproof=Entry(window).grid(row=10,column=2)

var=IntVar()
Radiobutton(window,text="Male",padx=20,variable=var,value=1).grid(row=9,column=1)
Radiobutton(window,text="Female",padx=30,variable=var,value=1).grid(row=9,column=2)

#List of Id proof
list_of_Id_proof =["Aadhar Card","Pan Card","Passport","Voter ID card"]

# dropdown menu 
A=StringVar()
dropdown = OptionMenu(window,A,*list_of_Id_proof)
dropdown.config(width=21)
A.set("Select")
dropdown.grid(row=10,column=1)

Button(window,text="Registration form",width=20,bg="blue",fg="White",font=("bold",10)).grid(row=0,column=1)
Button(window,text='Submit',width=20,bg="blue",fg='white',font=("bold",10)).grid(row = 15,column =1)
       
window.mainloop()
