from tkinter import *

class Game(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        parent.title("Tic Tac Toe - game")
        self.pack()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = Label(self, text="Hello, World!", background="white", font=("Arial", 24), foreground="black")
        self.label.pack()
        
        self.after(2000, self.update_label)
        
        self.button = Button(self, text="Quit", command=lambda: self.destroy_widget(self.label))
        self.button.pack()
    
    def destroy_widget(self, widget):
        widget.destroy()
    
    def update_label(self):
        self.label.config(text="Goodbye, World!")
        self.after(2000, self.destroy)