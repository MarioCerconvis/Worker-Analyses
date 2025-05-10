import sqlite3 as sql
import database as db

workers = [
('Alice', 'Desenvolvedora', 6000.00, '2020-01-15'),
('Bruno', 'Gerente', 30000.00, '2018-03-01'),
('Carlos', 'Analista', 8000.00, '2021-06-10'),
('Diana', 'Desenvolvedora', 7500.00, '2019-05-20'),
('Eva', 'Designer', 9000.00, '2022-02-25'),
('Faythe', 'Gerente de Projetos', 25000.00, '2017-07-30'),
('Gabriel', 'Desenvolvedora', 6200.00, '2021-04-15'),
('Heidi', 'Analista de Dados', 9500.00, '2020-08-10'),
('Ivan', 'Tester', 4500.00, '2020-12-05'),
('Judy', 'Desenvolvedora', 7000.00, '2019-10-25'),
('Karla', 'Analista', 12000.00, '2021-02-20'),
('Liam', 'Gerente', 28000.00, '2018-11-11'),
('Mariana', 'Desenvolvedora', 5700.00, '2019-03-30'),
('Nina', 'Designer', 11000.00, '2021-05-05'),
('Oscar', 'Desenvolvedor', 6400.00, '2020-06-15'),
('Peggy', 'Gerente de Marketing', 27000.00, '2016-09-01'),
('Quentin', 'Analista de Negócios', 10500.00, '2021-01-10'),
('Rupert', 'Tester', 4200.00, '2020-11-20'),
('Sybil', 'Desenvolvedora', 6200.00, '2019-12-15'),
('Trent', 'Gerente de Vendas', 29000.00, '2017-05-25'),
('Uma', 'Desenvolvedora', 6800.00, '2018-04-01'),
('Victor', 'Designer', 9600.00, '2021-03-20'),
('Walter', 'Analista de Dados', 8800.00, '2020-07-30'),
('Xena', 'Gerente de Projetos', 25000.00, '2016-08-15'),
('Yara', 'Desenvolvedora', 7300.00, '2021-09-10'),
('Zico', 'Tester', 4600.00, '2020-10-05'),
('André', 'Desenvolvedor', 5900.00, '2020-01-12'),
('Betty', 'Analista', 8500.00, '2021-06-10'),
('Clara', 'Gerente de Marketing', 26000.00, '2019-07-20'),
('David', 'Designer', 9500.00, '2022-02-25'),
('Eva', 'Desenvolvedora', 6400.00, '2020-04-15'),
('Finley', 'Analista de Sistemas', 8000.00, '2021-11-10'),
('Gina', 'Tester', 4700.00, '2020-12-05'),
('Harry', 'Desenvolvedor', 5800.00, '2019-10-25'),
('Isabel', 'Gerente', 27000.00, '2018-11-11'),
('Jack', 'Analista', 10200.00, '2021-02-20'),
('Lara', 'Desenvolvedora', 7500.00, '2019-03-30'),
('Mia', 'Designer', 9800.00, '2021-05-05'),
('Nate', 'Analista', 9900.00, '2021-06-15'),
('Olga', 'Gerente de Projetos', 24000.00, '2016-09-01'),
('Pete', 'Desenvolvedor', 7000.00, '2020-08-10'),
('Quinn', 'Analista de Negócios', 11400.00, '2021-01-10'),
('Ryan', 'Tester', 4200.00, '2020-11-20'),
('Sam', 'Desenvolvedora', 6500.00, '2019-12-15'),
('Tina', 'Gerente de Vendas', 28000.00, '2017-05-25'),
('Uma', 'Desenvolvedora', 6600.00, '2018-04-01'),
('Victor', 'Designer', 9700.00, '2021-03-20'),
('Wendy', 'Analista de Dados', 8900.00, '2020-07-30')]

#Insert Workers
def inserting_workers():
    db.insert_workers(workers)

#How many unique job roles do we have? and which are they?
def unique_jobs():
    conn, cursor = db.create_conn()
    query = '''
            SELECT DISTINCT cargo FROM workers
            ORDER BY cargo ASC
            '''

    cursor.execute(query)
    unique_jobs = cursor.fetchall()

    conn.close()
    return unique_jobs, len(unique_jobs)

#Top 5 biggest salaries
def biggest_salaries():
    conn, cursor = db.create_conn()
    query = '''
            SELECT salario FROM workers
            ORDER BY salario DESC
            LIMIT 5
            '''
    cursor.execute(query)
    bigger_salaries = cursor.fetchall()

    conn.close()
    return bigger_salaries

#Top 5 lowest salaries
def lowest_salaries():
    conn, cursor = db.create_conn()
    query = '''
            SELECT salario FROM workers
            ORDER BY salario ASC
            LIMIT 5
            '''
    cursor.execute(query)
    lowest_salaries = cursor.fetchall()

    conn.close()
    return lowest_salaries


#avg salary per job role
def avg_sal_per_role():
    conn, cursor = db.create_conn()
    query = '''
            SELECT
                cargo, CAST(AVG(salario) AS INTEGER) as average_income 
            FROM workers
            GROUP BY cargo
            ORDER BY average_income DESC
            '''
    cursor.execute(query)
    avg_sal_per_role = cursor.fetchall()

    conn.close()
    return avg_sal_per_role

#Which are the employees that earn the highest salaries per job role?
def highest_salaries_employees():
    conn, cursor = db.create_conn()
    query = '''
                SELECT w.nome, w.cargo, w.salario
                FROM workers w
                JOIN (
                    SELECT cargo, MAX(salario) AS max_salario
                    FROM workers
                    GROUP BY cargo
                ) m ON w.cargo = m.cargo AND w.salario = m.max_salario
                ORDER BY w.salario ASC;
            '''
    cursor.execute(query)
    highest_salaries_employees = cursor.fetchall()

    conn.close()
    return highest_salaries_employees