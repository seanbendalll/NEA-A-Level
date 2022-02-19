#the required imports for the project.
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from model import Model
from functools import partial
from PIL import ImageTk, Image
from PriorityQueue import PriorityQueue
import PyPDF2
import os
from fonts import Fonts
import pdfplumber
from getlearnpages import sub_topics as st

#class for the progress screen
class Progress():

    def __init__(self, root):
        self.root = root

        #localises a data model to the progress screen to access the database
        self.data_model = Model()
        #frame for the progress screen
        self.progress_frame = tk.Frame(self.root)

    #function for the confirmation of the resetting of the topics, to be called upon a reset button being pressed
    def ResetQuestions(self, topic_name):
        confirmation = tk.messagebox.askquestion("Warning", "Are you sure?")
        if confirmation == 'yes':
            #calls the data model to set all the confidences to red
            self.data_model.ResetQuestions(topic_name)

    #adds all the dictionary values, in this case to get the total number of questions in a topic.
    def SumDictionaryKeys(self, dict):
        num = 0
        for value in dict:
            num += dict[value]
        return num

    #function to show the progress given a topic name.
    def ShowProgress(self, topic_name):
        #uses a top level (a separate window) to show the progress for a given subject.
        progress_pane = Toplevel()
        progress_pane.title(f"Progress for {topic_name}")

        #sets the pane to a specific size and makes it so you cannot change the size.
        progress_pane.resizable(False, False)
        pane_size_x = 480
        pane_size_y = 225
        progress_pane.geometry("{}x{}".format(pane_size_x, pane_size_y))

        progress_label = tk.Label(progress_pane, text = f"Progress for - {topic_name}.", height =2,width = 50, font = Fonts().progress_title_font, anchor = "w")
        progress_label.grid(column = 0, row = 0, sticky = "ew", padx = 10, columnspan = 4)

        #add a divider below the progress icon
        separator = ttk.Separator(progress_pane, orient = "horizontal")
        separator.grid(column = 0, row = 1, columnspan = 4, sticky = "ew", padx = 10)

        #calls the data model to get the progress of a given topic.
        progress_dictionary = self.data_model.GetProgress(topic_name)
        red_label = tk.Label(progress_pane, text = f"Very Unconfident = {progress_dictionary['Red']}", font = Fonts().progress_font)
        red_label.grid(column = 0, row = 2, sticky = "w", padx = 10, pady = 7)
        orange_label = tk.Label(progress_pane, text = f"Unconfident = {progress_dictionary['Orange']}", font = Fonts().progress_font)
        orange_label.grid(column = 0, row = 3, sticky = "w", padx = 10, pady = 7)
        yellow_label = tk.Label(progress_pane, text = f"Confident = {progress_dictionary['Yellow']}", font = Fonts().progress_font)
        yellow_label.grid(column = 0, row = 4, sticky = "w", padx = 10, pady = 7)
        green_label = tk.Label(progress_pane, text = f"Very Confident = {progress_dictionary['Green']}", font = Fonts().progress_font)
        green_label.grid(column = 0, row = 5, sticky = "w", padx = 10, pady = 7)

        #creates a percentage shown to show the percentage of questions as green.
        percentage = int(progress_dictionary['Green'] / self.SumDictionaryKeys(progress_dictionary) * 100)
        percentage = tk.Label(progress_pane, text = f"{percentage}%",font = Fonts().percentage_font)
        percentage.grid(column = 2, row = 3, rowspan = 2)
        exit_button = tk.Button(progress_pane, text = "Exit", command = progress_pane.destroy)
        exit_button.grid(column = 3, row = 6, sticky = "se")

    #a function to initialise the progress screen.
    def FormatProgressScreen(self):
        #uses the data model to get all the topics as a list of titles.
        topic_names = self.data_model.GetTopics()

        #the first row should be row 6 - below the title
        row = 6
        #topicID starts as 1, is the same number of topic names and is passed to change test frame.
        topicID = 1
        for topic_name in topic_names:

            #for each topic, adds the following buttons:
            test_label = tk.Label(self.progress_frame,width = 40, text = topic_name)
            test_button = tk.Button(self.progress_frame,width = 15, text = "Click here for progress", command = partial(self.ShowProgress, topic_name))
            go_to_topic_button = tk.Button(self.progress_frame, width = 15, text = "Test yourself", command = partial(ChangeToTestFrame, greeting, topicID))
            reset_topic_button = tk.Button(self.progress_frame, width = 15, text = "Reset topic", command = partial(self.ResetQuestions, topic_name))
            test_label.grid(column = 0, row = row,columnspan = 2)
            test_button.grid(column = 2, row = row, columnspan = 1)
            go_to_topic_button.grid(column = 3, row = row, columnspan = 1)
            reset_topic_button.grid(column = 4, row = row, columnspan = 1)

            row +=1
            topicID += 1

        #a general reset all questions button.
        reset_button = tk.Button(self.progress_frame,width = 30, text = "Reset all to very unconfident", command = partial(self.ResetQuestions, "all"))
        reset_button.grid(column = 0, columnspan = 5, row = 20, pady = 10)

