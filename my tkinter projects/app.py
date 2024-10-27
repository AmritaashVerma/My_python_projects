import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry = ('400x400')
        self.mainframe = tk.Frame(self.root, background="white")
        self.text = ttk.Label(self.mainframe, text="Addition of 2 numbers:")

        self.root.mainloop()
        return
    
if __name__ == '__main__':
    App()