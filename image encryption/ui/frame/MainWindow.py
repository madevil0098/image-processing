from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from action.MainWindowAction import MyAction

class MainWindow(QMainWindow):
  def __init__(self, parent = None):
    super(MainWindow, self).__init__(parent)
    uic.loadUi('ui/uifiles/MainWindow.ui',self)
    self.showMaximized()
    self.session_uuid = None
    self.isSessionRunning = False
    self.sessionThreadObj = None
    self.mdi = QMdiArea()
    self.setCentralWidget(self.mdi)
    self.myaction = MyAction(self)
    self.setupAction()
  def setupAction(self):
    self.voiceMenu.triggered.connect(self.myaction.voiceRecords)
  def closeEvent(self,event):
    if self.isSessionRunning:
      QMessageBox.information(self, "Information","Session is running !")
      event.ignore()
    else:
      buttonReply = QMessageBox.question(self, 'Closing Message', "Are You Sure To Exit ?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      if buttonReply == QMessageBox.Yes:            
        event.accept()
        self.menuSession.setEnabled(True)
      else:
        event.ignore()