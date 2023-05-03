import psycopg2, re

conn = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',    
    password='Danabek007'
)

cur = conn.cursor()

cur.execute(
    '''CREATE OR REPLACE FUNCTION search_from_book(a VARCHAR, b VARCHAR)
      RETURNS SETOF book 
   AS
   $$
      SELECT * FROM book WHERE name = a AND phone = b;
   $$
   language sql;
   '''
)

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
   IN users TEXT[][]
 )
 
 LANGUAGE plpgsql
 
 AS $$
 
 DECLARE
   i TEXT[];
 
 BEGIN 
 
    Foreach i slice 1 in array users
    LOOP
       INSERT INTO book (name, phone) VALUES (i[1], i[2]);
    END LOOP;
 
 END
 $$;
 '''
)

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_to_book(nm VARCHAR, phon VARCHAR)
       LANGUAGE plpgsql
       AS $$
       DECLARE 
          cnt INTEGER;
       BEGIN
          SELECT INTO cnt (SELECT count(*) FROM book WHERE name = nm);
          IF cnt > 0 THEN
             UPDATE phonebook
                SET phone = phon
                WHERE name = nm;
          ELSE
             INSERT INTO book(name, phone) VALUES (nm, phon);
             END IF;
       END;
       $$;''')

cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_book(nm VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE cnt INTEGER;
BEGIN
    SELECT into cnt (SELECT count(*) FROM book WHERE name = nm);
	IF cnt IS NOT NULL THEN
        DELETE FROM book
		WHERE name=nm;
    END IF;
END;
$$;""")

cur.execute("""CREATE OR REPLACE FUNCTION paginatingfrom(a integer, b integer)
RETURNS SETOF book
AS $$
   SELECT * FROM book
	ORDER BY name
	LIMIT a OFFSET b;
$$
language sql;""")

a = input('search\ninsert\ninsertloop\ndelete\npaginating\n')
if a == 'search':
    cur.execute("SELECT search_from_book('Danabek', '87074830395')")
    result = cur.fetchall()
    print(result)
if a == 'insert':
    cur.execute("CALL insert_to_book('Danabek', '87074830395')")
if a == 'insertloop':
    cur.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['John Jones', '87076052769'],
    ARRAY['Johny Thinker', '87079815569'],
    ARRAY['Trolley', '87074793780']
]);''')
if a == 'delete':
    cur.execute("CALL delete_from_book ('Trolley')")
if a == 'paginating':
    cur.execute(
        '''SELECT * FROM paginatingfrom(6, 0);'''
    )
    print(cur.fetchall())
conn.commit()
cur.close()
conn.close()