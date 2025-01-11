from tkinter import *
from tkinter.ttk import *
from App.Game import Game
import os, time

class App(Tk):
    def __init__(self):
        super().__init__()

        self.iconphoto(True, PhotoImage(file="images/tic-tac-toe.png"))
        self.title("Tic Tac Toe - Menu")
        self.geometry("1280x720")
        self.configure(bg="white")

        self.button = Button(self, text="PLAY", command=self.play)
        self.button.pack()

        self.bind("<Destroy>", self.on_destroy)
    
    def on_destroy(self, event):
        if event.widget != self:
            return
        os.system("make clean")
    
    def destroy_widget(self, widget):
        widget.destroy()
    
    def update_label(self):
        self.label.config(text="Goodbye, World!")
        self.after(2000, self.destroy)

    def clear_all_wdigets(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def play(self):
        self.clear_all_wdigets()
        self.game = Game(self)
