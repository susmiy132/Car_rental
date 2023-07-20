
from tkinter import *
from tkinter import ttk
from turtle import ScrolledCanvas 
from PIL import ImageTk,Image
from tkinter import font 


root=Tk()
root.geometry('1000x500')

# <<<<<<< HEAD
# =======

def opendetailhonda():
    root.destroy()
    import honda

def opendetaillambo():
    root.destroy()
    import lambo

def opendetailpors():
    root.destroy()
    import pors

def opendetailnissan():
    root.destroy()
    import nissan

def opendetailmerce():
    root.destroy()
    import merce

def opendetailalto():
    root.destroy()
    import alto

def openprofile():
    root.destroy()
    import profile

# >>>>>>> b8bac092eb031a759612c8bda8281884023b1b64
frame3=LabelFrame(root)

mycanvas=Canvas(frame3)
mycanvas.pack(side=LEFT,expand="yes", fill="both")


yscrollbar= ttk.Scrollbar(frame3, orient='vertical', command= mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind ('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all') ))

myframe=Frame(mycanvas)



mycanvas.create_window((0,0), window=myframe, anchor='nw')

frame3.pack(expand="yes",fill="both",padx=10,pady=5)

frame=Frame(myframe,width=500,height=250,bg='#D3D3D3')
frame.grid(row=1, column=0,pady=5)
frame6=Frame(myframe,width=500,height=250,bg='#D3D3D3')
frame6.grid(row=2, column=0,pady=5)
frame7=Frame(myframe,width=500,height=250,bg='#D3D3D3')
frame7.grid(row=3, column=0,pady=5)
frame8=Frame(myframe,width=500,height=250,bg='#D3D3D3')
frame8.grid(row=4, column=0,pady=5)
frame9=Frame(myframe,width=500,height=250,bg='#D3D3D3')
frame9.grid(row=5, column=0,pady=5)
frame10=Frame(myframe,width=500,height=250,bg='#D3D3D3')
frame10.grid(row=6, column=0,pady=5)

ig=Image.open("porsche.png")
resized9=ig.resize((170,100), Image.ANTIALIAS)
newPic9 = ImageTk.PhotoImage(resized9)
Label(frame, image= newPic9, bg = "#D3D3D3").place(x=0,y=0)
gg= Label(frame, text= "Porsche 718 Cayman ", bg="#D3D3D3")
gg.configure(font= ("Gabriola",25,"bold"))
gg.place(x=190,y=0)

Label(frame, text= "Type : Manual",font= ("Roboto",'11',"bold"), fg="white", bg="#D3D3D3").place(x=200,y=50)

framex = Frame(myframe, height=20, width=50,bg= "green")
framex.place(x=200,y=89) 
Label(framex, text="4 Seats",font=("Roboto",8,"bold")).pack()
framey = Frame(myframe, height=20, width=50,bg= "blue")
framey.place(x=257,y=89)
Label(framey, text="4 Doors",font=("Roboto",8,"bold")).pack()
framez = Frame(myframe, height=20, width=50,bg= "green")
framez.place(x=314,y=89)
Label(framez, text="Petrol",font=("Roboto",8,"bold")).pack()
framea= Frame(myframe,bg="white",width=489, height= 130)
framea.place(x=5,y=117)
l1=Label(framea, text= "Description : " ,font = ("Roboto","11","bold") ,bg="white").place(x=0,y=0)
l2= Label(framea, text= "The GTR packs a 3.8-litre V6 twin-turbocharged petrol, which puts out 570PS power", font= ("Roboto", "10") ,bg="white").place(x=0, y=23)
l3= Label(framea, text= "Engine Displacement: 3798 cc", font= ("Roboto", "11","bold") ,bg = "white").place(x=6, y=56)
l3= Label(framea, text= "ARAI mileage: 9km/l", font= ("Roboto", "11","bold") ,bg = "white").place(x=227, y=56)
l4= Label(framea, text= "Fuel Tank Capacity: 74 L", font= ("Roboto", "11","bold") ,bg = "white").place(x=6, y=97)
l5=Label(framea, text= "Body type: Coupe", font= ("Roboto", "11","bold") ,bg = "white").place(x=227, y=97)
btn1=Button(myframe,text="View Details",font=("Roboto",10,"bold"),bg="#427ef5",fg= "white", borderwidth= 2, command= opendetailpors).place(x=402,y=217)




