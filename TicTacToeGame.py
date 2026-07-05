from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack(pady=20)
title_label = Label(frame1, text="Tic Tac Toe", font=("Arial", 24))
title_label.pack()

frame2 = Frame(root)
frame2.pack(pady=20)

turn = "X"  # Start with player X

def play(event):
    global turn
    button = event.widget

    if button["text"] == "":
        if turn == "X":
            button["text"] = "X"
            turn = "O"
        else:
            button["text"] = "O"
            turn = "X"
    
# Create buttons for the Tic Tac Toe grid

#1st row
button1 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button1.grid(row=0, column=0, padx=5, pady=5)
#button1.config(command=lambda: on_button_click(button1))
button1.bind("<Button-1>", play)

button2 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button2.grid(row=0, column=1, padx=5, pady=5)
#button2.config(command=lambda: on_button_click(button2))
button2.bind("<Button-1>", play)

button3 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button3.grid(row=0, column=2, padx=5, pady=5)
#button3.config(command=lambda: on_button_click(button3))
button3.bind("<Button-1>", play)

#2nd row
button4 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button4.grid(row=1, column=0, padx=5, pady=5)
#button4.config(command=lambda: on_button_click(button4))
button4.bind("<Button-1>", play)

button5 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button5.grid(row=1, column=1, padx=5, pady=5)
#button5.config(command=lambda: on_button_click(button5))
button5.bind("<Button-1>", play)

button6 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button6.grid(row=1, column=2, padx=5, pady=5)
#button6.config(command=lambda: on_button_click(button6))
button6.bind("<Button-1>", play)

#3rd row
button7 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")    
button7.grid(row=2, column=0, padx=5, pady=5)
#button7.config(command=lambda: on_button_click(button7))
button7.bind("<Button-1>", play)

button8 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button8.grid(row=2, column=1, padx=5, pady=5)
#button8.config(command=lambda: on_button_click(button8))
button8.bind("<Button-1>", play)

button9 = Button(frame2, text="", font=("Arial", 30), width=5, height=2, bg="#0D3B66", fg="#FAF0CA")
button9.grid(row=2, column=2, padx=5, pady=5)
#button9.config(command=lambda: on_button_click(button9))
button9.bind("<Button-1>", play)


root.mainloop()