from PyQt4 import QtGui, QtCore


class Dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.viewer = QtGui.QLabel(self)
        self.viewer.setMinimumSize(QtCore.QSize(400, 400))
        self.viewer.setScaledContents(True)
        self.viewer.setPixmap(QtGui.QPixmap("1.PNG"))
        self.youtube = QtGui.QLineEdit(self)
        self.youtube.returnPressed.connect(self.handle_return)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.viewer)
        layout.addWidget(self.youtube)

    def handle_return(self):
        if self.youtube.text().simplified().isEmpty():
            self.reject()
        else:
            self.accept()


def launch():
    _ = QtGui.QApplication([])
    dialog = Dialog()
    dialog.exec_()
