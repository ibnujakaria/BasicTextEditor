from PySide import QtGui

class EditMenu(QtGui.QMenu):

    def __init__(self, main, parent = None):
        super(EditMenu, self).__init__("Edit")

        self.prepareActions()
        self.mainWindow = main

    def prepareActions(self):
        self.addAction("Find", self.openFindPanel, 'Ctrl+F')
        self.addAction("Replace", self.replace, 'Ctrl+R')

    def openFindPanel(self):
        self.mainWindow.openFindPanel()

    def replace(self):
        print('replace...')