#a class for the test screen.
class Test():

    def __init__(self, root, topic_id):
        self.root = root
        self.data_model = Model()

        #has the three separate files localised to the scope of the test class.
        self.test_frame = tk.Frame(self.root)
        self.question_frame = tk.Frame(self.test_frame)
        self.answer_frame = tk.Frame(self.test_frame)

    #the initial set up of the test screen.
    def Initialise(self, topic_id):
        topic_label = tk.Label(self.test_frame, text = data_model.GetTopicTitle(topic_id) ,height = 1, font = Fonts().topic_font)
        topic_label.grid(column = 0, row = 5, columnspan = 4)
        #the form of question is [QUESTIONID, QUESTIONTEXT, ANSWERTYPE, ANSWER, CONFIDENCE, PAPER]
        #initialises the question queue by making a call to the priority queue file.
        self.question_queue = PriorityQueue(topic_id)
        question = self.question_queue.Dequeue()
        self.DisplayQuestion(question)

    def DisplayImage(self, image_name):
        #images displayed in tkinter must be on a canvas.
        photo_canvas = Canvas(self.answer_frame, width = 1200, height = 300)
        photo_canvas.grid(column = 0, row = 8, columnspan = 4)

        #localises the image to the self container as otherwise it does not display as is cleaned by the garbage collector on images.
        self.img = (Image.open(f'images/{image_name}.png'))

        #imports the image again in a format wherein the image width is retrievable.
        img_for_dimensions = PhotoImage(file = f'images/{image_name}.png')
        img_width = img_for_dimensions.width()
        img_height = img_for_dimensions.height()
        img_hw_ratio = img_width / img_height

        #three categories of image, very tall but slim, square, or very small but wide.
        if img_height < 200:
            self.resized_image = self.img.resize((1000, int(1000 / img_hw_ratio)), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_image)
            photo_canvas.create_image(600,150, image = self.new_image)
        elif img_height >= 200 and img_height <= 300:
            self.resized_image = self.img.resize((300, int(300 / img_hw_ratio)), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_image)
            photo_canvas.create_image(600,150, image = self.new_image)
        elif img_height > 300:
            self.resized_image = self.img.resize((int(300 * img_hw_ratio), 300), Image.ANTIALIAS)
            self.new_image = ImageTk.PhotoImage(self.resized_image)
            photo_canvas.create_image(600,150,  image = self.new_image)


    def DisplayQuestion(self, question):
        #the form of question is [QUESTIONID, QUESTIONTEXT, ANSWERTYPE, ANSWER, CONFIDENCE, PAPER]
        question_label = tk.Label(self.question_frame,font = Fonts().answer_font, width = 75, height = 15, wraplength = 500, text = question[1])
        question_label.grid(column = 0, row = 6, columnspan = 4)
        show_answer_button = tk.Button(self.question_frame, text = "Show Answer", command = partial(self.DisplayAnswer, question))
        show_answer_button.grid(column = 0, row = 7, columnspan = 4)

        #hides the answer frame and shows the question frame.
        self.answer_frame.grid_forget()
        self.question_frame.grid(column = 0, row = 6, columnspan = 4)

    def DisplayAnswer(self, question):

        #cleans up the answer_frame before displaying by forgetting all the widgets inside it.
        for w in self.answer_frame.winfo_children():
            w.grid_forget()

        #hides the question frame and shows the answer frame.
        self.question_frame.grid_forget()
        self.answer_frame.grid(column = 0, row = 6, columnspan = 4)

        question_label = tk.Label(self.answer_frame,text = question[1], font = Fonts().question_alpha_font, width = 75, height = 2)
        question_label.grid(column = 0, row = 7, columnspan =4)

        #if the answer type is image, call the display image function, otherwise just display text.
        if question[2] == "image":
            self.DisplayImage(question[1])
        else:
            answer = tk.Label(self.answer_frame,font = Fonts().answer_font,  width = 75, height = 15, wraplength = 500, text = question[3])
            answer.grid(column = 0, row = 8, columnspan = 4)


        #adds the confidence buttons that will call the update and proceed function when pressed, moving on.
        green_button = tk.Button(self.answer_frame, bg = "green", text = "Very Confident", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "green") )
        orange_button = tk.Button(self.answer_frame, bg = "orange", text = "Confident", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "yellow") )
        yellow_button = tk.Button(self.answer_frame, bg = "yellow", text = "Mediocre", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "orange") )
        red_button = tk.Button(self.answer_frame, bg = "maroon", text = "Unconfident", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "red") )
        green_button.grid(column = 0, row = 9)
        orange_button.grid(column = 1, row = 9)
        yellow_button.grid(column = 2, row = 9)
        red_button.grid(column = 3, row = 9)

        #passes the same confidence again into the update and proceed function, so that it will act unchanged.
        skip_button = tk.Button(self.answer_frame, text = "Skip", command = partial(self.UpdateAndProceed, question, question[4]))
        skip_button.grid(column = 0, row = 10, columnspan = 4, pady = 10)


    def UpdateAndProceed(self, question, new_confidence):
        #calls to the data model to perform an sql function to change the confidence of a given question to the new confidence.
        data_model.UpdateQuestion(question[0], new_confidence)
        self.question_queue.Requeue(question, new_confidence)

        #retrieves a new question from the Priority Queue and displays it by calling the display question function again.
        #this functionality acts as a circular nature.
        new_question = self.question_queue.Dequeue()
        self.DisplayQuestion(new_question)



