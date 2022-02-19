#required imports to import fonts
from tkinter import font
import tkinter as tk

#a class for the fonts to be accessed within the application class.
class Fonts():

    def __init__(self):
        #localises a selection of fonts to the Fonts() class using the tkinter inbuilt font class.
        self.title_font = tk.font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.topic_font = tk.font.Font(family = "Helvetica", size = 28)
        self.progress_title_font = tk.font.Font(family = "Helvetica", size = 16, weight = "bold")
        self.progress_font = tk.font.Font(family = "Helvetica", size = 14)
        self.percentage_font = tk.font.Font(family = "Helvetica", size = 36)
        self.answer_font = tk.font.Font(family = "Helvetica", size = 20, weight = "bold")
        self.question_alpha_font = tk.font.Font(family = "roboto", size = 12, slant = "italic")
        self.main_font = tk.font.Font(family = "Helvetica", size = 45, weight = "bold")
        self.description_font = tk.font.Font(family = "roboto", size = 16, slant = "italic")
