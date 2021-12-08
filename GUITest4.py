
import tkinter as tk 
import tkinter.filedialog as fd
import tkinter.messagebox as mb

class MyWindow(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self) # <=> super().__init__()
        
        self.minsize(500,200)
        self.title("File Browser")
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)


    # create a Text widget
        self.txt = tk.Text(self, wrap=tk.NONE)
        self.txt.grid(row=0, column=0, sticky=tk.E+tk.W+tk.N+tk.S, padx=2, pady=2)

   # create a Scrollbar and associate it with txt
        scrollb = tk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky=tk.N+tk.S)
        
        self.txt['yscrollcommand'] = scrollb.set
        
         # create a Scrollbar and associate it with txt
        scrollb2 = tk.Scrollbar(self, command=self.txt.xview, orient='horizontal')
        scrollb2.grid(row=1, column=0, sticky=tk.E+tk.W)
        
        self.txt['xscrollcommand'] = scrollb2.set  
        
        self.setMenu()
        
    def setMenu(self):
        import sys
        mainmenu = tk.Menu(self)  # MenuBar
         
        menuFile = tk.Menu(mainmenu)  # Menu File
        menuFile.add_command(label="Open", command=self.openFile)
        menuFile.add_command(label="Clear", command=self.clear)
        menuFile.add_command(label="Quit", command=sys.exit) 
  
        menuHelp = tk.Menu(mainmenu) # Menu Help
        menuHelp.add_command(label="About", command=self.about) 
        
        mainmenu.add_cascade(label = "File", menu=menuFile) 
        mainmenu.add_cascade(label = "Help", menu=menuHelp)
        
        # display the menu
        self.config(menu = mainmenu) 

    def about(self): 
        mb.showinfo("A tkinter example", "Version 1.0")
        
    def hello(self):
        print("Hello", self.nameStr.get())
        
    def clear(self):
        self.txt.delete('1.0', tk.END)     
        
    def openFile(self): 
        FILEOPENOPTIONS = dict(
                               filetypes=[('Text file', '*.txt'),('Python file','*.py'),('All files','*.*')])
        file_path = fd.askopenfilename(parent=self, **FILEOPENOPTIONS)
        if file_path:
            with open(file_path) as fic:
                self.txt.delete('1.0', tk.END) # To clear the content of the Text widget
                ix=1
                for line in fic:
                    line=f"{ix:6d} {line}"
                    self.txt.insert(tk.END, line)
                    ix+=1
                    
                    
              
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()
