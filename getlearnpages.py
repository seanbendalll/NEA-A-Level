#a file for getting the learn pages of the NEA.
from model import Model
import os
from pdf2image import convert_from_path
import pytesseract

data_model = Model()

"""
for topic_name in data_model.GetTopics():
    os.mkdir(f"/Users/seanbendall/Documents/A-Level/Computer Science/NEA/notes/{topic_name}", 0o666)
"""

sub_topics = ["1.1. Programming",
             "1.2. Programming Paradigms",
             "7.1. Data Structures and Abstract Data Types",
             "8.1. Graph-Traversal",
             "8.2. Tree-Traversal",
             "8.3. Reverse Polish",
             "8.4. Searching Algorithms",
             "8.5. Sorting Algorithms",
             "8.6. Optimisation Algorithm",
             "9.1. Abstraction and Automation",
             "9.2. Regular Languages",
             "9.3. Context-Free Languages",
             "9.4. Classification of Algorithms",
             "9.5. A Model of Computation",
             "3.1. Number Systems",
             "3.3. Units of Information",
             "3.2. Number Bases",
             "3.4. Binary Number System",
             "3.5. Information Coding Systems",
             "3.6. Representing Images, Sound and Other Data",
             "4.1. Hardware and Software",
             "4.2. Classification of Programming Languages",
             "4.3. Types of Program Translator",
             "4.4. Logic Gates",
             "4.5. Boolean Algebra",
             "5.1. Internal Hardware Components of A Computer",
             "5.2. The Stored Program Concept",
             "5.3. Structure and Role of the Processor and its Components",
             "5.4. External Hardware Devices",
             "6. Consequences of Uses of Computing",
             "6.1. Communication",
             "10.2. Networking",
             "10.3. The Internet",
             "10.4. The Transmission Control Protocol - Internet Protocol (TCP IP)",
             "11. Fundamentals of Databases",
             "11. Big Data",
             "12.1. Functional Programming Paradigm",
             "12.2. Writing Functional Programs",
             "2. Definitions"
             ]


"""
for sub_topic in sub_topics:
    print(sub_topic)
    #uses the first number in the title of the page to get the main topic it is from
    if sub_topic[1] == ".":
        parent_topic = data_model.GetTopicTitle(sub_topic[0])
    else:
        parent_topic = data_model.GetTopicTitle(sub_topic[:2])

    pages = convert_from_path(rf'/Users/seanbendall/Documents/A-Level/Computer Science/NEA/notes/{parent_topic}/{sub_topic}.pdf', 300)
    n = 1
    for page in pages:
        page.save(f"/Users/seanbendall/Documents/A-Level/Computer Science/NEA/notes/{parent_topic}/{sub_topic} {n}.png", 'PNG')
        n +=1
"""ap
