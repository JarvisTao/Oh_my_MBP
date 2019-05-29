from tkinter import *
from datetime import datetime as dt
from datetime import timedelta
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
    showText.insert(1.0, 'Beginning: '+'\t'+stEntry.get()+' ~ '+edEntry.get()+'\n')
    showText.update()
    time.sleep(5)
    stTime = dt.strptime(stEntry.get(), '%Y-%m-%d %H:%M')
    edTime = dt.strptime(edEntry.get(), '%Y-%m-%d %H:%M')
    sysOpenTime = dt(stTime.year,stTime.month,stTime.day,8,0)
    deltaTime = sysOpenTime - dt.now()
    minNum = deltaTime.seconds
    while i >= 0 and result.find('Success') == -1:
        if deltaTime.days > 13 and minNum%3600//60 > 4:
            showText.delete(1.0,END)
            showText.insert(1.0, "The left time is: {:02d}h {:02d}m {:02d}s\n".format(minNum//3600, minNum%3600//60,minNum%60))
            showText.insert(END, "The program will run in 5 min left, now waiting~~~")
            showText.update()
            deltaTime = sysOpenTime - dt.now()
            minNum = deltaTime.seconds
            continue
        # else:
        result = book_FIB(stEntry.get(),edEntry.get())
        # sttemp = '2019-05-31 08:00'
        # edtemp = '2019-05-31 12:00'
        # result = book_FIB(sttemp,edtemp)
        showText.config(state=NORMAL)
        # showText.delete(1.0,END)
        showText.insert(1.0, "This is the {} try at {}\n".format(i,dt.now().strftime("%Y-%m-%d %H:%M")))
        showText.insert(2.0, ('\tResult: '+result+'\n'))
        showText.update()
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
    now = dt.now()
    temp = dt(now.year,now.month,now.day,8,0) + timedelta(days=15)
    # e1.set("2019-05-31 08:00")
    e1.set(temp.strftime('%Y-%m-%d %H:%M'))
    f1.pack()

    f2 = Frame(top)
    Label(f2, text=' End time:  ').pack(side = LEFT, padx = 5, pady = 10)
    e1 = StringVar()
    edEntry = Entry(f2, width = 50, textvariable = e1)
    edEntry.pack(side = LEFT)
    temp = dt(now.year,now.month,now.day,12,0) + timedelta(days=15)
    e1.set(temp.strftime('%Y-%m-%d %H:%M'))
    # e1.set("2019-05-31 12:00")
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

