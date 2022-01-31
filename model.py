#data model - SQL database
import mysql.connector

class Model():

    def __init__(self):
        self.database = mysql.connector.connect(
          user="root",
          host = "localhost",
          password= self.GetPassword(),
          database="alca_db"
        )
        self.c = self.database.cursor(buffered=True)

    def GetPassword(self):
        password = ""
        with open("password.txt") as file:
            password = file.readline()
        return password

    def GetTopicID(self, subject_name):
        topicIDQuery = f"SELECT TopicID FROM topics WHERE TopicTitle = '{subject_name}'"
        self.c.execute(topicIDQuery)
        try:
            topic_id = self.c.fetchall()[0][0]
        except IndexError:
            print("The topic name could not be found")
        return topic_id

    def GetProgress(self, subject_name):
        #selects the questions
        topic_id = self.GetTopicID(subject_name)

        #initially will select every question and then query from within that question
        query = f"SELECT Confidence FROM questions WHERE TopicID = {topic_id}"
        self.c.execute(query)

        red = 0
        orange = 0
        yellow = 0
        green = 0

        #returns a list of tuples containing ("red",) and nothing more
        for result in self.c:
            if result[0] == "red":
                red += 1
            elif result[0] == "orange":
                orange += 1
            elif result[0] == "yellow":
                yellow += 1
            elif result[0] == "green":
                green +=1

        progress_dict = {
            "Red": red,
            "Orange": orange,
            "Yellow": yellow,
            "Green": green
        }

        return progress_dict

    def GetTableTitles(self):
        self.c.execute("SHOW TABLES")
        table_titles = []
        for table in self.c:
            table_titles.append(table[0])
        return table_titles

    def PrintTables(self):
        self.c.execute("SHOW TABLES")
        print("TABLES ARE: ")
        for table in self.c:
            print(table)

    def DeleteTable(self,table_name):
        self.c.execute("DROP TABLE " + table_name)


    def ClearTable(self):
        self.c.execute("DELETE FROM topics")

    def InsertIntoTopics(self, topic_name, paper):
        insert_statement = "INSERT INTO topics (TopicTitle, Paper) VALUES (%s, %s)"
        values = (topic_name, paper)
        self.c.execute(insert_statement, values)
        self.database.commit()

    def InsertIntoQuestions(self, topic_name, question_text, answer_type, answer_text):
        topic_id = self.GetTopicID(topic_name)

        print("topic id is " , topic_id)
        insert_statement = "INSERT INTO questions (QuestionText, AnswerType, AnswerText, TopicID) VALUES (%s, %s, %s, %s)"
        values = (question_text, answer_type, answer_text, topic_id)
        self.c.execute(insert_statement, values)
        self.database.commit()


    #confidence could be either red orange green, or by default,
    def Main(self):

        topics_table_creation = """
        CREATE TABLE topics (
            TopicID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            TopicTitle VARCHAR(255),
            Paper INT
        );
        """
        #CHANGING QUESTIONS TO TEST FOR A TEST, CHANGE BACK
        questions_table_creation = """
        CREATE TABLE test (
            QuestionID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            QuestionText VARCHAR(255),
            AnswerType VARCHAR(6),
            AnswerText VARCHAR(1000),
            Confidence VARCHAR(255) DEFAULT 'red',
            TopicID INT,
            FOREIGN KEY (TopicID) REFERENCES topics(TopicID)
        );
        """

        #start by creating the table for topics
        self.PrintTables()

        #creation of the topics table
        try:
            self.c.execute(topics_table_creation)
        except mysql.connector.Error as e:
            if e.errno == 1050:
                print("table already exists")
            else :
                print("other error occurred with error code : ", e.errno)


        #creation of the questions table
        try:
            self.c.execute(questions_table_creation)
        except mysql.connector.Error as e:
            if e.errno == 1050:
                print("table already exists")
            else:
                print("other error occured with error code : ", e.errno)
                print("error message is: ", e.msg)

model = Model()
