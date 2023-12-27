import mysql.connector
from config import DATABASE_CONFIG
from mysql.connector import errorcode

DB_NAME = "hq_rev"

TABLES = {}

TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ")")

try:
    cnx = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = cnx.cursor()

    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exist.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

    for table_name, create_table_query in TABLES.items():
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(create_table_query)
            print("OK")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table {} already exists.".format(table_name))
            else:
                print(err.msg)
        else:
            print("Table {} created successfully.".format(table_name))

    # Insert test data
    insert_test_data_query = """
    INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date)
    VALUES
    ('1990-01-01', 'John', 'Doe', 'M', '2022-01-01'),
    ('1995-02-15', 'Jane', 'Smith', 'F', '2022-02-01');
    """

    cursor.execute(insert_test_data_query)
    cnx.commit()
    print("Test data inserted successfully.")



finally:
    cursor.close()
    cnx.close()