#a class for the learn screen.
class Learn():

    #the initialise function, formatting all the frames required.
    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.learn_frame = tk.Frame(self.root)
        self.sub_topic_frame = Frame(self.learn_frame)

        #self.top will be the screen to show the notes, a separate window to the main application
        self.top = Toplevel(height = 500, width = 300)
        self.top.resizable(False, False)

        #hides the top level as it will immediately display when run and we only want it to display when prompted to do so.
        self.top.withdraw()
        self.FormatLearnScreen()

    #the initialisation of the learn screen, displaying a list of options.
    def FormatLearnScreen(self):
        #row variable incremented and used to create a list of topics in row format.
        row = 1
        for topic_title in self.data_model.GetTopics():
            row += 1
            topic_button = tk.Button(self.learn_frame, text = f"{topic_title}" ,command = partial(self.DisplaySubTopics, topic_title))
            topic_button.grid(row = row, column = 0, sticky = W)

    #when a topic button is pressed, this function is called to display the sub topics of a given topic.
    def DisplaySubTopics(self, topic_name):
        #displays the sub topic frame, ready to add widgets to it.
        self.sub_topic_frame.grid(column = 1, row = 1, rowspan = 12)

        #hides all the widgets currently in the sub topic frame.
        for widget in self.sub_topic_frame.winfo_children():
            widget.grid_forget()

        #checks if it is a single or double digit id, in order to pass it into getlearnpages.
        if topic_name[1] == " " or topic_name[1] == ".":
            id = topic_name[0] + "."
        else:
            #sets the id to the first two characters.
            id = topic_name[:2]

        row = 1
        #st is the imported list of subtopics outlined in getlearnpages.py
        for sub_topic in st:
            if id == sub_topic[:2]:
                #if the id is the same as the current sub topic, create that subtopic as a button.
                #when this button is pressed, run the display notes button, passing in an initial page number of 1.
                sub_topic_button = tk.Button(self.sub_topic_frame, text = sub_topic, command = partial(self.DisplayNotes,sub_topic, 1))
                sub_topic_button.grid(column = 0, row = row)
                row +=1

    #getlearnpages creates the images from the pdf files, this function will collect the associated images from my files.
    def FetchSubTopicImages(self, sub_topic_name):
        sub_topic_images = []
        #passes the sub_topic_name into the gettopicIdfrom string to return a valid id.
        id = self.GetTopicIDFromString(sub_topic_name)

        #gets all the files inside the topic file with images, and fetches them by comparing their file extension (image) and the contents of the title.
        for file in os.listdir(f"/Users/seanbendall/Documents/A-Level/Computer Science/NEA/notes/{self.data_model.GetTopicTitle(id)}"):
            if file[-4:] == ".png" and sub_topic_name in file:
                sub_topic_images.append(file)

        #sorts them numerically so they are displayed in order.
        sub_topic_images.sort()
        temp = []
        sub_topics_to_remove = []
        #when running the sort function, the pages arent entirely sorted. for example 12 comes before 2, because it starts with 1.
        #the two for loops takes the double id files, removes them and appends them to the end of the list to be ordered.
        for sub_topic in sub_topic_images:
            if sub_topic[-6] != " ":
                sub_topics_to_remove.append(sub_topic)
                temp.append(sub_topic)

        for sub_topic in sub_topics_to_remove:
            sub_topic_images.remove(sub_topic)

        #combines the current images and the list of double id images.
        sub_topic_images = sub_topic_images + temp
        return sub_topic_images

    #function to move back or forward, modifying the page number.
    def UpdatePage(self, sub_topic_name, page_number):
        if page_number >= 1 and page_number <= len(self.FetchSubTopicImages(sub_topic_name)):
            self.DisplayNotes(sub_topic_name, page_number)

    #takes a sub_topic_name and returns its id, first checking if its a double digit id or a single digit id.
    def GetTopicIDFromString(self, sub_topic_name):
        if sub_topic_name[1] == " " or sub_topic_name[1] == ".":
            id = sub_topic_name[0]
        else:
            id = sub_topic_name[:2]
        return id

    #a function for displaying the notes, given a page number and the sub topic to find.
    def DisplayNotes(self, sub_topic_name, page_number):
        #gets the topic_name using the primary key id and gets the page id for the subtopic.
        id = self.GetTopicIDFromString(sub_topic_name)
        topic_name = data_model.GetTopicTitle(id)
        sub_topic_images = self.FetchSubTopicImages(sub_topic_name)

        #displays the top level.
        self.top.state(newstate = "normal")

        #creates a canvas for the display of the image.
        canvas = Canvas(self.top, width = 550, height = 800)
        canvas.grid(column = 0,row = 0, columnspan = 4)

        #fetches the image from the corresponding file path, resizes it, and then displays it on the top level.
        img = (Image.open(f'/Users/seanbendall/Documents/A-Level/Computer Science/NEA/notes/{topic_name}/{sub_topic_images[page_number -1]}'))
        resized_image = img.resize((550, 800))
        new_image = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0,0, anchor = NW, image = new_image)

        page_label = tk.Label(self.top, text = f"Page {page_number}/{len(sub_topic_images)}", width = 10)
        page_label.grid(column = 0, row = 1, pady = 10)

        #adds the forward and back buttons so that the user can navigate between pages.
        next_page = tk.Button(self.top, text = "Next Page", width = 10, command = partial(self.UpdatePage, sub_topic_name, page_number + 1))
        next_page.grid(column = 2, row = 1, pady = 10)
        previous_page = tk.Button(self.top, text = "Previous Page", width = 10, command = partial(self.UpdatePage, sub_topic_name, page_number -1))
        previous_page.grid(column = 1 ,row = 1, pady = 10)
        #an exit button, as the close button will terminate the window rather than withdrawing it.
        exit_button = tk.Button(self.top, text = "Exit", width = 10, command = self.top.withdraw)
        exit_button.grid(column = 3, row = 1, pady = 10)
        self.top.mainloop()


