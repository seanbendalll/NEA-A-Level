from tkinter import font
import tkinter as tk

class Fonts():

    def __init__(self):
        self.title_font = tk.font.Font(family = "Helvetica", size = 36, weight = "bold")
        self.topic_font = tk.font.Font(family = "Helvetica", size = 28)
        self.progress_title_font = tk.font.Font(family = "Helvetica", size = 16, weight = "bold")
        self.progress_font = tk.font.Font(family = "Helvetica", size = 14)
        self.percentage_font = tk.font.Font(family = "Helvetica", size = 36)
        self.answer_font = tk.font.Font(family = "Helvetica", size = 20, weight = "bold")
        self.question_alpha_font = tk.font.Font(family = "roboto", size = 12, slant = "italic")
