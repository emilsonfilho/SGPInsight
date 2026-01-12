import psycopg2

try:
    conn = psycopg2.connect(
        dbname='bancodedados1',
        user='postgres',
        host='172.18.102.120',
        password='alunoufc',
        port='5432'
    )

    cursor = conn.cursor()

    try:
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS alunos(
                id SERIAL PRIMARY KEY
                nome TEXT NOT NULL
            )
            '''
        )

        cursor.execute('INSERT INTO alunos (nome) VALUES (%s)', ('Maria',))
        cursor.execute('INSERT INTO alunos (nome) VALUES (%s)', ('João',))

        conn.commit()

    except Exception as edb:
        conn.rollback()
        print(f"Erro ao executar operações no banco")

except Exception as e:
    print(e)