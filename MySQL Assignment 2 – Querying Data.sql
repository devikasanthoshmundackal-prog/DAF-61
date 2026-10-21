USE employee;
SHOW TABLES;
ALTER TABLE Employees MODIFY salary DECIMAL(10,2);
SET SQL_SAFE_UPDATES=0;
UPDATE Employees
SET designation = 'Data Scientist'
WHERE designation IS NULL OR designation = '';



-- 1. Distinct salaries
SELECT DISTINCT salary FROM Employees;

-- 2. Aliases
SELECT age AS Employee_Age, salary AS Employee_Salary FROM Employees;

-- 3a. Salary > 50000 and hired before 2016-01-01
SELECT * FROM Employees
WHERE salary > 50000 AND hire_date < '2016-01-01';

-- 3b. Fill missing designation with 'Data Scientist'
SELECT * FROM Employees WHERE designation IS NULL OR designation = '';

UPDATE Employees
SET designation = 'Data Scientist'
WHERE designation IS NULL OR designation = '';

-- ============ Sorting and Grouping ============

-- 1. ORDER BY
SELECT * FROM Employees
ORDER BY department_id ASC, salary DESC;

-- 2. LIMIT: first 5 employees hired in 2018
SELECT * FROM Employees
WHERE YEAR(hire_date) = 2018
ORDER BY hire_date
LIMIT 5;

-- 3a. Sum of salaries in Finance department
SELECT SUM(e.salary) AS total_finance_salary
FROM Employees e
JOIN Departments d ON e.department_id = d.department_id
WHERE d.department_name = 'Finance';

-- 3b. Minimum age
SELECT MIN(age) AS min_age FROM Employees;

-- 4a. Max salary per location
SELECT l.location, MAX(e.salary) AS max_salary
FROM Employees e
JOIN Location l ON e.location_id = l.location_id
GROUP BY l.location;

-- 4b. Average salary per designation containing 'Analyst'
SELECT designation, AVG(salary) AS avg_salary
FROM Employees
WHERE designation LIKE '%Analyst%'
GROUP BY designation;

-- 5a. Departments with fewer than 3 employees
SELECT d.department_id, d.department_name, COUNT(e.employee_id) AS emp_count
FROM Departments d
LEFT JOIN Employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(e.employee_id) < 3;

-- 5b. Locations with female employees whose average age is below 30
SELECT l.location, AVG(e.age) AS avg_age
FROM Employees e
JOIN Location l ON e.location_id = l.location_id
WHERE e.gender = 'F'
GROUP BY l.location
HAVING AVG(e.age) < 30;

-- ============ Joins ============

-- 1. INNER JOIN
SELECT e.employee_name, e.designation, d.department_name
FROM Employees e
INNER JOIN Departments d ON e.department_id = d.department_id;

-- 2. LEFT JOIN: all departments with employee count (including 0)
SELECT d.department_id, d.department_name, COUNT(e.employee_id) AS total_employees
FROM Departments d
LEFT JOIN Employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;

-- 3. RIGHT JOIN: all locations with employee names (NULL if none)
SELECT l.location, e.employee_name
FROM Employees e
RIGHT JOIN Location l ON e.location_id = l.location_id;