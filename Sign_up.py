from ast import Pass
import email
from tkinter import*
from tkinter import messagebox
from traceback import print_tb
from turtle import position
import sqlite3
from PIL import Image,ImageTk

root=Tk()
root.geometry('900x500')
root.title("Car Rental System")
# conn=sqlite3.connect("client.db")
# c=conn.cursor()
# c.execute("""CREATE TABLE users(
#     First_Name text,
#     Last_Name text,
#     Email text PRIMARY KEY,
#     Password text,
#     Confirm_Password text,
#     status boolean)""")
# print("Table created successfully")

# #Doping table if already exists
# c.execute("DROP TABLE bookcars")
# print("Table dropped... ")

# #Commit your changes in the database
# conn.commit()

root.configure(bg="#ADD8E6")
root.resizable(False,False)



root.configure(bg="#ADD8E6")
root.resizable(False,False)
img = PhotoImage(file="bg.png")
label = Label( image=img)
label.place(x=0, y=0)

frame=Frame(root,width=350,height=350,bg='#fff')
frame.place(x=500,y=90)
heading=Label(frame,text="Register",fg='red',bg='white',font=('Gabriola','25','bold'),bd=0)
heading.place(x=130,y=0)


passw = ''
fUserName = 1
fLastName = 1
fEmail = 1
fPassword = 1
fConfirmPassword = 1

def openlogin():
    root.destroy()
    import login

def write():
    if(Username.get()=='First name' or Usernames.get()=='Last name' or  Email.get()=='Email' or Password.get()=='Password' or Confirm_password.get()=='Confirm Password' ):
        messagebox.showinfo("Error","Fill the detail")
    if Confirm_password.get()!= Password.get(): 
        messagebox.showinfo("error","password didn't match")
    else:
        conn=sqlite3.connect("client.db")
        c=conn.cursor()
        c.execute("INSERT INTO users VALUES(:First_Name,:Last_Name,:Email,:Password,:Confirm_Password, :status)",{
            "First_Name":Username.get(),
            "Last_Name":Usernames.get(),
            "Email":Email.get(),
            "Password":Password.get(),
            "Confirm_Password":Confirm_password.get(),
            "status":False
        })

        conn.commit()
        conn.close()
        Username.delete(0,END)
        Usernames.delete(0,END)
        Email.delete(0,END)
        Password.delete(0,END)
        Confirm_password.delete(0,END)
        messagebox.showinfo("user","Your data has been registered")
        openlogin()

def enter(event):
    global fUserName
    if (fUserName == 1):
        if(Username.get() == "First name"):
            Username.delete(0,END)
            return
        fUserName = 2

def leave(event):
    if Username.get()=='':
        Username.insert(0,"First name")
Username=Entry(frame,width=20,bd=5, font= ("Arial",10,"bold"))
Username.place(x=15,y=80)
Username.insert(0,"First name")
Username.bind('<FocusIn>',enter)
Username.bind('<FocusOut>',leave)


def enter(event):
    global fEmail
    if (fEmail == 1):
        if(Email.get() == "Email"):
            Email.delete(0,END)
            return
        fEmail = 2
def leave(event):
    if Email.get()=='':
        Email.insert(0,"Email")
Email=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
Email.place(x=60,y=125)
Email.insert(1,"Email")
Email.bind('<FocusIn>',enter)
# Email.bind('<key>',enter)
Email.bind('<FocusOut>',leave)

def enter(event):
    global fPassword
    if (fPassword == 1):
        if(Password.get() == "Password"):
            Password.delete(0,END)
            return
        fPassword = 2

def leave(event):
    if Password.get()=='':
        Password.insert(0,"Password")    
Password=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
Password.place(x=60,y=170)
Password.insert(2,"Password")
Password.bind("<FocusIn>",enter)
Password.bind('<FocusOut>',leave)

def enter(event):
    global fLastName
    if (fLastName == 1):
        if(Usernames.get() == "Last name"):
            Usernames.delete(0,END)
            return
        fLastName = 2

def leave(event):
    if Usernames.get()=='':
        Usernames.insert(0,"Last name")
Usernames=Entry(frame,width=20,bd=5, font= ("Arial",10,"bold"))
Usernames.place(x=190,y=80)
Usernames.insert(0,"Last name")
Usernames.bind('<FocusIn>',enter)
Usernames.bind('<FocusOut>',leave)



def enter(event):
    # p = Password.get()
    # print(p)
    global fConfirmPassword
    if (fConfirmPassword == 1):
        if(Confirm_password.get() == "Confirm Password"):
            Confirm_password.delete(0,END)
            return
        fConfirmPassword = 2

def leave(event):
    if Confirm_password.get()=='':
        Confirm_password.insert(0,"Confirm Password")
Confirm_password=Entry(frame,width=30,bd=5, font= ("Arial",10,"bold"))
Confirm_password.place(x=60,y=210)
Confirm_password.insert(3,"Confirm Password")
Confirm_password.bind("<FocusIn>",enter)
Confirm_password.bind('<FocusOut>',leave) 


signup_btn=Button(frame,text="Sign Up",fg='white', bg='blue',width=15,font=('Roboto','12','bold'),command=write)
signup_btn.place(x=90,y=260)
label=Label(frame,text="I have an account",fg='black',bg='white',font=('Roboto',9))
label.place(x=85,y=300)

signin=Button(frame,width=6,text='Sign in',fg='blue',bg='white', bd=0, command= openlogin)
signin.place(x=190,y=300)



root.mainloop()