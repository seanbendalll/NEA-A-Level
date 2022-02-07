#file for home screen
import tkinter as tk
from tkinter import ttk
from tkinter import *
from model import Model
from functools import partial
from PIL import ImageTk, Image
from PriorityQueue import PriorityQueue
from fonts import Fonts
import application

class Home():

    def __init__(self, root):
        self.root = root
        self.data_model = Model()
        self.home_frame = tk.Frame(self.root, height = 500, width = 5)
        self.InitialiseBaseFrame()

    def InitialiseBaseFrame(self):
        greeting_for_home = tk.Label(self.home_frame, text="Welcome to home screen", height = 2, font = Fonts().title_font)
        home_screen_button_h = tk.Button(self.home_frame, text = "HOME", width = 32, height = 2)
        test_screen_button_h = tk.Button(self.home_frame, text = "TEST", width = 32, height = 2)
        learn_screen_button_h = tk.Button(self.home_frame, text = "LEARN", width = 32, height = 2)
        progress_screen_button_h = tk.Button(self.home_frame, text = "PROGRESS", width = 32, height = 2)

        greeting_for_home.grid(column = 0, row = 0, columnspan = 4)
        home_screen_button_h.grid(column = 0, row = 1)
        test_screen_button_h.grid(column = 1, row = 1)
        learn_screen_button_h.grid(column = 2, row = 1)
        progress_screen_button_h.grid(column = 3, row = 1)
        separator = ttk.Separator(self.home_frame, orient = "horizontal")
        separator.grid(column = 0, row = 4, columnspan = 4, sticky = "ew", pady = 10)
