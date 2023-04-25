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
