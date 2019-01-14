import pymel.core as pm
import maya.OpenMayaUI as omui

from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance

mainWindow = None
__title__ = 'Layouts'
__version__ = 'v1.1.0'

print ''
print ' > {} {}'.format(__title__,__version__)
print ' > by Jorge Sanchez Salcedo, 2019'
print ' > www.jorgesanchez-da.com'
print ' > jorgesanchez.da@gmail.com'
print ''

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    mainWindow = wrapInstance(long(ptr),QtWidgets.QWidget)
    return mainWindow

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UserInterface, self).__init__(parent)
        self.setWindowTitle('{} {}'.format(__title__, __version__))
        self.setMinimumWidth(300)
        self.createTab()

    def createTab(self):
        tabWidget = QtWidgets.QTabWidget()
        tabWidget.addTab(TabOne(), 'Tab#1')
        tabWidget.addTab(TabTwo(), 'Tab#2')
        tabWidget.addTab(TabThree(), 'Tab#3')
        self.setCentralWidget(tabWidget)

class TabOne (QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(TabOne, self).__init__(parent)
        self.createTab()

    def createTab(self):
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.setAlignment(QtCore.Qt.AlignTop)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        verticalWidget = QtWidgets.QWidget()
        verticalLayout = QtWidgets.QVBoxLayout(verticalWidget)
        mainLayout.addWidget(verticalWidget)

        text = QtWidgets.QLabel('QVBoxLayout and QHBoxLayout')
        verticalLayout.addWidget(text)

        horizontalWidget = QtWidgets.QWidget()
        horizontalLayout = QtWidgets.QHBoxLayout(horizontalWidget)
        mainLayout.addWidget(horizontalWidget)

        button1 = QtWidgets.QPushButton('QPushButton#1')
        horizontalLayout.addWidget(button1)

        button2 = QtWidgets.QPushButton('QPushButton#2')
        horizontalLayout.addWidget(button2)

        self.setLayout(mainLayout)

class TabTwo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TabTwo, self).__init__(parent)
        self.createTab()

    def createTab(self):
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setAlignment(QtCore.Qt.AlignTop)

        widget = QtWidgets.QSplitter(orientation=QtCore.Qt.Vertical)
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setAlignment(QtCore.Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)

        topWidget = QtWidgets.QWidget()
        topLayout = QtWidgets.QVBoxLayout(topWidget)
        topLayout.setAlignment(QtCore.Qt.AlignTop)
        topLayout.setContentsMargins(0, 0, 0, 0)
        widget.addWidget(topWidget)

        verticalTopWidget = QtWidgets.QWidget()
        verticalTopLayout = QtWidgets.QHBoxLayout(verticalTopWidget)
        topLayout.addWidget(verticalTopWidget)

        text = QtWidgets.QLabel('QVBoxLayout and QHBoxLayout')
        verticalTopLayout.addWidget(text)

        horizontalTopWidget = QtWidgets.QWidget()
        horizontalTopLayout = QtWidgets.QHBoxLayout(horizontalTopWidget)
        topLayout.addWidget(horizontalTopWidget)

        button1 = QtWidgets.QPushButton('QPushButton#1')
        horizontalTopLayout.addWidget(button1)

        button2 = QtWidgets.QPushButton('QPushButton#2')
        horizontalTopLayout.addWidget(button2)

        bottomWidget = QtWidgets.QWidget()
        self.bottomLayout = QtWidgets.QStackedLayout()
        bottomWidget.setLayout(self.bottomLayout)
        widget.addWidget(bottomWidget)

        stackedWidget1 = QtWidgets.QWidget()
        stackedLayout1 = QtWidgets.QVBoxLayout(stackedWidget1)
        stackedLayout1.setAlignment(QtCore.Qt.AlignTop)
        self.bottomLayout.addWidget(stackedWidget1)

        lineEdit = QtWidgets.QLineEdit('QStackedLayout#1')
        lineEdit.setMinimumHeight(75)
        lineEdit.setAlignment(QtCore.Qt.AlignTop)

        stackedLayout1.addWidget(lineEdit)

        stackedWidget2 = QtWidgets.QWidget()
        stackedLayout2 = QtWidgets.QVBoxLayout(stackedWidget2)
        stackedLayout2.setAlignment(QtCore.Qt.AlignTop)
        self.bottomLayout.addWidget(stackedWidget2)

        groupBox = QtWidgets.QGroupBox()
        groupBox.setMinimumHeight(75)
        groupBoxLayout = QtWidgets.QVBoxLayout(groupBox)
        groupBoxLayout.setAlignment(QtCore.Qt.AlignTop)

        groupBoxLabel = QtWidgets.QLabel('QStackedLayout#2')
        groupBoxLayout.addWidget(groupBoxLabel)

        stackedLayout2.addWidget(groupBox)

        self.bottomLayout.setCurrentIndex(0)

        mainLayout.addWidget(widget)

        self.setLayout(mainLayout)

        button1.clicked.connect(self.setStackedLayoutOne)
        button2.clicked.connect(self.setStackedLayoutTwo)

    def setStackedLayoutOne(self):
        self.bottomLayout.setCurrentIndex(0)

    def setStackedLayoutTwo(self):
        self.bottomLayout.setCurrentIndex(1)

