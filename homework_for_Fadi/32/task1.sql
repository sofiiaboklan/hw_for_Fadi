SELECT first_name, last_name, employees.department_id, departments.depart_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id;

SELECT first_name, last_name, departments.depart_name, locations.city, locations.state_province
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id
INNER JOIN locations ON departments.location_id = locations.location_id;

SELECT first_name, last_name, employees.department_id, departments.depart_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id
WHERE employees.department_id IN (40, 80);

SELECT departments.department_id, departments.depart_name, employees.first_name
FROM departments
LEFT JOIN employees ON departments.department_id = employees.department_id
ORDER BY departments.department_id;


SELECT e1.first_name AS employee_name,
       e2.first_name AS manager_name
FROM employees e1
LEFT JOIN employees e2
ON e1.manager_id = e2.employee_id
ORDER BY employee_name;

SELECT jobs.job_title, employees.first_name, employees.last_name, (jobs.max_salary - employees.salary) as salary_diff
FROM employees
INNER JOIN jobs ON employees.job_id = jobs.job_id;

SELECT jobs.job_title, AVG((jobs.max_salary + jobs.min_salary) / 2) AS avg_salary
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id
GROUP BY jobs.job_title;

SELECT employees.first_name, employees.last_name, employees.salary, locations.city
FROM employees
JOIN departments ON employees.department_id = departments.department_id
JOIN locations ON departments.location_id = locations.location_id
WHERE locations.city = 'London';

SELECT department.department_name, COUNT(employees.employee_id) AS num_employees
FROM department
LEFT JOIN employees ON department.department_id = employees.department_id
GROUP BY department.department_name;


