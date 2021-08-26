from tkinter import *
import sqlite3

root = Tk()
root.title("data_school")

conn = sqlite3.connect("school_data.db")

c = conn.cursor()
# c.execute("""CREATE TABLE addresses(
#     students_name text,
#     students_Id text,
#     students_gender text,
#     students_location text)""")

students_name = Entry(root, width= 30)
students_name.grid(row=0,column=1,padx=20 )

student_Id = Entry(root, width =30)
student_Id.grid(row=1,column=1)

print("works")



students_location = Entry(root, width=30)
students_location.grid(row=2,column=1)

student_name_label = Label(root,text="student's name")
student_name_label.grid(row=0,column=0)

student_Id_label = Label(root,text="student'Id")
student_Id_label.grid(row=1,column=0)


address_label = Label(root,text="students address")
address_label.grid(row = 2,column= 0)


r= StringVar()
r.set("2")
def clicked(value):
    radio_label = Label(root, text=value)
    radio_label.grid(row=5, column=1)

Radiobutton(root,text="male",variable=r,value=1,command = lambda:clicked(r.get())).grid(row=3,column=1)
Radiobutton(root,text="female",variable=r,value=2,command = lambda:clicked(r.get())).grid(row=4,column=1)

radio_label = Label(root,text=r.get())
radio_label.grid(row=5,column=1)

gender_label = Label(root,text = "students gender")
gender_label.grid(row= 4,column = 0)



address_label = Label(root,text="students address")
address_label.grid(row = 2,column= 0)



conn.commit()
conn.close()




mainloop()