class TabThree(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TabThree, self).__init__(parent)
        self.createTab()

    def createTab(self):
        mainLayout=QtWidgets.QVBoxLayout()
        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setAlignment(QtCore.Qt.AlignTop)

        widget = QtWidgets.QSplitter(orientation=QtCore.Qt.Vertical)
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setAlignment(QtCore.Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)

        topWidget = QtWidgets.QWidget()
        topLayout = QtWidgets.QVBoxLayout(topWidget)
        topLayout.setAlignment(QtCore.Qt.AlignTop)
        widget.addWidget(topWidget)

        self.comboBox = QtWidgets.QComboBox()
        topLayout.addWidget(self.comboBox)
        self.comboBox.addItems(['Item#1', 'Item#2'])

        bottomWidget = QtWidgets.QWidget()
        self.bottomLayout = QtWidgets.QStackedLayout()
        bottomWidget.setLayout(self.bottomLayout)
        widget.addWidget(bottomWidget)

        stackedWidget1 = QtWidgets.QWidget()
        stackedLayout1 = QtWidgets.QVBoxLayout(stackedWidget1)
        stackedLayout1.setAlignment(QtCore.Qt.AlignTop)
        self.bottomLayout.addWidget(stackedWidget1)

        lineEdit = QtWidgets.QLineEdit('QStackedLayout#1')
        lineEdit.setMinimumHeight(75)
        lineEdit.setAlignment(QtCore.Qt.AlignTop)
        stackedLayout1.addWidget(lineEdit)

        stackedWidget2 = QtWidgets.QWidget()
        stackedLayout2 = QtWidgets.QVBoxLayout(stackedWidget2)
        stackedLayout2.setAlignment(QtCore.Qt.AlignTop)
        self.bottomLayout.addWidget(stackedWidget2)

        groupBox = QtWidgets.QGroupBox()
        groupBox.setMinimumHeight(75)
        groupBoxLayout = QtWidgets.QVBoxLayout(groupBox)
        groupBoxLayout.setAlignment(QtCore.Qt.AlignTop)

        groupBoxLabel = QtWidgets.QLabel('QStackedLayout#2')
        groupBoxLayout.addWidget(groupBoxLabel)

        stackedLayout2.addWidget(groupBox)

        self.bottomLayout.setCurrentIndex(0)

        mainLayout.addWidget(widget)

        self.setLayout(mainLayout)

        self.comboBox.currentIndexChanged.connect(self.setStackedLayout)

    def setStackedLayout(self):
        if self.comboBox.currentIndex() == 0:
            self.bottomLayout.setCurrentIndex(0)
        else:
            self.bottomLayout.setCurrentIndex(1)

def run():
    global mainWindow
    if not mainWindow or not pm.window(mainWindow, q=True, e=True):
        mainWindow = UserInterface(parent=getMayaWindow())
    mainWindow.show()