#a class for the home screen.
class Home():

    #initialises the initial frames and formats the main screen.
    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.home_frame = tk.Frame(self.root)
        self.FormatHomeScreen()

    #initial display of the home screen.
    def FormatHomeScreen(self):
        title_label = tk.Label(self.home_frame, text = "ALCA - A Level Computer Science Application", font = Fonts().main_font)
        title_label.grid(column = 0, row = 0)

        desc = """
        Hello, and welcome to ALCA, an AQA A-Level Computer Science flashcard app. Answer questions, learn from notes, and track your progress, in this all in one revision app.
        """
        description = tk.Label(self.home_frame, text = desc, font = Fonts().description_font, wraplength = 1000)
        description.grid(column = 0, row = 1)

        canvas = Canvas(self.home_frame, width = 600, height = 300)
        canvas.grid(column = 0,row = 2)

        #displays the logo.
        self.img = (Image.open(r'/Users/seanbendall/Documents/A-Level/Computer Science/NEA/ALCALogo.png'))
        self.resized_image = self.img.resize((600, 300))
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        canvas.create_image(0,0, anchor = NW, image = self.new_image)

        progress_display_label = tk.Label(self.home_frame, text = "Current Overall Progress: ")
        progress_display_label.grid(column = 0, row = 3, pady = (0,20))
        progress_canvas = Canvas(self.home_frame, width = 1000, height = 20)
        progress_canvas.grid(column = 0, row = 4)


        #initial values for the red orange yellow and green totals.
        red_total = 0
        orange_total = 0
        yellow_total = 0
        green_total = 0

        #goes through every topic inside the data model, getting the progress of said topic, and adding the values it returns for the
        #red, yellow, orange and green confidences to the total values
        for topic in data_model.GetTopics():
            progress_for_subject = data_model.GetProgress(topic)
            red_total += progress_for_subject["Red"]
            orange_total += progress_for_subject["Orange"]
            yellow_total += progress_for_subject["Yellow"]
            green_total += progress_for_subject["Green"]

        #uses the confidence total values to display a total bar like image for the total progress.
        #width of first one, the red bar, is all the questions added together
        self.progress_img = Image.new("RGB", (red_total + orange_total + yellow_total + green_total, 20), "#FF0000")

        #overlays the current red bar with the orange bar, where the orange bar is the total of all the orange, green and yellow confidences.
        self.progress_img.paste((256,165, 0), (0, 0, orange_total + yellow_total + green_total, 20)) #orange bar

        #repeats the overlay process with the other two colours.
        self.progress_img.paste((256,256, 0), (0, 0, yellow_total + green_total, 20)) #yellow bar
        self.progress_img.paste((0,256, 0), (0, 0, green_total, 20)) #green bar

        #saves the image and displays it by importing it.
        self.progress_img.save("progress.png")
        self.progress_display = ImageTk.PhotoImage((Image.open(r'/Users/seanbendall/Documents/A-Level/Computer Science/NEA/progress.png')))
        progress_canvas.create_image(500, 0, image = self.progress_display)

