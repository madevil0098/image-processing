from PyQt5.QtWidgets import *

from ui.widget.convert_file_to_img import convertWidget
class MyAction:
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow

    def voiceRecords(self):
        sub = QMdiSubWindow()
        sub.setWidget(convertWidget(self.mainWindow))
        sub.setWindowTitle("convert file to image")
        self.mainWindow.mdi.addSubWindow(sub)
        sub.show()
        center = self.mainWindow.mdi.viewport().rect().center()
        geo = sub.geometry()
        geo.moveCenter(center)
        sub.setGeometry(geo)
        self.mainWindow.menuSession.setEnabled(False)

