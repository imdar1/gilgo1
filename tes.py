from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
import prototype1

# Saat tombol1 diklik
def start():
    #lblstat.grid(column=0,row=5)
    if (tombol1["text"]=="Start Game"):
        #lblstat.configure(text="Game dimulai")
        #lblstat.grid(row=0,column=2)
        #lblstat.pack(anchor=E)
        #lblwelcome.pack_forget()
        lblimg.configure(text="Sisa deck : "+str(len(templist)),font = ("Arial",8))
        tombol1.configure(text="Stop Game")
        random.shuffle(templist)
        gameStart()
    else:
        # reset cards
        #lblstat.configure(text="Game berhenti")
        lblimg['text'] = ""
        #lblwelcome.configure(text="Welcome to 24 game solver",font = ("Arial",20))
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
    imgtmp = imgtmp.resize((90, 137), Image.ANTIALIAS)
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
    lblimg.configure(text="Sisa deck : "+str(len(templist)),font = ("Arial",8))
    lblsolusi["text"] = "Solusi : "+prototype1.solution(int(lblangka1["text"]),int(lblangka2["text"]),int(lblangka3["text"]),int(lblangka4["text"]))
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
    lblsolusi["text"] =""
    global templist
    templist = [i for i in range(1,53) ]
    #templist.update([i for i in range(1,53) ])



cardsname = list(map(concatdir ,("red_back.png","AC.png","2C.png","3C.png","4C.png","5C.png",
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
window.title("24 Game Solver")
window.geometry('640x480')
window.minsize(640, 480)

# Style
style = ttk.Style()
style.configure("my.TFrame",background ='#008000')
style.configure("my.TLabel",background ='#008000',foreground = '#ffffff')
style.configure("my.TButton",font=("Calibri", 13, 'bold'),background="black",foreground="#008000")
style.map('my.TButton',background= [("active", "#008000")], foreground=[("active", 'black')])

#Frame game
split = 0.9
framegame = ttk.Frame(window,style = 'my.TFrame')
framegame.place(rely=0, relheight=split, relwidth=1)

#Frame menu
framemenu = ttk.Frame(window,relief="groove")
framemenu.place(rely=split, relheight=1.0-split, relwidth=1)

#frame 4 cards
framecards = ttk.Frame(framegame,style = 'my.TFrame')
framecards.place(rely=0.4,relheight = 0.5, relwidth=1)

# Cards Image
imgcards = Image.open(cardsname[0])
imgcards = imgcards.resize((90, 137), Image.ANTIALIAS) #69,105
imgtkcards = ImageTk.PhotoImage(imgcards)
lblimg = ttk.Label(framegame,image=imgtkcards,padding = 15,compound='top',style='my.TLabel')
lblimg.image = imgtkcards
lblimg.bind('<Button-1>',clickdecks)
lblimg.pack()

# cards in frame
lblimg1 = ttk.Label(framecards,image=imgtkcards,style='my.TLabel')
lblimg2 = ttk.Label(framecards,image=imgtkcards,style='my.TLabel')
lblimg3 = ttk.Label(framecards,image=imgtkcards,style='my.TLabel')
lblimg4 = ttk.Label(framecards,image=imgtkcards,style='my.TLabel')
lblimg1.place(relx =0.2, rely= 0.5, anchor = CENTER)
lblimg2.place(relx =0.4, rely= 0.5, anchor = CENTER)
lblimg3.place(relx =0.6, rely= 0.5, anchor = CENTER)
lblimg4.place(relx =0.8, rely= 0.5, anchor = CENTER)

#lblangka
lblangka1 = ttk.Label(framecards, text="",style='my.TLabel',font = ("Calibri",16,'bold'))
lblangka2 = ttk.Label(framecards, text="",style='my.TLabel',font = ("Calibri",16,'bold'))
lblangka3 = ttk.Label(framecards, text="",style='my.TLabel',font = ("Calibri",16,'bold'))
lblangka4 = ttk.Label(framecards, text="",style='my.TLabel',font = ("Calibri",16,'bold'))
lblangka1.place(relx =0.2, rely= 0.9, anchor = CENTER)
lblangka2.place(relx =0.4, rely= 0.9, anchor = CENTER)
lblangka3.place(relx =0.6, rely= 0.9, anchor = CENTER)
lblangka4.place(relx =0.8, rely= 0.9, anchor = CENTER)

# Label selamat datang
#lblwelcome = ttk.Label(framegame,text="",style='my.TLabel')
#lblwelcome.pack()

# Label solusi
lblsolusi = ttk.Label(framegame,text="",font = ("Cambria",20),style='my.TLabel')
lblsolusi.pack(side = BOTTOM)
#lblstat = ttk.Label(framemenu,text="", font = ("Arial",12))

# Tombol
tombol1 = ttk.Button(framemenu, text = "Start Game", style='my.TButton',command=start)
tombol1.grid(row=0,column=0,padx = 10, pady = 8)

tombol2 = ttk.Button(framemenu,text = "Exit",style='my.TButton',command=quit)
tombol2.grid(row=0,column=1,padx=10,pady = 8)

window.mainloop()
