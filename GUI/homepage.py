import tkinter as tk
from constants import *

class homepage:
    def __init__(self,currentFrame, newFrame, frames):
        # initiate the frame
        self.frame = frames
        currentFrame.forget()
        newFrame.pack(fill='both', expand=1)
        self.shown()
    
    def shown(self):
        # Title
        title = tk.Label(
            self.frame[1], 
            text="Welcome",
            bg='red',
            font='30'
            )

        titleWidth = 0.25*windowWidth
        titlex = (windowWidth*0.5) - (titleWidth*0.5)
        title.place(
            width=titleWidth, 
            x=titlex, 
            y=50
            )

        # logout button
        logout = tk.Button(
            self.frame[1],
            text='Logout', 
            command=lambda: home.loginPage(
                self.frame[2], 
                self.frame[0], 
                self.frame
                )
            )
        logout.place(width=150, x=600, y=50)