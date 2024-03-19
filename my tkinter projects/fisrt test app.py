import tkinter as tk 
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk() #the window of our app(esential)
        self.root.geometry = ('400x400') #the opening default size of our app
        self.root.title("A very simple test app") #the title bar of the app
        self.mainframe = tk.Frame(self.root, background="white") #over here we define the parent frame of the app in self and this is the frame in which all our UI and widgets will come 
        self.mainframe.pack(fill="both", expand=True)#this says the parent frame to span over the entire app
        self.text = ttk.Label(self.mainframe, text="Hello world!", background="black", font=("Harlow Solid Italic", 35))#adding text to the parent frame i.e. self.mainframe
        self.text.grid(row=0, column=0)#defining the location of the text
        self.set_text_field = ttk.Entry(self.mainframe)#this gives a text field to give our input
        self.set_text_field.grid(row= 2, column=0, sticky='NWES')#(sticky='NWES' EXPANDS THE TEXT FILED to the the full row width of previous element)) #this gives and input text field grid function puts the widget on the mainframe
        self.text_button = ttk.Button(self.mainframe, text='Set text', command=self.set_text)#this assigns the button with a function(change the heading text) and to assign a function command= is given    
        self.text_button.grid(row=2, column=2)

        color_options = ['red', 'green', 'blue', 'yellow']
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        set_color_button = ttk.Button(self.mainframe, text='Set text color', command=self.set_color)#this assigns the button with a function(change the heading text) and to assign a function command= is given    
        self.set_color_field.grid(row=3, column=0, sticky='NWES')
        set_color_button.grid(row=3, column=2)

        self.root.mainloop()#essential
        return
    
    def set_text(self):                     #function to change the heading text
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)# .config changes the original value of self.whatever

    def set_color(self):
        new_color = self.set_color_field.get()
        self.text.config(foreground=new_color)
    
if __name__ == '__main__':
    App() 