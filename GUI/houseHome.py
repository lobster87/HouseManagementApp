


class houseMain:
    def __init__(self,currentFrame, newFrame, frames):
        self.frames = frames
        currentFrame.forget()
        newFrame.pack(fill='both', expand=1)
        self.shown()
    
    def shown(self):
        pass