# -*- encoding: utf-8 -*-
#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        menuBar = QtGui.QMenuBar

        boton1 = QtGui.QPushButton('Salir', self)
        boton2 = QtGui.QPushButton('Inicio', self)
        boton1.move(710, 0)
        boton1.clicked.connect(QtCore.QCoreApplication.instance().quit)

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