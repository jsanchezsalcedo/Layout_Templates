import pymel.core as pm
import maya.OpenMayaUI as omui

from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance

mainWindow = None
__title__ = 'Layouts'
__version__ = 'v1.0.0'

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
        self.setWindowTitle('{} {}'.format(__title__,__version__))
        self.setMinimumWidth(300)
        self.createInterface()

    def createInterface(self):
        
        tabWidget = QtWidgets.QTabWidget()

        ######################################################

        tab1Widget = QtWidgets.QWidget()
        tab1Layout = QtWidgets.QVBoxLayout(tab1Widget)
        tab1Layout.setAlignment(QtCore.Qt.AlignTop)
        tab1Layout.setContentsMargins(0,0,0,0)

        tab1VWidget = QtWidgets.QWidget()
        tab1VLayout = QtWidgets.QVBoxLayout(tab1VWidget)
        tab1Layout.addWidget(tab1VWidget)

        tab1Text = QtWidgets.QLabel('QVBoxLayout and QHBoxLayout')
        tab1VLayout.addWidget(tab1Text)

        tab1HWidget = QtWidgets.QWidget()
        tab1HLayout = QtWidgets.QHBoxLayout(tab1HWidget)
        tab1Layout.addWidget(tab1HWidget)

        tab1Button1 = QtWidgets.QPushButton('QPushButton#1')
        tab1HLayout.addWidget(tab1Button1)

        tab1Button2 = QtWidgets.QPushButton('QPushButton#2')
        tab1HLayout.addWidget(tab1Button2)

        tabWidget.addTab(tab1Widget, 'Tab#1')

        ######################################################
        
        tab2Widget = QtWidgets.QSplitter(orientation=QtCore.Qt.Vertical)
        tab2Layout = QtWidgets.QVBoxLayout(tab2Widget)
        tab2Layout.setAlignment(QtCore.Qt.AlignTop)
        tab2Layout.setContentsMargins(0, 0, 0, 0)

        tab2TopWidget = QtWidgets.QWidget()
        tab2TopLayout = QtWidgets.QVBoxLayout(tab2TopWidget)
        tab2TopLayout.setAlignment(QtCore.Qt.AlignTop)
        tab2TopLayout.setContentsMargins(0, 0, 0, 0)
        tab2Widget.addWidget(tab2TopWidget)

        tab2VTopWidget = QtWidgets.QWidget()
        tab2VTopLayout = QtWidgets.QHBoxLayout(tab2VTopWidget)
        tab2TopLayout.addWidget(tab2VTopWidget)

        tab2Text = QtWidgets.QLabel('QVBoxLayout and QHBoxLayout')
        tab2VTopLayout.addWidget(tab2Text)

        tab2HTopWidget = QtWidgets.QWidget()
        tab2HTopLayout = QtWidgets.QHBoxLayout(tab2HTopWidget)
        tab2TopLayout.addWidget(tab2HTopWidget)

        tab2Button1 = QtWidgets.QPushButton('QPushButton#1')
        tab2HTopLayout.addWidget(tab2Button1)

        tab2Button2 = QtWidgets.QPushButton('QPushButton#2')
        tab2HTopLayout.addWidget(tab2Button2)

        tab2BottomWidget = QtWidgets.QWidget()
        self.tab2BottomLayout = QtWidgets.QStackedLayout()
        tab2BottomWidget.setLayout(self.tab2BottomLayout)
        tab2Widget.addWidget(tab2BottomWidget)

        tab2StackedWidget1 = QtWidgets.QWidget()
        tab2StackedLayout1 = QtWidgets.QVBoxLayout(tab2StackedWidget1)
        tab2StackedLayout1.setAlignment(QtCore.Qt.AlignTop)
        self.tab2BottomLayout.addWidget(tab2StackedWidget1)

        tab2LineEdit = QtWidgets.QLineEdit('QStackedLayout#1')
        tab2LineEdit.setMinimumHeight(75)
        tab2LineEdit.setAlignment(QtCore.Qt.AlignTop)
        tab2StackedLayout1.addWidget(tab2LineEdit)

        tab2StackedWidget2 = QtWidgets.QWidget()
        tab2StackedLayout2 = QtWidgets.QVBoxLayout(tab2StackedWidget2)
        tab2StackedLayout2.setAlignment(QtCore.Qt.AlignTop)
        self.tab2BottomLayout.addWidget(tab2StackedWidget2)

        tab2GroupBox = QtWidgets.QGroupBox()
        tab2GroupBox.setMinimumHeight(75)
        tab2GroupBoxLayout = QtWidgets.QVBoxLayout(tab2GroupBox)
        tab2GroupBoxLayout.setAlignment(QtCore.Qt.AlignTop)

        tab2GroupBoxLabel = QtWidgets.QLabel('QStackedLayout#2')
        tab2GroupBoxLayout.addWidget(tab2GroupBoxLabel)

        tab2StackedLayout2.addWidget(tab2GroupBox)

        self.tab2BottomLayout.setCurrentIndex(0)

        tabWidget.addTab(tab2Widget, 'Tab#2')

        ######################################################

        tab2Button1.clicked.connect(self.stackedLayoutOne)
        tab2Button2.clicked.connect(self.stackedLayoutTwo)

        ######################################################
        
        tab3Widget = QtWidgets.QSplitter(orientation=QtCore.Qt.Vertical)
        tab3Layout = QtWidgets.QVBoxLayout(tab3Widget)
        tab3Layout.setAlignment(QtCore.Qt.AlignTop)
        tab3Layout.setContentsMargins(0, 0, 0, 0)

        tab3TopWidget = QtWidgets.QWidget()
        tab3TopLayout = QtWidgets.QVBoxLayout(tab3TopWidget)
        tab3TopLayout.setAlignment(QtCore.Qt.AlignTop)
        tab3Widget.addWidget(tab3TopWidget)

        self.tab3ComboBox = QtWidgets.QComboBox()
        tab3TopLayout.addWidget(self.tab3ComboBox)
        self.tab3ComboBox.addItems(['Item#1', 'Item#2'])

        tab3BottomWidget = QtWidgets.QWidget()
        self.tab3BottomLayout = QtWidgets.QStackedLayout()
        tab3BottomWidget.setLayout(self.tab3BottomLayout)
        tab3Widget.addWidget(tab3BottomWidget)

        tab3StackedWidget1 = QtWidgets.QWidget()
        tab3StackedLayout1 = QtWidgets.QVBoxLayout(tab3StackedWidget1)
        tab3StackedLayout1.setAlignment(QtCore.Qt.AlignTop)
        self.tab3BottomLayout.addWidget(tab3StackedWidget1)

        tab3LineEdit = QtWidgets.QLineEdit('QStackedLayout#1')
        tab3LineEdit.setMinimumHeight(75)
        tab3LineEdit.setAlignment(QtCore.Qt.AlignTop)
        tab3StackedLayout1.addWidget(tab3LineEdit)

        tab3StackedWidget2 = QtWidgets.QWidget()
        tab3StackedLayout2 = QtWidgets.QVBoxLayout(tab3StackedWidget2)
        tab3StackedLayout2.setAlignment(QtCore.Qt.AlignTop)
        self.tab3BottomLayout.addWidget(tab3StackedWidget2)

        tab3GroupBox = QtWidgets.QGroupBox()
        tab3GroupBox.setMinimumHeight(75)
        tab3GroupBoxLayout = QtWidgets.QVBoxLayout(tab3GroupBox)
        tab3GroupBoxLayout.setAlignment(QtCore.Qt.AlignTop)

        tab3GroupBoxLabel = QtWidgets.QLabel('QStackedLayout#2')
        tab3GroupBoxLayout.addWidget(tab3GroupBoxLabel)

        tab3StackedLayout2.addWidget(tab3GroupBox)

        self.tab3BottomLayout.setCurrentIndex(0)

        tabWidget.addTab(tab3Widget, 'Tab#3')

        ######################################################

        self.tab3ComboBox.currentIndexChanged.connect(self.stackedLayoutThree)

        ######################################################

        self.setCentralWidget(tabWidget)

    def stackedLayoutOne(self):
        self.tab2BottomLayout.setCurrentIndex(0)

    def stackedLayoutTwo(self):
        self.tab2BottomLayout.setCurrentIndex(1)

    def stackedLayoutThree(self):
        if self.tab3ComboBox.currentIndex() == 0:
            self.tab3BottomLayout.setCurrentIndex(0)
        else:
            self.tab3BottomLayout.setCurrentIndex(1)

def run():
    global mainWindow
    if not mainWindow or not pm.window(mainWindow, q=True, e=True):
        mainWindow = UserInterface(parent=getMayaWindow())
    mainWindow.show()