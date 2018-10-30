from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QPushButton, QTextEdit, QStyleFactory, QHBoxLayout,QGridLayout,QTabWidget,QSizePolicy
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
from A import B


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.a = B(0.0, 1.0, 8.0, 100)

        difEquationLabel = QLabel("y' = y^4 * cos(x) - y * tg(x)")

        solButton = QPushButton('Solution')
        solButton.clicked.connect(self.showSolution)
        headLayout = QHBoxLayout()
        headLayout.addWidget(difEquationLabel, 5)
        headLayout.addWidget(solButton, 1)


        yLabel = QLabel("&y0:")
        xLabel = QLabel("&x0:")
        XLabel = QLabel("&X:")
        nLabel = QLabel("&N:")
        xTextEdit = QTextEdit()
        yTextEdit = QTextEdit()
        XTextEdit = QTextEdit()
        nTextEdit = QTextEdit()
        yLabel.setBuddy(yTextEdit)
        xLabel.setBuddy(xTextEdit)
        XLabel.setBuddy(XTextEdit)
        nLabel.setBuddy(nTextEdit)

        topLayout = QHBoxLayout()
        topLayout.addWidget(yLabel)
        topLayout.addWidget(yTextEdit)
        topLayout.addWidget(xLabel)
        topLayout.addWidget(xTextEdit)
        topLayout.addWidget(XLabel)
        topLayout.addWidget(XTextEdit)
        topLayout.addWidget(nLabel)
        topLayout.addWidget(nTextEdit)
        topLayout.addStretch(1)

        eulerButton = QPushButton('Euler')
        eulerButton.setCheckable(True)
        eulerButton.setChecked(True)
        impruvedEulerButton = QPushButton('Impuved Euler')
        impruvedEulerButton.setChecked(True)
        impruvedEulerButton.setCheckable(True)
        rungeKutteButton = QPushButton('Runge-Kutte')
        rungeKutteButton.setCheckable(True)
        rungeKutteButton.setChecked(True)
        exactButton = QPushButton('Exact')
        exactButton.setChecked(True)
        exactButton.setCheckable(True)
        methodLayout = QHBoxLayout()
        methodLayout.addWidget(eulerButton)
        methodLayout.addWidget(impruvedEulerButton)
        methodLayout.addWidget(rungeKutteButton)
        methodLayout.addWidget(exactButton)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        plotLayout = QVBoxLayout()
        plotLayout.addWidget(self.button)
        plotLayout.addWidget(self.toolbar)
        plotLayout.addWidget(self.canvas)

        localErrorLayout = QVBoxLayout()


        # self.setLayout(layout)
        bottomTabWidget = QTabWidget()

        plotTab = QWidget()
        plotTab.setLayout(plotLayout)
        bottomTabWidget.addTab(plotTab, 'Plot')

        mainLayout = QGridLayout()
        mainLayout.addLayout(headLayout, 0, 0)
        mainLayout.addLayout(topLayout, 1, 0)
        mainLayout.addLayout(methodLayout, 2, 0)
        mainLayout.addWidget(bottomTabWidget, 3, 0)

        self.setLayout(mainLayout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        ex, ey = self.a.exact()
        eulerx, eulery = self.a.euler()
        ax = self.figure.add_subplot(111)
        ax.clear()

        # plot data

        ax.plot(ex, ey)
        ax.plot(eulerx, eulery)
        ax.grid(True, which='both')

        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        # refresh canvas
        self.canvas.draw()

        # QApplication.setStyle(QStyleFactory.create('Fusion'))
        # QApplication.setPalette(QApplication.style().standardPalette())

    def showSolution(self):
        pass


    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n"
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n"
                              "How I wonder what you are!\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")



from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from PyQt5.QtCore import QDateTime, Qt, QTimer

