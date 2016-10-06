from PySide import QtGui

class FileMenu(QtGui.QMenu):

    def __init__(self, main):
        super(FileMenu, self).__init__("File")

        self.prepareActions()
        self.mainWindow = main

    def prepareActions(self):
        self.addAction("New File", self.actionNewFile, 'Ctrl+N')
        self.addAction("Open File", self.actionOpenFile, 'Ctrl+O')
        self.addAction("Setting", self.actionOpenFile, 'Ctrl+Alt+S')
        self.addAction("Exit", self.actionExit, 'Ctrl+Q')

    def actionNewFile(self):
        print ("new file")
        self.mainWindow.newTab()
        pass

    def actionOpenFile(self):
        print("open file")
        pass

    def actionSetting(self):
        print("setings")
        pass

    def actionExit(self):
        print("quit")
        pass