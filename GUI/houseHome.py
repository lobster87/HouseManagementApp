from constants import *
import tkinter as tk


class houseMain:
    def __init__(self,currentFrame, newFrame, frames):
        self.frames = frames
        currentFrame.forget()
        newFrame.pack(fill='both', expand=1)
        self.shown()
    
    def shown(self):
        title = tk.Label(
            self.frames[2], 
            text="House",
            font='30'
            )

        titleWidth = windowWidth
        titlex = (windowWidth*0.5) - (titleWidth*0.5)
        title.place(
            width=titleWidth, 
            x=titlex, 
            y=50
            )