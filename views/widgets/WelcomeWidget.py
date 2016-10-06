from PySide import QtGui

class WelcomeWidget(QtGui.QDockWidget):
    
    def __init__(self, parent):
        super(WelcomeWidget, self).__init__(parent)
        self.prepareUI()

    def prepareUI(self):
        self.resize(self.parent().size())
        # self.label = QtGui.QLabel("tessss", self)
        self.textEditor = QtGui.QTextEdit(self)
        self.textEditor.resize(self.size())