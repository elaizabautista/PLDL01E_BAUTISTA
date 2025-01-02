# login_page.py

import tkinter as tk
from tkinter import messagebox


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1920x1080")
        self.root.config(bg="#FADADD")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)

        # Title Label
        self.title_label = tk.Label(self.root, text="Welcome!", font=("Comic Sans MS", 40, "bold"), bg="#FADADD", fg="#FF6F91")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Email or Username
        self.email_or_username_label = tk.Label(self.root, text="Email or Username", font=("Comic Sans MS", 14), bg="#FADADD", fg="#FF6F91")
        self.email_or_username_label.place(relx=0.5, rely=0.2, anchor="center")

        self.email_or_username_entry = tk.Entry(self.root, font=("Comic Sans MS", 14), bd=2, relief="solid", width=30)
        self.email_or_username_entry.place(relx=0.5, rely=0.25, anchor="center")

        # Password
        self.password_label = tk.Label(self.root, text="Password", font=("Comic Sans MS", 14), bg="#FADADD", fg="#FF6F91")
        self.password_label.place(relx=0.5, rely=0.35, anchor="center")

        self.password_entry = tk.Entry(self.root, font=("Comic Sans MS", 14), bd=2, relief="solid", show="*", width=30)
        self.password_entry.place(relx=0.5, rely=0.4, anchor="center")

        # Remember Me checkbox
        self.remember_me = tk.BooleanVar()
        self.remember_me_checkbox = tk.Checkbutton(self.root, text="Remember Me", variable=self.remember_me, font=("Comic Sans MS", 12), bg="#FADADD", fg="#FF6F91")
        self.remember_me_checkbox.place(relx=0.5, rely=0.475, anchor="center")

        # Login button
        self.login_button = tk.Button(self.root, text="Login", font=("Comic Sans MS", 18, "bold"), bg="#FF6F91", fg="white", bd=0, relief="solid", width=20, command=self.login)
        self.login_button.place(relx=0.5, rely=0.55, anchor="center")

        # Forgot Password Label
        self.forgot_password_label = tk.Label(self.root, text="Forgot Password?", font=("Comic Sans MS", 12), fg="#FF6F91", bg="#FADADD", cursor="hand2")
        self.forgot_password_label.place(relx=0.5, rely=0.65, anchor="center")
        self.forgot_password_label.bind("<Button-1>", self.forgot_password)

        # Social Media Label
        self.social_media_label = tk.Label(self.root, text="Or sign in with", font=("Comic Sans MS", 12), bg="#FADADD", fg="#FF6F91")
        self.social_media_label.place(relx=0.5, rely=0.725, anchor="center")

        # Google Login Button
        self.google_button = tk.Button(self.root, text="Google", font=("Comic Sans MS", 12), bg="#FFB6C1", fg="white", bd=0, relief="solid", width=15, command=self.social_login_google)
        self.google_button.place(relx=0.4, rely=0.8, anchor="center")

        # Facebook Login Button
        self.facebook_button = tk.Button(self.root, text="Facebook", font=("Comic Sans MS", 12), bg="#FFEC99", fg="white", bd=0, relief="solid", width=15, command=self.social_login_facebook)
        self.facebook_button.place(relx=0.6, rely=0.8, anchor="center")

    def login(self):
        email_or_username = self.email_or_username_entry.get()
        password = self.password_entry.get()

        if (email_or_username == "admin" or email_or_username == "admin@example.com") and password == "password":
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
            self.email_or_username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Login Failed", "Invalid email/username or password!")

    def forgot_password(self, event):
        messagebox.showinfo("Forgot Password", "Redirecting to Password Reset Page...")

    def social_login_google(self):
        messagebox.showinfo("Google Login", "You have selected Google login!")

    def social_login_facebook(self):
        messagebox.showinfo("Facebook Login", "You have selected Facebook login!")

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen on and off."""
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))


if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()
