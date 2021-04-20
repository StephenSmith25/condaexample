from qtpy.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QMessageBox, QWidget

# Ensure that all expected packages are present
import PyQt5
import qtconsole
import numpy
import scipy
import sphinx
import CifFile  # pycifrw
import dateutil
import matplotlib
import h5py
import psutil
import requests
import toml
import yaml

# import qt from C++
from import_qt import import_qt

MessageBox = import_qt('_message_box', '', 'MessageBox')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.python_button = QPushButton("Python Button")
        self.cpp_button = QPushButton("C++ Button")
        self.layout.addWidget(self.python_button)
        self.layout.addWidget(self.cpp_button)
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.python_button.clicked.connect(self.display_message)
        self.cpp_button.clicked.connect(self.display_cpp_message)

    def display_message(self):
        QMessageBox.information(self, 'PyQt5 message', "This is from python!")

    def display_cpp_message(self):
        cpp_msg = "This is from C++"
        MessageBox(self, "Qt5 message", cpp_msg)


def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
