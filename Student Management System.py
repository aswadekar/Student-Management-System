from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Student:
    def __init__(self,root):

        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1920x1080+0+0")


        title=Label(self.root,text="WELCOME TO VIT INSTITUTE", bd=10, relief=GROOVE,font=("times new roman", 40, "bold"), bg="cornflower blue", fg="black")
        title.pack(side=TOP, fill=X)

        self.RollNo_var=StringVar()
        self.Name_var=StringVar()
        self.EMail_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.DOB_var=StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="cornflower blue")
        Manage_Frame.place(x=20,y=100,width=450,height=670)

        m_title=Label(Manage_Frame, text="MANAGE STUDENTS", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll=Label(Manage_Frame, text="Roll Number", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_roll = Entry(Manage_Frame,textvariable=self.RollNo_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20)

        lbl_Name = Label(Manage_Frame, text="Name", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20)

        lbl_EMail = Label(Manage_Frame, text="E-Mail", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_EMail.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_EMail = Entry(Manage_Frame,textvariable=self.EMail_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_EMail.grid(row=3, column=1, pady=10, padx=20)

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.Gender_var, font=("times new roman", 13, "bold"), state='readonly')
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_Contact = Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20)

        lbl_DOB = Label(Manage_Frame, text="D.O.B", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20)

        lbl_Address = Label(Manage_Frame, text="Address", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=30, height=3, font=("", 10))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="cornflower blue")
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn = Button(btn_Frame, text="ADD", width=10,command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="UPDATE", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="DELETE", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="CLEAR", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="cornflower blue")
        Detail_Frame.place(x=500, y=100, width=1020, height=670)

        lbl_search = Label(Detail_Frame, text="Search By", bg="cornflower blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, width=10, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("RollNo", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt, width=20, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        seachwbtn = Button(Detail_Frame, text="SEARCH", width=10, pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="SHOW ALL", width=10, pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg='cornflower blue')
        Table_Frame.place(x=10,y=70,width=990,height=550)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Frame,columns=("roll no", "name", "email", "gender", "contact", "dob", "Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll no", text="Roll Number")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="E-Mail")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll no",width=100)
        self.Student_table.column("name",width=200)
        self.Student_table.column("email", width=200)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=150)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=200)
        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>,self.get_cusor")
        self.fetch_data()
    def add_students(self):
        if self.RollNo_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:

                con = pymysql.connect(host="localhost", user="root", password="", database="syg")
                cur = con.cursor()
                cur.execute(
                    "insert into students values (%s,%s,%s,%s,%s,%s,%s)",(self, self.RollNo_var.get(),

                                                                          self.Name_var.get(),
                                                                          self.EMail_var.get(),
                                                                          self.Gender_var.get(),
                                                                          self.Contact_var.get(),
                                                                          self.DOB_var.get(),
                                                                          self.txt_Address.get('1.0', END)))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")


    def search_data(self):
        
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where"+str(self.search_by.get())+"Like %"+str(self.search_txt.get())+"%")
        rows=cur.fetchall()
        if len(rows)!=0:
                  self.Student_table.delete(*self.Student_table.get_children())
                  for row in rows:
                           self.Student_table.insert('',END,values=rows)
                  con.commit()
        con.close()
        
    def clear(self):
        self.RollNo_var.set("")
        self.Name_var.set("")
        self.EMail_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete("1.0",END)



    def get_cursor(self,ev):

        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']

        self.RollNo_var.set(row[0])
        self.Name_var.set(row[1])
        self.EMail_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="syg")
        cur = con.cursor()
        cur.execute("update into students set Name=%s,EMail=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s,where RollNo=%s)",(
                                                                          self.Name_var.get(),
                                                                          self.EMail_var.get(),
                                                                          self.Gender_var.get(),
                                                                          self.Contact_var.get(),
                                                                          self.DOB_var.get(),
                                                                          self.txt_Address.get('1.0', END),
                                                                          self.RollNo_var.get(),
                                                                          ))
        con.commit()

        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()

        cur.execute("delete from students where RollNo=%s",self.RollNo_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
    def fetch_data(self):
        
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where"+str(self.search_by.get())+"Like %"+str(self.search_txt.get())+"%")
        rows=cur.fetchall()
        if len(rows)!=0:
                  self.Student_table.delete(*self.Student_table.get_children())
                  for row in rows:
                           self.Student_table.insert('',END,values=rows)
                  con.commit()
        con.close()    

root=Tk()
ob=Student(root)
root.mainloop()