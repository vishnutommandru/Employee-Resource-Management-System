# /* Insert Query for Employees*/
INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (1, 'John', 'Doe', 'jdoe@email.com');

INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (2, 'Jane', 'Doe', 'jane.doe@email.com');

INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (3, 'Bob', 'Smith', 'bob.smith@email.com');

INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (4, 'Alice', 'Jones', 'alice.jones@email.com');

INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (5, 'Mike', 'Johnson', 'mike.johnson@email.com');

INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (6, 'Sara', 'Lee', 'sara.lee@email.com');

# /* Insert Query for Departments*/
INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (1, 'Sales', 1, 'New York');

INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (2, 'Marketing', 2, 'Los Angeles');

INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (3, 'Finance', 3, 'Chicago');

INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (4, 'Human Resources', 4, 'Houston');

INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (5, 'IT', 5, 'Seattle');

INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (6, 'Operations', 6, 'Miami');

# /* Insert Query for Projects*/
INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (1, 'Website Redesign', '2022-01-01', '2022-07-01');

INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (2, 'Marketing Campaign', '2022-02-15', '2022-05-15');

INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (3, 'Financial Audit', '2022-03-01', '2022-06-30');

INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (4, 'Employee Training Program', '2022-04-01', '2022-09-30');

INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (5, 'Product Launch', '2022-05-15', '2022-08-31');

INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (6, 'Office Move', '2022-06-01', '2022-07-31');
 
# /* Insert Query for Employee_Projects*/
INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (1, 1, 50, 'Project Manager');

INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (2, 6, 80, 'Designer');

INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (3, 2, 60, 'Marketing Specialist');

INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (4, 3, 100, 'Financial Analyst');

INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (5, 4, 120, 'Trainer');

INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (6, 5, 90, 'Product Manager');



