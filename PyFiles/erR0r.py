import pyautogui
import random
import tkinter as tk

class erR0r :
    
    # Position of the sprite on the screen 
    
    posX = 0
    posY = 0
    
    # The bounds X and Y (Change with the size of the sprites)
    
    boundX = 0
    boundY = 0
    
    # The size of the sprites
    
    spriteSizeX = 100
    spriteSizeY = 100
    
    # The current event of the sprite
    
    currentState = 0
    
    # Variable that count the frames in a gif
    
    cycle = 0
    
    # The folder path of the sprites
    
    impath = 'D:\\Cours\\3èmeAnnée\\Perso\\IT_Desktop_Pets\\Img\\erR0r\\'
    
    # Initialise all events gif
    
    idle = None                     # state : 0
    idleToMoveLeft = None           # state : 1
    idleToMoveRight = None          # state : 2
    idleToOnClick = None            # state : 3
    idleToAction = None             # state : 4
    
    moveLeft = None                 # state : 5
    moveLeftToIdle = None           # state : 6
    moveLeftToMoveRight = None      # state : 7
    moveLeftToOnClick = None        # state : 8
    moveLeftToAction = None         # state : 9
    
    moveRight = None                # state : 10
    moveRightToIdle = None          # state : 11
    moveRightToMoveLeft = None      # state : 12
    moveRightToOnClick = None       # state : 13
    moveRightToAction = None        # state : 14
    
    onClick = None                  # state : 15
    onClickToIdle = None            # state : 16
    onClickToMoveLeft = None        # state : 17
    onClickToOnRight = None         # state : 18
    onClickToAction = None          # state : 19
    
    action = None                   # state : 20
    actionToIdle = None             # state : 21
    actionToMoveLeft = None         # state : 22
    actionToMoveRight = None        # state : 23
    actionToOnClick = None          # state : 24
    
      
    def __init__(self, tk) :
        
        # Get the size of the screen
        
        self.boundX = pyautogui.size()[0]
        self.boundY = pyautogui.size()[1]
        
        # Initialise randomly the position of the sprite
        
        self.posX = random.randrange(0, self.boundX - self.spriteSizeX, 1)
        self.posY = self.boundY - self.spriteSizeY
        
        # Definition of all events gif
        # Stance = [tk.PhotoImage(file = self.impath + 'stance.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        
        self.idle = [tk.PhotoImage(file = self.impath + 'idle.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.idleToMoveLeft = [tk.PhotoImage(file = self.impath + 'idleToMoveLeft.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.idleToMoveRight = [tk.PhotoImage(file = self.impath + 'idleToMoveRight.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.idleToOnClick = [tk.PhotoImage(file = self.impath + 'idleToOnClick.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.idleToAction = [tk.PhotoImage(file = self.impath + 'idleToAction.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
           
        self.moveLeft = [tk.PhotoImage(file = self.impath + 'moveLeft.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveLeftToIdle = [tk.PhotoImage(file = self.impath + 'moveLeftToIdle.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveLeftToMoveRight = [tk.PhotoImage(file = self.impath + 'moveLeftToMoveRight.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveLeftToOnClick = [tk.PhotoImage(file = self.impath + 'moveLeftToOnClick.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveLeftToAction = [tk.PhotoImage(file = self.impath + 'moveLeftToAction.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        
        self.moveRight = [tk.PhotoImage(file = self.impath + 'moveRight.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveRightToIdle = [tk.PhotoImage(file = self.impath + 'moveRightToIdle.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveRightToMoveLeft = [tk.PhotoImage(file = self.impath + 'moveRightToMoveLeft.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveRightToOnClick = [tk.PhotoImage(file = self.impath + 'moveRightToOnClick.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.moveRightToAction = [tk.PhotoImage(file = self.impath + 'moveRightToAction.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        
        self.onClick = [tk.PhotoImage(file = self.impath + 'onClick.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.onClickToIdle = [tk.PhotoImage(file = self.impath + 'onClickToIdle.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.onClickToMoveLeft = [tk.PhotoImage(file = self.impath + 'onClickToMoveLeft.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.onClickToOnRight = [tk.PhotoImage(file = self.impath + 'onClickToOnRight.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.onClickToAction = [tk.PhotoImage(file = self.impath + 'onClickToAction.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        
        self.action = [tk.PhotoImage(file = self.impath + 'action.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.actionToIdle = [tk.PhotoImage(file = self.impath + 'ctionToIdle.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.actionToMoveLeft = [tk.PhotoImage(file = self.impath + 'actionToMoveLeftk.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.actionToMoveRight = [tk.PhotoImage(file = self.impath + 'actionToMoveRight.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        self.actionToOnClick = [tk.PhotoImage(file = self.impath + 'actionToOnClick.gif', format = 'gif -index %i' % (i)) for i in range(totalOfFrames)]
        
        
    def DefineNextEvent(self) :
        # Look at current state and choose the next event
        return self.currentState
    
    
    def GifWork(self) :
        # Next frame of the gif of the current state
        return None
        
    