# Employee resource Management System 
																		
* This database Model is a management tool that helps organisation to create employess profiles and departments and assign them to respective departments .
* We can update the employess information and thier departments.
* we have used 4 tables to handle this system.

For creating the database we've used MYSQL which is a free and popular DBMS.

This model has 4 tables listed below:


 
## 1.)  Table Name: Employees

* Attributes: 

	 employee_id INT ,
      
      first_name VARCHAR(40) ,
      
      last_name VARCHAR(40) ,
      
      email_address VARCHAR(40) ,
      
      PRIMARY KEY (employee_id),         Primary key

* Primary Key : employee_id

### Functional Dependencies:

* employee_id ---> first_name, last_name, email_address

* email_address ---> employee_id, first_name, last_name

### The above table is in 3NF as there are no transitive dependencies and free from anomalies.

### Sample Data:

* (1, Vijay, Hanumanthu, vijayhanumanthu@gmail.com)

* (2, Ajay, Hanumanthu, ajayhanumanthu@gmail.com )

## 2.)  Table Name: Project

* Attributes: 

	  project_id INT ,

       project_name VARCHAR(40) ,

       start_date DATE ,

       end_date DATE ,

       PRIMARY KEY (project_id)

* Primary Key : project_id

### Functional Dependencies:

*project_id ---> project_name, start_date, end_date

### The above table is in 3NF as there are no transitive dependencies and free from anomalies.

### Sample Data:

* (10, CBA, 20/11/2023, 11/04/2025 )

* (20, Dev, 21/04/2023, 16/07/2027  )


## 3.)  Table Name: Employee_Project

* Attributes: 

       employee_id INT ,

       project_id INT ,

      hours_worked INT ,

      role VARCHAR(40) ,

      PRIMARY KEY (employee_id, project_id),

      FOREIGN KEY (employee_id) REFERENCES Employees (employee_id)  ON DELETE CASCADE,

      FOREIGN KEY (project_id) REFERENCES Projects (project_id) ON DELETE CASCADE 


* Primary Key : The primary key for the Employees_Projects table is a composite key consisting of two columns: employee_id and project_id.

### Functional Dependencies:

* employee_id, project_id ---> hours_worked, role

* employee_id ---> project_id, hours_worked, role

* project_id ---> employee_id, hours_worked, role

### The above table is in 3NF as there are no transitive dependencies and free from anomalies.

### Sample Data:

* (1, 10, 90, Sap Consultant)

* (2, 20, 40, Sql Developer )

## 4.)  Table Name: Departments

* Attributes: 

	 department_id INT   ,

      department_name VARCHAR(40) ,

      manager_id INT ,

      location VARCHAR(40) ,

      PRIMARY KEY (department_id) , 
 
      FOREIGN KEY (manager_id) REFERENCES Employees (employee_id) ON DELETE SET NULL


* Primary Key : department_id

### Functional Dependencies:

* department_id ---> department_name, manager_id, location

* manager_id ---> department_id, department_name, location

### The above table is in 3NF as there are no transitive dependencies and free from anomalies.

### Sample Data:

* (100, Development, M1, Wichita)

* (200, testing, M2, Phoneix  )

# Relations among tables

### 1)One-to-Many relationship between Employees and Employee_Projects tables: 
 Each employee can work on many projects, but each project can be worked on by one employee (in the given schema). 
 This is established by the foreign key constraint in the Employee_Projects table that references the Employees table.

### 2)One-to-Many relationship between Projects and Employee_Projects tables: 
 Each project can have many employees working on it, but each employee can work on only one project (in the given schema). 
 This is established by the foreign key constraint in the Employee_Projects table that references the Projects table.

## 3) Many-to-One relationship between Employees and Departments tables: 
 any employees can belong to a single department, but each employee can belong to only one department. 
This is established by the foreign key constraint in the Departments table that references the Employees table.

### 4)One-to-One or Many-to-One relationship between Employees and Departments tables:
Each department can have only one manager, and each manager can manage only one department.
This is established by the manager_id column in the Departments table that references the employee_id column in the Employees table.
