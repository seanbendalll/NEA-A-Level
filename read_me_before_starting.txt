14.12.21:
- fixed the definequestion function, and it will now take a block and give a result for all the questions within that block successfully
- need to work on the fact that the questions have void subtopics and topics, and find a way of passing the topic through to all the questions.
- try and improve efficiency, potentially?

15.12.21:
- fixed the subtopic and topics issue, getting rid of the sub topics entirely and filtering the topic parameter through the code
- now we just need to bold out the questions in the notion documents
- clean up the fetch.py file
- come up with an idea for how to put it in said database.

18.12.21:
- the subtopic and topic issue was not fixed, as we had not changed the question class
- worked on bolding out questions in the notion documents, made progress

20.12.21:
- full list of questions acquired

25.1.22:
- need to create sql database filled with all the questions
- we have a list of blocks, containing the questions. The questions have a topic, an answer, a question, and an answer_type.
- work on creating user interface using tkinter
- tkinter currently not working, maybe wrong version of python? try fix.
- try to implement version control.

26.1.22:
- version control implemented
- user interface in progress
- user interface initial completed, menu with changing views working
- need to work on test screen first
- work on data model.

27.1.22:
- need to build a data model
- started to build a data model
- data functions working.
- need to finish data model.

28.1.22:
- continued working on data model. question system works
- need to delete the initial questions table and remake it.
- get topicID function returning nothing.
- the error at the moment is the length of the answer type is too limited - need to just use image and (ELSE)

29.1.22:
- data model completed
- can start working on implementation within the app
- need to clean up the code.