im=Image.open("lamborghini.png")
resized=im.resize((170,100), Image.ANTIALIAS)
newPic = ImageTk.PhotoImage(resized)
Label(frame6, image= newPic,bg = "#D3D3D3").place(x=0,y=0)
Label(frame6, text= "Lamborghini Aventador", font= ("Gabriola",'25',"bold"),bg = "#D3D3D3").place(x=190,y=4)

Label(frame6, text= "Type : Automatic",font= ("Roboto",'11',"bold"), fg="white",bg = "#D3D3D3").place(x=200,y=55)

framex = Frame(frame6, height=20, width=50,bg= "green")
framex.place(x=200,y=89) 
Label(framex, text="2 Seats",font=("Roboto",8,"bold")).pack()
framey = Frame(frame6, height=20, width=50,bg= "red")
framey.place(x=257,y=89)
Label(framey, text="2 Doors",font=("Roboto",8,"bold")).pack()
framez = Frame(frame6, height=20, width=50,bg= "green")
framez.place(x=314,y=89)
Label(framez, text="Diesel",font=("Roboto",8,"bold")).pack()
framea= Frame(frame6,bg="white",width=489, height= 130)
framea.place(x=5,y=117)
l1=Label(framea, text= "Description : " ,font = ("Roboto","11","bold") ,bg="white").place(x=0,y=0)
l2= Label(framea, text= "Aventador is powered by a 6.5-litre V12 engine with a power of 770PS ", font= ("Roboto", "10"),bg = "white").place(x=0, y=23)
l3= Label(framea, text= "Engine Displacement: 6498 cc", font= ("Roboto", "11","bold") ,bg="white").place(x=6, y=56)
l3= Label(framea, text= "ARAI mileage: 8km/l", font= ("Roboto", "11","bold") ,bg="white").place(x=227, y=56)
l4= Label(framea, text= "Fuel Tank Capacity: 70 L", font= ("Roboto", "11","bold") ,bg="white").place(x=6, y=97)
l5=Label(framea, text= "Body type: Coupe", font= ("Roboto", "11","bold") ,bg="white").place(x=227, y=97)
btn1=Button(frame6,text="View Details",font=("Roboto",10,"bold"),bg="#427ef5",fg= "white", borderwidth= 2, command= opendetaillambo).place(x=402,y=217)


ir=Image.open("civic sedan.png")
resized1=ir.resize((170,100), Image.ANTIALIAS)
newPics1 = ImageTk.PhotoImage(resized1)
Label(frame7, image= newPics1, bg= "#D3D3D3").place(x=0,y=0)
Label(frame7, text= "Honda Civic Sedan", font= ("Gabriola",25,"bold"), bg= "#D3D3D3").place(x=190,y=3)

Label(frame7, text= "Type : Automatic",font= ("Roboto",'11',"bold"), fg="white", bg ="#D3D3D3").place(x=200,y=55)
framex = Frame(frame7, height=20, width=50)
framex.place(x=200,y=89) 
Label(framex, text="4 Seats",font=("Roboto",8,"bold")).pack()
framey = Frame(frame7, height=20, width=50,)
framey.place(x=257,y=89)
Label(framey, text="4 Doors",font=("Roboto",8,"bold")).pack()
framez = Frame(frame7, height=20, width=50)
framez.place(x=314,y=89)
Label(framez, text="Petrol",font=("Roboto",8,"bold")).pack()
framea= Frame(frame7,bg="white",width=489, height= 130)
framea.place(x=5,y=117)
l1=Label(framea, text= "Description : " ,font = ("Roboto","11","bold"), bg="white").place(x=0,y=0)
l2= Label(framea, text= "The Civic is a 5 seater 4 cylinder car and has length of 4656 mm, width of 1799 mm and a wheelbase of 2700 mm", font= ("Roboto", "10"), bg= "white").place(x=0, y=23)
l3= Label(framea, text= "Engine Displacement: 1800 cc", font= ("Roboto", "11","bold"), bg= "white").place(x=6, y=56)
l3= Label(framea, text= "ARAI mileage: 16km/l", font= ("Roboto", "11","bold"),bg= "white").place(x=227, y=56)
l4= Label(framea, text= "Fuel Tank Capacity: 35 L", font= ("Roboto", "11","bold"),bg= "white").place(x=6, y=97)
l5=Label(framea, text= "Body type: Sedan", font= ("Roboto", "11","bold"), bg= "white").place(x=227, y=97)
btn1=Button(frame7,text="View Details",font=("Roboto",10,"bold"),bg="#427ef5",fg= "white", borderwidth= 2, command= opendetailhonda).place(x=402,y=217)



