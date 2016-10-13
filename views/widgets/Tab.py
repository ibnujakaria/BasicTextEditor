from PySide import QtGui, QtCore
from cores import TextManager

class Tab(QtGui.QWidget):

    textManager = None
    fileName = None
    active = True
    
    def __init__(self, parent, fileName = None):
        super(Tab, self).__init__(parent)
        self.textManager = TextManager()
        self.fileName = fileName

        self.prepareUI()

    def prepareUI(self):
        self.prepareTextView()

    def prepareTextView(self):
        self.textEditor = QtGui.QTextEdit(self)
        self.textEditor.resize(self.parent().width() - 5, self.parent().height() - 90)

        self.readTheTextFromSource()

    def readTheTextFromSource(self):
        print("prepare the text")
        if self.fileName != None:
            print("file name is not none")
            text = self.textManager.readFile(self.fileName)
            self.textEditor.setHtml(text)

        # print(text)