import time
import pymysql
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import Toplevel, messagebox, filedialog

#########################################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%m:%y")
    clock.config(text='Date: ' + date_string + "\nTime: "+  time_string)
    clock.after(200, tick )

def connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        passwrd = passval.get()
        try:
            con = pymysql.connect( host=host, port=3307, user=user, passwd=passwrd)
            mycursor = con.cursor()
        except Exception as es:
            messagebox.showerror("Error", "Data is incorrect, Please try again later", parent=dbroot)
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr='create table studentdata1(id int,name varchar(50),rollno varchar(20),dob varchar(20),gender varchar(10),mobile varchar(12),email varchar(50),address varchar(90),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database created and you are connected.', parent=dbroot)
        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database.',parent=dbroot)
            dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("400x280+800+211")
    dbroot.resizable(False,False)
    dbroot.config(bg="steel blue")

    hostval = StringVar()
    userval = StringVar()
    passval = StringVar()

    hostname = Label(dbroot, text="Hostname: ", font='comicsans 18 italic bold' , bg='white', fg='blue').place(x=10, y=30)
    txt_host = Entry(dbroot, font=('times new roman', 18), bg='lightgrey', textvariable=hostval)
    txt_host.place(x=160, y=30, width=220, height=35)

    username = Label(dbroot, text="Username: ", font='comicsans 18 italic bold', bg='white', fg='blue').place(x=10, y=90)
    txt_name = Entry(dbroot, font=('times new roman', 18), bg='lightgrey', textvariable=userval)
    txt_name.place(x=160, y=90, width=220, height=35)

    password = Label(dbroot, text="Password: ", font='comicsans 18 italic bold', bg='white', fg='blue').place(x=10, y=150)
    txt_password = Entry(dbroot, font=('times new roman', 18), bg='lightgrey', textvariable=passval)
    txt_password.place(x=160, y=150, width=220, height=35)

    buttonlogin = Button(dbroot, text="Submit", fg='medium blue', activebackground='steel blue', activeforeground='black',
                         cursor='hand2', font='comicsans 18 italic bold', width=12, relief=SUNKEN, command=submitdb)
    buttonlogin.place(x=100, y=210)

    dbroot.mainloop()
################################################################################

def showstudent():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
        studenttable.insert('', END, values=vv)
