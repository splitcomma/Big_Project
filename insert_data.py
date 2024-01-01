import mysql.connector
from config import DATABASE_CONFIG
from mysql.connector import errorcode

cnx = mysql.connector.connect(**DATABASE_CONFIG)
cursor = cnx.cursor()


# Insert test data
insert_test_data_query = """
INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date)
VALUES
('1995-01-01', 'bup', 'lup', 'M', '1934-01-01'),
('1934-02-15', 'bip', 'ght', 'F', '2034-02-01');
"""

cursor.execute(insert_test_data_query)
cnx.commit()
print("Test data inserted successfully.")
