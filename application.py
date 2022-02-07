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
        #self.InitialiseBaseFrame()

    def ResetQuestions(self):
        confirmation = tk.messagebox.askquestion("Warning", "Are you sure?")
        if confirmation == 'yes':
            self.data_model.ResetQuestions()

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
            test_label.grid(column = 0, row = row,columnspan = 2)
            test_button.grid(column = 2, row = row, columnspan = 1)
            go_to_topic_button.grid(column = 3, row = row, columnspan = 1)

            row +=1

        reset_button = tk.Button(self.progress_frame, text = "Reset all to very unconfident", command = self.ResetQuestions)
        reset_button.grid(column = 0, columnspan = 4, row = 20, pady = 10)
class Test():

    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.test_frame = tk.Frame(self.root)
        #self.InitialiseBaseFrame()

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

def ChangeToTestFrame(label):
    test_frame.grid(column = 0, row = 5, columnspan = 4)
    home_frame.grid_forget()
    learn_frame.grid_forget()
    progress_frame.grid_forget()
    UpdateLabel("test", label)

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
    test_screen_button_h = tk.Button(root, text = "TEST", width = 32, height = 2, command = partial(ChangeToTestFrame, greeting))
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




#MARK - TEST SCREEN CODE
"""
greeting_for_test = tk.Label(test_frame, text="TEST", height = 2, font = Fonts().title_font)
home_screen_button_t = tk.Button(test_frame, text = "HOME", width = 32, height = 2, command = ChangeToHomeFrame)
test_screen_button_t = tk.Button(test_frame, text = "TEST", width = 32, height = 2, command = ChangeToTestFrame)
learn_screen_button_t = tk.Button(test_frame, text = "LEARN", width = 32, height = 2, command = ChangeToLearnFrame)
progress_screen_button_t = tk.Button(test_frame, text = "PROGRESS", width = 32, height = 2, command = ChangeToProgressFrame)

greeting_for_test.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_t.grid(column = 0, row = 1)
test_screen_button_t.grid(column = 1, row = 1)
learn_screen_button_t.grid(column = 2, row = 1)
progress_screen_button_t.grid(column = 3, row = 1)
separator = ttk.Separator(test_frame, orient = "horizontal")
separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)
topic_label = tk.Label(test_frame, text = "TOPIC NAME HERE" ,height = 1, font = Fonts().topic_font)
topic_label.grid(column = 0, row = 5, columnspan = 4)
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


#MARK - LEARN SCREEN CODE
"""
greeting_for_learn = tk.Label(learn_frame, text="Welcome to learn screen", height = 2, font = Fonts().title_font)
home_screen_button_l = tk.Button(learn_frame, text = "HOME", width = 32, height = 2, command = ChangeToHomeFrame)
test_screen_button_l = tk.Button(learn_frame, text = "TEST", width = 32, height = 2, command = ChangeToTestFrame)
learn_screen_button_l = tk.Button(learn_frame, text = "LEARN", width = 32, height = 2, command = ChangeToLearnFrame)
progress_screen_button_l = tk.Button(learn_frame, text = "PROGRESS", width = 32, height = 2, command = ChangeToProgressFrame)

separator = ttk.Separator(learn_frame, orient = "horizontal")
separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)
greeting_for_learn.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_l.grid(column = 0, row = 1)
test_screen_button_l.grid(column = 1, row = 1)
learn_screen_button_l.grid(column = 2, row = 1)
progress_screen_button_l.grid(column = 3, row = 1)
"""



#MARK - PROGRESS SCREEN CODE
"""
greeting_for_progress = tk.Label(progress_frame, text="Welcome to progress screen", height = 2, font = title_font)
home_screen_button_p = tk.Button(progress_frame, text = "HOME", width = 32, height = 2, command = ChangeToHomeFrame)
test_screen_button_p = tk.Button(progress_frame, text = "TEST", width = 32, height = 2, command = ChangeToTestFrame)
learn_screen_button_p = tk.Button(progress_frame, text = "LEARN", width = 32, height = 2, command = ChangeToLearnFrame)
progress_screen_button_p = tk.Button(progress_frame, text = "PROGRESS", width = 32, height = 2, command = ChangeToProgressFrame)
separator = ttk.Separator(progress_frame, orient = "horizontal")
separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)

