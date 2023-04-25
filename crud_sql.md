use Empdepartment ;

show tables ;

###                                                         /*CRUD Operations*/
* Insert operations

  INSERT INTO Employees (employee_id, first_name, last_name, email_address) VALUES (1, 'John', 'Doe', 'jdoe@email.com');
 
  INSERT INTO Departments (department_id, department_name, manager_id, location) VALUES (1, 'Sales', 1, 'New York');
 
  INSERT INTO Projects (project_id, project_name, start_date, end_date) VALUES (1, 'Website Redesign', '2022-01-01', '2022-07-01');
 
  INSERT INTO Employee_Projects (employee_id, project_id, hours_worked, role) VALUES (1, 1, 50, 'Project Manager');

 
* Retrieve operations

  SELECT *  FROM   Departments ;

  SELECT *  FROM Employee_projects  WHERE project_id = 1; 

  SELECT *  FROM  Employees WHERE employee_id = 1 ;

  SELECT *  FROM  Projects WHERE project_id = 1;

  SELECT *  FROM  Departments WHERE department_id = 1;


* Update operations

  UPDATE  Departments SET location = 'Wichita' where  manager_id = 1 ;
  
  UPDATE  Departments SET location = 'Dallas' where  manager_id = 2;


* Delete Operations

  DELETE FROM Employee_projects  WHERE project_id = 1; 

  DELETE FROM  Employees WHERE employee_id = 1 ;

  DELETE FROM  Projects WHERE project_id = 1;

  DELETE FROM  Departments WHERE department_id = 1;
