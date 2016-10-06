from PySide import QtGui
from cores import TextManager

class TextView(QtGui.QDockWidget):

    textManager = None
    fileName = None
    
    def __init__(self, parent, fileName = None):
        super(TextView, self).__init__(parent)
        self.textManager = TextManager()
        self.fileName = fileName

        self.prepareUI()

    def prepareUI(self):
        self.resize(self.parent().size())
        # self.label = QtGui.QLabel("tessss", self)
        self.textEditor = QtGui.QTextEdit(self)
        self.textEditor.resize(self.size())

        self.prepareTheText()

    def prepareTheText(self):
        print("prepare the text")
        if self.fileName != None:
            print("file name is not none")
            text = self.textManager.readFile(self.fileName)
            self.textEditor.setText(text)

        print(self.fileName)