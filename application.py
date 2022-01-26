import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()
root.title("ALCA - A Level Computer Science Application")
root_size_x = 850
root_size_y = 700
root.geometry("{}x{}".format(root_size_x, root_size_y))


#using frames to give a multiple view application
home_frame = tk.Frame(root, height = 500, width = 5)
test_frame = tk.Frame(root, height = 500, width = 5)
learn_frame = tk.Frame(root, height = 500, width = 5)
progress_frame = tk.Frame(root, height = 500, width = 5)

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

def toggle_list(current_screen):
    print("hello world")
    
    

#MARK - HOME SCREEN CODE
greeting_for_home = tk.Label(home_frame, text="Welcome to home screen")
greeting_for_home.pack(padx = 10, pady = 10)
home_screen_button_h = tk.Button(home_frame, text = "HOME", width = 20, height = 2, command = change_to_home_frame)
test_screen_button_h = tk.Button(home_frame, text = "TEST", width = 20, height = 2, command = change_to_test_frame)
learn_screen_button_h = tk.Button(home_frame, text = "LEARN", width = 20, height = 2, command = change_to_learn_frame)
progress_screen_button_h = tk.Button(home_frame, text = "PROGRESS", width = 20, height = 2, command = change_to_progress_frame)
home_screen_button_h.pack(padx = 0, pady = 0, side = "left")
test_screen_button_h.pack(padx = 0, pady =0, side = "left")
learn_screen_button_h.pack(padx = 0, pady = 0, side = "left")
progress_screen_button_h.pack(padx = 0, pady = 0, side = "left")

label_for_testing = tk.Label(home_frame, text = "Welcome to shdf")
label_for_testing.pack(fill = "x")


#MARK - TEST SCREEN CODE
greeting_for_test = tk.Label(test_frame, text="Welcome to test screen")
greeting_for_test.pack(padx = 10, pady = 10)
home_screen_button_t = tk.Button(test_frame, text = "HOME", width = 25, height = 5, command = change_to_home_frame)
test_screen_button_t = tk.Button(test_frame, text = "TEST", width = 25, height = 5, command = change_to_test_frame)
learn_screen_button_t = tk.Button(test_frame, text = "LEARN", width = 25, height = 5, command = change_to_learn_frame)
progress_screen_button_t = tk.Button(test_frame, text = "PROGRESS", width = 25, height = 5, command = change_to_progress_frame)
home_screen_button_t.pack(padx = 10, pady = 10)
test_screen_button_t.pack(padx = 10, pady = 10)
learn_screen_button_t.pack(padx = 10, pady = 10)
progress_screen_button_t.pack(padx = 10, pady = 10)

#MARK - LEARN SCREEN CODE
greeting_for_learn = tk.Label(learn_frame, text="Welcome to learn screen")
greeting_for_learn.pack(padx = 10, pady = 10)
home_screen_button_l = tk.Button(learn_frame, text = "HOME", width = 25, height = 5, command = change_to_home_frame)
test_screen_button_l = tk.Button(learn_frame, text = "TEST", width = 25, height = 5, command = change_to_test_frame)
learn_screen_button_l = tk.Button(learn_frame, text = "LEARN", width = 25, height = 5, command = change_to_learn_frame)
progress_screen_button_l = tk.Button(learn_frame, text = "PROGRESS", width = 25, height = 5, command = change_to_progress_frame)
home_screen_button_l.pack(padx = 10, pady = 10, side = "left")
test_screen_button_l.pack(padx = 10, pady = 10, side = "left")
learn_screen_button_l.pack(padx = 10, pady = 10, side = "left")
progress_screen_button_l.pack(padx = 10, pady = 10, side = "left")

#MARK - PROGRESS SCREEN CODE
greeting_for_progress = tk.Label(progress_frame, text="Welcome to progress screen")
greeting_for_progress.pack(padx = 10, pady = 10)
home_screen_button_p = tk.Button(progress_frame, text = "HOME", width = 25, height = 5, command = change_to_home_frame)
test_screen_button_p = tk.Button(progress_frame, text = "TEST", width = 25, height = 5, command = change_to_test_frame)
learn_screen_button_p = tk.Button(progress_frame, text = "LEARN", width = 25, height = 5, command = change_to_learn_frame)
progress_screen_button_p = tk.Button(progress_frame, text = "PROGRESS", width = 25, height = 5, command = change_to_progress_frame)
home_screen_button_p.pack(padx = 10, pady = 10)
test_screen_button_p.pack(padx = 10, pady = 10)
learn_screen_button_p.pack(padx = 10, pady = 10) 
progress_screen_button_p.pack(padx = 10, pady = 10)




home_frame.pack(fill = "both")
root.mainloop()
