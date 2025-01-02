from tkinter import *
from UserInformationClasses2 import UserInformationClasses2

class UserAccountApplication:
    def __init__(self, window):
        self.window = window
        self.window.title('User Account Information')
        self.window.geometry('900x425')
        self.window.config(bg='#FAD0C9')

        self.profile_image = UserInformationClasses2.load_profile_image()

        self.create_user_account_label()
        self.create_main_frame()
        self.create_profile_picture()

        self.labels_each_row()
        self.buttons()

    def create_user_account_label(self):
        self.user_account_label = Label(self.window, text='User Account Information', font=('Segoe UI', 18, 'bold'), bg='#FAD0C9', fg='black')
        self.user_account_label.place(x=20, y=20)

    def create_main_frame(self):
        self.main_frame = Frame(self.window, bg='#FFD1DC')
        self.main_frame.place(x=20, y=150, width=860, height=240)

    def create_label_entry(self, label_text, x, y, width=23, show=None):
        label = Label(self.main_frame, text=label_text, font=('Segoe UI', 9), bg='#FFD1DC', fg='black')
        label.place(x=x, y=y)
        entry = Entry(self.main_frame, font=('Segoe UI', 9), width=width)
        entry.place(x=x, y=y + 20)
        if show:
            entry.config(show=show)
        return entry

    def create_profile_picture(self):
        if self.profile_image:
            profile_label = Label(self.window, image=self.profile_image, bg='#FAD0C9')
            profile_label.place(x=36, y=87)
            profile_label.image = self.profile_image
        else:
            print("No profile image to display.")

    def labels_each_row(self):
        self.create_label_entry('First Name', 150, 20)
        self.create_label_entry('Middle Name', 303, 20)
        self.create_label_entry('Last Name', 458, 20)
        self.create_label_entry('Suffix', 610, 20, width=14)
        self.create_label_entry('Department', 710, 20, width=22)
        self.create_label_entry('Designation', 20, 70, width=40)
        self.create_label_entry('Username', 278, 70, width=33)
        self.create_label_entry('Password', 493, 70, width=40, show='*')
        self.create_label_entry('Confirm Password', 20, 120, width=40, show='*')
        self.create_label_entry('User Type', 278, 120, width=33)
        self.create_label_entry('User Status', 493, 120, width=28)
        self.create_label_entry('Employee Number', 678, 120, width=27)

    def buttons(self):
        update_button = Button(self.window, text="Update", width=10, font=('Segoe UI', 9), bg='#FF69B4', fg='white')
        update_button.place(x=269, y=330, width=100)

        delete_button = Button(self.window, text="Delete", width=10, font=('Segoe UI', 9), bg='#FFB6C1', fg='black')
        delete_button.place(x=380, y=330, width=100)

        cancel_button = Button(self.window, text="Cancel", width=10, font=('Segoe UI', 9), bg='#FFDEFB', fg='black')
        cancel_button.place(x=490, y=330, width=100)

if __name__ == "__main__":
    window = Tk()
    app = UserAccountApplication(window)
    window.mainloop()
