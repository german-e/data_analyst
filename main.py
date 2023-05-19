import psycopg2
import config

connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password=config.password
    dbname='DBExample',
    port='5432'
)

connection.autocommit=True

def crear_tabla():
    cursor = connection.cursor()
    query = '''
    CREATE TABLE customers( 
        customerid INT primary key, 
        name VARCHAR(50), 
        occupation VARCHAR(50), 
        email VARCHAR(50), 
        company VARCHAR(50), 
        phonenumber VARCHAR(20), 
        age INT );
    '''

    try:
        cursor.execute(query=query)
    except psycopg2.errors.DuplicateTable():
        print('La tabla ya existe')
    except psycopg2.Error as e:
        print('Ocurrió el sig. error: ' + e)
    
    cursor.close()


datos = [102, 'Maximo Ivan']

def insert_data(valores):
    cursor = connection.cursor()
    query = '''INSERT INTO agents 
                (agentid, name) 
                VALUES (%s, %s)'''

    try:
        print(datos)
        cursor.execute(query, valores)

    except psycopg2.Error as e:
        connection.rollback()
        print(f'Error: {e}')

insert_data(datos)