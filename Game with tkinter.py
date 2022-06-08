from tkinter import *

score = 0
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']
time = 30
def startGame(event):
    if time==30:
        countdown()
    nextcolor()
def nextcolor():
    global score
    global time
    if time > 0:
        colour_entry.focus_set()
        if colour_entry.get().lower() == colours[1].lower():
            score += 1
        colour_entry.delete(0, END)
        colour.config(fg= str(colours[1]) , text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))
def countdown():
    global time
    if time > 0 :
        time -= 1
        timeLabel.config(text = "Time left: "+ str(time))
        timeLabel.after(1000, countdown)
if __name__=='__main__':
    root = Tk()
    root.title('Color Game')
    root.geometry('375x200')
    instructions = Label(root, text = 'Type in the colour of the words, and not the word text!', font = ('Helvetica', 12))
    instructions.pack()
    scoreLabel = Label(root, text = 'Score :'+str(score), font=('Helvetica' , 12))
    scoreLabel.pack()
    timeLabel = Label(root, text = 'Time Left : '+str(time), font=('Helvetica' , 12))
    timeLabel.pack()
    colour = Label(root, font=('pink',12))
    colour.pack()
    colour_entry = Entry(root)
    colour_entry.focus_set()
    root.bind('<Return>',startGame)

    colour_entry.pack()

    root.mainloop()