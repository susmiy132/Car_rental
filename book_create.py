from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

root=Tk()
root.title("booknow")
root.geometry("400x400")
# pr= sqlite3.connect("Booking.db")
# p=pr.cursor()
# p.execute("""CREATE TABLE Rent_Details(
#     Pick_Up_Location text,
#     Pick_Up_Time integer,
#     Rental_Duration integer,
#     Username text,
#     status boolean)""")

# print("Table created succesfully")

# #Doping User table if already exists
# p.execute("DROP TABLE User")
# print("Table dropped... ")

# #Commit your changes in the database
# pr.commit()


def opencardetails():
    root.destroy()
    import bookcar_details

def submit():
    if entry2.get()=='' or entry3.get()=='' or  entry4.get()=='' or entry5.get()=='':
        messagebox.showinfo("Error","Please fill all the required details")
    
    else:
        pr=sqlite3.connect("Booking.db")
        p=pr.cursor()
        p.execute("INSERT INTO Rent_Details VALUES( :Pick_Up_Location, :Pick_Up_Time, :Rental_Duration, :Username, :status)",
        {"Pick_Up_Location": entry2.get(),
        "Pick_Up_Time": entry3.get(),
        "Rental_Duration": entry4.get(),
        "Username": entry5.get(),
        "status": False})
        messagebox.showinfo("User information", "Inserted succesfully")
        pr.commit()
        pr.close()
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        opencardetails()



label1=Label(root,text="Enter Booking Details:",font=("Gabriola","25","bold")).place(x=10,y=28)
label2=Label(root,text="Pick Up Location:",font=('Roboto','9','bold')).place(x=15,y=100)
label3=Label(root,text="Pick Up Time:",font=('Roboto','9','bold')).place(x=15,y=150)
label4=Label(root,text="Rental Duration:",font=('Roboto','9','bold')).place(x=15,y=200)
label5=Label(root,text="Username:",font=('Roboto','9','bold')).place(x=15,y=250)

entry2=Entry(root,width=30,bd=5,font=('Roboto','9','bold'))
entry2.place(x=150,y=100)
entry3=Entry(root,width=30,bd=5,font=('Roboto','9','bold'))
entry3.place(x=150,y=150)
entry4=Entry(root,width=30,bd=5,font=('Roboto','9','bold'))
entry4.place(x=150,y=200)
entry5=Entry(root,width=30,bd=5,font=('Roboto','9','bold'))
entry5.place(x=150,y=250)


button1=Button(root,text="Confirm Booking",font=("Roboto","12","bold"),fg="blue",bd=0, borderwidth=2, command= submit).place(x=130,y=300)
backimage= Image.open("backicon.png")
resized=backimage.resize((50,45), Image.ANTIALIAS)
newPic9 = ImageTk.PhotoImage(resized)

def opendash():
    root.destroy()
    import dash

backbutton= Button(root, image= newPic9,bd=0, command=opendash).place(x=0,y=0)
root.mainloop()