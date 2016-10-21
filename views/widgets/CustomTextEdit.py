from PySide import QtGui, QtCore
import re

class CustomTextEdit(QtGui.QTextEdit):

    completion = None

    def __init__(self, parent):
        super(CustomTextEdit, self).__init__(parent)

        self.textChanged.connect(self.onTextChanged)
        self.completer = QtGui.QCompleter([])
        self.updateCompleterModel()
        self.completer.setWidget(self)
        self.completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.highlighted.connect(self.onCompleterHighLighted)

    def onTextChanged(self):
        cursor = self.textCursor()
        cursor.select(QtGui.QTextCursor.WordUnderCursor)
        currentWord = cursor.selectedText()

        self.completer.setCompletionPrefix(currentWord)

        cr = self.cursorRect()
        cr.setWidth(
            self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width()
        )

        if len(currentWord):
            self.completer.complete(cr)

    def onCompleterHighLighted(self, text):
        self.completion = text

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Space:
            if self.completer.popup().isVisible():
                completion = self.completion
                if not completion:
                    completion = self.completer.currentIndex().data()
                self.completer.popup().hide()
                self.insertCompletion(completion)
                return False

            self.updateCompleterModel()

        QtGui.QTextEdit.keyPressEvent(self, event)

    def insertCompletion(self, completion):
        cursor = self.textCursor()
        cursor.select(QtGui.QTextCursor.WordUnderCursor)
        cursor.insertText(completion + " ")
        self.setTextCursor(cursor)

    def updateCompleterModel(self):
        model = []

        words = re.sub('[^a-zA-Z0-9 \\n \n\.]', ' ', self.toPlainText()).split(' ')

        for word in words:
            if not word in model:
                model.append(word.strip())


        self.completer.setModel(QtGui.QStringListModel(model))