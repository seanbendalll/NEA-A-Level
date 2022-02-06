#file for the progress screen
import tkinter as tk
from tkinter import ttk
from tkinter import *
from model import Model
from functools import partial
from PIL import ImageTk, Image
from PriorityQueue import PriorityQueue
from fonts import Fonts

class Progress():

    def __init__(self, root):
        self.root = root
        self.progress_frame = tk.Frame(root, height = 500, width = 5)
        self.data_model = Model()
        self.InitialiseBaseFrame(self.root)


    def InitialiseBaseFrame(self, root):
        greeting_for_progress = tk.Label(self.progress_frame, text="Welcome to progress screen", height = 2, font = Fonts().title_font)
        home_screen_button_p = tk.Button(self.progress_frame, text = "HOME", width = 32, height = 2, command = ChangeToHomeFrame)
        test_screen_button_p = tk.Button(self.progress_frame, text = "TEST", width = 32, height = 2, command = ChangeToTestFrame)
        learn_screen_button_p = tk.Button(self.progress_frame, text = "LEARN", width = 32, height = 2, command = ChangeToLearnFrame)
        progress_screen_button_p = tk.Button(self.progress_frame, text = "PROGRESS", width = 32, height = 2, command = ChangeToProgressFrame)
        separator = ttk.Separator(self.progress_frame, orient = "horizontal")
        separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)

        greeting_for_progress.grid(column = 0, row = 0, columnspan = 4)
        home_screen_button_p.grid(column = 0, row = 1)
        test_screen_button_p.grid(column = 1, row = 1)
        learn_screen_button_p.grid(column = 2, row = 1)
        progress_screen_button_p.grid(column = 3, row = 1)

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
