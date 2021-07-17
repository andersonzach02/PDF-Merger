import tkinter.ttk as ttk
from PDFLabel import PDFLabel

class PDFLabels(ttk.Frame):

    def __init__(self, parent, row=0, column=0, master=None):
        super().__init__(master)
        self.grid(row=row, column=column)

        self.fileNames = []
        self.PDFLabels = []

        self.parent = parent

        self.PDFLabelFrame = ttk.Labelframe(self, labelanchor="n", text="PDFs to Merge")
        self.PDFLabelFrame.grid(row=1, column=0)

        self.scrollBar = ttk.Scrollbar(self.PDFLabelFrame)
        self.scrollBar.grid(row=0, column=3)


    def createChosenPDFLabels(self):
        for index in range(len(self.fileNames)):
            currentFilePath = self.fileNames[index]
            currentFilePath = currentFilePath.split("/")

            lastSplitItemIndex = len(currentFilePath) - 1
            currentFileName = currentFilePath[lastSplitItemIndex]

            self.PDFLabels.append(PDFLabel(self.PDFLabelFrame, currentFileName, index))
    
    def clearPDFLabelFrame(self):
        if(len(self.fileNames) > 0):
            self.fileNames.clear()
            PDFLabelFrameChildren = self.PDFLabelFrame.winfo_children()

            for child in PDFLabelFrameChildren:
                child.destroy()

    def updateLabelFrame(self, labelToRemove):
        self.fileNames.pop(labelToRemove.row)
        self.PDFLabels.remove(labelToRemove)

        labelWidgets = self.winfo_children()[0].winfo_children()

        labelWidgets = list(filter(lambda x: x.cget("text") != labelToRemove.PDFFileLabel.cget("text"), labelWidgets))

        labelToRemove.destroy()

        for index in range(len(self.PDFLabels)):
            self.PDFLabels[index].row = index
            

