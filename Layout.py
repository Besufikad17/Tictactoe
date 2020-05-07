from tkinter import *
from tkinter import ttk
from random import randint
from Controller import play


class App:
    def __init__(self,parent):
        self.val1 = StringVar()
        self.val2 = StringVar()
        self.val3 = StringVar()
        self.val4 = StringVar()
        self.val5 = StringVar()
        self.val6 = StringVar()
        self.val7 = StringVar()
        self.val8 = StringVar()
        self.val9 = StringVar()
        self.nb = ttk.Notebook(parent)
        self.value = StringVar()
        self.value2 = StringVar()
        self.incorrect = StringVar()
        self.mode = StringVar()
        self.create_widget(parent)

    def create_widget(self,parent):
        self.nb.config(height = 160)
        self.nb.pack()
        frame1 = ttk.Frame(self.nb)
        frame2 = ttk.Frame(self.nb)
        self.nb.add(frame1, text='One')
        self.nb.add(frame2, text='Two')
        self.nb.tab(1, state='disabled')

        ttk.Label(frame1, text='Game Mode').grid(row=1, column=0, padx=10,pady=20)
        ttk.Entry(frame1, textvariable=self.mode).grid(row=1, column=1,padx =5)
        ttk.Label(frame1, text='value').grid(row=3, column=0, padx=10)
        ttk.Entry(frame1, textvariable=self.value).grid(row=3, column=1)
        ttk.Button(frame1, text = 'Continue' , command = self.check).place(x = 60 , y = 110, width = 100,height = 30)
        ttk.Label(parent, textvariable = self.incorrect).pack()

        in1 = Entry(frame2, textvariable=self.val1).place(x = 60,y = 10, width = 40,height = 40)
        in2 = Entry(frame2, textvariable=self.val2).place(x = 90,y = 10, width = 40,height = 40)
        in3 = Entry(frame2, textvariable=self.val3).place(x = 120,y = 10, width = 40,height = 40)
        in4 = Entry(frame2, textvariable=self.val4).place(x = 60,y = 40, width = 40,height = 40)
        in5 = Entry(frame2, textvariable=self.val5).place(x = 90,y = 40, width = 40,height = 40)
        in6 = Entry(frame2, textvariable=self.val6).place(x = 120,y = 40, width = 40,height = 40)
        in7 = Entry(frame2, textvariable=self.val7).place(x = 60,y = 70, width = 40,height = 40)
        in8 = Entry(frame2, textvariable=self.val8).place(x = 90,y = 70, width = 40,height = 40)
        in9 = Entry(frame2, textvariable=self.val9).place(x = 120,y = 70, width = 40,height = 40)
        btn = ttk.Button(frame2, text='enter', command=self.submit).place(x = 60,y = 120, width = 100,height = 40)

    def check(self):
        game_mode =self.mode.get()
        val = self.value.get()
        if game_mode.startswith('2 players') or game_mode.startswith('single') and val.startswith('X') or val.startswith('O'):
           self.nb.tab(1,state ='normal')
           i = randint(0,1)
           if i ==0 :
               self.incorrect.set('player 1 turn')
           else:
               self.incorrect.set('player 2 turn')
           val = self.value.get()
           if val.startswith('X'):
               self.value2.set('O')
           else:
              self.value2.set('X')
        else:
            self.incorrect.set('Invalid Game Mode or Value')

    def submit(self):
        self.list = [[self.val1.get(), self.val2.get(), self.val3.get()],
                     [self.val4.get(), self.val5.get(), self.val6.get()],
                     [self.val7.get(), self.val8.get(), self.val9.get()]]
        i = 0
        turn = self.incorrect.get()
        print(self.list)
        if play(turn,self.list) is None:
            if turn == 'player 1 turn ':
                self.incorrect.set('player 2 turn')
            else:
                self.incorrect.set('player 1 turn')
        else:
            self.incorrect.set(play(turn,self.list))


def main():
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__": main()