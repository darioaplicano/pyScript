# -*- encoding: utf-8 -*-
#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('Images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.entrada_texto = QtGui.QTextEdit(self)
        self.entrada_texto.move(30, 100)
        self.entrada_texto.setFocus()
        self.entrada_texto.setFixedWidth(740)
        self.entrada_texto.setFixedHeight(470)

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('pyScript')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
  main()