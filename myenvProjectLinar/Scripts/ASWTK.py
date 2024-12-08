import tkinter as tkn
users= [("BECCA", "1234567")
        ("ASAKPA", "1234")
        ]

def loginclick():
  name = entry_userID.get()
  password = entry_Passkey.get()
  for x in users:
    if name and password in x:
      display.config(text= f'welcome {name}' )
    else:
      display.config(text="Enter valid details please!")
    
root = tkn.Tk()
root.title("ASW INVENTORY MANAGER")
root.geometry("600x600")

Label_title = tkn.Label(root, text= "ASOMA STEEL WORKS INVENTORY MANAGER", fg='DarkBlue', font=('Times New Romans', 14, 'bold'))
Label_userID = tkn.Label(root, text="Enter UserID", font=14)
entry_userID = tkn.Entry(root)
Label_Passkey = tkn.Label(root, text= "Enter Password", font=14)
entry_Passkey = tkn.Entry(root, show="*")
button_Login = tkn.Button(root, text= 'Login', command=loginclick)
button_newUser = tkn.Button(root, text='New User?' )
button_exit = tkn.Button(root, text='Exit')
display = tkn.Label(root, text='')

Label_title.grid(padx=45)
Label_userID.grid()
entry_userID.grid()
Label_Passkey.grid()
entry_Passkey.grid()
button_exit.grid(row=0, column=1)
button_Login.grid(row=0, column=2, pady=10)
button_newUser.grid()
display.grid()


root.mainloop()
