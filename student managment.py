
from tkinter import *
from tkinter import Toplevel, messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
import pandas


def tick():  # clock
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    Clock.config(text='Date :'+date_string+"\n"+"Time :"+time_string)
    Clock.after(200, tick)

# ===================== connectdb window


def connectdb():
    def submitdb():  # ========= GETTINg CONNECTDB INPUT
        global con, mycursor
        
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                'Notification', 'Invailed Data !! Please try again')
            return
        try:
            strr = 'create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(10),dob varchar(15),date varchar(30),time varchar(30))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo(
                'Notification', 'Database is created . Now yor are connected to database..', parent=dbroot)

        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo(
                'Notification', 'Connection established..', parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+700+180')
    dbroot.config(bg='blue')
    dbroot.resizable(False, False)

    # CONNECTDB window label
    hostlable = Label(dbroot, text='Enter Host', bg='gold2', font=(
        'Times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='c')
    hostlable.place(x=10, y=10)

    userlable = Label(dbroot, text='Enter User', bg='gold2', font=(
        'Times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='c')
    userlable.place(x=10, y=70)

    passwordlable = Label(dbroot, text='Enter Password', bg='gold2', font=(
        'Times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='c')
    passwordlable.place(x=10, y=130)

    # window Entry variables
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    # +++++++++++++++++++++++  CONNECTDB window Entery boxes

    hostentry = Entry(dbroot, bd='5', font=(
        'roman', 15, 'bold'), textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, bd='5', font=(
        'roman', 15, 'bold'), textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, bd='5', font=(
        'roman', 15, 'bold'),  textvariable=passwordval)
    passwordentry.place(x=250, y=130)

# ============== CONNECTDB BUTTON

    submitbutton = Button(dbroot, text='Submit', font=(
        'roman', 15, 'bold'), width=20, activebackground='blue', bg='red', bd=5, command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()


def addstudent():
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+105+170')
    addroot.resizable(False, False)
    addroot.config(bg='blue')
    addroot.title('Student Managment System')

    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email,
                             address, gender, dob, addedtime, addeddate))
            con.commit()
            res = messagebox.askyesnocancel(
                'Notification', 'Id {} Name {} Added succesfully...and want to clean the form'.format(id, name), parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')

        except:
            messagebox.showerror(
                'Notification', 'Id Already Exist..', parent=addroot)
        strr = 'Select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

# ---------------------ADD STUDENT LABEL

    idlabel = Label(addroot, text='Enter Id', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                       width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                         width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    doblabel.place(x=10, y=370)

# ------------ADD STUDENT ENTERY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'),
                       bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'),
                         bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'),
                     bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

# ================ ADDING BUTTON

    submitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), bd=5,
                       bg='red', activebackground='blue', width=20, activeforeground='white', command=submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()


def searchstudent():
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+105+140')
    searchroot.resizable(False, False)
    searchroot.config(bg='blue')
    searchroot.title('Student Managment System')

    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%y")
            
        if(id != ''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr, (id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(address != ''):
            strr = 'select * from studentdata where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select * from studentdata where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)


# ---------------------SEARCH STUDENT LABEL

    idlabel = Label(searchroot, text='Enter Id', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                       width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                         width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    datelabel.place(x=10, y=430)

# ------------SEARCH STUDENT ENTERY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'),
                       bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'),
                         bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'),
                     bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

# ================ ADDING BUTTON

    searchbtn = Button(searchroot, text='Search', font=('roman', 15, 'bold'), bd=5,
                       bg='red', activebackground='blue', width=20, activeforeground='white', command=search)
    searchbtn.place(x=150, y=485)

    searchroot.mainloop()


def deletstudent():
    deleting = studenttable.focus()
    content = studenttable.item(deleting)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo(
        'Notification', 'Id {} deleted succesfull...'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def updatestudent():
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x590+105+100')
    updateroot.resizable(False, False)
    updateroot.config(bg='blue')
    updateroot.title('Student Managment System')

    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s, mobile=%s, email=%s,address=%s, gender=%s, dob=%s, date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address,
                         gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo(
            'Notification', 'Id {} Updated succefully'.format(id), parent=updateroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)


# ---------------------ADD STUDENT LABEL

    idlabel = Label(updateroot, text='Enter Id', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                       width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                         width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time', bg='gold2', font=('Times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    timelabel.place(x=10, y=490)

# ------------ADD STUDENT ENTERY
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'),
                       bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'),
                         bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'),
                     bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)

# ================ ADDING BUTTON

    updatebtn = Button(updateroot, text='Update', font=('roman', 15, 'bold'), bd=5,
                       bg='red', activebackground='blue', width=20, activeforeground='white', command=update)
    updatebtn.place(x=150, y=540)

    # UPDATE WORKING

    updating = studenttable.focus()
    content = studenttable.item(updating)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()


def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def exportstudent():
    ff=filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content=studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),
        addeddate.append(pp[7]),addedtime.append(pp[8])
    dd=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Addedtime','Addeddate']
    df=pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths=r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','Student Data is Saved {}'.format(paths))



def exitstudent():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit')
    if(res == True):
        root.destroy()


# MAIN WINDOW

root = Tk()
root.title('Student Managment System')
root.config(bg='gold')
root.geometry('1174x700+80+0')

# Frame

# DATA ENTRY FRAME
DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=600)


frontlabel = Label(DataEntryFrame, text='****** Welcome ******',
                   width=30, font=('Helvetica', 22, 'bold'), bg='gold2')
frontlabel.pack(side=TOP, expand=True)

addbutton = Button(DataEntryFrame, text='1. Add Student', width=25, font=('Helvetica', 20, 'bold'),
                   bd=5, bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=addstudent)
addbutton.pack(side=TOP, expand=True)

searchbutton = Button(DataEntryFrame, text='2. Search Student', width=25, font=('Helvetica', 20, 'bold'),
                      bd=5, bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=searchstudent)
searchbutton.pack(side=TOP, expand=True)

deletbutton = Button(DataEntryFrame, text='3. Delet Student', width=25, font=('Helvetica', 20, 'bold'),
                     bd=5, bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=deletstudent)
deletbutton.pack(side=TOP, expand=True)

updatebutton = Button(DataEntryFrame, text='4. Update Student', width=25, font=('Helvetica', 20, 'bold'),
                      bd=5, bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=updatestudent)
updatebutton.pack(side=TOP, expand=True)

showallbutton = Button(DataEntryFrame, text='5. Show All', width=25, font=('Helvetica', 20, 'bold'),
                       bd=5, bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=showstudent)
showallbutton.pack(side=TOP, expand=True)

exportbutton = Button(DataEntryFrame, text='6. Export Data', width=25, font=('Helvetica', 20, 'bold'),
                      bd=5, bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=exportstudent)
exportbutton.pack(side=TOP, expand=True)

exitbutton = Button(DataEntryFrame, text='7. Exit', width=25, font=('Helvetica', 20, 'bold'),
                    bd=5, bg='skyblue3', activebackground='blue', relief=RIDGE, activeforeground='white', command=exitstudent)
exitbutton.pack(side=TOP, expand=True)

#############################################################################
############################################                     ########################################################
##########################################################                ############################################
###=========================================   SHOW ENTRY FRAME END  ==================================================== ###

ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620, height=600)

#############################################################################################
style = ttk.Style()
style.configure('Treeview.Heading', font=(
    'Times', 20, 'bold'), foreground='blue')
style.configure('Treeview', font=(
    'Times', 15, 'bold'), foreground='blue', background='cyan')

scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)


studenttable = Treeview(ShowDataFrame, columns=(
    'Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=X)

scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('Id', text='Id')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile No', text='Mobile No')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')

studenttable['show'] = 'headings'

studenttable.column('Id', width=100)
studenttable.column('Name', width=250)
studenttable.column('Mobile No', width=200)
studenttable.column('Email', width=300)
studenttable.column('Address', width=300)
studenttable.column('Gender', width=100)
studenttable.column('D.O.B', width=150)
studenttable.column('Added Date', width=150)
studenttable.column('Added Time', width=150)


studenttable.pack(fill=BOTH, expand=1)


ss = 'Student Managment System'

SliderLael1 = Label(root, text=ss, font=(
    'Helvetica', 30, 'italic bold'), relief=RIDGE, borderwidth=4, width=26, bg='#65ebc0')
SliderLael1.place(x=205, y=0)

Clock = Label(root, font=('Times', 14, 'bold'), relief=RIDGE,
              borderwidth=4, bg='lawn green')
Clock.place(x=10, y=0)
tick()
connectbutton = Button(root, text='Connect To Database', font=(
    'Helvetica', 19, 'bold'), relief=RIDGE, borderwidth=4, bd='6', activebackground='blue', bg='lawn green', command=connectdb)
connectbutton.place(x=880, y=0)


root.mainloop()
