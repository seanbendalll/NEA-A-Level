#file for learn screen
import tkinter as tk
from tkinter import ttk
from tkinter import *
from model import Model
from functools import partial
from PIL import ImageTk, Image
from PriorityQueue import PriorityQueue
from fonts import Fonts


class Learn():

    def __init__(self,root):
        self.root = root
        self.data_model = Model()
        self.learn_frame = tk.Frame(self.root, height = 500, width = 5)
        self.InitialiseBaseFrame()

    def InitialiseBaseFrame(self):
        greeting_for_learn = tk.Label(self.learn_frame, text="Welcome to learn screen", height = 2, font = Fonts().title_font)
        home_screen_button_l = tk.Button(self.learn_frame, text = "HOME", width = 32, height = 2)
        test_screen_button_l = tk.Button(self.learn_frame, text = "TEST", width = 32, height = 2)
        learn_screen_button_l = tk.Button(self.learn_frame, text = "LEARN", width = 32, height = 2)
        progress_screen_button_l = tk.Button(self.learn_frame, text = "PROGRESS", width = 32, height = 2)

        separator = ttk.Separator(self.learn_frame, orient = "horizontal")
        separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)
        greeting_for_learn.grid(column = 0, row = 0, columnspan = 4)
        home_screen_button_l.grid(column = 0, row = 1)
        test_screen_button_l.grid(column = 1, row = 1)
        learn_screen_button_l.grid(column = 2, row = 1)
        progress_screen_button_l.grid(column = 3, row = 1)
