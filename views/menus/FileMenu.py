from PySide import QtGui, QtCore

class FileMenu(QtGui.QMenu):

    def __init__(self, main, fileName = None):
        super(FileMenu, self).__init__("File")

        self.prepareActions()
        self.mainWindow = main
        self.fileName = fileName

    def prepareActions(self):
        self.addAction("New File", self.actionNewFile, 'Ctrl+N')
        self.addAction("Open File", self.actionOpenFile, 'Ctrl+O')
        self.addAction("Save", self.actionSaveFile, 'Ctrl+S')
        self.addAction("Setting", self.actionOpenFile, 'Ctrl+Alt+S')
        self.addAction("Exit", self.actionExit, 'Ctrl+Q')

    def actionNewFile(self):
        print ("new file")
        self.mainWindow.newTab()
        pass

    def actionOpenFile(self):
        print("open file")
        fileNames = QtGui.QFileDialog.getOpenFileNames(self, 'Open File', '~/')[0]

        for fileName in fileNames:
            print(fileName)
            self.mainWindow.newTab(fileName)

    def actionSaveFile(self):
        self.mainWindow.saveFile()

    def actionSetting(self):
        print("setings")
        pass

    def actionExit(self):
        QtCore.QCoreApplication.instance().exit()