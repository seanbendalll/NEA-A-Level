class Block:
    def __init__(self, block_id, block_type, has_children, content, topic, is_answer):
        self.block_id = block_id
        self.block_type = block_type
        self.has_children = has_children
        self.content = content
        self.topic = topic
        self.is_answer = is_answer

    def __str__(self):
        return str("Block(" + self.block_id + ", " + self.block_type + ", " + str(self.has_children) + ", " + self.content + ", " + self.topic + ", " + str(self.is_answer) + ")")

    def getAnswer(self):
        #if the answer is in bold or an image it is the answer
        answer = []
        answer_type = ''

        return (answer, answer_type)

class Question:
    def __init__(self, topic, question, answer_type, answer):
        self.topic = topic
        self.question = question
        self.answer_type = answer_type
        self.answer = answer

    def __str__(self):
        return str("Question(" + self.topic + ", "  + self.question + ", " + self.answer_type + ", " + self.answer + ")")

"""

QUESTION LOOKS LIKE

Question(1 Fundamentals of programming, What is a text file, text, a text file may have several text fields...)
"""
