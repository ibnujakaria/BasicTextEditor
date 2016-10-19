from PySide import QtGui, QtCore
from cores import TextManager

class Tab(QtGui.QWidget):

    textManager = None
    fileName = None
    active = True
    changed = False
    currentCursorPosition = 0
    i = 0

    def __init__(self, parent, fileName = None):
        super(Tab, self).__init__(parent)
        self.textManager = TextManager()
        self.fileName = fileName
        self.mainWindow = parent
        self.prepareUI()
        self.updateSizeAndPosition()

    def prepareUI(self):
        self.prepareTextView()

    def prepareTextView(self):
        self.textEditor = QtGui.QTextEdit(self)
        self.textEditor.textChanged.connect(self.onTextChanged)

        self.readTheTextFromSource()

        cursor = self.textEditor.textCursor()
        cursor.movePosition(QtGui.QTextCursor.Start)
        self.textEditor.setTextCursor(cursor)

    def focusToTheTextEditor(self):
        self.textEditor.setFocus()

    def readTheTextFromSource(self):
        print("prepare the text")
        if self.fileName != None:
            print("file name is not none")
            text = self.textManager.readFile(self.fileName)
            self.textEditor.setText(text)

            # print(text)

    def save(self):
        if self.fileName == None:
            # fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '~/')
            self.fileName = QtGui.QFileDialog.getSaveFileName(self, 'Open File', '~/')[0]
            title = self.fileName.split("/")[-1]
            self.mainWindow.updateCurrentTabTitle(title)
        self.textManager.save(self.fileName, self.textEditor.toPlainText())

    def onTextChanged(self):
        # do nothing
        pass


    def findText(self, keyword, replacement = None):
        results = self.textManager.findText(keyword, self.textEditor.toPlainText())
        yellowText = QtGui.QTextCharFormat()
        yellowText.setBackground(QtGui.QColor('yellow'))
        self.textEditor.selectAll()
        self.textEditor.setTextBackgroundColor(QtGui.QColor('transparent'))
        for result in results:
            start = result.get('start')
            end = result.get('end')

            cursor = self.textEditor.textCursor()
            cursor.setPosition(start)
            cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
            cursor.setCharFormat(yellowText)
            self.textEditor.setTextCursor(cursor)

            if replacement:
                self.textEditor.insertPlainText(replacement)

        if len(results):
            start = results[0].get('start')
            end = results[0].get('end')
            cursor = self.textEditor.textCursor()
            cursor.setPosition(start)
            cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
            self.textEditor.setTextCursor(cursor)

        # self.textEditor.setFocus()

        # update the find panel
        return results


    def updateSizeAndPosition(self):
        self.textEditor.resize(self.parent().width() - 5, self.parent().height() - 90)

    def resizeEvent(self, event):
        self.updateSizeAndPosition()