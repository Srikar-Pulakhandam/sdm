from tkinter import *
from tkinter import ttk
from tabulate import *
from datetime import datetime
td= datetime.now()
ts=td.strftime('''Date : %d/%m/%Y \nTime : %H:%M:%S''')
f=open(r"D:\SDBMS V2\Secure_Text.txt",'a')
f.write('\n')
f.write("Started SDBMS v2.0 beta \n")
f.write(ts)
f.flush()


rootlog=Tk()

rootlog.configure(bg='#2B2B2B')
rootlog.geometry("+1020+50")
rootlog.title("SDBMS v2.0  ACTIVITY LOG")
lb1=Label(rootlog,text="CHANGES TO THE DATABASE ARE SHOWN HERE",bg='#2B2B2B',fg='white',font=('Times New Roman',15))
lb1.grid(padx=15,pady=5)

rootp=Tk()
rootp.iconbitmap(r'D:\project_media\sdicon.ico')
rootp.configure(bg='#2B2B2B')
rootp.geometry('+590+50')
rootp.title("SDBMS v2.0  LOGIN")
psvar=StringVar()
usvar=StringVar()
avar=StringVar()
nvar=StringVar()
dvar=StringVar()
fvar=StringVar()
namevar=StringVar()
mvar=StringVar()
pvar=StringVar()
dbvar=StringVar()
gvar=StringVar()
davar=StringVar()
dnvar=StringVar()
clvvar=StringVar()

getps="phoenix"
getus=""
geta=""
getp=""
getdb=""
getn=""
getc=""
getd=""
getf=""
getm=""
getg=""
getgenrb=""
delname=""
delad=""
g=""
adm=""