#initial application set up.
def RootInitialisation():
    root = tk.Tk()
    root.title("ALCA - A Level Computer Science Application")
    root.resizable(False, False)
    root_size_x = 1300
    root_size_y = 750
    root.geometry("{}x{}".format(root_size_x, root_size_y))
    return root

#function for changing to home frame.
def ChangeToHomeFrame(label):

    #shows the home frame and hides all the others
    home_frame.grid(column = 0, row = 5, columnspan = 4)
    test_frame.grid_forget()
    learn_frame.grid_forget()
    progress_frame.grid_forget()
    UpdateLabel("home", label)

#function for changing the test frame.
def ChangeToTestFrame(label, topic_id):
    #hides all the current widgets on the test frame
    for w in test_frame.winfo_children():
        w.grid_forget()
    test_frame.grid(column = 0, row = 5, columnspan = 4)
    home_frame.grid_forget()
    learn_frame.grid_forget()
    progress_frame.grid_forget()
    UpdateLabel("test", label)

    #upon initialisation, an invalid topic id of -1 will be passed, meaning the general topics must be shown for selection.
    if topic_id == -1:
        #set general menu
        topic_names = data_model.GetTopics()
        id = 1
        #creates all the choosable buttons.
        for topic_name in topic_names:
            but = tk.Button(test_frame, text = topic_name, width = 35, height = 2, command = partial(ChangeToTestFrame, label, id))
            but.grid(column = 0, row = id, columnspan = 4)
            id += 1
    #if the topic id is valid, initialise the test screen with the chosen topic.
    else:
        test.Initialise(topic_id)

