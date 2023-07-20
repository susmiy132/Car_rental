from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image
root=Tk()
root.title("booknow")
root.geometry("510x510")
root.config(bg="#bcd4f7")

label1=Label(root,text="Your Booking Details:",font=("Gabriola","25","bold"),bg="#bcd4f7").pack(side=TOP)

#fetching the booking info
def table():
    table=Frame(root,height=580,width=950,bg='white')
    table.place(x=10,y=70)

    try:
        conn=sqlite3.connect('Booking.db')
        c=conn.cursor()
        c.execute("SELECT oid, Pick_Up_Location, Pick_Up_Time, Rental_Duration, Username from Rent_Details")
        records=c.fetchall()

        conn.commit()
        conn.close()
    except:
        records=[]

    finally:
        records.insert(0,('ID',"Pick_Up_Location", "Pick_Up_Time", "Rental_Duration", "Username"))

#creating a table to fetch/retrive
    total_rows =len(records)
    total_columns=len(records[0])
    for i in range(total_rows):
        if i==0:
            #table heading
            fontt=('Arial',10,'bold')
            jus=CENTER
            bgc ='#9cc2e5'
        else:
            #table data
            fontt=('Arial',10)
            jus=CENTER
            bgc='white'
        for j in range(total_columns):
            #width for all columns
            if j==0:
                wid=5
            elif j==1:
                wid=17
            elif j==2:
                wid=14
            elif j==3:
                wid=17
            elif j==4:
                wid=13

            e=Entry(
                table,
                width=wid,
                font=fontt,
                justify=jus,
                disabledforeground='black',
                disabledbackground=bgc
            )
            e.grid(row=i,column=j)
            e.insert(0,records[i][j])
            e.config(state=DISABLED)

#calling table function
table()

#Update the booking data

def update():
    pr= sqlite3.connect("Booking.db")
    p= pr.cursor()

    record_id= up.get()
    p.execute("""UPDATE Rent_Details SET
    Pick_Up_Location = :PUL,
    Pick_Up_Time= :PUT,
    Rental_Duration= :RD,
    Username= :Usr,
    status= :act
    WHERE oid = :oid""",
    {"PUL": PUL_editor_entry.get(),
    "PUT": PUT_editor_entry.get(),
    "RD": RD_editor_entry.get(),
    "Usr": Usr_editor_entry.get(),
    "act": True,
    "oid": record_id})
    
    pr.commit()
    pr.close()
    editor.destroy()

    messagebox.showinfo("Data update", "Your information has been upadated successfully.")

def edit():
    global editor
    editor= Toplevel()
    editor.title("Edit Rental Data")
    editor.geometry("300x210")
    editor.iconbitmap("refresh.ico")
    editor.configure(bg="white")

    pr= sqlite3.connect("Booking.db")
    p= pr.cursor()
    record_id= up.get()
    p.execute("SELECT * FROM Rent_Details WHERE oid="+record_id)
    records= p.fetchall()
    global PUL_editor_entry
    global PUT_editor_entry
    global RD_editor_entry
    global Usr_editor_entry


    PUL_editor_label= Label(editor, text= "Pick up Location",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    PUL_editor_label.grid(row=0, column=0)

    PUT_editor_label= Label(editor, text= "Pick up Time",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    PUT_editor_label.grid(row=1, column=0)

    RD_editor_label= Label(editor, text= "Rental Duration",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    RD_editor_label.grid(row=2, column=0)

    Usr_editor_label= Label(editor, text= "Username",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    Usr_editor_label.grid(row=3, column=0)

    PUL_editor_entry= Entry(editor, borderwidth=2)
    PUL_editor_entry.grid(row=0, column=1)

    PUT_editor_entry= Entry(editor, borderwidth=2)
    PUT_editor_entry.grid(row=1, column=1)

    RD_editor_entry= Entry(editor, borderwidth=2)
    RD_editor_entry.grid(row=2, column=1)

    Usr_editor_entry= Entry(editor, borderwidth=2)
    Usr_editor_entry.grid(row=3, column=1)

    for record in records:
        PUL_editor_entry.insert(0, record[0])
        PUT_editor_entry.insert(0, record[1])
        RD_editor_entry.insert(0, record[2])
        Usr_editor_entry.insert(0, record[3])

    save_btn= Button(editor, text= "SAVE",bg="grey55", command= update)
    save_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

#Delete or cancel the booking

def delete():
    pr= sqlite3.connect("Booking.db")
    p= pr.cursor()

    response= messagebox.askyesno("Permission", "Do you really want to delete the data of ID no. "+dele.get()+" ?"+"\n"+ "Data deleted from here can not be recover from anywhere.")
    if response== True:
        p.execute("DELETE from Rent_Details WHERE oid="+dele.get())
        messagebox.showinfo("info", "Your data has been deleted succesfully.")
    else:
        messagebox.showinfo("info", "Your data has not been deleted.")

    dele.delete(0, END)
    pr.commit()
    pr.close()

#defining fup and fdel
fup=1
fdel=1

def enter(event):
    global fup
    if (fup == 1):
        if(up.get() == "Enter CID to update"):
            up.delete(0,END)
            return
        fup = 2
def leave(event):
    if up.get()=='':
        up.insert(0,"Enter CID to update")
up=Entry(width=17,bd=5,font=('Arial',12,'bold'))
up.place(x=170,y=250)
up.insert(1,"Enter CID to update")
up.bind('<FocusIn>',enter)
up.bind('<FocusOut>',leave)


def enter(event):
    global fdel
    if (fdel == 1):
        if(dele.get() == "Enter CID to cancel"):
            dele.delete(0,END)
            return
        fdel =2
def leave(event):
    if dele.get()=='':
        dele.insert(0,"Enter CID to cancel")
dele=Entry(width=17,bd=5,font=('Arial',12,'bold'))
dele.place(x=170,y=370)
dele.insert(2,"Enter CID to cancel")
dele.bind("<FocusIn>",enter)
dele.bind('<FocusOut>',leave)

def opendash1():
    root.destroy()
    import dash 


Button5= Button(root, text= "Back to Dashboard",font=('Roboto',14,'bold'),bg="black",fg="white", command=opendash1).pack(side=BOTTOM)
Button6= Button(root, text= "Edit Booking Details",font=('Roboto',14,'bold'),fg="white",bg="#34a8eb", command=edit).place(x=153,y=293)
Button6= Button(root, text= "Cancel booking",font=('Roboto',14,'bold'),bg="red", fg="white", command=delete).place(x=172,y=410)
backimage= Image.open("backicon.png")
resized=backimage.resize((50,50), Image.ANTIALIAS)
newPic9 = ImageTk.PhotoImage(resized)

# backbutton= Button(root, image= newPic9,bd=0,bg="#bcd4f7",activebackground="#bcd4f7",command= opendash1).place(x=0,y=0)
root.mainloop()