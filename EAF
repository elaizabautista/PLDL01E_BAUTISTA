import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Enrollment Assessment Form")
root.geometry("1050x1200")
root.resizable(False, False)

class DesignGUI:
    def __init__(self):
        pass

    def label(self, text, x, y, font=("Arial", 10), width=None, anchor="w"):
        lbl = tk.Label(root, text=text, font=font, anchor=anchor)
        lbl.place(x=x, y=y, width=width)

    def entry(self, x, y, width=20):
        txt = tk.Entry(root, width=width)
        txt.place(x=x, y=y)
        return txt

    def button(self, text, x, y, width=10, command=None):
        btn = tk.Button(root, text=text, width=width, command=command, font=("Arial", 10, "bold"))
        btn.place(x=x, y=y)


design = DesignGUI()

# Header Section
design.label("LYCEUM OF THE PHILIPPINES UNIVERSITY", 250, 20, font=("Arial", 16, "bold"))
design.label("Enrollment Assessment Form", 300, 50, font=("Arial", 14))
design.label("2nd Semester, AY 2023-2024", 330, 80, font=("Arial", 12))

# Student Information Section
design.label("Student Number:", 20, 130)
student_number = design.entry(150, 130, width=30)

design.label("Name:", 20, 160)
student_name = design.entry(150, 160, width=30)

design.label("Course:", 20, 190)
course = design.entry(150, 190, width=30)

design.label("College:", 20, 220)
college = design.entry(150, 220, width=30)

# Subject List Section
design.label("Subject List", 20, 270, font=("Arial", 12, "bold"))

columns = ["Subject Code", "Course Description", "Section", "Time", "Days", "Room", "Units"]
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")
tree.place(x=20, y=300)

# Subjects Data
subjects = [
    ("CALNO2E", "Calculus 2: Integral Calculus", "ENG 102", "02:30PM-04:00PM", "M/W", "C-702", "3"),
    ("DRWL12E", "Computer-Aided Drafting", "ENG 102", "07:00AM-10:00AM", "F", "C-201", "1"),
    ("MATH02E", "Mathematics for Engineers 2", "ENG 102", "08:30AM-10:00AM", "M/W", "C-702", "3"),
    ("PHYLO1E", "Physics for Engineers 1", "ENG 102", "10:00AM-11:30AM", "F", "L-305", "3"),
    ("HUMNO2G", "Art Appreciation", "ENG 102", "02:30PM-04:00PM", "F/S", "C-701", "3"),
    ("LVTNO1E", "Living in the IT Era", "ENG 102", "01:00PM-02:30PM", "M/W", "C-702", "1"),
    ("NSTP02G", "National Service Training Program 2", "ENG 102", "07:00AM-10:00AM", "S", "SRDB1", "3"),
    ("PATHFIT2", "Physical Activities Towards Health-Fit 2", "ENG 102", "11:00AM-01:00PM", "S", "SRDB1", "2"),
    ("RPHIS01G", "Readings in Philippine History", "ENG 102", "04:00PM-05:30PM", "F/S", "C-701", "3"),
    ("STS11G", "Science, Technology and Society", "ENG 102", "04:00PM-05:30PM", "M/W", "C-702", "3"),
]

for subject in subjects:
    tree.insert("", "end", values=subject)

# Fees Section (Lowered further down to avoid collision)
design.label("Fees Section", 20, 570, font=("Arial", 12, "bold"))
design.label("TOTAL UNITS: 28", 20, 600)
design.label("Tuition Fee: 37,600.00", 20, 620)
design.label("Miscellaneous Fees: 13,148.00", 20, 640)
design.label("Laboratory Fees:", 20, 660)
design.label("Computer Lab Fee: 3,854.00", 20, 680)
design.label("Physics Lab Fee: 2,201.00", 20, 700)
design.label("NSTP Fee: 1,760.00", 20, 720)


acknowledgement_text = "Acknowledgement: I understand and agree to the terms stated above."
signature_text = "Signature over Printed Name and Date"


design.label(acknowledgement_text, 270, 770, font=("Arial", 10), anchor="center", width=500)
design.label(signature_text, 270, 800, font=("Arial", 10, "bold"), anchor="center", width=500)


buttons = [("SUBMIT", 20), ("CANCEL", 150)]
for text, x in buttons:
    design.button(text, x, 850, width=12)

root.mainloop()
