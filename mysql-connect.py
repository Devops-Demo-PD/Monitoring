import sys
import mysql.connector
import base64

try:

    connection = mysql.connector.connect(host='localhost',
                                         database='jude',
                                         user=base64.b64decode('ZGJfdXNlcl9hbGw='),
                                         password=base64.b64decode('RGJfdXNlcl8xMjM0NQ=='))
    if connection.is_connected():
        print("Connection to the MySQL database is sucessful")
        connection.close()
        sys.exit(0)

except Exception as e:
    print("Connection to the MySQL database failed")
    sys.exit(2)
