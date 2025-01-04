import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Main window
window = tk.Tk()
window.title("SE-RI'S CHOICE PAYROLL")
window.geometry("900x1000")
window.resizable(False, False)

class DesignGUI:
    def __init__(self):
        pass

    def label(self, text, x, y, font=("Arial", 10), width=None):
        lbl = Label(window, text=text, font=font)
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = Entry(window, width=width)
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None, bg="lightgray", fg="black"):
        btn = Button(window, text=text, width=width, command=command, font=("Arial", 10, "bold"), bg=bg, fg=fg)
        btn.place(x=x, y=y)

    def frame(self, x, y, w, h):
        frame = Frame(window, width=w, height=h, bg="gray")
        frame.place(x=x, y=y)
        return frame

    def add_image(self, x, y, image_path, width=100, height=100):
        # Open image using PIL
        img = Image.open(image_path)
        img = img.resize((width, height))  # Resize image to fit the frame
        photo = ImageTk.PhotoImage(img)

        # Label to display the image
        label = Label(window, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.place(x=x, y=y)

# Instantiate the design class
design = DesignGUI()

# Header
design.label("SE-RI'S CHOICE PAYROLL", 300, 20, font=("Arial", 16, "bold"))

# Employee Basic Info
design.label("EMPLOYEE BASIC INFO:", 20, 60, font=("Arial", 12, "bold"))

# Image frame for employee picture
image_frame = design.frame(20, 100, 100, 100)  # Placeholder for the employee image
design.label("Image", 35, 140, font=("Arial", 10), width=50)


image_path = r"C:\Users\acer\Downloads\seri.jpg"
design.add_image(20, 100, image_path)

# Basic Info Fields
design.label("Employee Number:", 130, 110)
employee_number = design.entry(250, 110)
design.label("Search Employee:", 130, 140)
search_entry = design.entry(250, 140)


design.button("SEARCH", 20, 240, width=15, bg="red", fg="white")

design.label("Department:", 130, 170)
department = design.entry(250, 170)


fields_right = [
    ("Firstname:", 100),
    ("Middlename:", 130),
    ("Surname:", 160),
    ("Civil Status:", 190),
    ("Qualified Dependents:", 220),
    ("Paydate:", 250),
    ("Employee Status:", 280),
    ("Designation:", 310),
]

for label, y in fields_right:
    design.label(label, 400, y)
    design.entry(550, y, width=25)


income_sections = [
    ("BASIC INCOME", 350),
    ("Rate / Hour:", 380),
    ("No. of Hours / Cut Off:", 410),
    ("Income / Cut Off:", 440),
    ("HONORARIUM INCOME", 470),
    ("Rate / Hour:", 500),
    ("No. of Hours / Cut Off:", 530),
    ("Income / Cut Off:", 560),
    ("OTHER INCOME", 590),
    ("Rate / Hour:", 620),
    ("No. of Hours / Cut Off:", 650),
    ("Income / Cut Off:", 680),
]

for label, y in income_sections:
    if "INCOME" in label:
        design.label(label, 20, y, font=("Arial", 12, "bold"))
    else:
        design.label(label, 20, y)
        design.entry(180, y)


deduction_start_y = 340

# Deductions Section
deduction_sections = [
    ("REGULAR DEDUCTIONS", deduction_start_y),
    ("SSS Contribution:", deduction_start_y + 30),
    ("PhilHealth Contribution:", deduction_start_y + 60),
    ("Pagibig Contribution:", deduction_start_y + 90),
    ("OTHER DEDUCTIONS", deduction_start_y + 120),
    ("SSS Loan:", deduction_start_y + 150),
    ("Pagibig Loan:", deduction_start_y + 180),
    ("Other Loan:", deduction_start_y + 210),
    ("DEDUCTION SUMMARY", deduction_start_y + 240),
    ("Total Deductions:", deduction_start_y + 270),
]

for label, y in deduction_sections:
    if "DEDUCTIONS" in label:
        design.label(label, 400, y, font=("Arial", 12, "bold"))
    else:
        design.label(label, 400, y)
        design.entry(580, y)


design.label("SUMMARY INCOME", 20, 710, font=("Arial", 12, "bold"))
design.label("Gross Income:", 20, 740)
design.entry(180, 740)
design.label("Net Income:", 20, 770)
design.entry(180, 770)


design.label("DEDUCTION SUMMARY", 400, 710, font=("Arial", 12, "bold"))
design.label("Total Deductions:", 400, 740)
design.entry(580, 740)


buttons = [
    ("GROSS INCOME", 20, "blue"),  # Blue
    ("NET INCOME", 180, "lightblue"),  # Light Blue
    ("SAVE", 360, "lightblue"),  # Light Blue
    ("UPDATE", 540, "yellow"),  # Yellow
    ("NEW", 720, "yellow")  # Yellow
]


for text, x, color in buttons:
    design.button(text, x, 820, width=15, bg=color, fg="black")

window.mainloop()
