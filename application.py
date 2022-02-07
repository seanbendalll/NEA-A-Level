import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from model import Model
from functools import partial
from PIL import ImageTk, Image
from PriorityQueue import PriorityQueue


from fonts import Fonts

class Progress():

    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.progress_frame = tk.Frame(self.root)

    def ResetQuestions(self, topic_name):
        confirmation = tk.messagebox.askquestion("Warning", "Are you sure?")
        if confirmation == 'yes':
            self.data_model.ResetQuestions(topic_name)

    def SumDictionaryKeys(self, dict):
        num = 0
        for value in dict:
            num += dict[value]
        return num

    def ShowProgress(self, topic_name):
        #progress pane modification
        progress_pane = Toplevel()
        progress_pane.title(f"Progress for {topic_name}")
        progress_pane.resizable(False, False)
        pane_size_x = 480
        pane_size_y = 225
        progress_pane.geometry("{}x{}".format(pane_size_x, pane_size_y))

        progress_label = tk.Label(progress_pane, text = f"Progress for - {topic_name}.", height =2,width = 50, font = Fonts().progress_title_font, anchor = "w")
        progress_label.grid(column = 0, row = 0, sticky = "ew", padx = 10, columnspan = 4)

        #add a divider below the progress icon
        separator = ttk.Separator(progress_pane, orient = "horizontal")
        separator.grid(column = 0, row = 1, columnspan = 4, sticky = "ew", padx = 10)

        progress_dictionary = self.data_model.GetProgress(topic_name)
        red_label = tk.Label(progress_pane, text = f"Very Unconfident = {progress_dictionary['Red']}", font = Fonts().progress_font)
        red_label.grid(column = 0, row = 2, sticky = "w", padx = 10, pady = 7)
        orange_label = tk.Label(progress_pane, text = f"Unconfident = {progress_dictionary['Orange']}", font = Fonts().progress_font)
        orange_label.grid(column = 0, row = 3, sticky = "w", padx = 10, pady = 7)
        yellow_label = tk.Label(progress_pane, text = f"Confident = {progress_dictionary['Yellow']}", font = Fonts().progress_font)
        yellow_label.grid(column = 0, row = 4, sticky = "w", padx = 10, pady = 7)
        green_label = tk.Label(progress_pane, text = f"Very Confident = {progress_dictionary['Green']}", font = Fonts().progress_font)
        green_label.grid(column = 0, row = 5, sticky = "w", padx = 10, pady = 7)

        percentage = int(progress_dictionary['Green'] / self.SumDictionaryKeys(progress_dictionary) * 100)
        percentage = tk.Label(progress_pane, text = f"{percentage}%",font = Fonts().percentage_font)
        percentage.grid(column = 2, row = 3, rowspan = 2)


        exit_button = tk.Button(progress_pane, text = "Exit", command = progress_pane.destroy)
        exit_button.grid(column = 3, row = 6, sticky = "se")
        Toplevel.mainloop(self.root)

    def FormatProgressScreen(self):

        topic_names = self.data_model.GetTopics()
        #the first row should be row 6 - below the title
        row = 6
        for topic_name in topic_names:

            test_label = tk.Label(self.progress_frame,width = 40, text = topic_name)
            arguments = partial(self.ShowProgress, topic_name)
            test_button = tk.Button(self.progress_frame,width = 15, text = "Click here for progress", command = arguments)
            go_to_topic_button = tk.Button(self.progress_frame, width = 15, text = "Test yourself")
            reset_topic_button = tk.Button(self.progress_frame, width = 15, text = "Reset topic", command = partial(self.ResetQuestions, topic_name))
            test_label.grid(column = 0, row = row,columnspan = 2)
            test_button.grid(column = 2, row = row, columnspan = 1)
            go_to_topic_button.grid(column = 3, row = row, columnspan = 1)
            reset_topic_button.grid(column = 4, row = row, columnspan = 1)

            row +=1

        reset_button = tk.Button(self.progress_frame,width = 30, text = "Reset all to very unconfident", command = partial(self.ResetQuestions, "all"))
        reset_button.grid(column = 0, columnspan = 5, row = 20, pady = 10)

