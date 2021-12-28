# ----- Example Python Program to remove a PostgreSQL database table 

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

 

# Start a PostgreSQL database session

psqlCon         = psycopg2.connect("dbname=mailsaas user=postgres_user password=externlabs")

psqlCon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

 

# Open a database cursor

psqlCursor      = psqlCon.cursor()

 

# Name of the table to be deleted

DbName       = "mailsaas"

 

# Form the SQL statement - DROP TABLE

dropTableStmt   = "DROP SCHEMA public CASCADE;"

createTableStmt   = "CREATE SCHEMA public;"

permissionTable = "GRANT ALL ON SCHEMA public TO postgres;"

permissionTable2 = "GRANT ALL ON SCHEMA public TO public;"



 

# Execute the drop table command

psqlCursor.execute(dropTableStmt);
psqlCursor.execute(createTableStmt);
psqlCursor.execute(permissionTable);
psqlCursor.execute(permissionTable2);

 

# Free the resources

psqlCursor.close();

psqlCon.close();