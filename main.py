from views import MainWindow
from PySide import QtGui
import sys

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()

    sys.exit(app.exec_())