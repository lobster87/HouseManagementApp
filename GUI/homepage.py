import tkinter as tk
from constants import *
import GUI.login as login
import GUI.houseHome as houseMain

class homepage:
    def __init__(self,currentFrame, newFrame, frames):
        # initiate the frame
        self.frames = frames
        currentFrame.forget()
        newFrame.pack(fill='both', expand=1)
        self.shown()
    
    def shown(self):
        """ Header """
        # Title
        title = tk.Label(
            self.frames[1], 
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
            self.frames[1],
            text='Logout', 
            command=lambda: login.loginPage(
                self.frames[1], 
                self.frames[0], 
                self.frames
                )
            )
        logoutWidth = 100
        logout.place(
            width= logoutWidth, 
            x= windowWidth - (logoutWidth + 10), 
            y=50)

        """ portol buttons"""
        portolSectionWidth = 0.25*windowWidth
        portol_select = tk.Frame(
            self.frames[1],
            width=portolSectionWidth,
            height=500,
            bg='white'
            )
        portol_select.place(
            width = windowWidth - 10,
            x = 5,
            y = 75
        )

        # house button
        house = tk.Button(
            portol_select,
            text='House',
            command=lambda:houseMain.houseMain(
                self.frames[1], 
                self.frames[2], 
                self.frames)
            )
        house.place(x=10, y=50)