from tkinter import *
from PIL import ImageTk, Image

def start():
    #lblstat.grid(column=0,row=5)
    lblstat.configure(text="Game dimulai")
    lblstat.pack(side=LEFT)
    #lblstat.pack(anchor=E)
    lblwelcome.pack_forget()
    
# Jendela
window = Tk()
window.title("24 Solver Game")
window.geometry('640x480')

split = 0.9
#Frame game
framegame = Frame(window,bg="green",relief=RAISED)
framegame.place(rely=0, relheight=split, relwidth=1)
#framegame.place(width=640)
#framegame.
#Frame menu
framemenu = Frame(window)
framemenu.place(rely=split, relheight=1.0-split, relwidth=1)

# Cards Image
cardsname = ["./cards/blue_back.png"]
imgcards = Image.open(cardsname[0])
imgcards = imgcards.resize((69, 105), Image.ANTIALIAS)
imgtkcards = ImageTk.PhotoImage(imgcards)
lblimg = Label(framegame,image=imgtkcards)
lblimg.image = imgtkcards
lblimg.pack()


# Label
lblwelcome = Label(framegame,text="Welcome to 24 game solver", bg="green",font = ("Arial",20))
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