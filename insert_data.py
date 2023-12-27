import mysql.connector
from config import DATABASE_CONFIG
from mysql.connector import errorcode

cnx = mysql.connector.connect(**DATABASE_CONFIG)
cursor = cnx.cursor()


# Insert test data
insert_test_data_query = """
INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date)
VALUES
('1990-01-01', 'Norobi', 'Doe', 'M', '1965-01-01'),
('1995-02-15', 'Brorobi', 'Lucan', 'F', '2000-02-01');
"""

cursor.execute(insert_test_data_query)
cnx.commit()
print("Test data inserted successfully.")
