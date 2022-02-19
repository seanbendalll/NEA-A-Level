#a file to implement a priority queue based on the questions in a topic
from model import Model
import random
from block import Question

#Priority queue class.
class PriorityQueue():

    def __init__(self, topic_id):
        self.topic_id = topic_id
        #localises a Model instance to the scope of the class
        self.data_model = Model()
        #initialises and defines the queue.
        self.queue = self.InitialiseQueue()
        self.priority = ["red", "orange", "yellow", "green", ""] #the extra "" is for the prioritisation without getting an index error.

    def InitialiseQueue(self):
        #accesses all the questions under the topicname
        questions = self.data_model.GetAllQuestions(self.topic_id)
        priority_queue = []
        red_questions = []
        orange_questions = []
        yellow_questions = []
        green_questions = []

        #compares the retrieved questions confidence value to a set of concrete values to create the priorityu queue
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

        #adds the lists together in order to generate the priority queue.
        priority_queue = red_questions + orange_questions + yellow_questions + green_questions
        return priority_queue

    def Dequeue(self):
        #dequeues a question from the front of a list and returns it to the program
        question = self.queue[0]
        self.queue.pop(0)
        return question

    def Requeue(self, question_to_insert, new_confidence):

        #tuples are immutable, which is the default fetch datatype from the database.
        #changes it to a list to change the confidence then reinserts it as a tuple.
        question_to_insert = list(question_to_insert)
        question_to_insert[4] = new_confidence
        question_to_insert = tuple(question_to_insert)

        inserted = False
        for question in self.queue:
            #compares the new confidence to the confidences of the questions already in the queue to find the placement of the list.
            if self.priority.index(new_confidence) < self.priority.index(question[4]):
                #if this is run, a place has been found and you can break the requeue loop.
                self.queue.insert(self.queue.index(question), question_to_insert)
                inserted = True
                break
        #if a place hasnt been found, its confidence is most likely green, so it inserts it at the end.
        if inserted == False:
            self.queue.append(question_to_insert)
