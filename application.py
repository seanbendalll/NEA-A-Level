import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
from model import Model

root = tk.Tk()
root.title("ALCA - A Level Computer Science Application")
root.resizable(False, False)
root_size_x = 865
root_size_y = 700
root.geometry("{}x{}".format(root_size_x, root_size_y))

data_model = Model()

def showAnswer():
    question_frame.grid_forget()
    answer_frame.grid(column = 0, row = 6, columnspan = 4)

def showQuestion():
    answer_frame.grid_forget()
    question_frame.grid(column = 0, row = 6, columnspan = 4)

def change_to_home_frame():
    home_frame.pack(fill = "both")
    test_frame.forget()
    learn_frame.forget()
    progress_frame.forget()

def change_to_test_frame():
    test_frame.pack(fill = "both")
    home_frame.forget()
    learn_frame.forget()
    progress_frame.forget()
    showQuestion()

def change_to_learn_frame():
    learn_frame.pack(fill = "both")
    test_frame.forget()
    home_frame.forget()
    progress_frame.forget()

def change_to_progress_frame():
    progress_frame.pack(fill = "both")
    home_frame.forget()
    learn_frame.forget()
    test_frame.forget()
    FormatProgressScreen()

title_font = tk.font.Font(family = "Helvetica", size = 36, weight = "bold")
topic_font = tk.font.Font(family = "Helvetica", size = 28)

#using frames to give a multiple view application
home_frame = tk.Frame(root, height = 500, width = 5)
test_frame = tk.Frame(root, height = 500, width = 5)
learn_frame = tk.Frame(root, height = 500, width = 5)
progress_frame = tk.Frame(root, height = 500, width = 5)

#MARK - HOME SCREEN CODE
greeting_for_home = tk.Label(home_frame, text="Welcome to home screen", height = 2, font = title_font)
home_screen_button_h = tk.Button(home_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_h = tk.Button(home_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_h = tk.Button(home_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_h = tk.Button(home_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)

greeting_for_home.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_h.grid(column = 0, row = 1)
test_screen_button_h.grid(column = 1, row = 1)
learn_screen_button_h.grid(column = 2, row = 1)
progress_screen_button_h.grid(column = 3, row = 1)
separator = ttk.Separator(home_frame, orient = "horizontal")
separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)

#MARK - TEST SCREEN CODE
greeting_for_test = tk.Label(test_frame, text="TEST", height = 2, font = title_font)
home_screen_button_t = tk.Button(test_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_t = tk.Button(test_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_t = tk.Button(test_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_t = tk.Button(test_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)

greeting_for_test.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_t.grid(column = 0, row = 1)
test_screen_button_t.grid(column = 1, row = 1)
learn_screen_button_t.grid(column = 2, row = 1)
progress_screen_button_t.grid(column = 3, row = 1)
separator = ttk.Separator(test_frame, orient = "horizontal")
separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)
topic_label = tk.Label(test_frame, text = "TOPIC NAME HERE" ,height = 1, font = topic_font)
topic_label.grid(column = 0, row = 5, columnspan = 4)

#CODE FOR WHEN ANSWER IS NOT SHOWN
question_frame = tk.Frame(test_frame)
question_label = tk.Label(question_frame,width = 75, height = 20, wraplength = 500, text = "qweuquefhysdfgysgyfugyuyyyugyuyuggyugyugyugyugyuuiawdhfuiashdfuiahsdfuihaisdufhasdfshadfjihasdjihasduifhhuiasdffhuiasdfihuasdfhuiasdf")
question_label.grid(column = 0, row = 6, columnspan = 4)
show_answer_button = tk.Button(question_frame, text = "Show Answer", command = showAnswer)
show_answer_button.grid(column = 0, row = 7, columnspan = 4)
question_frame.grid(column = 0, row = 6, columnspan = 4)



#CODE FOR WHEN ANSWER IS SHOWN
answer_frame = tk.Frame(test_frame)

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



#MARK - LEARN SCREEN CODE
greeting_for_learn = tk.Label(learn_frame, text="Welcome to learn screen", height = 2, font = title_font)
home_screen_button_l = tk.Button(learn_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_l = tk.Button(learn_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_l = tk.Button(learn_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_l = tk.Button(learn_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)

separator = ttk.Separator(learn_frame, orient = "horizontal")
separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)
greeting_for_learn.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_l.grid(column = 0, row = 1)
test_screen_button_l.grid(column = 1, row = 1)
learn_screen_button_l.grid(column = 2, row = 1)
progress_screen_button_l.grid(column = 3, row = 1)

#MARK - PROGRESS SCREEN CODE
greeting_for_progress = tk.Label(progress_frame, text="Welcome to progress screen", height = 2, font = title_font)
home_screen_button_p = tk.Button(progress_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_p = tk.Button(progress_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_p = tk.Button(progress_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_p = tk.Button(progress_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)
separator = ttk.Separator(progress_frame, orient = "horizontal")
separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)

greeting_for_progress.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_p.grid(column = 0, row = 1)
test_screen_button_p.grid(column = 1, row = 1)
learn_screen_button_p.grid(column = 2, row = 1)
progress_screen_button_p.grid(column = 3, row = 1)

def showProgress(subject):
    #progress pane modification
    progress_pane = Toplevel()
    progress_pane.title(f"Progress for {subject}")
    progress_pane.resizable(False, False)
    pane_size_x = 500
    pane_size_y = 300
    progress_pane.geometry("{}x{}".format(pane_size_x, pane_size_y))

    #adds the title of the progress tab
    progress_font = tk.font.Font(family = "Helvetica", size = 16, weight = "bold")
    progress_label = tk.Label(progress_pane, text = f"Progress for - {subject}", height =2, font = progress_font)
    progress_label.grid(column = 0, row = 0, sticky = "ew", padx = 10)

    #add a divider below the progress icon
    separator = ttk.Separator(progress_pane, orient = "horizontal")
    separator.grid(column = 0, row = 1, columnspan = 4, sticky = "ew", padx = 10)

    progress_dictionary = data_model.GetProgress(subject)
    red_label = tk.Label(progress_pane, text = f"Red = {progress_dictionary['Red']}")
    red_label.grid(column = 0, row = 2, sticky = "w", padx = 10)
    orange_label = tk.Label(progress_pane, text = f"Orange = {progress_dictionary['Orange']}")
    orange_label.grid(column = 0, row = 3, sticky = "w", padx = 10)
    yellow_label = tk.Label(progress_pane, text = f"Yellow = {progress_dictionary['Yellow']}")
    yellow_label.grid(column = 0, row = 4, sticky = "w", padx = 10)
    green_label = tk.Label(progress_pane, text = f"Green = {progress_dictionary['Green']}")
    green_label.grid(column = 0, row = 5, sticky = "w", padx = 10)


    Toplevel.mainloop(root)

def FormatProgressScreen():

    topic_names = data_model.GetTopics()
    #the first row should be row 6 - below the title
    row = 6
    for topic_name in topic_names:

        test_label = tk.Label(progress_frame,width = 40, text = topic_name)
        test_button = tk.Button(progress_frame,width = 15, text = "Click here for progress", command = lambda: showProgress(topic_name))
        go_to_topic_button = tk.Button(progress_frame, width = 15, text = "Go To Topic")
        test_label.grid(column = 0, row = row,columnspan = 2)
        test_button.grid(column = 2, row = row, columnspan = 1)
        go_to_topic_button.grid(column = 3, row = row, columnspan = 1)
        row +=1

#main startup
home_frame.pack(fill = "both") #pack the frames but grid the stuff within the frames
root.mainloop()