def done():
    global f
    global getps
    global getus
    global rootlog
    getus=(usentry.get().upper())
    getus='Dev_Admin'
    if getus=="":
        erc=Label(rootp,text="Enter Your Name To Proceed",font=('Times',15),fg='red',bg='white')
        erc.grid(padx=10,pady=5)
    else:
        
        if getps!="phoenix":
            
            getps=(psentry.get())
        import mysql.connector as p
        con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
        if con.is_connected():
            cflabel=Label(rootlog,text="SUCCESSFULLY CONNECTED TO THE SQL DATABASE",bg='#2B2B2B',fg='white',font=('Times New Roman',10))
            cflabel.grid(padx=15,pady=5)
            welabel=Label(rootlog,text="HI  "+getus+" !!  WELCOME TO SDBMS v2.0",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
            welabel.grid(padx=15,pady=5)
            f.write('\n')
            f.write("USER :  "+getus)
            f.flush()
            rootp.destroy()

            def run():
                global f
                global getus
                global rootlog   
                import mysql.connector as p
                con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                c=con.cursor()
                c.execute('insert into student(Admn_No,Name,Class,DOB,Father,Mother,Gender,Mobile)VALUES("{}","{}",{},"{}","{}","{}","{}",{})'.format(adm,getn,getc,getd,getf,getm,getgenrb,getp))
                con.commit()
                c.close()
                lb2=Label(rootlog,text=getus+" :  STUDENT  -  "+getn+"'S  ADMISSION SUCCESSFUL",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                lb2.grid(padx=10,pady=10)
                f.write('\n')
                f.write(getus+" :  STUDENT  -  "+getn+"'S  ADMISSION SUCCESSFUL")
                f.flush()

                
            def add():
                global adm
                import mysql.connector as p
                con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                c=con.cursor()
                c.execute('select max(Admn_No) from student')
                s=c.fetchall()
                f=s[0]
                q=f[0]
                s=int(q)
                no=q+1
                adm=str(no)
                # here q is the last admisssion number of the database
                roots=Tk()
                roots.iconbitmap(r'D:\project_media\sdicon.ico')
                roots.configure(bg='#2B2B2B')
                roots.geometry('+100+50')
                roots.title("SDBMS v2.0 : ADMISSION FORM")


                global genrb
                genrb=StringVar(roots)
                alabel=Label(roots,text="4 DIGIT ADMISSION NO.",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                alabel.grid(padx=50,pady=5)
                admnno=Label(roots,text=adm,font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                admnno.grid(padx=50,pady=5)
                slabel=Label(roots,text="ENTER STUDENT'S NAME",bg='#2B2B2B',fg='white',font=('Times New Roman',10))
                slabel.grid(padx=50,pady=5)
                student=Entry(roots,width=50,textvariable=nvar,fg="#2B2B2B",bg="pink")
                student.grid(padx=50,pady=5)
                clabel=Label(roots,text="ENTER THE CLASS OF ADMISSION",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                clabel.grid(padx=50,pady=5)
                centry=Entry(roots,width=10,textvariable=namevar,fg="#2B2B2B",bg="pink")
                centry.grid(padx=50,pady=5)
                dlabel=Label(roots,text="DATE OF BIRTH (YYYY-MM-DD)",bg='#2B2B2B',fg='white',font=('Times New Roman',10))
                dlabel.grid(padx=50,pady=5)
                dentry=Entry(roots,width=10,textvariable=dvar,fg="#2B2B2B",bg="pink")
                dentry.grid(padx=50,pady=5)
                flabel=Label(roots,text="ENTER FATHER'S NAME",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                flabel.grid(padx=50,pady=5)
                fentry=Entry(roots,width=50,textvariable=fvar,fg="#2B2B2B",bg="pink")
                fentry.grid(padx=50,pady=5)
                mlabel=Label(roots,text="ENTER MOTHER'S NAME",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                mlabel.grid(padx=50,pady=5)
                mentry=Entry(roots,width=50,textvariable=mvar,fg="#2B2B2B",bg="pink")
                mentry.grid(padx=50,pady=5)
                glabel=Label(roots,text="Choose Gender",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                glabel.grid(padx=50,pady=5)
                malerb=Radiobutton(roots,text="Male",height=1,width=20,variable=genrb,indicatoron=0,value="M",font=('Times New Roman',15),bg='#2B2B2B',fg='pink')
                malerb.grid(padx=50,pady=5)
                femalerb=Radiobutton(roots,text="Female",height=1,width=20,variable=genrb,indicatoron=0,value="F",font=('Times New Roman',15),bg='#2B2B2B',fg='pink')
                femalerb.grid(padx=50,pady=5)
                plabel=Label(roots,text="ENTER MOBILE NUMBER",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                plabel.grid(padx=50,pady=5)
                pentry=Entry(roots,width=30,textvariable=pvar,fg="#2B2B2B",bg="pink")
                pentry.grid(padx=50,pady=5)
                def getdetails():
                    global getn
                    global getc
                    global getd
                    global getf
                    global getm
                    global getg
                    global getp
                    global geta
                    global getgenrb
                    
                    getn=(student.get().upper())
                    c=centry.get()
                    getc=int((c))
                    getd=(dentry.get().upper())
                    getf=(fentry.get().upper())
                    getm=(mentry.get().upper())
                    getgenrb=(genrb.get().upper())
                    p=pentry.get()
                    getp=int(p)
                    run()
                    roots.destroy()
                submit=Button(roots,text="SUBMIT",command=getdetails,fg="white",bg="grey",font=('Times New Roman',15))
                submit.grid(padx=100,pady=20)
                roots.mainloop()

                
            def delete():
                rootd=Tk()
                rootd.iconbitmap(r'D:\project_media\sdicon.ico')
                rootd.configure(bg='#2B2B2B')
                rootd.title("SDBMS v2.0 : REMOVE STUDENT")
                rootd.geometry("400x250+100+50")
                
                def deletes():
                        global getus
                        global rootlog
                        global delad
                        adm=dela.get()
                        delad=int(adm)
                        nam=(deln.get().upper())
                        import mysql.connector as p
                        con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                        c=con.cursor()
                        delstatement='delete from student where Admn_No = {}'.format(delad)
                        c.execute(delstatement)
                        con.commit()
                        rootd.destroy()
                        lb3=Label(rootlog,text=getus+" :  STUDENT  "+nam+"  DELETED SUCCESSFULLY",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                        lb3.grid(padx=10,pady=10)
                        f.write('\n')
                        f.write(getus+" :  STUDENT  "+nam+"  DELETED SUCCESSFULLY")
                        f.flush()
                    
                global delname
                global delad
                delan=Label(rootd,text="ENTER ADMISSION NUMBER",font=('Times New Roman',20),bg='#2B2B2B',fg='white')
                delan.place(relx=0.5,rely=0.15,anchor=CENTER)
                dela=Entry(rootd,width=10,textvariable=davar,fg="#2B2B2B",bg="pink")
                dela.place(relx=0.5,rely=0.30,anchor=CENTER)
                delnn=Label(rootd,text="ENTER NAME",font=('Times New Roman',20),bg='#2B2B2B',fg='white')
                delnn.place(relx=0.5,rely=0.50,anchor=CENTER)
                deln=Entry(rootd,width=30,textvariable=dnvar,fg="#2B2B2B",bg="pink")
                deln.place(relx=0.5,rely=0.65,anchor=CENTER)
                delname=deln.get()
                delete=Button(rootd,text="CONFIRM & DELETE",command=deletes,fg="white",bg="grey",font=('Times New Roman',17))
                delete.place(relx=0.5,rely=0.80,anchor=CENTER)
                rootd.mainloop()

                
            def viewdetails():
                rootv=Tk()
                rootv.iconbitmap(r'D:\project_media\sdicon.ico')
                rootv.configure(bg='#2B2B2B')
                rootv.geometry("400x250+100+50")
                rootv.title("SDBMS v2.0 : VIEW STUDENT RECORDS")
                
                def getsin():
                    rootsi=Tk()
                    rootsi.iconbitmap(r'D:\project_media\sdicon.ico')
                    rootsi.configure(bg='#2B2B2B')
                    rootsi.geometry("400x150+545+275")
                    rootsi.title("SDBMS v2.0 : VIEW STUDENTS BY CLASS")
                    
                    aenvar=StringVar()
                    def submit():
                        global getus
                        global rootlog
                        import mysql.connector as p
                        con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                        c=con.cursor()
                        r=aen.get()
                        txt='select * from student where Admn_No = '+r
                        c.execute(txt)
                        x=c.fetchall()
                        print(tabulate(x))
                        lb4=Label(rootlog,text=getus+" :  VIEWED  "+r+"'S  DETAILS",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                        lb4.grid(padx=10,pady=10)
                        f.write('\n')
                        f.write(getus+" :  VIEWED  "+r+"'S  DETAILS")
                        f.flush()
                        rootsi.destroy()
                    sl=Label(rootsi,text="ENTER ADMISSION NUMBER",font=('Times New Roman',20),bg='#2B2B2B',fg='white')
                    sl.place(relx=0.5,rely=0.25,anchor=CENTER)
                    aen=Entry(rootsi,width=20,textvariable=aenvar,fg="#2B2B2B",bg="pink")
                    aen.place(relx=0.5,rely=0.50,anchor=CENTER)
                    submit=Button(rootsi,text="VIEW RECORD",command=submit,fg="white",bg="grey",font=('Times New Roman',15))
                    submit.place(relx=0.5,rely=0.80,anchor=CENTER)
                    rootv.destroy()
                    rootsi.mainloop()
                def getall():
                    global getus
                    global rootlog
                    import mysql.connector as p
                    con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                    c=con.cursor()
                    c.execute('select * from student')
                    r=c.fetchall()
                    print(tabulate(r))
                    lb5=Label(rootlog,text=getus+" :  VIEWED FULL STUDENT DATABASE",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    lb5.grid(padx=10,pady=10)
                    f.write('\n')
                    f.write(getus+" :  VIEWED FULL STUDENT DATABASE")
                    f.flush()
                    rootv.destroy()
                def getcla():
                    rootc=Tk()
                    rootc.iconbitmap(r'D:\project_media\sdicon.ico')
                    rootc.configure(bg='#2B2B2B')
                    rootc.geometry("300x150+595+275")
                    rootc.title("SDBMS v2.0 : VIEW STUDENTS BY CLASS")
                    
                    def submit():
                        global getus
                        global rootlog
                        import mysql.connector as p
                        con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                        c=con.cursor()
                        r=clltb.get()
                        txt='select * from student where class = '+r
                        c.execute(txt)
                        x=c.fetchall()
                        print(tabulate(x))
                        lb6=Label(rootlog,text=getus+" :  VIEWED CLASS  "+r+"  DATABASE",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                        lb6.grid(padx=10,pady=10)
                        f.write('\n')
                        f.write(getus+" :  VIEWED CLASS  "+r+"  DATABASE")
                        f.flush()
                        rootc.destroy()
                    clla=Label(rootc,text="ENTER THE CLASS",font=('Times New Roman',25),bg='#2B2B2B',fg='white')
                    clla.place(relx=0.5,rely=0.20,anchor=CENTER)
                    clltb=Entry(rootc,width=10,textvariable=clvvar,fg="#2B2B2B",bg="pink")
                    clltb.place(relx=0.5,rely=0.48,anchor=CENTER)
                    submit=Button(rootc,text="VIEW RECORDS",command=submit,fg="white",bg="grey",font=('Times New Roman',15))
                    submit.place(relx=0.5,rely=0.80,anchor=CENTER)
                    rootv.destroy()
                    rootc.mainloop()
                def getgen():
                    rootg=Tk()
                    rootg.iconbitmap(r'D:\project_media\sdicon.ico')
                    rootg.configure(bg='#2B2B2B')
                    rootg.geometry("300x200+595+275")
                    rootg.title("SDBMS v2.0 : VIEW STUDENTS BY GENDER")
                    
                    def gens():
                        global getus
                        global rootlog
                        import mysql.connector as p
                        con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                        c=con.cursor()
                        global g
                        gchoice=choosegender.get()
                        if gchoice=="GIRLS":
                            g="F"  
                            txt='select * from student where Gender= "F"'
                            c.execute(txt)
                            x=c.fetchall()
                            print(tabulate(x))
                            lb7=Label(rootlog,text=getus+" :  VIEWED FEMALE STUDENT DATABASE",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                            lb7.grid(padx=10,pady=10)
                            f.write('\n')
                            f.write(getus+" :  VIEWED FEMALE STUDENT DATABASE")
                            f.flush()
                            rootg.destroy()
                        elif gchoice=="BOYS":
                            g="M"  
                            txt='select * from student where Gender= "M"'
                            c.execute(txt)
                            x=c.fetchall()
                            print(tabulate(x))
                            lb8=Label(rootlog,text=getus+" :  VIEWED MALE STUDENT DATABASE",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                            lb8.grid(padx=10,pady=10)
                            f.write('\n')
                            f.write(getus+" :  VIEWED MALE STUDENT DATABASE")
                            f.flush()
                            rootg.destroy()
                    ch=Label(rootg,text="CHOOSE GENDER",font=('Times New Roman',20),bg='#2B2B2B',fg='white')
                    ch.place(relx=0.50,rely=0.20,anchor=CENTER)
                    gender=["GIRLS","BOYS"]
                    choosegender=ttk.Combobox(rootg,values=gender)
                    choosegender.place(relx=0.50,rely=0.45,anchor=CENTER)
                    s=Button(rootg,text="VIEW RECORDS",command=gens,fg="white",bg="grey",font=('Times New Roman',15))
                    s.place(relx=0.50,rely=0.70,anchor=CENTER)
                    rootv.destroy()
                    rootg.mainloop()
                sinb=Button(rootv,text="VIEW SINGLE RECORD",command=getsin,fg="white",bg="grey",font=('Times New Roman',15))
                sinb.place(relx=0.5,rely=0.20,anchor=CENTER)
                allb=Button(rootv,text="VIEW ALL RECORDS",command=getall,fg="white",bg="grey",font=('Times New Roman',15))
                allb.place(relx=0.5,rely=0.40,anchor=CENTER)
                classb=Button(rootv,text="VIEW RECORDS BY CLASS",command=getcla,fg="white",bg="grey",font=('Times New Roman',15))
                classb.place(relx=0.5,rely=0.60,anchor=CENTER)
                genb=Button(rootv,text="VIEW RECORDS BY GENDER",command=getgen,fg="white",bg="grey",font=('Times New Roman',15))
                genb.place(relx=0.5,rely=0.80,anchor=CENTER)
                rootv.mainloop()

                
            def update():
                rootu=Tk()
                rootu.iconbitmap(r'D:\project_media\sdicon.ico')
                rootu.configure(bg='#2B2B2B')
                rootu.geometry("350x220+150+50")
                rootu.title("SDBMS v2.0 : UPDATE MANAGER")
                
                def updatesclass():
                    global getus
                    global rootlog
                    global getn
                    import mysql.connector as p
                    con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                    c=con.cursor()
                    global geta
                    global getc
                    c.execute('update student set Class = {} where Admn_No = {}'.format(getc,geta))
                    con.commit()
                    lb10=Label(rootlog,text=getus+" :  UPDATED  "+getn+"'S  CLASS",font=('Times New Roman',10),fg="white",bg="#2B2B2B")
                    lb10.grid(padx=10,pady=10)
                    f.write('\n')
                    f.write(getus+" :  UPDATED  "+getn+"'S  CLASS")
                    f.flush()
                def updatesmob():
                    global getus
                    global rootlog
                    global getn
                    import mysql.connector as p
                    con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                    c=con.cursor()
                    global geta
                    global getp
                    c.execute('update student set Mobile = {} where Admn_No = {}'.format(getp,geta))
                    con.commit()
                    lb11=Label(rootlog,text=getus+" :  UPDATED  "+getn+"'S  MOBILE NUMBER",font=("Times New Roman",10),fg="white",bg="#2B2B2B")
                    lb11.grid(padx=10,pady=10)
                    f.write('\n')
                    f.write(getus+" :  UPDATED  "+getn+"'S  MOBILE NUMBER")
                    f.flush()
                def updatesdb():
                    global getus
                    global rootlog
                    global getn
                    import mysql.connector as p
                    con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                    c=con.cursor()
                    global geta
                    global getdb
                    c.execute('update student set DOB = "{}" where Admn_No = {}'.format(getdb,geta))
                    con.commit()
                    lb11=Label(rootlog,text=getus+" :  UPDATED  "+getn+"'S  DATE OF BIRTH",font=("Times New Roman",10),fg="white",bg="#2B2B2B")
                    lb11.grid(padx=10,pady=10)
                    f.write('\n')
                    f.write(getus+" :  UPDATED  "+getn+"'S  DATE OF BIRTH")
                    f.flush()    
                def updatesall():
                    global getus
                    global rootlog
                    import mysql.connector as p
                    con=p.connect(host="localhost",user="root",passwd=getps,database="sdbms")
                    c=con.cursor()
                    global getn
                    global getc                     #Admn_No,Name,Class,DOB,Father,Mother,Gender,Mobile
                    global getd
                    global getf
                    global getm
                    global getg
                    global getgenrb
                    global getp
                    global geta
                    c.execute('update student set Admn_No = {}, Name = "{}", Class = {}, DOB = "{}", Father = "{}", Mother = "{}", Gender = "{}", Mobile = {} where Admn_No = {}'.format(geta,getn,getc,getd,getf,getm,getgenrb,getp,geta))
                    con.commit()
                    lb9=Label(rootlog,text=getus+' :  UPDATED  '+getn+"'S  DETAILS",font=('Times New Roman',10),fg='white',bg='#2B2B2B')
                    lb9.grid(padx=10,pady=10)
                    f.write('\n')
                    f.write(getus+' :  UPDATED  '+getn+"'S  DETAILS")
                    f.flush()
                def updateclass():
                    roots=Tk()
                    roots.iconbitmap(r'D:\project_media\sdicon.ico')
                    roots.configure(bg='#2B2B2B')
                    roots.geometry('+100+50')
                    roots.title("SDBMS v2.0 : UPDATE STUDENT'S CLASS")
                    
                    alabel=Label(roots,text="4 DIGIT ADMISSION NO.",font=('Times New Roman',15),bg='#2B2B2B',fg='white')
                    alabel.grid(padx=50,pady=5)
                    admnno=Entry(roots,width=8,textvariable=avar,fg="#2B2B2B",bg="pink")
                    admnno.grid(padx=50,pady=5)
                    slabel=Label(roots,text="ENTER STUDENT'S NAME",font=('Times New Roman',15),bg='#2B2B2B',fg='white')
                    slabel.grid(padx=50,pady=5)
                    student=Entry(roots,width=50,textvariable=nvar,fg="#2B2B2B",bg="pink")
                    student.grid(padx=50,pady=5)
                    clabel=Label(roots,text="ENTER NEW CLASS",font=('Times New Roman',15),bg='#2B2B2B',fg='white')
                    clabel.grid(padx=50,pady=5)
                    centry=Entry(roots,width=10,textvariable=namevar,fg="#2B2B2B",bg="pink")
                    centry.grid(padx=50,pady=5)
                    def get_class():
                        global getn
                        global getc
                        global geta
                        a=admnno.get()
                        geta=int(a)
                        getn=(student.get().upper())
                        c=centry.get()
                        getc=int((c))
                        updatesclass()
                        roots.destroy()
                    submit=Button(roots,text="UPDATE",command=get_class,fg="white",bg="grey",font=('Times New Roman',15))
                    submit.grid(padx=100,pady=20)
                    rootu.destroy()
                    roots.mainloop()
                def updatemobile():
                    rootm=Tk()
                    rootm.iconbitmap(r'D:\project_media\sdicon.ico')
                    rootm.configure(bg='#2B2B2B')
                    rootm.geometry('+100+50')
                    rootm.title("SDBMS v2.0 : UPDATE MOBILE NUMBER")
                    
                    alabel=Label(rootm,text="4 DIGIT ADMISSION NO.",font=('Times New Roman',15),bg='#2B2B2B',fg='white')
                    alabel.grid(padx=50,pady=5)
                    admnno=Entry(rootm,width=8,textvariable=avar,fg="#2B2B2B",bg="pink")
                    admnno.grid(padx=50,pady=5)
                    slabel=Label(rootm,text="ENTER STUDENT'S NAME",font=('Times New Roman',15),bg='#2B2B2B',fg='white')
                    slabel.grid(padx=50,pady=5)
                    student=Entry(rootm,width=50,textvariable=nvar,fg="#2B2B2B",bg="pink")
                    student.grid(padx=50,pady=5)
                    plabel=Label(rootm,text="ENTER NEW MOBILE NUMBER",font=('Times New Roman',15),bg='#2B2B2B',fg='white')
                    plabel.grid(padx=50,pady=5)
                    pentry=Entry(rootm,width=30,textvariable=pvar,fg="#2B2B2B",bg="pink")
                    pentry.grid(padx=50,pady=5)
                    def get_mobile():
                        global getn
                        global getp
                        global geta
                        a=admnno.get()
                        geta=int(a)
                        getn=(student.get().upper())
                        p=pentry.get()
                        getp=int(p)
                        updatesmob()
                        rootm.destroy()
                    submit=Button(rootm,text="UPDATE",command=get_mobile,fg="white",bg="grey",font=('Times New Roman',15))
                    submit.grid(padx=100,pady=20)
                    rootu.destroy()
                    rootm.mainloop()
                def updatedob():
                    rootdb=Tk()
                    rootdb.iconbitmap(r'D:\project_media\sdicon.ico')
                    rootdb.configure(bg='#2B2B2B')
                    rootdb.geometry('+100+50')
                    rootdb.title("SDBMS v2.0 : CHANGE 'Date Of Birth'")
                    
                    alabel=Label(rootdb,text="4 DIGIT ADMISSION NO.",font=('Times New Roman',15),fg='white',bg='#2B2B2B')
                    alabel.grid(padx=50,pady=5)
                    admnno=Entry(rootdb,width=8,textvariable=avar,fg="#2B2B2B",bg='pink')
                    admnno.grid(padx=50,pady=5)
                    slabel=Label(rootdb,text="ENTER STUDENT'S NAME",font=('Times New Roman',15),fg='white',bg='#2B2B2B')
                    slabel.grid(padx=50,pady=5)
                    student=Entry(rootdb,width=50,textvariable=nvar,fg="#2B2B2B",bg='pink')
                    student.grid(padx=50,pady=5)
                    dblabel=Label(rootdb,text="ENTER DATE OF BIRTH",font=('Times New Roman',15),fg='white',bg='#2B2B2B')
                    dblabel.grid(padx=50,pady=5)
                    dbentry=Entry(rootdb,width=30,textvariable=dbvar,fg="#2B2B2B",bg='pink')
                    dbentry.grid(padx=50,pady=5)
                    def get_dob():
                        global getn
                        global getdb
                        global geta
                        a=admnno.get()
                        geta=int(a)
                        getn=(student.get().upper())
                        getdb=dbentry.get()
                        updatesdb()
                        rootdb.destroy()
                    submit=Button(rootdb,text="UPDATE",command=get_dob,font=('Times New Roman',15),fg="white",bg="grey")
                    submit.grid(padx=100,pady=20)
                    rootu.destroy()
                    rootdb.mainloop()
                    
                def updateall():
                    roota=Tk()
                    roota.iconbitmap(r'D:\project_media\sdicon.ico')
                    roota.configure(bg='#2B2B2B')
                    roota.geometry('+100+50')
                    roota.title("SDBMS v2.0 : UPDATE STUDENT DETAILS")


                    global genrb
                    genrb=StringVar(roota)
                    alabel=Label(roota,text="4 DIGIT ADMISSION NO.",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    alabel.grid(padx=50,pady=5)
                    admnno=Entry(roota,width=8,textvariable=avar,fg="#2B2B2B",bg="pink")
                    admnno.grid(padx=50,pady=5)
                    slabel=Label(roota,text="ENTER STUDENT'S NAME",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    slabel.grid(padx=50,pady=5)
                    student=Entry(roota,width=50,textvariable=nvar,fg="#2B2B2B",bg="pink")
                    student.grid(padx=50,pady=5)
                    clabel=Label(roota,text="ENTER THE CLASS OF ADMISSION",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    clabel.grid(padx=50,pady=5)
                    centry=Entry(roota,width=10,textvariable=namevar,fg="#2B2B2B",bg="pink")
                    centry.grid(padx=50,pady=5)
                    dlabel=Label(roota,text="DATE OF BIRTH (YYYY-MM-DD)",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    dlabel.grid(padx=50,pady=5)
                    dentry=Entry(roota,width=10,textvariable=dvar,fg="#2B2B2B",bg="pink")
                    dentry.grid(padx=50,pady=5)
                    flabel=Label(roota,text="ENTER FATHER'S NAME",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    flabel.grid(padx=50,pady=5)
                    fentry=Entry(roota,width=50,textvariable=fvar,fg="#2B2B2B",bg="pink")
                    fentry.grid(padx=50,pady=5)
                    mlabel=Label(roota,text="ENTER MOTHER'S NAME",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    mlabel.grid(padx=50,pady=5)
                    mentry=Entry(roota,width=50,textvariable=mvar,fg="#2B2B2B",bg="white")
                    mentry.grid(padx=50,pady=5)
                    glabel=Label(roota,text="Choose Gender",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    glabel.grid(padx=50,pady=5)
                    malerb=Radiobutton(roota,text="Male",height=1,width=20,variable=genrb,indicatoron=0,value="M",font=('Times New Roman',15),bg='#2B2B2B',fg='pink')
                    malerb.grid(padx=50,pady=5)
                    femalerb=Radiobutton(roota,text="Female",height=1,width=20,variable=genrb,indicatoron=0,value="F",font=('Times New Roman',15),bg='#2B2B2B',fg='pink')
                    femalerb.grid(padx=50,pady=5)
                    plabel=Label(roota,text="ENTER MOBILE NUMBER",font=('Times New Roman',10),bg='#2B2B2B',fg='white')
                    plabel.grid(padx=50,pady=5)
                    pentry=Entry(roota,width=30,textvariable=pvar,fg="#2B2B2B",bg="pink")
                    pentry.grid(padx=50,pady=5)
                    def get_details():
                        global getn
                        global getc
                        global getd
                        global getf
                        global getm
                        global getg
                        global getp
                        global geta
                        global getgenrb
                        a=admnno.get()
                        geta=int(a)
                        getn=(student.get().upper())
                        c=centry.get()
                        getc=int((c))
                        getd=(dentry.get().upper())
                        getf=(fentry.get().upper())
                        getm=(mentry.get().upper())
                        getgenrb=(genrb.get().upper())
                        p=pentry.get()
                        getp=int(p)
                        updatesall()
                        roota.destroy()
                    submit=Button(roota,text="UPDATE",command=get_details,fg="white",bg="grey",font=('Times New Roman',15))
                    submit.grid(padx=100,pady=20)
                    rootu.destroy()
                    roota.mainloop()
                updall = Button(rootu, text="UPDATE ALL DETAILS", command=updateall, font=('Times New Roman', 15),fg="white", bg="grey")
                updall.place(relx=0.5,rely=0.75, anchor=CENTER)
                updcl = Button(rootu,text="UPDATE CLASS", command=updateclass, font=('Times New Roman', 15),fg="white", bg="grey")
                updcl.place(relx=0.5,rely=0.35, anchor=CENTER)
                updob = Button(rootu,text="CHANGE DATE OF BIRTH",command=updatedob, font=('Times New Roman', 15), fg="white",bg="grey")
                updob.place(relx=0.5, rely=0.15, anchor=CENTER)
                updmbl = Button(rootu,text="CHANGE MOBILE NUMBER", command=updatemobile, font=('Times New Roman', 15),fg="white", bg="grey")
                updmbl.place(relx=0.5,rely=0.55, anchor=CENTER)
                rootu.mainloop()




            root=Tk()
            root.iconbitmap(r'D:\project_media\sdicon.ico')
            root.title("SDBMS v2.0 ")
            root.configure(bg='#2B2B2B')
            root.geometry("+450+50")
            addimg=PhotoImage(file=r'D:\project_media\Add_Dark.png',master=root)
            adds=Button(root,command=add,text="ADD STUDENT",bg="#2B2B2B",borderwidth=5,font=('Times New Roman',15),fg="beige")
            adds.grid(padx=10,pady=10,row=0,column=0)
            delimg=PhotoImage(file=r'D:\project_media\Del_Dark.png',master=root)
            deletes=Button(root,command=delete,text="DELETE STUDENT",bg="#2B2B2B",borderwidth=5,font=('Times New Roman',15),fg="beige")
            deletes.grid(padx=10,pady=10,row=1,column=0)
            vwimg=PhotoImage(file=r'D:\project_media\Vw_Dark.png',master=root)
            views=Button(root,command=viewdetails,text="VIEW DETAILS",bg="#2B2B2B",borderwidth=5,font=('Times New Roman',15),fg="beige")
            views.grid(padx=10,pady=10,row=0,column=2)
            updimg=PhotoImage(file=r'D:\project_media\Upd_Dark.png',master=root)
            updates=Button(root,command=update,text="UPDATE DETAILS",bg="#2B2B2B",borderwidth=5,font=('Times New Roman',15),fg="beige")
            updates.grid(padx=10,pady=15,row=1,column=2)
            #cl=Label(root,text="srikar's ",fg="beige",bg='#2B2B2B',font=('twilight',30))
            #cl.grid(padx=5,pady=5,row=0,column=1)
            cl1=Label(root,text="SDBMS v2.0",fg="beige",bg='#2B2B2B',font=('Times New Roman',20))
            cl1.grid(padx=5,pady=5,row=1,column=1)
            root.mainloop()


pslabel=Label(rootp,text="ENTER SQL PASSWORD",font=('Times New Roman',20),bg='#2B2B2B',fg='white')
pslabel.grid(padx=50,pady=5)
psentry=Entry(rootp,width=40,textvariable=psvar,show='*',fg="#2B2B2B",bg="pink")
psentry.grid(padx=50,pady=5)
uslabel=Label(rootp,text="ENTER YOUR NAME",font=("Times New Roman",15),bg='#2B2B2B',fg='white')
uslabel.grid(padx=50,pady=10)
usentry=Entry(rootp,width=50,textvariable=usvar,fg="#2B2B2B",bg="pink")
usentry.grid(padx=50,pady=5)

sb=Button(rootp,text="SUBMIT",command=done,fg="white",bg="grey",font=('Times New Roman',15))
sb.grid(padx=10,pady=10)
rootp.mainloop()
rootlog.mainloop()
f.close()
