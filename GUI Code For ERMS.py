from tkinter import *


class Empdepartment:
    def __init__(self, root):
        self.root = Tk()
        self.root.title('Account From')
        self.root.config(bg='pink')
        self.root.geometry('1000x700')
        tit = Label(self.root, text="Employee Department form", bg="pink", font=("bold", '18'))
        tit.pack()

        dis_tables = Label(self.root, text="Display Tables", bg="pink", font=("Cambria", '18'))
        dis_tables.place(x=750, y=30)

        F2 = Frame(self.root, bg="#5DE095")
        F2.place(x=720, y=60, width=250, height=400)

        ## middle frame
        F1 = Frame(self.root, bg="#5DE095")
        F1.place(x=380, y=60, width=250, height=400)

        ## right frame
        F2 = Frame(self.root, bg="#5DE095")
        F2.place(x=720, y=60, width=250, height=400)

        attributes = Label(self.root, text="Attributes", bg='pink', font=("Cambria", '20'))
        attributes.place(x=30, y=30)

        # empoyee_id
        emp_id = Label(self.root, text="Employee_id", bg='#1EB5F1', font=("Cambria", '16'))
        emp_id.place(x=20, y=80)
        self.empid_entry = Entry(self.root)
        self.empid_entry.place(x=170, y=85)

        # first_name
        first_name = Label(self.root, text="first_name", bg='#1EB5F1', font=("Cambria", '16'))
        first_name.place(x=20, y=120)
        self.fname_entry = Entry(self.root)
        self.fname_entry.place(x=170, y=125)

        # last_name
        last_name = Label(self.root, text="last_name", bg='#1EB5F1', font=("Cambria", '16'))
        last_name.place(x=20, y=160)
        self.lname_entry = Entry(self.root)
        self.lname_entry.place(x=170, y=165)

        # email_address
        email_adds = Label(self.root, text="email_address", bg='#1EB5F1', font=("Cambria", '16'))
        email_adds.place(x=20, y=200)
        self.email_entry = Entry(self.root)
        self.email_entry.place(x=170, y=205)

        # project_id
        pro_id = Label(self.root, text="project_id", bg='#1EB5F1', font=("Cambria", '16'))
        pro_id.place(x=20, y=240)
        self.proid_entry = Entry(self.root)
        self.proid_entry.place(x=170, y=245)

        # hours_worked
        hours_worked = Label(self.root, text="hours_worked", bg='#1EB5F1', font=("Cambria", '16'))
        hours_worked.place(x=20, y=280)
        self.hrs_entry = Entry(self.root)
        self.hrs_entry.place(x=170, y=285)

        # role
        role = Label(self.root, text="role", bg='#1EB5F1', font=("Cambria", '16'))
        role.place(x=20, y=320)
        self.role_entry = Entry(self.root)
        self.role_entry.place(x=170, y=325)

        # project_name
        pro_name = Label(self.root, text="project_name", bg='#1EB5F1', font=("Cambria", '16'))
        pro_name.place(x=20, y=360)
        self.proname_entry = Entry(self.root)
        self.proname_entry.place(x=170, y=365)

        # start_date
        start_dt = Label(self.root, text="start_date", bg='#1EB5F1', font=("Cambria", '16'))
        start_dt.place(x=20, y=400)
        self.start_entry = Entry(self.root)
        self.start_entry.place(x=170, y=405)

        # end_date
        end_dt = Label(self.root, text="end_date", bg='#1EB5F1', font=("Cambria", '16'))
        end_dt.place(x=20, y=440)
        self.end_entry = Entry(self.root)
        self.end_entry.place(x=170, y=445)

        # department_id
        dept_id = Label(self.root, text="department_id", bg='#1EB5F1', font=("Cambria", '16'))
        dept_id.place(x=20, y=480)
        self.deptid_entry = Entry(self.root)
        self.deptid_entry.place(x=200, y=485)

        # department_name
        dept_name = Label(self.root, text="department_name", bg='#1EB5F1', font=("Cambria", '16'))
        dept_name.place(x=20, y=520)
        self.deptname_entry = Entry(self.root)
        self.deptname_entry.place(x=200, y=525)

        # manager_id
        manager_id = Label(self.root, text="manager_id", bg='#1EB5F1', font=("Cambria", '16'))
        manager_id.place(x=20, y=560)
        self.mgr_entry = Entry(self.root)
        self.mgr_entry.place(x=170, y=565)

        # location
        location_id = Label(self.root, text="location", bg='#1EB5F1', font=("Cambria", '16'))
        location_id.place(x=20, y=600)
        self.loc_entry = Entry(self.root)
        self.loc_entry.place(x=170, y=605)

        insert_buton = Button(self.root, text="INSERT", bg="red", font=("bold italic", '12'), height=2, width=7,
                              command=self.insert)
        insert_buton.place(x=480, y=90)

        update_button = Button(self.root, text="UPDATE", bg="red", font=("bold italic", '12'), height=2, width=10,
                               command=self.update)
        update_button.place(x=480, y=180)

        retrieve_button = Button(self.root, text="RETRIEVE", bg="red", font=("bold italic", '12'), height=2, width=10,
                                 command=self.retrieve)
        retrieve_button.place(x=475, y=270)

        delete_button = Button(self.root, text="DELETE", bg="red", font=("bold italic", '12'), height=2, width=10,
                               command=self.delete)
        delete_button.place(x=480, y=360)

        fetch_empolyees = Button(self.root, text="EMPLOYEES", bg="red", font=("bold italic", '12'), height=2, width=13,
                                 command=self.femp)
        fetch_empolyees.place(x=800, y=90)

        fetch_departments = Button(self.root, text="DEPARTMENTS", bg="red", font=("bold italic", '12'), height=2,
                                   width=14, command=self.fdepts)
        fetch_departments.place(x=800, y=180)

        fetch_projects = Button(self.root, text="PROJECTS", bg="red", font=("bold italic", '12'), height=2, width=14,
                                command=self.fpro)
        fetch_projects.place(x=790, y=270)

        fetch_emp_pro = Button(self.root, text="EMPLOYEE_PROJECT", bg="red", font=("bold italic", '12'), height=2,
                               width=20, command=self.femppro)
        fetch_emp_pro.place(x=770, y=360)

        hard_emp_m = Button(self.root, text="HARD Work managers ", bg="#00F9F5", font=("bold italic", '12'), height=2,
                            width=20, command=self.hardwork)
        hard_emp_m.place(x=420, y=620)

        sub_q = Label(self.root, text='display managers who work more than 90 hours', bg='#1EB5F1',
                      font=("Cambria", '16'))
        sub_q.place(x=420, y=580)

        join_q = Label(self.root, text='Employees with working hours', bg='#1EB5F1', font=("Cambria", '16'))
        join_q.place(x=420, y=480)

        work_hrs = Button(self.root, text="Employees & hours ", bg="#00F9F5", font=("bold italic", '12'), height=2,
                          width=20, command=self.workhours)
        work_hrs.place(x=420, y=520)

        self.root, mainloop()

    def insert(self):
        import mysql.connector
        import tkinter.messagebox as msg
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')

        eid = int(self.empid_entry.get())
        efna = str(self.fname_entry.get())
        elna = str(self.lname_entry.get())
        egmail = str(self.email_entry.get())

        depid = int(self.deptid_entry.get())
        depna = str(self.deptname_entry.get())
        mgrid = int(self.mgr_entry.get())
        loc = str(self.loc_entry.get())

        pid = int(self.proid_entry.get())
        pname = str(self.proname_entry.get())
        star = str(self.start_entry.get())
        endt = str(self.end_entry.get())

        hrs = int(self.hrs_entry.get())
        erole = str(self.role_entry.get())
        print(eid)
        mycursor = mydb.cursor()

        mycursor.execute(
            "INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (%s,%s,%s,%s)",
            (eid, efna, elna, egmail))
        mydb.commit()
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')
        mycursor = mydb.cursor()
        mycursor.execute(
            " INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (%s,%s,%s,%s)",
            (depid, depna, mgrid, loc))
        mydb.commit()
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')
        mycursor = mydb.cursor()
        mycursor.execute(" INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (%s,%s,%s,%s)",
                         (pid, pname, star, endt))
        mydb.commit()
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')
        mycursor = mydb.cursor()
        mycursor.execute(
            " INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (%s,%s,%s,%s)",
            (eid, pid, hrs, erole))
        msg.showinfo("One record inserted successfully")
        msg.showinfo(title="response", message="update details successful")

        mydb.commit()

    def update(self):
        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')
        mycursor = mydb.cursor()

        rootu = Tk()
        rootu.geometry('500x500')
        rootu.config(bg='magenta')
        rootu.title('update operation')
        lb1 = Label(rootu, text="UPDADE Employee details", bg='yellow', font=("Bold", '18'))
        lb1.place(x=50, y=10)

        empid = Label(rootu, text="employee id", bg='magenta', font=("Bold", '18'))
        empid.place(x=20, y=60)
        eid_entry = Entry(rootu)
        eid_entry.place(x=200, y=65)

        fname_label = Label(rootu, text=" new first name ", bg='magenta', font=("Bold", '18'))
        fname_label.place(x=20, y=100)
        fname_entry = Entry(rootu)
        fname_entry.place(x=200, y=105)

        lname_label = Label(rootu, text="new last name", bg='magenta', font=("Bold", '18'))
        lname_label.place(x=20, y=140)
        lname_entry = Entry(rootu)
        lname_entry.place(x=200, y=145)

        gmail_label = Label(rootu, text="new gmail address", bg='magenta', font=("Bold", '18'))
        gmail_label.place(x=20, y=180)
        gm_entry = Entry(rootu)
        gm_entry.place(x=200, y=185)

        def validate():
            import mysql.connector
            import tkinter.messagebox as msg
            mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                           database='Empdepartment')
            mycursor = mydb.cursor()
            idd = eid_entry.get()
            idd = int(idd)
            fn = fname_entry.get()
            ln = lname_entry.get()
            gm = gm_entry.get()

            mycursor.execute(
                "UPDATE Employees set first_name = %s, last_name = %s  , email_address = %s where employee_id = %s ",
                (fn, ln, gm, idd))
            if mycursor:
                msg.Message("update details successful")
            mydb.commit()
            msg.showinfo(title="response", message="update details successful")

        upb = Button(rootu, text="change employe details", bg="red", font=("Bold", '15'), command=validate)
        upb.place(x=200, y=225)

        rootu.mainloop()
        mydb.commit()

    def retrieve(self):
        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')
        mycursor = mydb.cursor()
        mydb.commit()

        rootr = Tk()
        rootr.geometry('500x500')
        rootr.config(bg='magenta')
        rootr.title('Retrieve details prjects and timing ')
        lb1 = Label(rootr, text="Retreve all details of project duration and time", bg='yellow', font=("Bold", '16'))
        lb1.place(x=10, y=10)

        proid = Label(rootr, text="project id", bg='magenta', font=("Bold", '18'))
        proid.place(x=20, y=60)
        pid_entry = Entry(rootr)
        pid_entry.place(x=200, y=65)

        def validated():
            import mysql.connector
            import tkinter.messagebox as msg
            mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                           database='Empdepartment')
            mycursor = mydb.cursor()
            idd = pid_entry.get()
            idd = int(idd)

            import mysql.connector

            from tkinter import ttk
            import tkinter.messagebox as msg
            root5 = Tk()

            import mysql.connector
            mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                           database='Empdepartment')

            mycursor = mydb.cursor()

            # Using treeview widget
            trv = ttk.Treeview(root5)
            trv.grid(row=1, column=1, padx=20, pady=20)
            # number of columns
            trv["columns"] = ("1", "2", "3", "4", "5", "6")

            # Defining heading
            trv['show'] = 'headings'

            # width of columns and alignment
            trv.column("1", width=100, anchor='c')
            trv.column("2", width=120, anchor='c')
            trv.column("3", width=120, anchor='c')
            trv.column("4", width=150, anchor='c')
            trv.column("5", width=150, anchor='c')
            trv.column("6", width=150, anchor='c')

            # Headings
            # respective columns
            trv.heading("1", text="project_id")
            trv.heading("2", text="project_name")
            trv.heading("3", text="start_date")
            trv.heading("4", text="end_date")
            trv.heading("5", text="hours_worked")
            trv.heading("6", text="role")

            # getting data from MySQL student table
            mycursor.execute("select  pj.project_id, pj.project_name, pj.start_date,pj.end_date , ep.hours_worked,ep.role \
                                 from  Employee_Projects  as  ep inner join  Projects  as pj \
                                    on ep.project_id = pj.project_id \
                                        where pj.project_id= %s ", (idd,))
            r_set = mycursor.fetchall()
            for dt in r_set:
                trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))

            mydb.commit()
            root5.mainloop()

        retb = Button(rootr, text="retrieve project details", bg="red", font=("Bold", '15'), command=validated)
        retb.place(x=200, y=225)

        rootr.mainloop()
        mydb.commit()

    def delete(self):
        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')
        mycursor = mydb.cursor()
        mydb.commit()
        rootd = Tk()
        rootd.geometry('500x500')
        rootd.config(bg='magenta')
        rootd.title('DELETE operation')
        lb1 = Label(rootd, text=" DELETE Employee Records", bg='yellow', font=("Bold", '18'))
        lb1.place(x=50, y=10)

        empid = Label(rootd, text="employee id", bg='magenta', font=("Bold", '18'))
        empid.place(x=20, y=60)
        eid_entry = Entry(rootd)
        eid_entry.place(x=200, y=65)

        def valid():
            import mysql.connector
            import tkinter.messagebox as msg
            mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                           database='Empdepartment')
            mycursor = mydb.cursor()
            ide = eid_entry.get()
            ide = int(ide)

            mycursor.execute("DELETE from Employees where  employee_id = %s ", (ide,))
            if mycursor:
                msg.Message("record deleted successfuly")
            mydb.commit()
            msg.showinfo(title="response", message="employee records deleted successfully")

        delb = Button(rootd, text="Delete details of an employee ", bg="red", font=("Bold", '15'), command=valid)
        delb.place(x=200, y=225)

        rootd.mainloop()
        mydb.commit()

    def hardwork(self):
        import mysql.connector

        from tkinter import ttk
        import tkinter.messagebox as msg
        root5 = Tk()

        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')

        mycursor = mydb.cursor()

        # Using treeview widget
        trv = ttk.Treeview(root5)
        trv.grid(row=1, column=1, padx=20, pady=20)
        # number of columns
        trv["columns"] = ("1", "2", "3", "4")

        # Defining heading
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=100, anchor='c')
        trv.column("2", width=120, anchor='c')
        trv.column("3", width=120, anchor='c')
        trv.column("4", width=150, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="manager_id")
        trv.heading("2", text="manager first name")
        trv.heading("3", text="manager last name")
        trv.heading("4", text="manager email address")

        # getting data from MySQL student table
        mycursor.execute('    select e1.employee_id as manager_id ,e1.first_name as manager_firstname,e1.last_name as manager_last_name \
                          ,e1.email_address as manager_email from Employees e1 where e1.employee_id in ( \
                          select d.manager_id  from Departments  d where d.manager_id in ( \
                         select   e.employee_id   from Employees e where e.employee_id  in \
                        (select ep2.employee_id from Employee_projects ep2 where ep2.hours_worked > 90 ) ) )')

        r_set = mycursor.fetchall()
        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3]))

        mydb.commit()
        root5.mainloop()

    def workhours(self):
        import mysql.connector

        from tkinter import ttk
        import tkinter.messagebox as msg
        root5 = Tk()

        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')

        mycursor = mydb.cursor()

        # Using treeview widget
        trv = ttk.Treeview(root5)
        trv.grid(row=1, column=1, padx=20, pady=20)
        # number of columns
        trv["columns"] = ("1", "2", "3", "4", "5", "6")

        # Defining heading
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=100, anchor='c')
        trv.column("2", width=120, anchor='c')
        trv.column("3", width=120, anchor='c')
        trv.column("4", width=150, anchor='c')
        trv.column("5", width=150, anchor='c')
        trv.column("6", width=150, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="employee_id")
        trv.heading("2", text="employee first name")
        trv.heading("3", text="employee last name")
        trv.heading("4", text="employee email address")
        trv.heading("5", text="hours worked")
        trv.heading("6", text="employee role")

        # getting data from MySQL student table
        mycursor.execute('    select e1.employee_id,first_name,last_name,email_address ,hours_worked,role\
                         from Employees e1  inner join Employee_projects ep1     on e1.employee_id = ep1.employee_id  ')

        r_set = mycursor.fetchall()
        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))

        mydb.commit()
        root5.mainloop()

    def femp(self):
        import mysql.connector

        from tkinter import ttk
        import tkinter.messagebox as msg
        root5 = Tk()

        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')

        mycursor = mydb.cursor()

        # Using treeview widget
        trv = ttk.Treeview(root5)
        trv.grid(row=1, column=1, padx=20, pady=20)
        # number of columns
        trv["columns"] = ("1", "2", "3", "4")

        # Defining heading
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=100, anchor='c')
        trv.column("2", width=120, anchor='c')
        trv.column("3", width=120, anchor='c')
        trv.column("4", width=150, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="employee_id")
        trv.heading("2", text="first_name")
        trv.heading("3", text="last_name")
        trv.heading("4", text="email_address")

        # getting data from MySQL student table
        mycursor.execute('select * from Employees')
        r_set = mycursor.fetchall()
        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3]))

        mydb.commit()
        root5.mainloop()

    def fdepts(self):
        import mysql.connector

        from tkinter import ttk
        import tkinter.messagebox as msg
        root5 = Tk()

        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')

        mycursor = mydb.cursor()

        # Using treeview widget
        trv = ttk.Treeview(root5)
        trv.grid(row=1, column=1, padx=20, pady=20)
        # number of columns
        trv["columns"] = ("1", "2", "3", "4")

        # Defining heading
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=100, anchor='c')
        trv.column("2", width=120, anchor='c')
        trv.column("3", width=120, anchor='c')
        trv.column("4", width=150, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="department_id")
        trv.heading("2", text="department_name")
        trv.heading("3", text="manager_id")
        trv.heading("4", text="location")

        # getting data from MySQL student table
        mycursor.execute('select * from Departments')
        r_set = mycursor.fetchall()
        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3]))

        mydb.commit()
        root5.mainloop()

    def fpro(self):
        import mysql.connector

        from tkinter import ttk
        import tkinter.messagebox as msg
        root5 = Tk()

        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')

        mycursor = mydb.cursor()

        # Using treeview widget
        trv = ttk.Treeview(root5)
        trv.grid(row=1, column=1, padx=20, pady=20)
        # number of columns
        trv["columns"] = ("1", "2", "3", "4")

        # Defining heading
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=100, anchor='c')
        trv.column("2", width=120, anchor='c')
        trv.column("3", width=120, anchor='c')
        trv.column("4", width=150, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="project_id")
        trv.heading("2", text="project_name")
        trv.heading("3", text="start_date")
        trv.heading("4", text="end_date")

        # getting data from MySQL student table
        mycursor.execute('select * from Projects')
        r_set = mycursor.fetchall()
        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3]))

        mydb.commit()
        root5.mainloop()

    def femppro(self):
        import mysql.connector

        from tkinter import ttk
        import tkinter.messagebox as msg
        root5 = Tk()

        import mysql.connector
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', port=3306,
                                       database='Empdepartment')

        mycursor = mydb.cursor()

        # Using treeview widget
        trv = ttk.Treeview(root5)
        trv.grid(row=1, column=1, padx=20, pady=20)
        # number of columns
        trv["columns"] = ("1", "2", "3", "4")

        # Defining heading
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=100, anchor='c')
        trv.column("2", width=120, anchor='c')
        trv.column("3", width=120, anchor='c')
        trv.column("4", width=150, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="employee_id")
        trv.heading("2", text="project_id")
        trv.heading("3", text="hours_worked")
        trv.heading("4", text="role")

        # getting data from MySQL student table
        mycursor.execute('select * from Employee_Projects')
        r_set = mycursor.fetchall()
        for dt in r_set:
            trv.insert("", 'end', iid=dt[0], text=dt[0], values=(dt[0], dt[1], dt[2], dt[3]))

        mydb.commit()
        root5.mainloop()


emp = Empdepartment(Tk)
