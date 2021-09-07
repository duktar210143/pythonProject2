from tkinter import *
from tkinter import messagebox
import sqlite3
import pytest


root = Tk()
root.title("data_school")
root.geometry("400x500")

# creating a database or connecting to one
conn = sqlite3.connect("school_data.db")

# creating a cursor
c = conn.cursor()

# c.execute("""CREATE TABLE addresses(
#     students_name text,
#     students_Id text,
#     students_gender text,
#     students_location text)""")
# print("table created successfully")


def submit():

    conn = sqlite3.connect("school_data.db")

    c = conn.cursor()

    #Inserting the information into  a table
    c.execute("INSERT INTO addresses  VALUES(:students_name,:student_Id,:students_location,:student_gender)",{
        'students_name':students_name.get(),
        'student_Id': student_Id.get(),
        'student_gender': student_gender.get(),
        'students_location': students_location.get()
    })


        #'students_gender':students_gender.get()



    # show info in message box
    messagebox.showinfo("addresses","inserted successfully")

    conn.commit()

    conn.close()




def query():

    conn = sqlite3.connect("school_data.db")

    c = conn.cursor()

    #query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    print(records)

    #loop through results
    print_record = ""

    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1])+' '+'\t' + str(record[4])+"\n"

    query_label = Label(root, text= print_record)
    query_label.grid(row=17,column=0,columnspan =2)

    conn.commit()
    conn.close()


def delete():
    """creting or connecting to a database"""
    conn = sqlite3.connect("school_data.db")

    #create cursor
    c = conn.cursor()

    #delete a record
    c.execute("DELETE from addresses WHERE oid = "+ delete_box.get())
    print("deleted successfully")

    c.execute("SELECT *,oid FROM addresses")

    records = c.fetchall()

    #loop through the results
    print_record = ""
    for record in records:
        print_record += str(record[0]) + '' + str(record[1]) + '' + '\t' + str(record[4]) + "\n"

    query_label = Label(root,text=print_record)
    query_label.grid(row=19,column=1,columnspan=2)

    conn.commit()
    conn.close()


students_name = Entry(root, width= 30)
students_name.grid(row=0,column=1,padx=20 )

student_Id = Entry(root, width =30)
student_Id.grid(row=1,column=1)

student_gender = Entry(root,width=30)
student_gender.grid(row=3,column=1)

students_location = Entry(root, width=30)
students_location.grid(row=2,column=1)

delete_box = Entry(root,width=30)
delete_box.grid(row=10,column=1)


student_name_label = Label(root,text="student's name")
student_name_label.grid(row=0,column=0)

student_Id_label = Label(root,text="student'Id")
student_Id_label.grid(row=1,column=0)

address_label = Label(root,text="students address")
address_label.grid(row = 2,column= 0)

student_gender_lbl = Label(root,text="students gender")
student_gender_lbl.grid(row=3,column=0)

delete_lbl = Label(root,text="delete student's Id")
delete_lbl.grid(row=10,column=0)


submit_button = Button(root,text="add records",command=submit,width=20)
submit_button.grid(row=6,column=1)


delete_btn = Button(root,text= "delete record",command=delete,width=20)
delete_btn.grid(row=14,column=1)

# creating a query button

query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row=8,column=1)


conn.commit()


conn.close()


root.mainloop()