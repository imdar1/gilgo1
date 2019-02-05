from tkinter import *
from PIL import ImageTk, Image
import random

# Saat tombol1 diklik
def start():
    #lblstat.grid(column=0,row=5)
    if (tombol1["text"]=="Start Game"):
        lblstat.configure(text="Game dimulai")
        lblstat.pack(side=LEFT)
        #lblstat.pack(anchor=E)
        #lblwelcome.pack_forget()
        lblwelcome.configure(text="Sisa deck : "+str(len(templist)),font = ("Arial",8))
        tombol1.configure(text="Stop Game")
        random.shuffle(templist)
        gameStart()
    else:
        # reset cards
        lblstat.configure(text="Game berhenti")
        lblwelcome.configure(text="Welcome to 24 game solver",font = ("Arial",20))
        #lblwelcome.pack()
        resetGame()
        tombol1.configure(text="Start Game")

def clickdecks(event):
    if (len(templist)>0 and tombol1["text"]=="Stop Game"):
        gameStart()

def concatdir(a):
    const_dir = "./cards/"
    return const_dir+a

def idxtoval(idx):
    x = idx % 13
    if (x == 0):
        return 13
    else:
        return x

def updateImg(lbl,idx):
    imgtmp = Image.open(cardsname[idx])
    imgtmp = imgtmp.resize((69, 105), Image.ANTIALIAS)
    imgtktmp = ImageTk.PhotoImage(imgtmp)
    #lbl["image"] = imgtmp
    lbl.configure(image=imgtktmp)
    lbl.image = imgtktmp

def changeCard(list,lbl, lblimg):
    idx = list.pop()
    updateImg(lblimg,idx)
    lbl.configure(text=str(idxtoval(idx)))

def gameStart():
    changeCard(templist,lblangka1,lblimg1)
    changeCard(templist,lblangka2,lblimg2)
    changeCard(templist,lblangka3,lblimg3)
    changeCard(templist,lblangka4,lblimg4)
    lblwelcome.configure(text="Sisa deck : "+str(len(templist)),font = ("Arial",8))
    #if (len(templist) == 0):
    #    start()

def resetGame():
    updateImg(lblimg1,0)
    updateImg(lblimg2,0)
    updateImg(lblimg3,0)
    updateImg(lblimg4,0)
    lblangka1["text"] =""
    lblangka2["text"] =""
    lblangka3["text"] =""
    lblangka4["text"] =""
    global templist
    templist = [i for i in range(1,53) ]
    #templist.update([i for i in range(1,53) ])

const_cardslist = list(map(concatdir ,("blue_back.png","AC.png","2C.png","3C.png","4C.png","5C.png",
                                       "6C.png","7C.png","8C.png","9C.png","10C.png","JC.png","QC.png","KC.png",
                                       "AD.png","2D.png","3D.png","4D.png","5D.png","6D.png","7D.png","8D.png",
                                       "9D.png","10D.png","JD.png","QD.png","KD.png","AH.png","2H.png","3H.png",
                                       "4H.png","5H.png","6H.png","7H.png","8H.png","9H.png","10H.png","JH.png",
                                       "QH.png","KH.png","AS.png","2S.png","3S.png","4S.png","5S.png","6S.png",
                                       "7S.png","8S.png","9S.png","10S.png","JS.png","QS.png","KS.png")))

#Untuk shuffle list
templist = [i for i in range(1,53) ]

# Jendela
window = Tk()
window.title("24 Solver Game")
window.geometry('640x480')
window.minsize(640, 480)

#Frame game
split = 0.9
framegame = Frame(window,relief=RAISED)
framegame.place(rely=0, relheight=split, relwidth=1)

#Frame menu
framemenu = Frame(window)
framemenu.place(rely=split, relheight=1.0-split, relwidth=1)

#frame 4 cards
framecards = Frame(framegame)
framecards.place(rely=0.4,relheight = 0.5, relwidth=1)

# Cards Image
cardsname = const_cardslist
imgcards = Image.open(cardsname[0])
imgcards = imgcards.resize((69, 105), Image.ANTIALIAS)
imgtkcards = ImageTk.PhotoImage(imgcards)
lblimg = Label(framegame,image=imgtkcards)
lblimg.image = imgtkcards
lblimg.bind('<Button-1>',clickdecks)
lblimg.pack()

# cards in frame
#img1 = ImageTk.PhotoImage(imgcards)
lblimg1 = Label(framecards,image=imgtkcards)
#img2 = ImageTk.PhotoImage(imgcards)
lblimg2 = Label(framecards,image=imgtkcards)
#img3 = ImageTk.PhotoImage(imgcards)
lblimg3 = Label(framecards,image=imgtkcards)
#img4 = ImageTk.PhotoImage(imgcards)
lblimg4 = Label(framecards,image=imgtkcards)
lblimg1.place(relx =0.2, rely= 0.5, anchor = CENTER)
lblimg2.place(relx =0.4, rely= 0.5, anchor = CENTER)
lblimg3.place(relx =0.6, rely= 0.5, anchor = CENTER)
lblimg4.place(relx =0.8, rely= 0.5, anchor = CENTER)

#lblangka
lblangka1 = Label(framecards, text="")
lblangka2 = Label(framecards, text="")
lblangka3 = Label(framecards, text="")
lblangka4 = Label(framecards, text="")
lblangka1.place(relx =0.2, rely= 0.8, anchor = CENTER)
lblangka2.place(relx =0.4, rely= 0.8, anchor = CENTER)
lblangka3.place(relx =0.6, rely= 0.8, anchor = CENTER)
lblangka4.place(relx =0.8, rely= 0.8, anchor = CENTER)


# Label selamat datang
lblwelcome = Label(framegame,text="Welcome to 24 game solver",font = ("Arial",20))
lblwelcome.pack()
#lblwelcome.grid(column=0,row=0)

lblstat = Label(framemenu,text="", font = ("Arial",12))

# Tombol
tombol1 = Button(framemenu, text = "Start Game", command=start)
tombol1.pack(side = LEFT)
#tombol1.place(width = 50)
#tombol1.grid(column = 0, row=0)
#tombol1.place(width=100)

tombol2 = Button(framemenu,text = "Exit",command=quit)
tombol2.pack(side = LEFT)
#tombol2.grid(column = 1, row=0)
#tombol2.place(width=50)

window.mainloop()