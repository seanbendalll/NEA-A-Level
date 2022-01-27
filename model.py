#data model - SQL database
import mysql.connector

database = mysql.connector.connect(
  user="root",
  host = "localhost",
  password="PlayTheGame707#",
  database="alca_db"
)
c = database.cursor()

print(database)


def GetTableTitles():
    c.execute("SHOW TABLES")
    table_titles = []
    for table in c:
        table_titles.append(table[0])
    return table_titles

def PrintTables():
    c.execute("SHOW TABLES")
    print("TABLES ARE: ")
    for table in c:
        print(table)

def DeleteTable(table_name):
    c.execute("DROP TABLE " + table_name)

def CreateTopic(topic_name, paper):
    print("topic created.")

table_creation = "CREATE TABLE topics (topic_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), paper INT)"
def Main():
    #start by creating the table for topics
    PrintTables()
    try:
        c.execute(table_creation)
    except mysql.connector.Error as e:
        if e.errno == 1050:
            print("table already exists")
        else :
            print("other error occurred with error code : ", e.errno)
    PrintTables()
Main()