ir=Image.open("mercedes.png")
resized3=ir.resize((170,100), Image.ANTIALIAS)
newPic3 = ImageTk.PhotoImage(resized3)
Label(frame8, image= newPic3, bg="#D3D3D3").place(x=0,y=0)
Label(frame8, text= "Mercedes-Benz G-Class", font= ("Gabriola",25,"bold"), bg= "#D3D3D3").place(x=190,y=3)

Label(frame8, text= "Type : Automatic",font= ("Roboto",'11',"bold"), fg="white", bg = "#D3D3D3").place(x=200,y=55)
framexy = Frame(frame8, height=20, width=50)
framexy.place(x=200,y=89) 
Label(framexy, text="2 Seats",font=("Roboto",8,"bold")).pack()
frameyx = Frame(frame8, height=20, width=50)
frameyx.place(x=257,y=89)
Label(frameyx, text="2 Doors",font=("Roboto",8,"bold")).pack()
framezx = Frame(frame8, height=20, width=50,bg= "blue")
framezx.place(x=314,y=89)
Label(framezx, text="Petrol",font=("Roboto",8,"bold")).pack()
frameax= Frame(frame8,bg="white",width=489, height= 130)
frameax.place(x=5,y=117)
l1=Label(frameax, text= "Description : " ,font = ("Roboto","11","bold"), bg= "white").place(x=0,y=0)
l2= Label(frameax, text= "The G-Wagon is a four-wheel drive automobile manufactured by Magna Steyr", font= ("Roboto", "10"), bg = "white").place(x=0, y=23)
l3= Label(frameax, text= "Engine Displacement: 3986 cc", font= ("Roboto", "11","bold"), bg = "white").place(x=6, y=56)
l3= Label(frameax, text= "ARAI mileage: 9km/l", font= ("Roboto", "11","bold"), bg = "white").place(x=227, y=56)
l4= Label(frameax, text= "Fuel Tank Capacity: 80 L", font= ("Roboto", "11","bold"), bg = "white").place(x=6, y=97)
l5=Label(frameax, text= "Body type: SUV", font= ("Roboto", "11","bold"), bg = "white").place(x=227, y=97)
btn1=Button(frame8,text="View Details",font=("Roboto",10,"bold"),bg="#427ef5",fg= "white", borderwidth= 2, command= opendetailmerce).place(x=402,y=217)


ir=Image.open("nissan.png")
resized4=ir.resize((170,100), Image.ANTIALIAS)
newPic4 = ImageTk.PhotoImage(resized4)
Label(frame9, image= newPic4, bg = "#D3D3D3").place(x=0,y=0)
Label(frame9, text= "Nissan GT-R 2021", font= ("Gabriola",25,"bold"),bg="#D3D3D3").place(x=190,y=3)

Label(frame9, text= "Type : Automatic",font= ("Roboto",'11',"bold"), fg="white", bg="#D3D3D3").place(x=200,y=55)


