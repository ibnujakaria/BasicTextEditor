from PySide import QtGui

class FindPanel(QtGui.QGroupBox):

    def __init__(self, parent):
        super(FindPanel, self).__init__(parent)

        self.prepareUI()
        self.prepareSignalAndSlots()

    def prepareSignalAndSlots(self):
        self.findEditText.returnPressed.connect(self.findText)
        self.findBtn.clicked.connect(self.findText)
        self.replaceEditText.returnPressed.connect(lambda: self.findText(action = 'replace'))
        self.replaceBtn.clicked.connect(lambda: self.findText(action = 'replace'))

    def prepareUI(self):
        self.setStyleSheet('background-color: rgb(240, 240, 240)')
        self.layout = QtGui.QGridLayout()
        self.prepareButton()
        self.updateTheSizeAndThePosition()
        self.setLayout(self.layout)

    def prepareButton(self):
        self.resultLabel = QtGui.QLabel("Find something..")
        self.findBtn = QtGui.QPushButton("Find")
        self.findEditText = QtGui.QLineEdit()
        self.findEditText.setStyleSheet('background-color: white')
        self.replaceBtn = QtGui.QPushButton("Replace")
        self.replaceEditText = QtGui.QLineEdit()
        self.replaceEditText.setStyleSheet('background-color: white')
        # self.layout.addStretch(1)
        self.layout.setVerticalSpacing(10)
        self.layout.addWidget(self.resultLabel, 0, 1)
        self.layout.addWidget(self.findEditText, 1, 1)
        self.layout.addWidget(self.findBtn, 1, 2)
        self.layout.addWidget(self.replaceEditText, 2, 1)
        self.layout.addWidget(self.replaceBtn, 2, 2)

    def updateTheSizeAndThePosition(self):
        self.resize(self.parent().width(), 120)
        self.move(0, (self.parent().height() - self.height()))

        print('panjang: ' + str(self.width()))

    def setFocus(self, focus):
        if focus == 'find':
            self.findEditText.setFocus()

    def findText(self, action = 'find'):
        tab = self.parent().getCurrentActiveTab()
        replacement = None
        if action == 'replace':
            replacement = self.replaceEditText.text()
        results = tab.findText(self.findEditText.text(), replacement)

        self.resultLabel.setText("there are " + str(len(results)) + " results")