greeting_for_progress.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_p.grid(column = 0, row = 1)
test_screen_button_p.grid(column = 1, row = 1)
learn_screen_button_p.grid(column = 2, row = 1)
progress_screen_button_p.grid(column = 3, row = 1)

"""
"""
def ResetQuestions():
    confirmation = messagebox.askquestion("Warning", "Are you sure?")
    if confirmation == 'yes':
        data_model.ResetQuestions()
    """
"""
def SumDictionaryKeys(dict):
    num = 0
    for value in dict:
        num += dict[value]
    return num
"""
"""
def showProgress(topic_name):
    #progress pane modification
    progress_pane = Toplevel()
    progress_pane.title(f"Progress for {topic_name}")
    progress_pane.resizable(False, False)
    pane_size_x = 480
    pane_size_y = 225
    progress_pane.geometry("{}x{}".format(pane_size_x, pane_size_y))

    #adds the title of the progress tab
    progress_title_font = tk.font.Font(family = "Helvetica", size = 16, weight = "bold")
    progress_font = tk.font.Font(family = "Helvetica", size = 14)
    progress_label = tk.Label(progress_pane, text = f"Progress for - {topic_name}.", height =2,width = 50, font = Fonts().progress_title_font, anchor = "w")
    progress_label.grid(column = 0, row = 0, sticky = "ew", padx = 10, columnspan = 4)

    #add a divider below the progress icon
    separator = ttk.Separator(progress_pane, orient = "horizontal")
    separator.grid(column = 0, row = 1, columnspan = 4, sticky = "ew", padx = 10)

    progress_dictionary = data_model.GetProgress(topic_name)
    red_label = tk.Label(progress_pane, text = f"Very Unconfident = {progress_dictionary['Red']}", font = Fonts().progress_font)
    red_label.grid(column = 0, row = 2, sticky = "w", padx = 10, pady = 7)
    orange_label = tk.Label(progress_pane, text = f"Unconfident = {progress_dictionary['Orange']}", font = Fonts().progress_font)
    orange_label.grid(column = 0, row = 3, sticky = "w", padx = 10, pady = 7)
    yellow_label = tk.Label(progress_pane, text = f"Confident = {progress_dictionary['Yellow']}", font = Fonts().progress_font)
    yellow_label.grid(column = 0, row = 4, sticky = "w", padx = 10, pady = 7)
    green_label = tk.Label(progress_pane, text = f"Very Confident = {progress_dictionary['Green']}", font = Fonts().progress_font)
    green_label.grid(column = 0, row = 5, sticky = "w", padx = 10, pady = 7)

    percentage = int(progress_dictionary['Green'] / SumDictionaryKeys(progress_dictionary) * 100)
    percentage_font = tk.font.Font(family = "Helvetica", size = 36)
    percentage = tk.Label(progress_pane, text = f"{percentage}%",font = Fonts().percentage_font)
    percentage.grid(column = 2, row = 3, rowspan = 2)


    exit_button = tk.Button(progress_pane, text = "Exit", command = progress_pane.destroy)
    exit_button.grid(column = 3, row = 6, sticky = "se")
    Toplevel.mainloop(root)

"""
"""
def FormatProgressScreen():

    topic_names = data_model.GetTopics()
    #the first row should be row 6 - below the title
    row = 6
    for topic_name in topic_names:

        test_label = tk.Label(progress_frame,width = 40, text = topic_name)
        arguments = partial(showProgress, topic_name)
        test_button = tk.Button(progress_frame,width = 15, text = "Click here for progress", command = arguments)
        go_to_topic_button = tk.Button(progress_frame, width = 15, text = "Test yourself")
        test_label.grid(column = 0, row = row,columnspan = 2)
        test_button.grid(column = 2, row = row, columnspan = 1)
        go_to_topic_button.grid(column = 3, row = row, columnspan = 1)

        row +=1
    reset_button = tk.Button(progress_frame, text = "Reset all to very unconfident", command = ResetQuestions)
    reset_button.grid(column = 0, columnspan = 4, row = 20, pady = 10)
"""
#main startup
#application = Application()
"""
home_frame.pack(fill = "both") #pack the frames but grid the stuff within the frames
root.mainloop()
"""
