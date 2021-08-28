from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("data_school")

# creating a database or connecting to one
conn = sqlite3.connect("school_datas.db")

# # creating a cursor
# c = conn.cursor()
# c.execute("""CREATE TABLE addresses(
#     students_name text,
#     students_Id text,
#     students_location text)""")
def submit():

    conn = sqlite3.connect("school_datas.db")

    c = conn.cursor()

    #Inserting the information into  a table
    c.execute("INSERT INTO addresses  VALUES(:students_name,:student_Id,:students_location)",{
        'students_name':students_name.get(),
        'student_Id': student_Id.get(),
        'students_location': students_location.get()
        #'students_gender':students_gender.get()


    })
    # show info in message box
    messagebox.showinfo("addresses","inserted successfully")

    conn.commit()

    conn.close()

def query():

    conn = sqlite3.connect("school_datas.db")

    c = conn.cursor()

    #query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)

    conn.commit()
    conn.close()


students_name = Entry(root, width= 30)
students_name.grid(row=0,column=1,padx=20 )

student_Id = Entry(root, width =30)
student_Id.grid(row=1,column=1)

students_location = Entry(root, width=30)
students_location.grid(row=2,column=1)

# students_gender = Entry(root, width=30)
# students_gender.grid(row=3,column=1)

student_name_label = Label(root,text="student's name")
student_name_label.grid(row=0,column=0)

student_Id_label = Label(root,text="student'Id")
student_Id_label.grid(row=1,column=0)


address_label = Label(root,text="students address")
address_label.grid(row = 2,column= 0)


r = StringVar()
r.set("2")


def clicked(value):

    radio_label = Label(root, text=value)
    radio_label.grid(row=5, column=1)


Radiobutton(root,text="male",variable=r,value=1,command = lambda:clicked(r.get())).grid(row=3,column=1)
Radiobutton(root,text="female",variable=r,value=2,command = lambda:clicked(r.get())).grid(row=4,column=1)

radio_label = Label(root,text=r.get())
radio_label.grid(row=5,column=1)

gender_label = Label(root,text = "students gender")
gender_label.grid(row=4,column =0)


address_label = Label(root,text="students address")
address_label.grid(row=2,column=0)

submit_button = Button(root,text="add records",command = submit)
submit_button.grid(row=6,column=0)

# creatting a query button

query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row=7,column=1 )


conn.commit()


conn.close()


mainloop()