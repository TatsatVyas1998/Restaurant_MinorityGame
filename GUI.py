from tkinter import *
#import Pmw

window=Tk()
window.geometry("455x350")
window.title("Minority Game")
window.configure(background="#2a2a2a")

labelTitle = Label(window,text="Restaurant Occupency Prediction",bg="#102A43",fg="white",pady=10,font="Time 20 bold").pack()

#agent frame
agentFrame = Frame(window,pady=10,bg="#2a2a2a")

labelAgents = Label(agentFrame,text= "Number of agents",fg="white",bg="#2a2a2a",font="Time 13 bold")
labelAgents.pack(side=LEFT)

entryAgents = Entry(agentFrame)
entryAgents.pack(side=LEFT)

agentFrame.pack()
lst1=[] 
# memory storage of the previous inputs
for i in range(0, 20):
    agents = str(agentFrame)
    lst1.append(agents)
#print the lists - still in progress
root = Tk()
t = Text(root)
for x in lst1:
    t.insert(END, x + '\n')
t.pack()
root.mainloop()

#roundsFrame
roundsFrame = Frame(window, bg="#2a2a2a")

labelRounds = Label(roundsFrame,text= "Number of rounds",fg="white",bg="#2a2a2a",font="Time 13 bold",anchor=E)
labelRounds.pack(side=LEFT)
lst = []



entryRounds = Entry(roundsFrame)
entryRounds.pack(side=LEFT)

roundsFrame.pack()

# memory storage of the previous inputs
for i in range(0, 20):
    rounds = str(roundsFrame)
    lst.append(rounds)
#print the lists - still in progress
root = Tk()
t = Text(root)
for x in lst:
    t.insert(END, x + '\n')
t.pack()
root.mainloop()




var=IntVar()
c= Checkbutton(window, text="Groups",variable=var,background="#2a2a2a",activebackground="#2a2a2a",fg="white",selectcolor="#2a2a2a")
c.pack()


buttonRun = Button(window, text="RUN SIMULATION",fg="white",bg="black",pady="15").pack(pady=15)

#var=IntVar()
#c= Checkbutton(window, text="Groups",variable=var)


window.mainloop()