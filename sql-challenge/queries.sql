--List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees as e
INNER JOIN salaries as s
USING (emp_no) ;

--List employees who were hired in 1986.

SELECT emp_no, last_name, first_name, hire_date
FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31' ;

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.

SELECT dm.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name, dm.from_date, dm.to_date
FROM employees AS e
INNER JOIN dept_manager as dm
USING (emp_no)
INNER JOIN departments as d
USING (dept_no) ;

--List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees as e
INNER JOIN dept_emp as de
USING (emp_no)
INNER JOIN departments as d
USING (dept_no) ;

--List all employees whose first name is "Hercules" and last names begin with "B."

SELECT *
FROM employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%' ;

--List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees as e
INNER JOIN dept_emp as de
USING (emp_no)
INNER JOIN departments as d
USING (dept_no)
WHERE d.dept_name = 'Sales' ;

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employees as e
INNER JOIN dept_emp as de
USING (emp_no)
INNER JOIN departments as d
USING (dept_no)
WHERE d.dept_name IN ('Sales', 'Development') ;

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT last_name, COUNT(*) as Counts
FROM employees
GROUP BY last_name
ORDER BY Counts DESC ;