class Test():

    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.test_frame = tk.Frame(self.root)
        self.question_frame = tk.Frame(self.test_frame)
        self.answer_frame = tk.Frame(self.test_frame)

    def Main(self, topic_id):
        topic_label = tk.Label(self.test_frame, text = data_model.GetTopicTitle(topic_id) ,height = 1, font = Fonts().topic_font)
        topic_label.grid(column = 0, row = 5, columnspan = 4)
        question_queue = PriorityQueue(topic_id)

        question = question_queue.Dequeue()
        self.DisplayQuestion(question)
        print("hello")

    def DisplayImage(self, image_name):

        photo_canvas = Canvas(answer_frame, width = 1200, height = 400)
        photo_canvas.grid(column = 0, row = 6, columnspan = 4)
        img = (Image.open(f'images/{image_name}.png'))
        img_for_dimensions = PhotoImage(file = f'images/{image_name}.png')
        img_width = img_for_dimensions.width()
        img_height = img_for_dimensions.height()
        img_hw_ratio = round(img_width / img_height)
        print("width is ", img_width, " and image height is ", img_height)
        print(img_hw_ratio)

        if img_height < 300:
            resized_image = img.resize((1000, int(1000 / img_hw_ratio)), Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(resized_image)
            photo_canvas.create_image(100,10, anchor = NW, image = new_image)
        elif img_height > 300:
            resized_image = img.resize((int(350 * img_hw_ratio), 350), Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(resized_image)
            photo_canvas.create_image(425,10, anchor = NW, image = new_image)

    def DisplayQuestion(self, question):

        self.answer_frame.grid_forget()
        question_label = tk.Label(self.question_frame,font = Fonts().answer_font, width = 75, height = 15, wraplength = 500, text = question.question)
        question_label.grid(column = 0, row = 6, columnspan = 4)
        show_answer_button = tk.Button(self.question_frame, text = "Show Answer", command = partial(self.DisplayAnswer, question))
        show_answer_button.grid(column = 0, row = 7, columnspan = 4)
        self.question_frame.grid(column = 0, row = 6, columnspan = 4)

    def DisplayAnswer(self, question):

        self.question_frame.grid_forget()
        self.answer_frame.grid(column = 0, row = 6, columnspan = 4)

        question_label = tk.Label(self.answer_frame,text = question.question, font = Fonts().question_alpha_font, width = 75, height = 2)
        question_label.grid(column = 0, row = 7, columnspan =4)

        if question.answer_type == "image":
            self.DisplayImage(question.answer)
        else:
            answer = tk.Label(self.answer_frame,font = Fonts().answer_font,  width = 75, height = 15, wraplength = 500, text = question.answer)
            answer.grid(column = 0, row = 8, columnspan = 4)


        green_button = tk.Button(self.answer_frame, bg = "green", text = "Very Confident", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "green") )
        orange_button = tk.Button(self.answer_frame, bg = "orange", text = "Confident", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "yellow") )
        yellow_button = tk.Button(self.answer_frame, bg = "yellow", text = "Mediocre", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "orange") )
        red_button = tk.Button(self.answer_frame, bg = "maroon", text = "Unconfident", height = 5, width = 15, command = partial(self.UpdateAndProceed, question, "red") )
        green_button.grid(column = 0, row = 9)
        orange_button.grid(column = 1, row = 9)
        yellow_button.grid(column = 2, row = 9)
        red_button.grid(column = 3, row = 9)

        skip_button = tk.Button(self.answer_frame, text = "Skip")
        skip_button.grid(column = 0, row = 10, columnspan = 4, pady = 10)

    def UpdateAndProceed(self, question, new_confidence):
        data_model.UpdateQuestion(question.question, new_confidence)





class Learn():

    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.learn_frame = tk.Frame(self.root)
        #self.InitialiseBaseFrame()

class Home():

    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.home_frame = tk.Frame(self.root)

def RootInitialisation():
    root = tk.Tk()
    root.title("ALCA - A Level Computer Science Application")
    root.resizable(False, False)
    root_size_x = 1300
    root_size_y = 750
    root.geometry("{}x{}".format(root_size_x, root_size_y))
    return root

def ChangeToHomeFrame(label):
    home_frame.grid(column = 0, row = 5, columnspan = 4)
    test_frame.grid_forget()
    learn_frame.grid_forget()
    progress_frame.grid_forget()
    UpdateLabel("home", label)

def ChangeToTestFrame(label, topic_id):
    test_frame.grid(column = 0, row = 5, columnspan = 4)
    home_frame.grid_forget()
    learn_frame.grid_forget()
    progress_frame.grid_forget()
    UpdateLabel("test", label)
    test.Main(topic_id)

def ChangeToLearnFrame(label):
    learn_frame.grid(column = 0, row = 5, columnspan = 4)
    test_frame.grid_forget()
    home_frame.grid_forget()
    progress_frame.grid_forget()
    UpdateLabel("learn", label)

def ChangeToProgressFrame(label):
    progress_frame.grid(column = 0, row = 5, columnspan = 4)
    home_frame.grid_forget()
    learn_frame.grid_forget()
    test_frame.grid_forget()
    progress.FormatProgressScreen()
    UpdateLabel("progress", label)

