import sys
import mysql.connector
import base64

try:

    connection = mysql.connector.connect(host='localhost',
                                         database='laravel',
                                         user=base64.b64decode('cm9vdA=='),
                                         password=base64.b64decode('YWxlZl8xMjM0NQ=='))
    if connection.is_connected():
        print("Connection to the MySQL database is sucessful")
        connection.close()
        sys.exit(0)

except Exception as e:
    print("Connection to the MySQL database failed")
    sys.exit(2)
