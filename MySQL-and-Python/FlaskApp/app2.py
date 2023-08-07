import mysql.connector

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "MyPassword@123",
    "database": "BucketList"
}

# Establish a connection
connection = mysql.connector.connect(**db_config)

# Create a cursor to interact with the database
cursor = connection.cursor()
