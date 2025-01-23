# FOREGIN KEY, triger , cascade

import sqlite3

def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student(usn TEXT PRIMARY KEY,
        name TEXT,
        mobileno TEXT,
        address TEXT,
        email TEXT)""")
    con.commit()
    con.close()
studentData()
def addstdrec(usn,name,mobileno,address,email):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    # print("testtttt========",type(usn),type(name),type(mobileno),type(address),type(email))
    cur.execute("""INSERT INTO student VALUES (:usn,:name,:mobileno,:address,:email)""",{'usn':usn,'name':name,'mobileno':mobileno,'address':address,'email':email})
    # print("000000000000000000000000000")
    con.commit()
    con.close()

def viewdatastud():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close()
    return rows
# addstdrec("1CR18CS","harsh","875814979","india","a@b.com")
# print(viewdatastud(),"------------------")

def deletestdrec(usn):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""PRAGMA foreign_keys = ON""")
    con.commit()
    cur.execute("DELETE FROM student WHERE usn=:usn",{'usn':usn})
    con.commit()
    con.close()


def updatestddata(usn,name,mobileno,address,email):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE student SET name=:name,mobileno=:mobileno,address=:address,email=:email WHERE usn=:usn",{'name':name,'mobileno':mobileno,'address':address,'email':email,'usn' : usn})
    con.commit()
    con.close()


# print(viewdatastud())
def moderatordata():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS moderator(usr TEXT PRIMARY KEY,
        namem TEXT,
        password TEXT,
        emailm TEXT,
        contactno TEXT)""")
    con.commit()
    con.close()

moderatordata()

def addmoderator(idm,namem,password,emailm,contactno):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO moderator VALUES (:usr,:namem,:password,:emailm,:contactno)""",{'usr':idm,'namem':namem,'password':password,'emailm':emailm,'contactno':contactno})
    con.commit()
    con.close()

# addmoderator(69,"harsh","hd","fk@gmail.com",111)
# addmoderator(2,"gsgg","kl","fs@gmail.com",21)

def viewmoderator():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM moderator")
    rows=cur.fetchall()
    con.close()
    return rows

# print(viewmoderator())
def deleterecmoderator(idm):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM moderator WHERE usr=:idm",{'idm':idm})
     con.commit()
     con.close()



def updaterecmoderator(idm,namem,password,emailm,contactno):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("UPDATE moderator SET namem=:namem,password=:password,emailm=:emailm,contactno=:contactno WHERE idm=:idm",{'namem':namem,'password':password,'emailm':emailm,'contactno':contactno,'idm':idm})
     con.commit()
     con.close()

# print(viewmoderator())

#add student registration
def studentdata():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS stude(usr TEXT PRIMARY KEY,
        namem TEXT,
        password TEXT,
        contactno TEXT)""")
    con.commit()
    con.close()

studentdata()

#add stsudentreg

def addstudent(idm,namem,password,contactno):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO stude VALUES (:usr,:namem,:password,:contactno)""",{'usr':idm,'namem':namem,'password':password,'contactno':contactno})
    con.commit()
    con.close()
    
def view_student():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM stude")
    rows=cur.fetchall()
    con.close()
    return rows


def deleterecstudent(idm):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM stude WHERE usr=:idm",{'idm':idm})
     con.commit()
     con.close()
def feedata():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    con.execute("""PRAGMA foreign_keys = ON""")
    cur.execute("""CREATE TABLE IF NOT EXISTS fee(usn TEXT,
    amount TEXT,
    status TEXT,
    payment_date TEXT,
    penalty TEXT,
    foreign key (usn) references student(usn) ON DELETE CASCADE)""")
    con.commit()
    con.close()

feedata()
def addfeedetails(usn,amount,status,payment_date,penalty):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute(""" INSERT INTO fee VALUES(:usn,:amount,:status,:payment_date,:penalty) """, {'usn':usn,'amount':amount,'status':status,'payment_date':payment_date,'penalty':penalty} )
     con.commit()
     con.close()