# class WidgetGallery(QDialog):
#     def __init__(self, parent=None):
#         super(WidgetGallery, self).__init__(parent)
#
#         self.originalPalette = QApplication.palette()
#
#         # styleComboBox = QComboBox()
#         # styleComboBox.addItems(QStyleFactory.keys())
#         #
#         # styleLabel = QLabel("&Style:")
#         # styleLabel.setBuddy(styleComboBox)
#         #
#         # self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
#         # self.useStylePaletteCheckBox.setChecked(True)
#         #
#         # disableWidgetsCheckBox = QCheckBox("&Disable widgets")
#
#         # self.createTopLeftGroupBox()
#         # self.createTopRightGroupBox()
#         # self.createBottomLeftTabWidget()
#         # self.createBottomRightGroupBox()
#
#         # styleComboBox.activated[str].connect(self.changeStyle)
#         # self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
#         # disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
#         # disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
#         # disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
#         # disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)
#
#         yLabel = QLabel("&Y:")
#         xLabel = QLabel("&X:")
#
#         topLayout = QHBoxLayout()
#         # topLayout.addWidget(styleLabel)
#         # topLayout.addWidget(styleComboBox)
#         # topLayout.addStretch(4)
#         topLayout.addWidget(yLabel)
#         topLayout.addWidget(xLabel)
#         # topLayout.addWidget(self.useStylePaletteCheckBox)
#         # topLayout.addWidget(disableWidgetsCheckBox)
#
#         mainLayout = QGridLayout()
#         mainLayout.addLayout(topLayout, 0, 0, 1, 2)
#         # mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
#         # mainLayout.addWidget(self.topRightGroupBox, 1, 1)
#         # mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
#         # mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
#         mainLayout.setRowStretch(1, 1)
#         mainLayout.setRowStretch(2, 1)
#         mainLayout.setColumnStretch(0, 1)
#         mainLayout.setColumnStretch(1, 1)
#         self.setLayout(mainLayout)
#
#         # self.setWindowTitle("Styles")
#         self.changeStyle('Fusion')
#
#     def changeStyle(self, styleName):
#         QApplication.setStyle(QStyleFactory.create(styleName))
#         self.changePalette()
#
#     def changePalette(self):
#         if (True):
#             QApplication.setPalette(QApplication.style().standardPalette())
#         else:
#             QApplication.setPalette(self.originalPalette)
#
#     def advanceProgressBar(self):
#         curVal = self.progressBar.value()
#         maxVal = self.progressBar.maximum()
#         self.progressBar.setValue(curVal + (maxVal - curVal) / 100)
#
#     def createTopLeftGroupBox(self):
#         self.topLeftGroupBox = QGroupBox("Group 1")
#
#         radioButton1 = QRadioButton("Radio button 1")
#         radioButton2 = QRadioButton("Radio button 2")
#         radioButton3 = QRadioButton("Radio button 3")
#         radioButton1.setChecked(True)
#
#         checkBox = QCheckBox("Tri-state check box")
#         checkBox.setTristate(True)
#         checkBox.setCheckState(Qt.PartiallyChecked)
#
#         layout = QVBoxLayout()
#         layout.addWidget(radioButton1)
#         layout.addWidget(radioButton2)
#         layout.addWidget(radioButton3)
#         layout.addWidget(checkBox)
#         layout.addStretch(1)
#         self.topLeftGroupBox.setLayout(layout)
#
#     def createTopRightGroupBox(self):
#         self.topRightGroupBox = QGroupBox("Group 2")
#
#         defaultPushButton = QPushButton("Default Push Button")
#         defaultPushButton.setDefault(True)
#
#         togglePushButton = QPushButton("Toggle Push Button")
#         togglePushButton.setCheckable(True)
#         togglePushButton.setChecked(True)
#
#         flatPushButton = QPushButton("Flat Push Button")
#         flatPushButton.setFlat(True)
#
#         layout = QVBoxLayout()
#         layout.addWidget(defaultPushButton)
#         layout.addWidget(togglePushButton)
#         layout.addWidget(flatPushButton)
#         layout.addStretch(1)
#         self.topRightGroupBox.setLayout(layout)
#
#     def createBottomLeftTabWidget(self):
#         self.bottomLeftTabWidget = QTabWidget()
#         self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
#                 QSizePolicy.Ignored)
#
#         tab1 = QWidget()
#         tableWidget = QTableWidget(10, 10)
#
#         tab1hbox = QHBoxLayout()
#         tab1hbox.setContentsMargins(5, 5, 5, 5)
#         tab1hbox.addWidget(tableWidget)
#         tab1.setLayout(tab1hbox)
#
#         tab2 = QWidget()
#         textEdit = QTextEdit()
#
#         textEdit.setPlainText("Twinkle, twinkle, little star,\n"
#                               "How I wonder what you are.\n"
#                               "Up above the world so high,\n"
#                               "Like a diamond in the sky.\n"
#                               "Twinkle, twinkle, little star,\n"
#                               "How I wonder what you are!\n")
#
#         tab2hbox = QHBoxLayout()
#         tab2hbox.setContentsMargins(5, 5, 5, 5)
#         tab2hbox.addWidget(textEdit)
#         tab2.setLayout(tab2hbox)
#
#         self.bottomLeftTabWidget.addTab(tab1, "&Table")
#         self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")
#
#     def createBottomRightGroupBox(self):
#         self.bottomRightGroupBox = QGroupBox("Group 3")
#         self.bottomRightGroupBox.setCheckable(True)
#         self.bottomRightGroupBox.setChecked(True)
#
#         lineEdit = QLineEdit('s3cRe7')
#         lineEdit.setEchoMode(QLineEdit.Password)
#
#         spinBox = QSpinBox(self.bottomRightGroupBox)
#         spinBox.setValue(50)
#
#         dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
#         dateTimeEdit.setDateTime(QDateTime.currentDateTime())
#
#         slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
#         slider.setValue(40)
#
#         scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
#         scrollBar.setValue(60)
#
#         dial = QDial(self.bottomRightGroupBox)
#         dial.setValue(30)
#         dial.setNotchesVisible(True)
#
#         layout = QGridLayout()
#         layout.addWidget(lineEdit, 0, 0, 1, 2)
#         layout.addWidget(spinBox, 1, 0, 1, 2)
#         layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
#         layout.addWidget(slider, 3, 0)
#         layout.addWidget(scrollBar, 4, 0)
#         layout.addWidget(dial, 3, 1, 2, 1)
#         layout.setRowStretch(5, 1)
#         self.bottomRightGroupBox.setLayout(layout)



app = QApplication([])
gallery = WidgetGallery()
gallery.show()
sys.exit(app.exec_())