#################################################################################
def addition():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        rollno = rollnoval.get()
        dob = dobval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        addedtime = time.strftime("%H:%M:%S")
        added_date = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,rollno,dob,gender,mobile,email,address,added_date,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification',"Data added successfully and want to clean the form", parent=addroot)
            if res == True:
                idval.set("")
                nameval.set("")
                rollnoval.set("")
                dobval.set("")
                genderval.set("")
                mobileval.set("")
                emailval.set("")
                addressval.set("")
        except:
            if id == '':
                messagebox.showinfo('Notification','Fill the data correctly', parent=addroot)
            else:
                messagebox.showinfo('Notification', 'Please check the data as this id is already added.', parent=addroot)
        showstudent()

    addroot = Toplevel()
    addroot.grab_set()
    addroot.geometry("450x595+180+100")
    addroot.resizable(False,False)
    addroot.config(bg="steel blue")

    idval = StringVar()
    nameval = StringVar()
    rollnoval = StringVar()
    dobval = StringVar()
    genderval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()

    welcome = Label(addroot, text="Enter the following data", bg='steel blue', foreground='black', font=('comicsans 18 italic bold')).place(x=90, y=10)
    Sid = Label(addroot, text="Enter Id ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=55)
    txt_id = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=idval)
    txt_id.place(x=200, y=55, width=225, height=30)

    Sname = Label(addroot, text="Name ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=115)
    txt_sname = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=nameval)
    txt_sname.place(x=200, y=115, width=225, height=30)

    SrollNo = Label(addroot, text="Roll No. ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=175)
    txt_roll = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=rollnoval)
    txt_roll.place(x=200, y=175, width=225, height=30)

    Sdob = Label(addroot, text="D. O. B. ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=235)
    txt_dob = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=dobval)
    txt_dob.place(x=200, y=235, width=225, height=30)

    Sgender = Label(addroot, text="Gender ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=295)
    txt_gender = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=genderval)
    txt_gender.place(x=200, y=295, width=225, height=30)

    Smobile = Label(addroot, text="Mobile No. ", font='comicsans 14 italic',width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=355)
    txt_mobile = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=mobileval)
    txt_mobile.place(x=200, y=355, width=225, height=30)

    Semail = Label(addroot, text="Email ", font='comicsans 14 italic',width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=415)
    txt_email = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=emailval)
    txt_email.place(x=200, y=415, width=225, height=30)

    Saddress = Label(addroot, text="Address ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=475)
    txt_address = Entry(addroot, font='comicsans 14 italic', bg='lightgrey', textvariable=addressval)
    txt_address.place(x=200, y=475, width=225, height=30)

    button7 = Button(addroot, text="Submit", fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                     width=12, relief=SUNKEN, borderwidth=5, command=submitadd)
    button7.place(x=140, y=525)

    addroot.mainloop()
#############################################################################################################
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        rollno = rollnoval.get()
        dob = dobval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        date = dateval.get()
        if id != '':
            strr = 'select * from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
        elif name != '':
            strr = 'select * from studentdata1 where name=%s'
            mycursor.execute(strr, (name))
        elif rollno != '':
            strr = 'select * from studentdata1 where rollno=%s'
            mycursor.execute(strr, (rollno))
        elif dob != '':
            strr = 'select * from studentdata1 where dob=%s'
            mycursor.execute(strr, (dob))
        elif gender != '':
            strr = 'select * from studentdata1 where gender=%s'
            mycursor.execute(strr, (gender))
        elif mobile != '':
            strr = 'select * from studentdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
        elif email != '':
            strr = 'select * from studentdata1 where email=%s'
            mycursor.execute(strr, (email))
        elif address != '':
            strr = 'select * from studentdata1 where address=%s'
            mycursor.execute(strr, (address))
        elif date != '':
            strr = 'select * from studentdata1 where date=%s'
            mycursor.execute(strr, (date))

        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]]
            studenttable.insert('', END, values=vv)

    searchroot = Toplevel()
    searchroot.grab_set()
    searchroot.geometry("450x640+180+100")
    searchroot.resizable(False, False)
    searchroot.config(bg="steel blue")

    idval = StringVar()
    nameval = StringVar()
    rollnoval = StringVar()
    dobval = StringVar()
    genderval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    dateval = StringVar()

    welcome = Label(searchroot, text="Enter the following data", bg='steel blue', foreground='black', font=('comicsans 18 italic bold')).place(x=90, y=10)
    id = Label(searchroot, text="Enter Id ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=55)
    txt_id = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=idval)
    txt_id.place(x=200, y=55, width=225, height=30)

    studentname = Label(searchroot, text="Name ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=115)
    txt_sname = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=nameval)
    txt_sname.place(x=200, y=115, width=225, height=30)

    rollNo = Label(searchroot, text="Roll No. ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=175)
    txt_roll = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=rollnoval)
    txt_roll.place(x=200, y=175, width=225, height=30)

    dob = Label(searchroot, text="D. O. B. ", font='comicsans 14 italic', width=12, bg='white', fg='blue',relief=SUNKEN).place(x=25, y=235)
    txt_dob = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=dobval)
    txt_dob.place(x=200, y=235, width=225, height=30)

    gender = Label(searchroot, text="Gender ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=295)
    txt_gender = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=genderval)
    txt_gender.place(x=200, y=295, width=225, height=30)

    mobile = Label(searchroot, text="Mobile No. ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=355)
    txt_mobile = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=mobileval)
    txt_mobile.place(x=200, y=355, width=225, height=30)

    email = Label(searchroot, text="Email ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=415)
    txt_email = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=emailval)
    txt_email.place(x=200, y=415, width=225, height=30)

    address = Label(searchroot, text="Address ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=475)
    txt_address = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=addressval)
    txt_address.place(x=200, y=475, width=225, height=30)

    date = Label(searchroot, text="Date ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=535)
    txt_date = Entry(searchroot, font='comicsans 14 italic', bg='lightgrey', textvariable=dateval)
    txt_date.place(x=200, y=535, width=225, height=30)

    button7 = Button(searchroot, text="Submit", fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                     width=12, relief=SUNKEN, borderwidth=5, command=search)
    button7.place(x=135, y=580)

    searchroot.mainloop()

###################################################################################################
def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr, (pp[0]))
    con.commit()
    messagebox.showinfo("Notification", "Data deleted")
    showstudent()

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        rollno = rollnoval.get()
        dob = dobval.get()
        gender = genderval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s, rollno=%s, dob=%s, gender=%s, mobile=%s, email=%s, address=%s, date=%s, time=%s where id=%s'
        mycursor.execute(strr,(name,rollno,dob,gender,mobile,email,address,date,time,id))
        con.commit()
        messagebox.showinfo("Notification", "Data Updatedd", parent=updateroot)
        showstudent()

    updateroot = Toplevel()
    updateroot.grab_set()
    updateroot.geometry("450x660+180+100")
    updateroot.resizable(False, False)
    updateroot.config(bg="steel blue")

    idval = StringVar()
    nameval = StringVar()
    rollnoval = StringVar()
    dobval = StringVar()
    genderval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    id = Label(updateroot, text="Enter Id ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=20)
    txt_id = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=idval)
    txt_id.place(x=200, y=20, width=225, height=30)

    studentname = Label(updateroot, text="Name ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=80)
    txt_sname = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=nameval)
    txt_sname.place(x=200, y=80, width=225, height=30)

    rollNo = Label(updateroot, text="Roll No. ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=140)
    txt_roll = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=rollnoval)
    txt_roll.place(x=200, y=140, width=225, height=30)

    dob = Label(updateroot, text="D. O. B. ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=200)
    txt_dob = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=dobval)
    txt_dob.place(x=200, y=200, width=225, height=30)

    gender = Label(updateroot, text="Gender ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=260)
    txt_gender = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=genderval)
    txt_gender.place(x=200, y=260, width=225, height=30)

    mobile = Label(updateroot, text="Mobile No. ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=320)
    txt_mobile = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=mobileval)
    txt_mobile.place(x=200, y=320, width=225, height=30)

    email = Label(updateroot, text="Email ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=380)
    txt_email = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=emailval)
    txt_email.place(x=200, y=380, width=225, height=30)

    address = Label(updateroot, text="Address ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=440)
    txt_address = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=addressval)
    txt_address.place(x=200, y=440, width=225, height=30)

    date = Label(updateroot, text="Added Date ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=500)
    txt_adate = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=dateval)
    txt_adate.place(x=200, y=500, width=225, height=30)

    time = Label(updateroot, text="Added Time ", font='comicsans 14 italic', width=12, bg='white', fg='blue', relief=SUNKEN).place(x=25, y=560)
    txt_atime = Entry(updateroot, font='comicsans 14 italic', bg='lightgrey', textvariable=timeval)
    txt_atime.place(x=200, y=560, width=225, height=30)

    button7 = Button(updateroot, text="Submit", fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                     width=12, relief=SUNKEN, borderwidth=5, command=update)
    button7.place(x=135, y=605)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if len(pp) != 0:
        idval.set(pp[0])
        nameval.set(pp[1])
        rollnoval.set(pp[2])
        dobval.set(pp[3])
        genderval.set(pp[4])
        mobileval.set(pp[5])
        emailval.set(pp[6])
        addressval.set(pp[7])
        dateval.set(pp[8])
        timeval.set(pp[9])

    updateroot.mainloop()

