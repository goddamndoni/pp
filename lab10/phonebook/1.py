import psycopg2
# creating table of phonebook
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',    
    password='Danabek007'
)

current = config.cursor()
sql = '''
        CREATE TABLE phonebook(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            number VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()