from tkinter import tk
import Pet
#import Folder0
#import SECUR

mainWindow = tk.Tk()

errorWindow = tk.Tk()
folderWindow = tk.Tk()
securWindow = tk.Tk()

Error = Pet(tk, 'erR0r\\Gifs\\', 8, 8, 8, 8, 8)
#Folder = Pet(tk, 'Folder0\\Gifs\\', 8, 8, 8, 8, 8)
#Secur = Pet(tk, 'SECUR\\Gifs\\', 8, 8, 8, 8, 8)


def Update() :
    frameError = Error.GifWork()
    #frameFolder = Folder.GifWork()
    #frameSecur = Secur.GifWork()
    
    Error.Move()
    #Folder.Move()
    #Secur.Move()
    
    # window.geometry('gifSize+' + str(Position x) + '+Floor y')
    
    errorWindow.geometry(str(Error.spriteSizeX) + 'x' + str(Error.spriteSizeY) + str(Error.posX) + str(Error.posY)) 
    errorLabel.configure(image = frameError)
    
    #folderWindow.geometry(str(Folder.spriteSizeX) + 'x' + str(Folder.spriteSizeY) + str(Folder.posX) + str(Folder.posY)) 
    #folderLabel.configure(image = frameFolder)
    
    #securWindow.geometry(str(Secur.spriteSizeX) + 'x' + str(Secur.spriteSizeY) + str(Secur.posX) + str(Secur.posY)) 
    #securLabel.configure(image = frameSecur)
    
    Error.DefineNextEvent()
    #Folder.DefineNextEvent()
    #Secur.DefineNextEvent()
    
    mainWindow.after(1, Update)
  

# all windows configuration
    
mainWindow.config(highlightbackground = 'black')
mainLabel = tk.Label(mainWindow, bd = 0, bg = 'black')
mainWindow.overrideredirect(True)
mainWindow.wm_attributes('-transparentcolor', 'black')
mainLabel.pack()

errorWindow.config(highlightbackground = 'black')
errorLabel = tk.Label(errorWindow, bd = 0, bg = 'black')
errorWindow.overrideredirect(True)
errorWindow.wm_attributes('-transparentcolor', 'black')
errorLabel.pack()

folderWindow.config(highlightbackground = 'black')
folderLabel = tk.Label(folderWindow, bd = 0, bg = 'black')
folderWindow.overrideredirect(True)
folderWindow.wm_attributes('-transparentcolor', 'black')
folderLabel.pack()

securWindow.config(highlightbackground = 'black')
securLabel = tk.Label(securWindow, bd = 0, bg = 'black')
securWindow.overrideredirect(True)
securWindow.wm_attributes('-transparentcolor', 'black')
securLabel.pack()

mainWindow.after(1, Update)
mainWindow.mainloop()