######################################################################

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,rollno,dob,gender,mobile,email,address,added_date,added_time = [],[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),rollno.append(pp[2]),dob.append(pp[3]),gender.append(pp[4]),mobile.append(pp[5]),
        email.append(pp[6]),address.append(pp[7]),added_date.append(pp[8]),added_time.append(pp[9])
    dd = ['Id','Name','Roll No.','D.O.B.','Gender','Mobile','Email','Address','Added Date','Added Time']
    df = pd.DataFrame(list(zip(id,name,rollno,dob,gender,mobile,email,address,added_date,added_time)),columns=dd)
    path = r'{}.csv'.format(ff)
    df.to_csv(path,index=False)
    messagebox.showinfo('Notification',"Student data saved successfully {}.".format(path))

def exitstudent():
    res = messagebox.askyesnocancel("Warning", "Are you sure you want to exit??", parent=root)
    if res == True:
        root.destroy()
#######################################################################
root = Tk()
root.maxsize(width=1250, height=750)
root.geometry("1200x800+100+20")
root.title("Student Management System")
root.config(bg='DodgerBlue2')
##################################################################################
leftFrame = Frame(root, bg='gold2', height=650, width=450, borderwidth=4, relief=GROOVE)
leftFrame.place(x=24, y=80)

welcome = Label(leftFrame, text="-----------------WELCOME-----------------",bg='gold2', foreground='black', font=('comicsans 16 italic'))
welcome.place(x=40, y=25)
button1 = Button(leftFrame, text="Add Student",fg='medium blue', activebackground='cornflower blue',  cursor='hand2', font=('comicsans 14 italic'),
                 width=25, relief=SUNKEN, borderwidth=5, command=addition)
