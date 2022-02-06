#a file to implement a priority queue based on the questions in a topic
from model import Model
import random

class PriorityQueue():

    def __init__(self, topic_id):
        self.topic_id = topic_id
        self.data_model = Model()
        self.queue = self.InitialiseQueue()

    def InitialiseQueue(self):
        #accesses all the questions under the topicname
        questions = self.data_model.GetAllQuestions(self.topic_id)
        priority_queue = []
        red_questions = []
        orange_questions = []
        yellow_questions = []
        green_questions = []
        for question in questions:
            if question[4] == "red":
                red_questions.append(question)
            elif question[4] == "orange":
                orange_questions.append(question)
            elif question[4] == "yellow":
                yellow_questions.append(question)
            elif question[4] == "green":
                green_questions.append(question)
        #adds them together in order after shuffling them to give a random effect
        random.shuffle(red_questions)
        random.shuffle(orange_questions)
        random.shuffle(yellow_questions)
        random.shuffle(green_questions)
        priority_queue = red_questions + orange_questions + yellow_questions + green_questions
        return priority_queue

    def DequeueItem(self, question):
        #dequeues a question from the front of a list
        print("")
