from PySide import QtGui, QtCore
from views.menus import FileMenu
from views.widgets import WelcomeWidget

class MainWindow(QtGui.QMainWindow):

    statusBar = None
    menuBar = None

    def __init__(self):
        super(MainWindow, self).__init__()

        self.prepareUI()

    def prepareUI(self):
        self.resize(800, 600)

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
        self.label.resize(self.size())

    def newTab(self):
        self.dockWidget = WelcomeWidget(self)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.dockWidget)

        self.label.hide()