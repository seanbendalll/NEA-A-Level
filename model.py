#data model - SQL database
import mysql.connector

class Model():

    def __init__(self):
        #uses the module mysql.connector in python to develop a connection to my local database.
        self.database = mysql.connector.connect(
          user="root",
          host = "localhost",
          password= self.GetPassword(),
          database="alca_db"
        )

        #initialises a localised cursor to navigate around the database.
        self.c = self.database.cursor(buffered=True)

    #uses the hidden file in the git ignore to access my password.
    def GetPassword(self):
        password = ""
        with open("password.txt") as file:
            password = file.readline()
        return password

    #gets a topic title via the topic ID.
    def GetTopicTitle(self, topic_id):
        topic_title_query = f"SELECT TopicTitle FROM topics WHERE TopicID = {topic_id}"
        self.c.execute(topic_title_query)
        try:
            #uses the cursors result to get the topic title.
            topic_title = self.c.fetchall()[0][0]
        except IndexError:
            print("The topic name could not be found")
        return topic_title

    #gets a topic id from the topic title.
    def GetTopicID(self, topic_title):
        topicIDQuery = f"SELECT TopicID FROM topics WHERE TopicTitle = '{topic_title}'"
        self.c.execute(topicIDQuery)
        #sets it initially to -1 so that if not found it can be recognised elsewhere
        topic_id = -1
        try:
            topic_id = self.c.fetchall()[0][0]
        except IndexError:
            print("The topic ID could not be found")
        return topic_id

    """
    #gets the associated topic id from the question.
    def GetTopicIDFromQuestion(self, question_text):
        topicIDQuery = f"SELECT TopicID FROM questions WHERE QuestionText = '{question_text}'"
        self.c.execute(topicIDQuery)
        topic_id = -1
        try:
            topic_id = self.c.fetchall()[0][0]
        except IndexError:
            print("The TopicID could not be found")
        return topic_id
    """

    #retrieves all the questions from a given topic given its ID
    def GetAllQuestions(self, topic_id):
        questions = []
        question_query = f"SELECT * FROM questions WHERE TopicID = '{topic_id}'"
        self.c.execute(question_query)
        for question in self.c:
            questions.append(question)
        return questions

    #this function was used inside the fetch.py in order to get the images that needed to be saved.
    #could have completed this more efficiently, but due to the chronological order of the design i had to go back to retrieve the questions.
    def GetImageQuestions(self):
        image_urls = []
        image_titles = []
        imageurl_query = "SELECT AnswerText FROM questions WHERE AnswerType = 'image'"
        self.c.execute(imageurl_query)
        for image_url in self.c:
            image_urls.append(image_url[0])
        imagetitle_query = "SELECT QuestionText FROM questions WHERE AnswerType = 'image'"
        self.c.execute(imagetitle_query)
        for imagetitle in self.c:
            image_titles.append(imagetitle[0])
        #creates a dictionary wherein it will contain the question of the image (soon to be set as the title of the image in files) and the answer, which is the image url.
        image_questions = {}
        for i in range(1, len(image_urls)):
            image_questions[image_titles[i -1]] = image_urls[i -1]
        return image_questions

    #a function to retrieve all the topics from the model.
    def GetTopics(self):
        topics = []
        get_topics_query = "SELECT TopicTitle FROM topics"
        self.c.execute(get_topics_query)
        for topic in self.c:
            topics.append(topic[0])
        return topics

    #reset the questions in a given topic name
    def ResetQuestions(self, topic_name):
        #if the topic name passed is all, it will reset every question to red
        if topic_name == "all":

            reset_query = """
            UPDATE questions
            SET Confidence = 'red'
            """
            self.c.execute(reset_query)
            #commits the changes.
            self.database.commit()
        else:
            #otherwise, sets for the individual topic_name
            topic_id = self.GetTopicID(topic_name)

            #outlines the reset query using a DDL script.
            reset_query = f"""
            UPDATE questions
            SET Confidence = 'red'
            WHERE TopicID = {topic_name}
            """
            try:
                self.c.execute(reset_query)
            except:
                print("Could not be found - invalid name.")
            self.database.commit()

    #function to be called to update the question to a new confidence.
    def UpdateQuestion(self, question_id, new_confidence):
        update_statement = f"UPDATE questions SET Confidence = '{new_confidence}' WHERE QuestionID = {question_id}"
        self.c.execute(update_statement)
        self.database.commit()

    def GetNumberOfQuestions(self, topic_name):
        topic_id = self.GetTopicID(topic_name)
        query = f"SELECT COUNT(*) FROM questions WHERE TopicID = {topic_id}"
        self.c.execute(query)
        print(self.c.fetchall())

    #function to generate a progress dictionary for a given subject.
    def GetProgress(self, topic_name):
        #selects the questions
        topic_id = self.GetTopicID(topic_name)

        #initially will select every question and then query from within that question
        query = f"SELECT Confidence FROM questions WHERE TopicID = {topic_id}"
        self.c.execute(query)

        #generates a counter for each of the confidences
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

        #assigns the progress dictionary according to the counters for each of the confidences.
        progress_dict = {
            "Red": red,
            "Orange": orange,
            "Yellow": yellow,
            "Green": green
        }

        #returns the dictionary to whereever in another file it is called.
        return progress_dict

    """
    THE FOLLOWING FUNCTIONS ARE NOT USED IN THE APPLICATION.PY FILE, RATHER THEY WERE USED TO
    CREATE THE DATABASE AND MODIFY IT WITHIN THE TERMINAL.
    """

    #a function for printing the table titles to see which tables i had created.
    def PrintTables(self):
        self.c.execute("SHOW TABLES")
        print("TABLES ARE: ")
        for table in self.c:
            print(table)

    #delete a table of a given name.
    def DeleteTable(self,table_name):
        self.c.execute("DROP TABLE " + table_name)

    #clears a given table to an empty table.
    def ClearTable(self):
        self.c.execute("DELETE FROM topics")

    #insert a value into topics with a given topic title and the paper it is from.
    def InsertIntoTopics(self, topic_name, paper):
        insert_statement = "INSERT INTO topics (TopicTitle, Paper) VALUES (%s, %s)"
        values = (topic_name, paper)

        #executes the insert statement and commits it to the final database.
        self.c.execute(insert_statement, values)
        self.database.commit()

    #insert a question into topics in the given format.
    def InsertIntoQuestions(self, topic_name, question_text, answer_type, answer_text):
        #gets the topic id of the topic_name you wish to insert (foreign key.)
        topic_id = self.GetTopicID(topic_name)

        print("topic id is " , topic_id)
        insert_statement = "INSERT INTO questions (QuestionText, AnswerType, AnswerText, TopicID) VALUES (%s, %s, %s, %s)"
        values = (question_text, answer_type, answer_text, topic_id)
        self.c.execute(insert_statement, values)
        self.database.commit()

    #a function to create the topic and table creation with the autoincrement and the keys set up.
    def Main(self):

        topics_table_creation = """
        CREATE TABLE topics (
            TopicID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            TopicTitle VARCHAR(255),
            Paper INT
        );
        """

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

        #creation of the topics table
        try:
            self.c.execute(topics_table_creation)
        except mysql.connector.Error as e:
            print("error occurred with error code : ", e.errno)
            print("error message is: ", e.msg)


        #creation of the questions table
        try:
            self.c.execute(questions_table_creation)
        except mysql.connector.Error as e:
            print("other error occured with error code : ", e.errno)
            print("error message is: ", e.msg)

model = Model()