button1.place(x=70, y=80)
button2 = Button(leftFrame, text="Remove Student",fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                 width=25, relief=SUNKEN, borderwidth=5, command=deletestudent)
button2.place(x=70, y=160)
button3 = Button(leftFrame, text="Search Student",fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                 width=25, relief=SUNKEN, borderwidth=5, command=searchstudent)
button3.place(x=70, y=240)
button4 = Button(leftFrame, text="Update Student",fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                 width=25, relief=SUNKEN, borderwidth=5, command=updatestudent)
button4.place(x=70, y=320)
button5 = Button(leftFrame, text="Show All",fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                 width=25, relief=SUNKEN, borderwidth=5, command=showstudent)
button5.place(x=70, y=400)
button6 = Button(leftFrame, text="Export Data",fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                 width=25, relief=SUNKEN, borderwidth=5, command=exportstudent)
button6.place(x=70, y=480)
button7 = Button(leftFrame, text="Quit",fg='medium blue', activebackground='cornflower blue', cursor='hand2', font=('comicsans 14 italic'),
                 width=25, relief=SUNKEN, borderwidth=5, command=exitstudent)
button7.place(x=70, y=560)

#############################################################################################################
rightFrame = Frame(root, bg='gold2', borderwidth=4, relief=GROOVE)
rightFrame.place(x=500, y=80, width=675, height=650)
style = ttk.Style()
style.configure('Treeview.Heading', font='chiller 18 italic bold', foreground='dodgerblue4')
style.configure('Treeview', font='chiller 16 italic bold', background='light sky blue', foreground='black')
scrollx = Scrollbar(rightFrame, orient=HORIZONTAL)
scrolly = Scrollbar(rightFrame, orient=VERTICAL)
studenttable = Treeview(rightFrame, columns=('Id','Name','Roll No.','D.O.B.','Gender','Mobile','E-mail','Address','Added Date','Added Time'),
                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, show='headings')
scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)
scrollx.config(command=studenttable.xview)
scrolly.config(command=studenttable.yview)
studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Roll No.', text='Roll No.')
studenttable.heading('D.O.B.', text='D.O.B.')
studenttable.heading('Gender', text='Gender')
studenttable.heading('Mobile', text='Mobile')
studenttable.heading('E-mail', text='E-mail')
studenttable.heading('Address', text='Address')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable.column('Id', width=100)
studenttable.column('Name', width=220)
studenttable.column('Roll No.', width=150)
studenttable.column('D.O.B.', width=150)
studenttable.column('Gender', width=150)
studenttable.column('Mobile', width=150)
studenttable.column('E-mail', width=250)
studenttable.column('Address', width=250)
studenttable.column('Added Date', width=150)
studenttable.column('Added Time', width=150)
studenttable.pack(fill=BOTH, expand=True)

##################################################################################
clock = Label(root, font='times 14 bold', relief=SUNKEN, borderwidth=4, bg='steelblue1')
clock.place(x=2,y=2)
tick()
headlabel = Label(root, text="Welcome to Student Management System", bg='skyblue1',
                   fg='midnight blue', font=('chiller 28 italic bold'), relief=GROOVE, borderwidth=4, padx=30)
headlabel.place(x=310, y=3)

button = Button(root, text="Connect to Database", font=('comicsans 16 italic'), width=20, relief=SUNKEN, borderwidth=5, bg='steelblue1',
                activebackground='dodgerblue2', activeforeground='black', cursor='hand2', command=connectdb)
button.place(x=950,y=3)
######################################################################################

root.mainloop()