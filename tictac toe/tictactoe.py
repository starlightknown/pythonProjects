import tkinter as tk
from tkinter import *
import tkinter.messagebox
def createWidgets():
    label1 = Label(root, text= "player1",font = 20, bg= "pink", fg = "white", height = 1, width= 8 )
    label1.grid(row= 1 , column= 0)
    player1_name = Entry(root, textvariable = p1, bd = 5)
    player1_name.grid(row = 1, column = 1, columnspan = 4)
    
    label2 = Label(root, text= "player2",font = 20 , bg= "pink", fg = "white", height = 1, width= 8 )
    label2.grid(row= 2 , column= 0)
    player2_name = Entry(root, textvariable = p2, bd = 5)
    player2_name.grid(row = 2, column = 1, columnspan = 4)

    global button1
    button1 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button1))
    button1.grid(row = 3, column = 0)

    global button2
    button2 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button2))
    button2.grid(row = 3, column = 1)

    global button3
    button3 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button3))
    button3.grid(row = 3, column = 2)

    global button4
    button4 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button4))
    button4.grid(row = 4, column = 0)

    global button5
    button5 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button5))
    button5.grid(row = 4, column = 1)

    global button6
    button6 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button6))
    button6.grid(row = 4, column = 2)

    global button7
    button7 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button7))
    button7.grid(row = 5, column = 0)

    global button8
    button8 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button8))
    button8.grid(row = 5, column = 1)

    global button9
    button9 = Button(root, text = "", font= 20, bg = "pink", fg = "black", height = 4, width = 8, command =lambda: Btnclick(button9))
    button9.grid(row = 5, column = 2)
def Btnclick(buttons):
    global bclick, flag, pa, pb
    if buttons["text"]=="" and bclick == True:
        buttons["text"] = "X"
        bclick = False
        pa = p1.get() + "wins"
        pb = p2.get() + "wins"
        checkforwin()
        flag += 1
    elif buttons["text"] == "" and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkforwin()
        flag +=1
    else:
         tkinter.messagebox.showinfo("tic tac toe", "button is already clicked")      
def checkforwin():
    global button1, button2, button3, buttton4, button5, button6, button7, button8, button9
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("tic tac toe", pa)
        

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pb)
    elif(flag == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

def disableButton():
    button1.configure(state= DISABLED)
    button2.configure(state= DISABLED)
    button3.configure(state= DISABLED)
    button4.configure(state= DISABLED)
    button5.configure(state= DISABLED)
    button6.configure(state= DISABLED)
    button7.configure(state= DISABLED)
    button8.configure(state= DISABLED)
    button9.configure(state= DISABLED)
    
    
          

root = tk.Tk()
root.title("Tic Tac Toe")

p1 = StringVar()
p2 = StringVar()
buttons = StringVar()
bclick = True
flag = 0
pa = StringVar()
pb = StringVar()
createWidgets()
root.mainloop()


