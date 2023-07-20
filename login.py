

from re import A
from tkinter import*
from tkinter import messagebox
import tkinter.font as font
from PIL import ImageTk, Image
import sqlite3

window= Tk()
window.geometry("900x500")
window.title("Login")
window.configure(bg= "#ADD8E6")
font1= font.Font(family="Georgia")
font2= font.Font(family="Georgia", size=8)
window.resizable(False,False)
img0= PhotoImage(file="bg3.png")
label1=Label(window, image= img0,bg="#ADD8E6")
label1.pack(side=LEFT)

# Label(window,text= "Car Rental System", bg="#ADD8E6", font= ("Impact", 30)).place(x=100,y=20)



frame=Frame(window,width=300,height=350,bg='#fff', borderwidth=3)
frame.place(x=550,y=100)
femail=1
fpassword=1
def opensignup():
    window.destroy()
    import Sign_up

def opendash():
    window.destroy()
    import dash

#Read and Verify the database info
def check():
        a=Email.get()
        b=Password.get()
        try:
            conn=sqlite3.connect('client.db')
            c=conn.cursor()

            c.execute("SELECT * FROM users")
            records=c.fetchall()
            i=len(records)-1
            while i>=0:
                if records[i][2]!=a or records[i][3]!=b:
                    i=i-1
                    if i==-1:
                        messagebox.showerror("Login","Invalid Credentials")
                        break
                else:
                    #change user status to active after login and set other user as inactive
                    c.execute("""UPDATE users SET
                    status=:inactive
                    WHERE status=:active""",
                    {'inactive':False,
                    'active':True})
                    conn.commit()
                    
                    c.execute("""UPDATE users SET
                    status= :val
                    WHERE Email = :a""",
                    {
                        'val':True,
                        'a':a
                    })
                    conn.commit()
                    messagebox.showinfo("Login","Logged in Successfully")
                    opendash()
                    break           
            conn.commit()
            conn.close()
        except:
            messagebox.showerror("Login","Sign Up First")

def enter(event):
    global femail
    if (femail == 1):
        if(Email.get() == "Email"):
            Email.delete(0,END)
            return
        femail = 2
def leave(event):
    if Email.get()=='':
        Email.insert(0,"Email")
Email=Entry(frame,width=23,bd=5,font=('Arial',12,'bold'))
Email.place(x=50,y=75)
Email.insert(1,"Email")
Email.bind('<FocusIn>',enter)
Email.bind('<FocusOut>',leave)


def enter(event):
    global fpassword
    if (fpassword == 1):
        if(Password.get() == "Password"):
            Password.delete(0,END)
            return
        fpassword =2
def leave(event):
    if Password.get()=='':
        Password.insert(0,"Password")
Password=Entry(frame,width=23,bd=5,font=('Arial',12,'bold'))
Password.place(x=50,y=130)
Password.insert(2,"Password")
Password.bind("<FocusIn>",enter)
Password.bind('<FocusOut>',leave)
heading=Label(frame,text="Login",fg='red',bg='white',font=('Gabriola','25','bold'))
heading.place(x=110,y=5)


    #login button
bt1=Button(frame,text="LOGIN",font=('Arial',10,'bold'),fg='white',bg="#338bd7",width=16,height=2,cursor='hand2', command= check)
bt1.place(x=75,y=180)
btn2=Button(frame,text="SignUp",font=("Roboto","9","bold"),bd=0,fg="blue",bg="white", command= opensignup).place(x=170,y=250)
signup_label= Label(window, text="don't have an account?",font= font2,bg='white' )
signup_label.place(x=570,y=350)

window.mainloop()