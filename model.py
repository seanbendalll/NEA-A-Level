#data model - SQL database
import mysql.connector

def GetPassword():
    password = ""
    with open("password.txt") as file:
        password = file.readline()
    return password

database = mysql.connector.connect(
  user="root",
  host = "localhost",
  password=GetPassword(),
  database="alca_db"
)
c = database.cursor(buffered=True)

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

def ClearTable():
    c.execute("DELETE FROM topics")

def InsertIntoTopics(topic_name, paper):
    insert_statement = "INSERT INTO topics (TopicTitle, Paper) VALUES (%s, %s)"
    values = (topic_name, paper)
    c.execute(insert_statement, values)
    database.commit()

def InsertIntoQuestions(topic_name, question_text, answer_type, answer_text):
    topic_id = 1
    topicIDQuery = f"SELECT TopicID FROM topics WHERE TopicTitle = '{topic_name}'"
    c.execute(topicIDQuery)
    topic_id = c.fetchall()[0][0]
    print("topic id is " , topic_id)
    insert_statement = "INSERT INTO questions (QuestionText, AnswerType, AnswerText, TopicID) VALUES (%s, %s, %s, %s)"
    values = (question_text, answer_type, answer_text, topic_id)
    c.execute(insert_statement, values)
    database.commit()

topics_table_creation = """
CREATE TABLE topics (
    TopicID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    TopicTitle VARCHAR(255),
    Paper INT
);
"""
questions_table_creation = """
CREATE TABLE questions (
    QuestionID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    QuestionText VARCHAR(255),
    AnswerType VARCHAR(6),
    AnswerText VARCHAR(1000),
    Confidence VARCHAR(255) DEFAULT 'red',
    TopicID INT,
    FOREIGN KEY (TopicID) REFERENCES topics(TopicID)
);
"""
#confidence could be either red orange green, or by default,
def Main():
    #start by creating the table for topics
    PrintTables()

    #creation of the topics table
    """
    try:
        c.execute(topics_table_creation)
    except mysql.connector.Error as e:
        if e.errno == 1050:
            print("table already exists")
        else :
            print("other error occurred with error code : ", e.errno)
    """

    #creation of the questions table
    try:
        c.execute(questions_table_creation)
    except mysql.connector.Error as e:
        if e.errno == 1050:
            print("table already exists")
        else:
            print("other error occured with error code : ", e.errno)
            print("error message is: ", e.msg)


Main()
