import sqlite3 as sql

# Create Connection/database
def create_conn():
    conn = sql.connect('./company.db')
    cursor  = conn.cursor()

    return conn, cursor

# Create the table workers for this job
def create_workers():
    conn, cursor = create_conn()
    sql = '''
            CREATE TABLE workers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                cargo VARCHAR(50) NOT NULL,
                salario INTEGER NOT NULL,
                data_admissao TEXT NOT NULL
            )
            '''
    cursor.execute(sql)
    conn.commit()
    conn.close()

# Save results from a query and returns it
def query_fetch(sql):
    conn, cursor = create_conn()

    cursor.execute(sql)
    retorno_query = cursor.fetchall()

    conn.commit()
    conn.close()

    return retorno_query

#insert any data that fits on the table workers
def insert_workers(dados):
    conn, cursor = create_conn()
    query = """
        INSERT INTO workers (nome, cargo, salario, data_admissao)
        VALUES (?, ?, ?, ?)
    """
    cursor.executemany(query, dados)  # Pass the parameters here
    conn.commit()
    conn.close()