# addfeedetails("1CR18CS","50000","PAID","25-JULY","NHI LAGI")
def viewfeedetails():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("SELECT * FROM fee")
     rows=cur.fetchall()
     con.close()
     return rows
# print(viewfeedetails())


def deletefeerec(usn):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM fee WHERE usn=:usn",{'usn':usn})
     con.commit()
     con.close()

 
def updatefeerec(usn,amount,status,date,penalty):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM fee WHERE usn=:usn",{'usn':usn})
     con.commit()
     con.close()
     addfeedetails(usn,amount,status,date,penalty)

     #cur.execute("UPDATE fee SET amount=:amount,status=:status,date=:date,penalty=:penalty WHERE usn=:usn",{'amount':amount,'status':status,'date':date,'penalty':penalty,'usn':usn})
     


def subjectdata():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     con.execute("""PRAGMA foreign_keys = ON""")
     cur.execute("""CREATE TABLE IF NOT EXISTS subject(usn TEXT PRIMARY KEY,
     sub1 INTEGER,
     sub2 INTEGER,
     sub3INTEGER,
     backlogs INTEGER,
     sub4 INTEGER,
     sub5 INTEGER,
     sub6 INTEGER,
     foreign key (usn) references student(usn) ON DELETE CASCADE)""")
     con.commit()
     con.close()

subjectdata()
def addsubject(usn,sub1,sub2,sub3,backlogs,sub4,sub5,sub6):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("""INSERT INTO subject VALUES (:usn,:sub1,:sub2,:sub3,:backlogs,:sub4,:sub5,:sub6)""",{'usn':usn,'sub1':sub1,'sub2':sub2,'sub3':sub3,'backlogs':backlogs,'sub4':sub4,'sub5':sub5,'sub6':sub6})
     con.commit()
     con.close()

def viewsubject():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("SELECT * FROM subject")
     rows=cur.fetchall()
     con.close()
     return rows

      

def deletesubjectrec(usn):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM subject WHERE usn=:usn",{'usn':usn})
     con.commit()
     con.close()


def updaterecsubject(usn,sub1,sub2,sub3,backlogs,sub4,sub5,sub6):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("DELETE FROM subject WHERE usn=:usn",{'usn':usn})
     con.commit()
     con.close()
     addsubject(usn,sub1,sub2,sub3,backlogs,sub4,sub5,sub6)
     



def performancedata():
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     cur.execute("""PRAGMA foreign_keys = ON""")
     cur.execute("""CREATE TABLE IF NOT EXISTS performance(usn TEXT PRIMARY KEY,
     iat1 INTEGER,
     iat2 INTEGER,
     AVG INTEGER,
     external INTEGER,
     total INTEGER,
     foreign key (usn) references student(usn) ON DELETE CASCADE)""")
     con.commit()
     con.close()
performancedata()

def trigger():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""CREATE TRIGGER IF NOT EXISTS calculate AFTER INSERT ON performance
        BEGIN
        UPDATE performance
        set AVG=(new.iat1+new.iat2)/2 where new.usn=usn;
        UPDATE performance
        set total=(new.AVG/2)+new.external where new.usn=usn;
        -- where usn=new.usn
        END""")
    con.commit()
    con.close()


trigger()
def addmark(usn,iat1,iat2,ex,avg,total):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO performance VALUES(:usn,:iat1,:iat2,:AVG,:external,:total)""",{'usn':usn,'iat1':iat1,'iat2':iat2,'external':ex,'AVG':avg,'total':total})
    con.commit()
    con.close()

def check_marks():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM performance")
    rows=cur.fetchall()
    con.close()
    return rows

def updatemark(usn,iat1,iat2,ex,avg,total):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM performance WHERE usn=:usn",{'usn':usn})
    con.commit()
    con.close()
    addmark(usn,iat1,iat2,ex,avg,total)

def deletemark(usn):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM performance WHERE usn=:usn",{'usn':usn})
    con.commit()
    con.close()
