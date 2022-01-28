import tkinter as tk
from constants import *
from GUI import login

window = tk.Tk()
window.title('House Management System')
window.geometry(f'{windowWidth}x{windowHeight}')
window.resizable(True, True)

"""
Set up frames in list

0 - login
1 - homepage
2 - houseBoard
3 - lodgerBoard
4 - addLodger
"""


frames = [
    tk.Frame(window, bg='white'),
    tk.Frame(window, bg='white'),
    tk.Frame(window, bg='white'),
    tk.Frame(window, bg='white'),
    tk.Frame(window, bg='white')
    ]
    
login.loginPage(frames[0], frames[0], frames[0:])

window.mainloop()
