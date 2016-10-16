from PySide import QtGui, QtCore
from cores import TextManager

class Tab(QtGui.QWidget):

    textManager = None
    fileName = None
    active = True
    changed = False
    currentCursorPosition = 0

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
        self.textEditor.textChanged.connect(self.onTextChanged)

        self.readTheTextFromSource()

    def readTheTextFromSource(self):
        print("prepare the text")
        if self.fileName != None:
            print("file name is not none")
            text = self.textManager.readFile(self.fileName)
            self.textEditor.setText(text)

        # print(text)

    def save(self):
        print('save file of' + self.fileName)
        print(self.textEditor.toPlainText())
        self.textManager.save(self.fileName, self.textEditor.toPlainText())

    def onTextChanged(self):
        # do nothing
        pass


