from PySide import QtGui, QtCore
from views.menus import FileMenu
from views.widgets import Tab

class MainWindow(QtGui.QMainWindow):

    statusBar = None
    menuBar = None
    tabs = []

    def __init__(self):
        super(MainWindow, self).__init__()

        self.prepareUI()

    def prepareUI(self):
        self.resize(800, 600)
        self.setWindowTitle('Basic Text Editor')
        self.prepareStatusBar()
        self.prepareMenuBar()
        self.prepareDockWidget()
        self.prepareTabWidget()
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

    def prepareTabWidget(self):
        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.resize(self.label.size())
        self.tabWidget.move(0, 30)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.hide()

    def newTab(self, fileName = None):
        print(fileName)
        tab = Tab(self, fileName)
        title = fileName

        self.tabs.append(tab)

        if not title:
            title = "Untitled " + str(len(self.tabs))
        else:
            title = title.split("/")[-1]

        self.tabWidget.show()
        index = self.tabWidget.addTab(tab, title)
        self.tabWidget.setCurrentIndex(index)

    def hideAllTextViews(self):
        for tab in self.tabs:
            tab.setActive(False)

    def drawTextView(self, textView):
        self.textEditor.show()
        self.textEditor.setText(textView.getTheText())

    def closeTab(self, index):
        self.tabWidget.removeTab(index)
        self.tabs.pop(index)

        if not len(self.tabs):
            self.tabWidget.hide()


    def saveFile(self):
        self.tabs[self.tabWidget.currentIndex()].save()