from sqlite3 import Cursor
from tkinter import *
import pymysql
import tkinter.messagebox as m

r = Tk()
r.geometry("400x400")
r.title("User Details")
r.configure(bg="Blue")

def CreateConn():
    return pymysql.connect(host="localhost",database="tkinter",user="root",password="",port=3306)

def InsertData():
    f = enfn.get()
    l = enln.get()
    e = enem.get()
    u = enuid.get()

    if (f==" " or l==" " or e==" " or u==" "):
        m.showinfo("Insert Status","All Fields are Mandatory")
    else:
        try:
            conn = CreateConn()
            Cursor = conn.cursor()
            args = (f,l,e,u)
            query = "insert into user(fname,lname,email,userid) values (%s,%s,%s,%s)"
            Cursor.execute(query,args)
            conn.commit()
            m.showinfo("Insert Status","Data Inserted")
            conn.close()

        except Exception as ee:
            print("Insert Exception :",ee)


def UpdateData():
    f = enfn.get()
    l = enln.get()
    e = enem.get()
    u = enuid.get()

    if (f==" " or l==" " or e==" " or u==" "):
        m.showinfo("Insert Status","All Fields are Mandatory")
    else:
        try:
            conn = CreateConn()
            Cursor = conn.cursor()
            args = (f,l,e,u)
            query = "Update user set fname = %s , lname = %s , email = %s where userid = %s"
            Cursor.execute(query,args)
            conn.commit()
            m.showinfo("Insert Status","Data Updated")
            conn.close()

        except Exception as ee:
            print("Insert Exception :",ee)



def DeleteData():
    u = enuid.get()

    if u == " ":
        m.showinfo("Insert Status","Enter UserId")
    else:
        try:
            conn = CreateConn()
            Cursor = conn.cursor()
            args = (u)
            query = "delete from user where userid = %s"
            Cursor.execute(query,args)
            conn.commit()
            m.showinfo("Insert Status","Data Deleted")
            conn.close()

        except Exception as ee:
            print("Insert Exception ;",ee)



     
fname = Label(r,text="First Name")
fname.place(x=20,y=20)
lname = Label(r,text="Last Name")
lname.place(x=20,y=50)
email = Label(r,text="Email Id")
email.place(x=20,y=80)
uid = Label(r,text="User Id")
uid.place(x=20,y=110)

enfn = Entry()
enfn.place(x=100,y=20)
enln = Entry()
enln.place(x=100,y=50)
enem = Entry()
enem.place(x=100,y=80)
enuid = Entry()
enuid.place(x=100,y=110)

button1 = Button(r,text="Insert",bg="White",command=InsertData)
button1.place(x=100,y=150)
button1 = Button(r,text="Update",bg="White",command=UpdateData)
button1.place(x=175,y=150)
button1 = Button(r,text="Delete",bg="White",command=DeleteData)
button1.place(x=250,y=150)
    
mainloop()