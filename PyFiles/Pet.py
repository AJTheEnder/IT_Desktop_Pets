import pyautogui
import random
import tkinter as tk

class Pet :
    
    # Position of the sprite on the screen 
    
    posX = 0
    posY = 0
    
    # The bounds X and Y (Change with the size of the sprites)
    
    boundX = 0
    boundY = 0
    
    # The size of the sprites
    
    spriteSizeX = 640
    spriteSizeY = 640
    
    # The current event of the sprite
    
    currentStateNumber = 0
    currentStateFrames = 0
    
    # Variable that count the frames in a gif
    
    cycle = 0
    
    # The folder path of the sprites
    
    impath = 'D:\\Cours\\3emeAnnee\\Perso\\IT_Desktop_Pets\\Img\\'
    
    # Initialise all events gif 
    
    idle = None                     # state : 0  
    moveLeft = None                 # state : 1
    moveRight = None                # state : 2
    onClick = None                  # state : 3
    action = None                   # state : 4
    
    # Memory of the number of frames for teh current event
    
    numOfFrames = 0
      
    def __init__(self, tk, path, iNumFrames, mlNumFrames, mrNumFrames, ocNumFrames, aNumFrames) :
        
        # Get the size of the screen
        
        self.boundX = pyautogui.size()[0]
        self.boundY = pyautogui.size()[1]
        
        # Initialise randomly the position of the sprite
        
        self.posX = random.randrange(0, self.boundX - self.spriteSizeX, 1)
        self.posY = self.boundY - self.spriteSizeY
        
        # Initialise the correct path
        
        self.impath += path
        
        # Definition of all events gif
        # Stance = [tk.PhotoImage(file = self.impath + 'stance.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        
        self.idle = [tk.PhotoImage(file = self.impath + 'idle.gif', format = 'gif -index %i' % (i)) for i in range(iNumFrames)]     
        self.moveLeft = [tk.PhotoImage(file = self.impath + 'moveLeft.gif', format = 'gif -index %i' % (i)) for i in range(mlNumFrames)]  
        self.moveRight = [tk.PhotoImage(file = self.impath + 'moveRight.gif', format = 'gif -index %i' % (i)) for i in range(mrNumFrames)]
        self.onClick = [tk.PhotoImage(file = self.impath + 'onClick.gif', format = 'gif -index %i' % (i)) for i in range(ocNumFrames)]
        self.action = [tk.PhotoImage(file = self.impath + 'action.gif', format = 'gif -index %i' % (i)) for i in range(aNumFrames)]
        
        # The first event is Idle
        
        self.currentStateNumber = 0
        self.currentStateFrames = self.idle
        
        
    def DefineNextEvent(self, isWindowAction, isClicked) :
        # Look at current state and choose the next event
        
        # Define if the current animation is finished
        if (self.cycle == len(self.currentStateFrames)) :
            isAnimationFinished = True
        else :
            isAnimationFinished = False
            
        # Create a random number for next event
        randNumber = random.randrange(0, 100, 1)
            
        # From Idle state to ...
        if (self.currentStateNumber == 0) :
            # ... Action state
            if (isWindowAction) :
                self.currentStateNumber = 4
                self.cycle = 0
            # ... Clicked state
            elif (isClicked) :
                self.currentStateNumber = 3
                self.cycle = 0
            # ... Move to left state
            elif (randNumber < 33 and self.posX > 2 and isAnimationFinished == True) :
                self.currentStateNumber = 1
                self.cycle = 0
            # ... Idle state
            elif (randNumber >= 33 and randNumber <= 66) :
                self.currentStateNumber = 0
            # ... Move to right state
            elif (randNumber > 66 and self.posX < 3198 and isAnimationFinished == True) :
                self.currentStateNumber = 2
                self.cycle = 0
    
    
    def GifWork(self) :
        # Next frame of the gif of the current state
        if (self.cycle < len(self.currentStateFrames) - 1) :
            self.cycle += 1
        else :
            self.cycle = 0
        return self.currentStateFrames[self.cycle]
    
    
    def Move(self) :
        # Move left
        if (self.currentStateNumber == 1) :
            self.posX -= 3
        # Move right
        elif (self.currentStateNumber == 2) :
            self.posX += 3 