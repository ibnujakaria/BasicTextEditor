from PySide import QtGui, QtCore
from cores import TextManager

class Tab(QtGui.QWidget):

    textManager = None
    fileName = None
    active = True
    tabCloseRequested = QtCore.Signal()
    
    def __init__(self, parent, fileName = None):
        super(Tab, self).__init__(parent)
        self.textManager = TextManager()
        self.fileName = fileName

        self.tabCloseRequested.connect(self.closeThisTab)
        self.prepareUI()

    def prepareUI(self):
        self.prepareTextView()

    def prepareTextView(self):
        self.textEditor = QtGui.QTextEdit(self)
        self.textEditor.resize(self.parent().width() - 5, self.parent().height() - 20)

        if (self.fileName):
            self.readTheTextFromSource()

    def readTheTextFromSource(self):
        print("prepare the text")
        if self.fileName != None:
            print("file name is not none")
            text = self.textManager.readFile(self.fileName)
            self.textEditor.setText(text)

        # print(text)

    def setActive(self, active):
        if not active:
            self.textEditor.hide()
        else:
            self.textEditor.show()

        self.active = active

    def closeThisTab(self):
        print('closing tab')