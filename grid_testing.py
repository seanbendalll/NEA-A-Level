import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.title("ALCA - A Level Computer Science Application")
root_size_x = 865
root_size_y = 700
root.geometry("{}x{}".format(root_size_x, root_size_y))

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

#using frames to give a multiple view application
home_frame = tk.Frame(root, height = 500, width = 5)
test_frame = tk.Frame(root, height = 500, width = 5)
learn_frame = tk.Frame(root, height = 500, width = 5)
progress_frame = tk.Frame(root, height = 500, width = 5)

#MARK - HOME SCREEN CODE
greeting_for_home = tk.Label(home_frame, text="Welcome to home screen", height = 2)
home_screen_button_h = tk.Button(home_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_h = tk.Button(home_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_h = tk.Button(home_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_h = tk.Button(home_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)

greeting_for_home.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_h.grid(column = 0, row = 1)
test_screen_button_h.grid(column = 1, row = 1)
learn_screen_button_h.grid(column = 2, row = 1)
progress_screen_button_h.grid(column = 3, row = 1)

body_text = tk.Label(home_frame, text = "text underudfhsfdfjsdhfjsdhfjshdfjdfjsdfsdfjsdfhshdfhsdfhk")
body_text.grid(column = 0, row = 2, columnspan = 4)

#MARK - TEST SCREEN CODE
greeting_for_test = tk.Label(test_frame, text="Welcome to test screen", height = 2)
home_screen_button_t = tk.Button(test_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_t = tk.Button(test_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_t = tk.Button(test_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_t = tk.Button(test_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)

greeting_for_test.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_t.grid(column = 0, row = 1)
test_screen_button_t.grid(column = 1, row = 1)
learn_screen_button_t.grid(column = 2, row = 1)
progress_screen_button_t.grid(column = 3, row = 1)

#MARK - LEARN SCREEN CODE
greeting_for_learn = tk.Label(learn_frame, text="Welcome to learn screen", height = 2)
home_screen_button_l = tk.Button(learn_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_l = tk.Button(learn_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_l = tk.Button(learn_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_l = tk.Button(learn_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)

greeting_for_learn.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_l.grid(column = 0, row = 1)
test_screen_button_l.grid(column = 1, row = 1)
learn_screen_button_l.grid(column = 2, row = 1)
progress_screen_button_l.grid(column = 3, row = 1)

#MARK - PROGRESS SCREEN CODE
greeting_for_progress = tk.Label(progress_frame, text="Welcome to progress screen", height = 2)
home_screen_button_p = tk.Button(progress_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_p = tk.Button(progress_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_p = tk.Button(progress_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_p = tk.Button(progress_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)

greeting_for_progress.grid(column = 0, row = 0, columnspan = 4)
home_screen_button_p.grid(column = 0, row = 1)
test_screen_button_p.grid(column = 1, row = 1)
learn_screen_button_p.grid(column = 2, row = 1)
progress_screen_button_p.grid(column = 3, row = 1)

#main startup
home_frame.pack(fill = "both") #pack the frames but grid the stuff within the frames
