from PySide import QtGui, QtCore
from views.menus import FileMenu
from views.widgets import TextView

class MainWindow(QtGui.QMainWindow):

    statusBar = None
    menuBar = None
    textViews = []

    def __init__(self):
        super(MainWindow, self).__init__()

        self.prepareUI()

    def prepareUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Basic Text Editor')
        self.prepareStatusBar()
        self.prepareMenuBar()
        self.prepareDockWidget()
        self.show()

    def prepareStatusBar(self):
        self.statusBar = QtGui.QStatusBar()
        self.statusBar.showMessage('Ready')
        self.setStatusBar(self.statusBar)

    def prepareMenuBar(self):
        self.menuBar = QtGui.QMenuBar()
        self.menuBar.addMenu(FileMenu(self))

        self.setMenuBar(self.menuBar)

    def prepareDockWidget(self):
        self.label = QtGui.QLabel("Selamat datang di basic text editor :)", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.resize(self.width(), self.height() - 50)
        self.label.setFont(QtGui.QFont('Sans', 20))
        self.label.move(0, 30)

    def newTab(self, fileName = None):
        print("mainmenu-new-tab")
        print(fileName)
        textView = TextView(self, fileName)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, textView)
        self.textViews.append(textView)

        #self.label.hide()