from tkinter import ttk
from ProgressWindow import ProgressWindow
from tkinter.ttk import Frame
from ControlsBar import ControlsBar
from PDFLabels import PDFLabels
import tkinter as tk
import os

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master) 

        self.outputFileName = ""
        self.pdfMerger = None
        self.progressLabel = None
        self.progressMarker = None
        self.buttonControls = ControlsBar(self, row=1, column=0)
        self.PDFLabels = PDFLabels(self, row=0, column=0)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1) 


app = Application() 
app.master.title('PDF Merger') 
app.mainloop()