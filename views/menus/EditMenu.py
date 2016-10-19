from PySide import QtGui

class EditMenu(QtGui.QMenu):

    def __init__(self, main, parent = None):
        super(EditMenu, self).__init__("Edit")

        self.prepareActions()
        self.mainWindow = main

    def prepareActions(self):
        self.addAction("Find and Replace", self.openFindPanel, 'Ctrl+F')

    def openFindPanel(self):
        self.mainWindow.openFindPanel()