def InitialiseMenu(root, greeting):
    home_screen_button_h = tk.Button(root, text = "HOME", width = 32, height = 2, command = partial(ChangeToHomeFrame, greeting))
    test_screen_button_h = tk.Button(root, text = "TEST", width = 32, height = 2, command = partial(ChangeToTestFrame, greeting, 1))
    learn_screen_button_h = tk.Button(root, text = "LEARN", width = 32, height = 2, command = partial(ChangeToLearnFrame, greeting))
    progress_screen_button_h = tk.Button(root, text = "PROGRESS", width = 32, height = 2, command = partial(ChangeToProgressFrame, greeting))


    home_screen_button_h.grid(column = 0, row = 1)
    test_screen_button_h.grid(column = 1, row = 1)
    learn_screen_button_h.grid(column = 2, row = 1)
    progress_screen_button_h.grid(column = 3, row = 1)
    separator = ttk.Separator(root, orient = "horizontal")
    separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)


def UpdateLabel(frame_name, label):
    label['text'] = f"Welcome to the {frame_name} screen"


data_model = Model()
root = RootInitialisation()
test = Test(root)
test_frame = test.test_frame
home = Home(root)
home_frame = home.home_frame
progress = Progress(root)
progress_frame = progress.progress_frame
learn = Learn(root)
learn_frame = learn.learn_frame
greeting = tk.Label(root, text=f"Welcome to home Screen", height = 2, font = Fonts().title_font)
greeting.grid(column = 0, row = 0, columnspan = 4)
InitialiseMenu(root, greeting)
ChangeToHomeFrame(greeting)
root.mainloop()
#TEST CODE
"""
def ShowAnswer():
    question_frame.grid_forget()
    answer_frame.grid(column = 0, row = 6, columnspan = 4)

def ShowQuestion():
    answer_frame.grid_forget()
    question_frame.grid(column = 0, row = 6, columnspan = 4)
"""




"""
#CODE FOR WHEN ANSWER IS NOT SHOWN
question_frame = tk.Frame(test_frame)
question_label = tk.Label(question_frame,width = 75, height = 20, wraplength = 500, text = "qweuquefhysdfgysgyfugyuyyyugyuyuggyugyugyugyugyuuiawdhfuiashdfuiahsdfuihaisdufhasdfshadfjihasdjihasduifhhuiasdffhuiasdfihuasdfhuiasdf")
question_label.grid(column = 0, row = 6, columnspan = 4)
show_answer_button = tk.Button(question_frame, text = "Show Answer", command = ShowAnswer)
show_answer_button.grid(column = 0, row = 7, columnspan = 4)
question_frame.grid(column = 0, row = 6, columnspan = 4)



#CODE FOR WHEN ANSWER IS SHOWN
answer_frame = tk.Frame(test_frame)


def DisplayImage(image_name):

    photo_canvas = Canvas(answer_frame, width = 1200, height = 400)
    photo_canvas.grid(column = 0, row = 6, columnspan = 4)
    img = (Image.open(f'images/{image_name}.png'))
    img_for_dimensions = PhotoImage(file = f'images/{image_name}.png')
    img_width = img_for_dimensions.width()
    img_height = img_for_dimensions.height()
    img_hw_ratio = round(img_width / img_height)
    print("width is ", img_width, " and image height is ", img_height)
    print(img_hw_ratio)

    if img_height < 300:
        resized_image = img.resize((1000, int(1000 / img_hw_ratio)), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        photo_canvas.create_image(100,10, anchor = NW, image = new_image)
    elif img_height > 300:
        resized_image = img.resize((int(350 * img_hw_ratio), 350), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        photo_canvas.create_image(425,10, anchor = NW, image = new_image)


green_button = tk.Button(answer_frame, bg = "green", text = "Very Confident", height = 5, width = 15)
orange_button = tk.Button(answer_frame, bg = "orange", text = "Confident", height = 5, width = 15)
yellow_button = tk.Button(answer_frame, bg = "yellow", text = "Mediocre", height = 5, width = 15)
red_button = tk.Button(answer_frame, bg = "maroon", text = "Unconfident", height = 5, width = 15)
green_button.grid(column = 0, row = 7)
orange_button.grid(column = 1, row = 7)
yellow_button.grid(column = 2, row = 7)
red_button.grid(column = 3, row = 7)

skip_button = tk.Button(answer_frame, text = "Skip")
skip_button.grid(column = 0, row = 8, columnspan = 4, pady = 10)
"""

#main startup
#application = Application()
"""
home_frame.pack(fill = "both") #pack the frames but grid the stuff within the frames
root.mainloop()
"""
