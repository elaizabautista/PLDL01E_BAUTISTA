# emp_regis1.py
import tkinter as tk
from tkinter import ttk
from tkinter import Label, Frame, Text, Button
from PIL import Image, ImageTk

class DesignGUI:
    # Initialize the window
    def __init__(self, window):
        self.window = window
        self.window.title('Employee Registration')
        self.window.geometry('782x1040')
        self.window.configure(bg='#f0e0f0')  # Light pink background


    def create_frame(self, x, y, width, height, bg='#f8d8f8'):  # Light pink frames
        frame = Frame(self.window, width=width, height=height, bg=bg)
        frame.place(x=x, y=y)
        return frame

    def create_heading(self, x, y, text):
        heading = Label(self.window, text=text, fg='#ff66cc', bg='#f0e0f0', font=('Algerian', 25, 'bold'))  # Pink text
        heading.place(x=x, y=y)
        return heading

    def create_label(self, x, y, text, font=('Segoe UI', 9), bg='#f8d8f8'):
        label = Label(self.window, text=text, bg=bg, font=font, fg='#ff66cc')  # Pink text
        label.place(x=x, y=y)
        return label


    def create_textbox(self, x, y, width=25, height=1, bg_color='#ffccff'):  # Light pink background for textboxes
        textbox = Text(self.window, width=width, height=height, fg="black", bg=bg_color, font=('Segoe UI', 9))
        textbox.place(x=x, y=y)
        return textbox

    def create_combobox(self, x, y, values, width=22):
        combo = ttk.Combobox(self.window, width=width, values=values, font=('Segoe UI', 9))
        combo.place(x=x, y=y)
        return combo

    # Define buttons
    def create_button(self, x, y, text, width=10, height=1, command=None, font=('Segoe UI', 10), fg='white', bg='#ff66cc'):  # Pink button
        button = Button(self.window, text=text, width=width, height=height, bg=bg, fg=fg, font=font, command=command)
        button.place(x=x, y=y)
        return button

    # Define by adding Profile Image
    def create_image(self, image_path, x, y, width, height):
        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        label = Label(self.window, image=photo, bg='#f0e0f0')  # Pink background for the image
        label.image = photo  # Prevent garbage collection
        label.place(x=x, y=y)
        return label
