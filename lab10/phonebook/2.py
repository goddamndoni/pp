import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',    
    password='Danabek007'
)

current = config.cursor()
# добавляем значения в таблицу 
id = 1
name = 'Danabek'
number = '87777777777'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()