#a file to implement a priority queue based on the questions in a topic
from model import Model
import random
from block import Question

class PriorityQueue():

    def __init__(self, topic_id):
        self.topic_id = topic_id
        self.data_model = Model()
        self.queue = self.InitialiseQueue()
        self.priority = ["red", "orange", "yellow", "green", ""]

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

    def Dequeue(self):
        #dequeues a question from the front of a list
        question = self.queue[0]
        self.queue.pop(0)
        return question

    def Requeue(self, question_to_insert, new_confidence):
        print("queue before is: \n\n ")
        question_to_insert = list(question_to_insert)
        question_to_insert[4] = new_confidence
        question_to_insert = tuple(question_to_insert)
        for question in self.queue:
            print(question[1] ," : ", question[3], " with confidence ", question[4])


        inserted = False
        for question in self.queue:
            if self.priority.index(new_confidence) < self.priority.index(question[4]):
                self.queue.insert(self.queue.index(question), question_to_insert)
                inserted = True
                break
        if inserted == False:
            self.queue.append(question_to_insert)
        print("queue after is: \n\n ")
        for question in self.queue:
            print(question[1] ," : ", question[3], " with confidence ", question[4])
