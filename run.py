# -*- encoding: utf-8 -*-
#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.filename = ''
        self.initUI()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon('Images/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        openAction = QtGui.QAction(QtGui.QIcon('Images/openlogo-50.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        self.connect(openAction, QtCore.SIGNAL('triggered()'), self.showDialog)

        saveAction = QtGui.QAction(QtGui.QIcon('Images/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        self.connect(saveAction, QtCore.SIGNAL('triggered()'), self.saveDocument)

        self.toolbar = self.addToolBar('werever')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)

        self.entrada_texto = QtGui.QTextEdit(self)
        self.entrada_texto.move(30, 100)
        self.entrada_texto.setFocus()
        self.setCentralWidget(self.entrada_texto)

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('pyScript: ')
        self.show()

    def showDialog(self):
        #Se captura el nombre del archivo a abrir
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Abrir archivo',
                    '/home')
        #Se define un neuvo titulo a la ventan de la aplicacion
        self.setWindowTitle('pyScript:%s' %self.filename)
        #Se abre el archivo y se
        #desplega la informacion en el widget de
        #edicion de texto
        fname = open(self.filename)
        data = fname.read()
        self.entrada_texto.setText(data)

    def saveDocument(self):
        fname = open(self.filename, 'w')
        fname.write(self.entrada_texto)
        fname.close()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
  main()