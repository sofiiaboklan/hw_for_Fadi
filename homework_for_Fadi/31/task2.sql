SELECT first_name, last_name from employees;

SELECT DISTINCT department_id from employees;

SELECT * FROM employees ORDER BY first_name DESC;

SELECT first_name, last_name, salary, salary * 0.12 AS PF from employees;

SELECT MAX(salary) FROM employees;

SELECT MIN(salary) FROM employees;

SELECT ROUND(salary/12.0, 2) AS monthly_salary from employees;

