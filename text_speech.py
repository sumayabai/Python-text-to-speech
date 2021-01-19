#import libraries
from Tkinter import *
from gtts import gTTS
from playsound import playsound

#initializing windows
root = Tk() #initialie tkinter
geometry.root("350x300") #width and height of the windows
root.configure(bg='ghost white')#access window attributes
root.title("DataFlair - TEXT TO SPEECH")#title of the window

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="DataFlair", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

#function to convert text to speech
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
#function to exit
def Exit():
	root.destroy()
#function to reset
def Reset():
    Msg.set("")

#define buttons
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()