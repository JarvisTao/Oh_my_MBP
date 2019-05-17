from tkinter import *
from datetime import datetime as dt
from FIB import book_FIB
import time

class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Book FIB for my Pig!!',height=10, width=30)
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command = self.quit, height = 2, width = 5, bg = 'gray')
        self.quitButton.pack()



def runFn():
    i = 1
    result = ''
    while i < 5 and result.find('Success') == -1:
        deltaTime = stTime - dt.now()
        result = book_FIB(stEntry.get(),edEntry.get())
        showText.config(state=NORMAL)
        # showText.delete(1.0,END)
        showText.insert(END, "Beginning: this is the {} try at {}\n".format(i,dt.now().strftime("%Y-%m-%d %H:%M")))
        showText.insert(END, ('\t'+stEntry.get()+' ~ '+edEntry.get()+'\n'))
        showText.insert(END, ('\tResult: '+result+'\n'))
        showText.config(state=DISABLED)
        showText.pack()
        i += 1
        # for i in range(10):
        #     showText.insert(END,(str(i)+'\n'))
        #     showText.pack()
    #     time.sleep(1)

if __name__ == '__main__':
    # app = Application()
    # app.master.title('Book FIB')
    #
    # app.mainloop()
    top = Tk()
    top.title('Book FIB')
    titleMessageLable = Label(top, text = "Book FIB for my Pig!!", height = 5)
    titleMessageLable.pack()

    f1 = Frame(top)
    Label(f1, text='Start time: ').pack(side = LEFT, padx = 5, pady = 10)
    e1 = StringVar()
    stEntry = Entry(f1, width = 50, textvariable = e1)
    stEntry.pack(side = LEFT)
    e1.set("2019-05-31 8:00")
    f1.pack()

    f2 = Frame(top)
    Label(f2, text=' End time:  ').pack(side = LEFT, padx = 5, pady = 10)
    e1 = StringVar()
    edEntry = Entry(f2, width = 50, textvariable = e1)
    edEntry.pack(side = LEFT)
    e1.set("2019-05-31 12:00")
    f2.pack()

    stTime = dt.strptime(stEntry.get(), '%Y-%m-%d %H:%M')
    edTime = dt.strptime(edEntry.get(), '%Y-%m-%d %H:%M')

    runButton = Button(top, text = 'Run', command = runFn,height = 2, width= 5, bg = 'gray')
    runButton.pack()
    # showText = Text(top, height = 10, width = 50, bg = 'white')
    f3 = Frame(top)
    showText = Text(f3, height = 10, width = 55, bg = 'white')
    showText.pack(side = LEFT)
    scrl = Scrollbar(f3,command = showText.yview)
    showText.config(yscrollcommand = scrl.set)
    scrl.pack(side=RIGHT, fill=Y)
    showText.pack()
    f3.pack()


    # while deltaTime.days == 13:

    quitButton = Button(top, text = "Quit", command = top.quit, height = 2, width = 5, bg = 'gray', relief = SUNKEN)
    quitButton.pack()
    top.mainloop()

