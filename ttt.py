#!/usr/bin/env python3

from tkinter import *
import aimodule as ai

class TTT(Tk):

    messlist = ["", "X Wins", "O Wins", "Tie"]
    winners = ( (0,1,2), (3,4,5), (6,7,8), (0,3,6),
                (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    symbol = [" ","X","O"]
 
    EMPTY   = 0
    NOTOVER = 0    # game states 0 to 3
    XPLAYER = 1
    OPLAYER = 2
    TIEGAME = 3

    def __init__(self):
        self.parent = Tk.__init__(self)

        self.mess = Label(text="", width=9, font=("Helvetica",60), relief="groove")
        self.mess.grid(row=0,column=0,columnspan=3)

        self.lablist = []
        for row in [1,2,3]:
            for col in [0,1,2]:
                lab = Label(text=" ", width=3, font=("Helvetica",60), relief='ridge')
                lab.grid(row=row,column=col)
                lab.bind("<Button-1>", self.callback)
                lab.num = 3*(row-1) + col
                self.lablist.append(lab)

        self.board = [0] * 9
        self.turn = TTT.XPLAYER 
        self.gameover = False

        self.but1 = Button(text="Quit", font=("Helvetica",20),
                          relief="groove", command=self.quit)
        self.but1.grid(row=4,column=0,sticky="nsew")

        self.but2 = Button(text="Reset", font=("Helvetica",20),
                          relief="groove", command=self.reset)
        self.but2.grid(row=4,column=2,sticky="nsew")

    def reset(self):
        self.mess.configure(text=" ")
        self.board = [0] * 9
        self.turn = TTT.XPLAYER 
        self.gameover = False
        for lab in self.lablist:
            lab.configure(text=" ")

    def checkgame(self):
        who = self.turn
        for pat in TTT.winners:
            if all([self.board[x] == who for x in pat]):
                return who
        if 0 not in self.board:           # no empty squares left?  is none, game is over.
            return TTT.TIEGAME
        return TTT.NOTOVER

    def callback(self,event):
        if self.gameover:                 # if game is over return
            return
        if self.turn == TTT.XPLAYER:
            n = event.widget.num              # n is square player clicked
        else:
            n = ai.phase2(self.board, self.turn)
        if self.board[n] != 0:
            return
        lab = self.lablist[n]                          # which label was clicked
        lab.configure(text=TTT.symbol[self.turn])      # make mark on the graphical board
        self.board[n] = self.turn                      # mark the logical board where player moved
        retval = self.checkgame()
        if retval != 0:
            self.mess.configure(text=TTT.messlist[retval])
            self.gameover = True
        self.turn = 3 - self.turn

if __name__ == "__main__":

    game = TTT()
    game.mainloop()
