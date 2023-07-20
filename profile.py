from tkinter import*
import sqlite3
from tkinter import messagebox

from PIL import ImageTk,Image
root=Tk()
root.title('profile')
root.geometry('1000x500')
root.configure(bg="#c2d4e3")

root.configure(bg="#ADD8E6")
root.resizable(False,False)
img = PhotoImage(file="bg.png")
label = Label( image=img)
label.place(x=0, y=0)

lab1=Label(root,text="First Name",bg="#c2d4e3",font=("Roboto","9","bold")).place(x=550,y=65)

lab2=Label(root,text="Last Name",bg="#c2d4e3",font=("Roboto","9","bold")).place(x=760,y=65)

lab3=Label(root,text="Email",bg="#c2d4e3",font=("Roboto","9","bold")).place(x=610,y=120)

lab4=Label(root,text="Password",bg="#c2d4e3",font=("Roboto","9","bold")).place(x=610,y=160)

lab5=Label(root,text="Confirm_Password",bg="#c2d4e3",font=("Roboto","9","bold")).place(x=610,y=210)


#fetching the user info
try:
    conn=sqlite3.connect('client.db')
    c=conn.cursor()
    c.execute("SELECT * from users WHERE status=:act",{'act':True})
    records=c.fetchall()
    a=records[0][0]
    b=records[0][1]
    c=records[0][2]
    d=records[0][3]
    e=records[0][4]
    
    conn.commit()
    conn.close()
except:
    a="First Name"
    b="Last Name"
    c="Email"
    d="Password"
    e="Confirm Password"

#Putting fetched info in entries box automatically
fname=Entry(root, width=20,bd=4)
fname.insert(0,a)
fname.place(x=620,y=67)

lname=Entry(root, width=20,bd=4)
lname.insert(0,b)
lname.place(x=830,y=67)

Email=Entry(root,width=30,bd=4)
Email.insert(0,c)
Email.place(x=730,y=122)

pws=Entry(root,width=30,bd=4)
pws.insert(0,d)
pws.place(x=730,y=162)

con_pws=Entry(root,width=30,bd=4)
con_pws.insert(0,e)
con_pws.place(x=730,y=212)
 
#updatation of profile
def update():
    #database update
    conn=sqlite3.connect('client.db')
    c=conn.cursor()
    c.execute("""UPDATE users SET
    First_Name=:a,
    Last_Name=:b,
    Email=:d,
    Password=:e,
    Confirm_Password=:f
    WHERE status=:act""",
    {
        'a':fname.get(),
        'b':lname.get(),
        'd':Email.get(),
        'e':pws.get(),
        'f':con_pws.get(),
        'act':True
    })
    conn.commit()
    conn.close()

    #messagebox after update
    messagebox.showinfo("Accounts","Your profile details have been updated successfully!")

#delete the info
def delete():
    msg=messagebox.askquestion("Delete","Are you sure you want to delete record?")
    if msg=='yes':
        conn=sqlite3.connect('client.db')
        c=conn.cursor()
        c.execute("DELETE from users WHERE status=:act",{'act':True})
        conn.commit()
        conn.close()

        #import function
        root.destroy()
        import login

#Logout
def logout():
    msb=messagebox.askquestion("Logout","Are you sure you want to logout?")
    if msb=='yes':
        #set user status to inactive
        conn=sqlite3.connect('client.db')
        c=conn.cursor()
        c.execute("""UPDATE users SET
        status= :off
        WHERE status= :on""",
        {
            'off':False,
            'on':True
        })
        conn.commit()
        conn.close()

        try:
        #logout
            root.destroy()
            import login
        except:
            pass





but=Button(root,text="Edit Profile",width=25,font=('Roboto','11','bold'),bg="black",fg="white",bd=8, command= update).place(x=670,y=265)
but1=Button(root,text="Delete Profile",width=25,font=('Roboto','11','bold'),bg="black",fg="white",bd=8, command= delete).place(x=670,y=330)
but1=Button(root,text="Logout",width=25,font=('Roboto','11','bold'),bg="black",fg="white",bd=8, command = logout).place(x=670,y=400)
label=Label(root,text="Your Profile",font=("georgia","15","bold"),bg="#c2d4e3").place(x=700,y=10)

def opendash():
    root.destroy()
    import dash

backimage= Image.open("backicon.png")
resized=backimage.resize((50,50), Image.ANTIALIAS)
newPic9 = ImageTk.PhotoImage(resized)

backbutton= Button(root, image= newPic9,bd=0,bg="black", activebackground="black", command=opendash).place(x=5,y=3)
root.mainloop()
