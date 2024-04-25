from mysql.connector import connect


def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

connection = mysql_connection('localhost', 'root', 'vltech123')

query = '''

  use VLTech;
Iselect * from clientes;

   
   
'''
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()
for row in result:
  print(row)