def ChangeToLearnFrame(label):
    #hides all other frames and shows the learn one.
    learn_frame.grid(column = 0, row = 5, columnspan = 4)
    test_frame.grid_forget()
    home_frame.grid_forget()
    progress_frame.grid_forget()
    UpdateLabel("learn", label)

def ChangeToProgressFrame(label):
    #hides all other frames and shows the progress one.
    progress_frame.grid(column = 0, row = 5, columnspan = 4)
    home_frame.grid_forget()
    learn_frame.grid_forget()
    test_frame.grid_forget()

    #calls the function inside the progress class to format the screen.
    progress.FormatProgressScreen()
    UpdateLabel("progress", label)

#the menu will sit on the root of the application at the top, allowing as a tab bar menu.
def InitialiseMenu(root, greeting):

    #adds the home, test, learn and progress screen buttons that will call their corresponding change to (FRAME NAME) frame function.
    home_screen_button_h = tk.Button(root, text = "HOME", width = 32, height = 2, command = partial(ChangeToHomeFrame, greeting))
    test_screen_button_h = tk.Button(root, text = "TEST", width = 32, height = 2, command = partial(ChangeToTestFrame, greeting, -1))
    learn_screen_button_h = tk.Button(root, text = "LEARN", width = 32, height = 2, command = partial(ChangeToLearnFrame, greeting))
    progress_screen_button_h = tk.Button(root, text = "PROGRESS", width = 32, height = 2, command = partial(ChangeToProgressFrame, greeting))


    home_screen_button_h.grid(column = 0, row = 1)
    test_screen_button_h.grid(column = 1, row = 1)
    learn_screen_button_h.grid(column = 2, row = 1)
    progress_screen_button_h.grid(column = 3, row = 1)

    #uses the updated ttk module to include a separator.
    separator = ttk.Separator(root, orient = "horizontal")
    separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)

#changes the rooted label text value to display the current screen the user is on.
def UpdateLabel(frame_name, label):
    label['text'] = f"{frame_name.upper()} SCREEN"

#initialises a global data model using the imported model class.
data_model = Model()
root = RootInitialisation()

#creates the frames and their objects, creating global references to their local frames, in order to hide them.
test = Test(root, 1)
test_frame = test.test_frame
home = Home(root)
home_frame = home.home_frame
progress = Progress(root)
progress_frame = progress.progress_frame
learn = Learn(root)
learn_frame = learn.learn_frame

#sets the initial global greeting label.
greeting = tk.Label(root, text=f"Welcome to home Screen", height = 2, font = Fonts().title_font)
greeting.grid(column = 0, row = 0, columnspan = 4)
InitialiseMenu(root, greeting)

#changes to the home screen for the first time.
ChangeToHomeFrame(greeting)

#runs the mainloop, meaning it will not terminate, and will show all widgets until instructed not to.
root.mainloop()
