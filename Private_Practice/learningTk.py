#LINAR PROJECT
#python pacckages imported:
import tkinter as tk
from tkinter import messagebox
import csv
import re
import os

#Created a function to valid email
def valid_email(email):
  #created  variable to store the email pattern
  #imported re to use expression that symbolize how email pattern format
  emailpattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9._-]{2,}$'
  #using the match function from re to check if the email entry matches the email patern
  return re.match(emailpattern, email)

def Reg_Success():
  msg_showinfo = tk.Toplevel()
  msg_showinfo.title("Message Info")
  msg_showinfo.geometry("300x100")
  
  tk.Label(msg_showinfo, text='Registration Successful\nYour details have been saved', wraplength=350).pack(pady=20, padx=20)
  tk.Button(msg_showinfo, text='close', command=msg_showinfo.destroy).pack()
  msg_showinfo.mainloop()


def register_button():
  error = []
  Fname = entry_Firstname.get()
  Lname = entry_Lastname.get()
  email = entry_EmailAddress.get()
  confirm = entry_confirmEmail.get()
  phoneno = entry_PhoneNumber.get()
  passkey = entry_Password.get()
  gender= selectgender.get()
  Age = AgeBracket.get()
  state = entry_StateofOrigin.get()
  residence = entry_StateofResidence.get()
  course = course_entry.get()

  if not Fname:
    error.append("First name required")
  if not Lname:
    error.append("Last name required")
  if not valid_email(email):
    error.append("Enter Valid Email")
  if not confirm:
    error.append("Reconfirm Email")
  if email != confirm:
    error.append("Email doesn't match")
  if not phoneno.isdigit() or len(phoneno) <11 or len(phoneno) >11:
    error.append("Enter valid phone number")
  if not passkey:
    error.append("Create a Password")
  if not len(passkey) >=10:
    error.append("Password must be 10 or above characters")
  if Age == "Select Age Bracket":
    error.append("Age required")
  if gender == "Select Gender":
    error.append("Gender required")
  if course == 'Available Courses':
        error.append("Course selection required")
  if not state:
     error.append("State of origin required")
  if not residence:
    error.append("State of residence required")
  if not all([Fname,Lname,email,confirm, phoneno,passkey,Age,state, residence, gender, course]):
    messagebox.showerror("All fields required")
  if error:
    messagebox.showerror('errors', '\n'.join(error))
  else:
    data = [Fname, Lname, email, phoneno, gender, Age, state, residence]
    with open('Linar_Project.csv', 'a', newline='') as file:
      #mode- append new dta at the end of the file
      writer = csv.writer(file)
      writer.writerow(data)
    clear_fields()
    #message = "Registration Successful! \n Your details have been saved."
    Reg_Success()
    
#clear the registration form after successful registration
def clear_fields():
  entry_Firstname.delete(0, tk.END)
  entry_Lastname.delete(0, tk.END)
  entry_PhoneNumber.delete(0, tk.END)
  entry_EmailAddress.delete(0, tk.END)
  entry_confirmEmail.delete(0, tk.END)
  entry_Password.delete(0, tk.END)
  AgeBracket.set("Select Age Bracket")
  entry_StateofOrigin.delete(0, tk.END)
  entry_StateofResidence.delete(0, tk.END)
  selectgender.set("Select Gender")
  course_entry.set("Select Course")
   
root = tk.Tk()
root.title("REGISTRATION FORM")
root.geometry("400x600")
#Title
tk.Label(root, text= "REGISTRATION FORM", font=("Ariel", 16, 'bold'), fg="Black").grid(row=0, column=0,pady=5, padx=20)
#FirstName
tk.Label(root, text= "Enter your First Name", font="bold").grid(row=1, column=0)
entry_Firstname = tk.Entry(root)
entry_Firstname.grid(row=1, column=1)
#Last Name
tk.Label(root, text="Enter your Last Name", font="bold").grid(row=2, column=0, pady=5)
entry_Lastname = tk.Entry(root)
entry_Lastname.grid(row=2, column=1)
#Gender
tk.Label(root, text="Gender", font="bold").grid(row=3, column=0)
selectgender = tk.StringVar(value="Select Gender")
genderoptions = ["Male", "Female"]
genderdropdown = tk.OptionMenu(root, selectgender, *genderoptions).grid(row=3, column=1, pady=5)
#Email Address
tk.Label(root, text="Email Address", font="bold").grid(row=4, column=0, pady=5)
entry_EmailAddress = tk.Entry(root)
entry_EmailAddress.grid(row=4, column=1)
#Confirm Email Address
tk.Label(root, text="Confirm Email Address", font="bold").grid(row=5, column=0, pady=5)
entry_confirmEmail = tk.Entry(root)
entry_confirmEmail.grid(row=5, column=1)
#Phone Number
tk.Label(root, text="Phone Number", font="bold").grid(row=6, column=0, pady=5)
entry_PhoneNumber = tk.Entry(root)
entry_PhoneNumber.grid(row=6, column=1)
#Create a Password
tk.Label(root, text="Create password", font="bold").grid(row=7, column=0, pady=5)
entry_Password = tk.Entry(root, show="*")
entry_Password.grid(row=7, column=1)
#Age Bracket
tk.Label(root, text="Age Bracket", font="bold").grid(row=8, column=0, pady=5)
AgeBracket = tk.StringVar(value="Select Age Bracket")
Ageoptions = ["18-22", "23-27", "28-32", "33-38", "39-43", "44-Above"]
Agedropdown= tk.OptionMenu(root, AgeBracket, *Ageoptions).grid(row=8, column=1)
#State_of_Origin
tk.Label(root, text="State of Origin", font="bold").grid(row=9, column=0, pady=5)
entry_StateofOrigin = tk.Entry(root)
entry_StateofOrigin.grid(row=9, column=1)
#State_of_residence
tk.Label(root, text="City of Residence", font="bold").grid(row=10, column=0, pady=5)
entry_StateofResidence = tk.Entry(root)
entry_StateofResidence.grid(row=10, column=1)
#course_enrolling_for
tk.Label(root, text="Select Course", font="bold").grid(row=11, column=0, pady=5)
course_entry =tk.StringVar(value='Available Courses')
course_options =['Python', 'Web Development', 'Mobile App Development', 'UI/UX', 'Cybersecurity']
Coursedropsown= tk.OptionMenu(root, course_entry, *course_options).grid(row=11, column=1)
#Register Button
tk.Button(root, text="Register", font= 'bold', command=register_button).grid(row=12, column=0, columnspan=2)
root.mainloop()