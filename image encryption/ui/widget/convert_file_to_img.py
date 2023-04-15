from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from code.ui.convert_to_img import convert_file
import os
import numpy as np

class convertWidget(QtWidgets.QWidget):
    def __init__(self,mainWindow):
      super().__init__()      
      self.mainWindow = mainWindow
      uic.loadUi('ui/uifiles/convert_img.ui',self)
      
      self.uploadbtn.clicked.connect(self.upload)
    
    def upload(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file')
      path = fname[0].split("/")
      print(path[-1])
      convert_file(fname[0])
