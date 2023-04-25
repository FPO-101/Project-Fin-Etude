from tkinter import *


# Privacy Policy window
def privacy_window():
    fpage = Frame(root, width=1000, height=1000, bg='green')
    fpage.place(x=0, y=0)
    privacy_win.title("Privacy Policy")
    privacy_win.geometry("400x300")

    privacy_text = """Privacy Policy:

We do not collect any personally identifiable information through this application. Any data entered into the application is only used for the purpose of performing the requested calculation, and is not stored or shared.

If you have any concerns about privacy, please contact us at privacy@myapp.com.
"""

    privacy_label = Label(privacy_win, text=privacy_text, justify=LEFT)
    privacy_label.pack(pady=10)


# About Me window
def about_window():
    fpage = Frame(root, width=1000, height=1000, bg='green')
    fpage.place(x=0, y=0)
    about_win.title("About Me")
    about_win.geometry("400x300")

    about_text = """About Me:

I am a software developer with a passion for creating innovative applications that solve real-world problems. I have experience in Python, Java, and web development, and am always looking to learn new technologies and frameworks.

If you would like to get in touch, please email me at info@myapp.com.
"""

    about_label = Label(about_win, text=about_text, justify=LEFT)
    about_label.pack(pady=10)