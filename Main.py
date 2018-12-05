import tkinter as tk
import random

root = tk.Tk()
winWidth = 600
winHeight = 500
canvas = tk.Canvas(root, width=winWidth, height=winHeight)
blackLine = canvas.create_line(10, 10, 50, 200)
x = canvas.winfo_width()
y = canvas.winfo_height()
#snakeBit = canvas.create_rectangle(9, 9, x, y, fill='blue')
snakeBits = []

class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.minsize(width=winWidth, height=winHeight)
        self.master.config()
        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>',self.right_key)
        self.master.bind('<Up>', self.up_key)
        self.master.bind('<Down>', self.down_key)


        self.main_frame = tk.Frame()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()

        canvas.update()
        x = canvas.winfo_width()
        y = canvas.winfo_height()
        snakeBits.append(canvas.create_rectangle((winWidth/2) - 9, (winHeight/2) - 9, winWidth/2, winHeight/2, fill='blue'))
        canvas.pack()

    def draw_black_line():
        canvas.delete(ALL)

    @staticmethod
    def left_key(event):
        global snakeBits
        snakeBits.append(7)

    @staticmethod
    def right_key(event):
        for x in snakeBits:
            print(x)

    @staticmethod
    def up_key(event):
        print("up", canvas.winfo_width())

    @staticmethod
    def down_key(event):
        print("down", y)

xUnit = 200
mainSnake = Main(root)

mainSnake.mainloop()