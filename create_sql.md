#                        /* Create DataBase */
CREATE DATABASE  Empdepartment ;  

USE  Empdepartment ; 

show tables ;

#                  /* Create Query For Employees Table */

CREATE TABLE  Employees (
  employee_id INT ,
  first_name VARCHAR(40) ,
  last_name VARCHAR(40) ,
  email_address VARCHAR(40) ,
  PRIMARY KEY (employee_id) 
);

#                  /* Create Query For Projects Table */
CREATE TABLE Projects (
  project_id INT ,
  project_name VARCHAR(40) ,
  start_date DATE ,
  end_date DATE ,
  PRIMARY KEY (project_id)
);

#               /* Create Query For Employee_Projects Table */

CREATE TABLE Employee_Projects (
  employee_id INT ,
  project_id INT ,
  hours_worked INT ,
  role VARCHAR(40) ,
  PRIMARY KEY (employee_id, project_id),
  FOREIGN KEY (employee_id) REFERENCES Employees (employee_id)  ON DELETE CASCADE,
  FOREIGN KEY (project_id) REFERENCES Projects (project_id) ON DELETE CASCADE 
) ;

#                  /* Create Query For Departments Table */

CREATE TABLE Departments (
  department_id INT   ,
  department_name VARCHAR(40) ,
  manager_id INT ,
  location VARCHAR(40) ,
  PRIMARY KEY (department_id) ,  
  FOREIGN KEY (manager_id) REFERENCES Employees (employee_id) ON DELETE SET NULL
);
