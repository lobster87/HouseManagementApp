import tkinter as tk
from constants import *
import buttonFunctions.buttonFunctions as bf

class loginPage:
    def __init__(self,currentFrame, newFrame, frames):
        self.frames = frames
        currentFrame.forget()
        newFrame.pack(fill='both', expand=1)
        self.shown()
    
    def shown(self):
        title = tk.Label(
            self.frames[0], 
            text="House Management System",
            font='30'
            )

        titleWidth = windowWidth
        titlex = (windowWidth*0.5) - (titleWidth*0.5)
        title.place(
            width=titleWidth, 
            x=titlex, 
            y=50
            )
        
        # Create frame for login details
        loginSectionWidth = 0.25*windowWidth
        loginSection = tk.Frame(
            self.frames[0],
            width= loginSectionWidth,
            height=500,
            bg='white'
            )
        loginSection.place(
            x= (windowWidth*0.5) - (loginSectionWidth*0.5), 
            y=150
            )

        # Enter username
        userTitle = tk.Label(
            loginSection, 
            text="Username:", 
            bg='white',
            anchor='w'
            )

        userTitleWidth = 0.1*windowWidth
        userTitlex = (windowWidth*0.5) - (titleWidth*0.5)
        userTitle.place(
            width=userTitleWidth, 
            x=userTitlex, 
            y=0
            )

        userWidth = 0.25*windowWidth
        userx = (windowWidth*0.5) - (titleWidth*0.5)
        user = tk.Entry(loginSection)
        user.place(
            width=userWidth, 
            x=userx, 
            y=25
            )

        # Enter password
        passTitle = tk.Label(
            loginSection, 
            text="Password:", 
            bg='white',
            anchor='w'
            )

        passTitleWidth = 0.1*windowWidth
        passTitlex = (windowWidth*0.5) - (titleWidth*0.5)
        passTitle.place(
            width=passTitleWidth, 
            x=passTitlex, 
            y=50
            )

        passWidth = 0.25*windowWidth
        passx = (windowWidth*0.5) - (titleWidth*0.5)
        password = tk.Entry(loginSection)
        password.place(
            width=passWidth, 
            x=passx, 
            y=75
            )

        # buttons
        butWidth = 0.1*windowWidth
        loginbutton = tk.Button(
            loginSection, 
            text='Login', 
            command=lambda: bf.login(
                user,
                password,
                self.frames
                )
            )

        loginbutton.place(
            width= butWidth,
            x=(windowWidth*0.5) - (titleWidth*0.5), 
            y=100)