framexy = Frame(frame9, height=20, width=50)
framexy.place(x=200,y=89) 
Label(framexy, text="4 Seats",font=("Roboto",8,"bold")).pack()
frameyf = Frame(frame9, height=20, width=50)
frameyf.place(x=257,y=89)
Label(frameyf, text="4 doors",font=("Roboto",8,"bold")).pack()
framezf = Frame(frame9, height=20, width=50)
framezf.place(x=314,y=89)
Label(framezf, text="Petrol",font=("Roboto",8,"bold")).pack()
frameaf= Frame(frame9,bg="white",width=489, height= 130)
frameaf.place(x=5,y=117)
l11=Label(frameaf, text= "Description : " ,font = ("Roboto","11","bold"), bg= "white").place(x=0,y=0)
l21= Label(frameaf, text= "The GT-R packs a 3.8-litre V6 twin-turbocharged petrol, which puts out 570PS power", font= ("Roboto", "10"), bg="white").place(x=0, y=23)
l31= Label(frameaf, text= "Engine Displacement: 3798 cc", font= ("Roboto", "11","bold"),bg="white").place(x=6, y=56)
l31= Label(frameaf, text= "ARAI mileage: 9km/l", font= ("Roboto", "11","bold"),bg="white").place(x=227, y=56)
l41= Label(frameaf, text= "Fuel Tank Capacity: 74 L", font= ("Roboto", "11","bold"),bg="white").place(x=6, y=97)
l51=Label(frameaf, text= "Body type: Coupe", font= ("Roboto", "11","bold"),bg="white").place(x=227, y=97)
btn1=Button(frame9,text="View Details",font=("Roboto",10,"bold"),bg="#427ef5",fg= "white", borderwidth= 2, command= opendetailnissan).place(x=402,y=217)

ir=Image.open("alto.png")
resized6=ir.resize((180,95), Image.ANTIALIAS)
newPic6 = ImageTk.PhotoImage(resized6)
Label(frame10, image= newPic6, bg= "#D3D3D3").place(x=0,y=0)
Label(frame10, text= "Maruti Suzuki Alto", font= ("Gabriola",25,"bold"), bg= "#D3D3D3").place(x=190,y=10)

Label(frame10, text= "Type : Manual",font= ("Roboto",'11',"bold"), fg="white", bg= "#D3D3D3").place(x=200,y=55)

framexy = Frame(frame10, height=20, width=50)
framexy.place(x=200,y=89) 
Label(framexy, text="4 Doors",font=("Roboto",8,"bold")).pack()
frameyf = Frame(frame10, height=20, width=50)
frameyf.place(x=257,y=89)
Label(frameyf, text="4 Seats",font=("Roboto",8,"bold")).pack()
framezf = Frame(frame10, height=20, width=50)
framezf.place(x=314,y=89)
Label(framezf, text="Diesel",font=("Roboto",8,"bold")).pack()
frameaf= Frame(frame10,bg="white",width=489, height= 130)
frameaf.place(x=5,y=117)
l1=Label(frameaf, text= "Description : " ,font = ("Roboto","11","bold"),bg= "white").place(x=0,y=0)
l2= Label(frameaf, text= "The Maruti Alto has 2 Petrol Engine and 1 CNG Engine on offer.", font= ("Roboto", "10"), bg= "white").place(x=0, y=23)
l3= Label(frameaf, text= "Engine Displacement: 796 cc", font= ("Roboto", "11","bold"),bg= "white").place(x=6, y=56)
l3= Label(frameaf, text= "ARAI mileage: 18km/l", font= ("Roboto", "11","bold"),bg= "white").place(x=227, y=56)
l4= Label(frameaf, text= "Fuel Tank Capacity: 35 L", font= ("Roboto", "11","bold"),bg= "white").place(x=6, y=97)
l5=Label(frameaf, text= "Body type: Hatchback", font= ("Roboto", "11","bold"),bg= "white").place(x=227, y=97)

btn1=Button(frame10,text="View Details",font=("Roboto",10,"bold"),bg="#427ef5",fg= "white", borderwidth= 2, command=opendetailalto).place(x=402,y=217)



icon1=Image.open("icon2.png")
resized10=icon1.resize((70,50), Image.ANTIALIAS)
newPic10= ImageTk.PhotoImage(resized10)
btn_pro=Button(frame3, text="profile", command= openprofile, image= newPic10,borderwidth= 0)
btn_pro.place(x=870,y=0)
Label(frame3, text = "Our Cars~",font= ("Georgia",30,"bold")).place(x=515,y=0)

it=Image.open("creview.png")
resized0=it.resize((420,350), Image.ANTIALIAS)
newPic69 = ImageTk.PhotoImage(resized0)
Label(frame3, image= newPic69, bg="#D3D3D3").place(x=519,y=120)

root.mainloop()


