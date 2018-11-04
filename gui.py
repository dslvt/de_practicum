from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QPushButton, QTextEdit, QStyleFactory, QHBoxLayout,QGridLayout,\
    QTabWidget,QSizePolicy, QGroupBox, QVBoxLayout, QWidget
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
from euler import Euler
from exact import Exact
from improved_euler import Improved_euler
from rungekutta import RungeKutta

class GUI(QDialog):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)

        self.euler = Euler(1.0, 1.0, 9.5, 100)
        self.exact = Exact(1.0, 1.0, 9.5, 100)
        self.improved_euler = Improved_euler(1.0, 1.0, 9.5, 100)
        self.rungekutta = RungeKutta(1.0, 1.0, 9.5, 100)

        self.createTopGroupBox()
        self.createSelectInitialBox()
        self.createMethodBox()
        self.createTabBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topGroupBox, 0, 0)
        mainLayout.addWidget(self.selectInitialBox, 1, 0)
        mainLayout.addWidget(self.methodBox, 2, 0)
        mainLayout.addWidget(self.bottomTabWidget, 3, 0)

        self.setLayout(mainLayout)

    def createTopGroupBox(self):
        self.topGroupBox = QGroupBox()

        difEquationLabel = QLabel("y' = y^4 * cos(x) - y * tg(x)")

        init_x0 = QLabel('x0=')
        self.init_x0_val = QLabel('1.0')
        init_x0.setBuddy(self.init_x0_val)
        init_y0 = QLabel('y0=')
        self.init_y0_val = QLabel('1.0')
        init_y0.setBuddy(self.init_x0_val)
        init_X = QLabel('X=')
        self.init_X_val = QLabel('9.5')
        init_X.setBuddy(self.init_X_val)
        init_n = QLabel('n=')
        self.init_n_val = QLabel('100')
        init_n.setBuddy(self.init_n_val)

        self.plotButton = QPushButton('Plot')
        self.plotButton.clicked.connect(self.plot)

        headLayout = QHBoxLayout()
        headLayout.addWidget(difEquationLabel, 5)
        headLayout.addWidget(init_x0)
        headLayout.addWidget(self.init_x0_val)
        headLayout.addWidget(init_y0)
        headLayout.addWidget(self.init_y0_val)
        headLayout.addWidget(init_X)
        headLayout.addWidget(self.init_X_val)
        headLayout.addWidget(init_n)
        headLayout.addWidget(self.init_n_val)
        headLayout.addWidget(self.plotButton)
        self.topGroupBox.setLayout(headLayout)

    def createSelectInitialBox(self):
        self.selectInitialBox = QGroupBox()
        yLabel = QLabel("&y0:")
        xLabel = QLabel("&x0:")
        XLabel = QLabel("&X:")
        nLabel = QLabel("&N:")
        self.xTextEdit = QTextEdit()
        self.yTextEdit = QTextEdit()
        self.XTextEdit = QTextEdit()
        self.nTextEdit = QTextEdit()
        yLabel.setBuddy(self.yTextEdit)
        xLabel.setBuddy(self.xTextEdit)
        XLabel.setBuddy(self.XTextEdit)
        nLabel.setBuddy(self.nTextEdit)

        topLayout = QHBoxLayout()
        topLayout.addWidget(yLabel)
        topLayout.addWidget(self.yTextEdit)
        topLayout.addWidget(xLabel)
        topLayout.addWidget(self.xTextEdit)
        topLayout.addWidget(XLabel)
        topLayout.addWidget(self.XTextEdit)
        topLayout.addWidget(nLabel)
        topLayout.addWidget(self.nTextEdit)
        topLayout.addStretch(1)
        self.selectInitialBox.setLayout(topLayout)

    def createMethodBox(self):
        self.methodBox = QGroupBox()

        self.eulerButton = QPushButton('Euler(Red)')
        self.eulerButton.setCheckable(True)
        self.eulerButton.setChecked(True)
        self.impruvedEulerButton = QPushButton('Impuved Euler(Blue)')
        self.impruvedEulerButton.setChecked(True)
        self.impruvedEulerButton.setCheckable(True)
        self.rungeKutteButton = QPushButton('Runge-Kutte(Yellow)')
        self.rungeKutteButton.setCheckable(True)
        self.rungeKutteButton.setChecked(True)
        self.exactButton = QPushButton('Exact(Green)')
        self.exactButton.setChecked(True)
        self.exactButton.setCheckable(True)
        methodLayout = QHBoxLayout()
        methodLayout.addWidget(self.eulerButton)
        methodLayout.addWidget(self.impruvedEulerButton)
        methodLayout.addWidget(self.rungeKutteButton)
        methodLayout.addWidget(self.exactButton)

        self.methodBox.setLayout(methodLayout)

    def createTabBox(self):
        self.plotFigure = Figure()
        self.plotCanvas = FigureCanvas(self.plotFigure)
        plotToolbar = NavigationToolbar(self.plotCanvas, self)

        self.localErrorFigure = Figure()
        self.localErrorCanvas = FigureCanvas(self.localErrorFigure)
        localErrorToolbar = NavigationToolbar(self.localErrorCanvas, self)

        self.globalErrorFigure = Figure()
        self.globalErrorCanval = FigureCanvas(self.globalErrorFigure)
        globalErrorToolbar = NavigationToolbar(self.globalErrorCanval, self)

        plotLayout = QVBoxLayout()
        plotLayout.addWidget(plotToolbar)
        plotLayout.addWidget(self.plotCanvas)

        localErrorLayout = QVBoxLayout()
        localErrorLayout.addWidget(localErrorToolbar)
        localErrorLayout.addWidget(self.localErrorCanvas)

        globalErrorLayout = QVBoxLayout()
        selectNLayout = QHBoxLayout()
        self.startNTextEdit = QTextEdit()
        self.finishNTextEdit = QTextEdit()
        selectNLayout.addWidget(self.startNTextEdit)
        selectNLayout.addWidget(self.finishNTextEdit)

        globalErrorLayout.addLayout(selectNLayout)
        globalErrorLayout.addWidget(globalErrorToolbar)
        globalErrorLayout.addWidget(self.globalErrorCanval)

        # self.setLayout(layout)
        self.bottomTabWidget = QTabWidget()

        plotTab = QWidget()
        plotTab.setLayout(plotLayout)
        localErrorTab = QWidget()
        localErrorTab.setLayout(localErrorLayout)
        globalErrorTab = QWidget()
        globalErrorTab.setLayout(globalErrorLayout)
        self.bottomTabWidget.addTab(plotTab, 'Plot')
        self.bottomTabWidget.addTab(localErrorTab, 'Local Error')
        self.bottomTabWidget.addTab(globalErrorTab, 'Global Error')

    def plot(self):
        global_error_startn, global_error_finishn = 1, int(self.exact.h)
        if self.startNTextEdit.toPlainText() != '':
            try:
                global_error_startn = int(self.startNTextEdit.toPlainText())
            except BaseException:
                print('invalid startn global error')

        if self.finishNTextEdit.toPlainText() != '':
            try:
                global_error_finishn = int(self.finishNTextEdit.toPlainText())
            except BaseException:
                print('invalid finishn global error')

        methods = [self.euler, self.improved_euler, self.rungekutta, self.exact]

        if self.xTextEdit.toPlainText() != '':
            for method in methods:
                method.set_x0(self.xTextEdit.toPlainText())
            self.init_x0_val.setText(self.xTextEdit.toPlainText())

        if self.yTextEdit.toPlainText() != '':
            for method in methods:
                method.set_y0(self.yTextEdit.toPlainText())
            self.init_y0_val.setText(self.yTextEdit.toPlainText())

        if self.nTextEdit.toPlainText() != '':
            for method in methods:
                method.set_n(self.nTextEdit.toPlainText())
            self.init_n_val.setText(self.nTextEdit.toPlainText())

        if self.XTextEdit.toPlainText() != '':
            for method in methods:
                method.set_X(self.XTextEdit.toPlainText())
            self.init_X_val.setText(self.XTextEdit.toPlainText())

        ax = self.plotFigure.add_subplot(111)
        ax.clear()

        local_error_fig = self.localErrorFigure.add_subplot(111)
        local_error_fig.clear()

        global_error_fig = self.globalErrorFigure.add_subplot(111)
        global_error_fig.clear()

        if self.eulerButton.isChecked():
            eulerx, eulery = self.euler.plot()
            ax.plot(eulerx, eulery, label='euler', color='r')

            local_errory = self.euler.local_error()
            local_error_fig.plot(eulerx, local_errory, color='r')

            global_errorx, global_errory = self.euler.global_error(global_error_startn, global_error_finishn)
            global_error_fig.plot(global_errorx, global_errory, color='r')


        if self.impruvedEulerButton.isChecked():
            impruved_eulerx, impruved_eulery = self.improved_euler.plot()
            ax.plot(impruved_eulerx, impruved_eulery, label='impruved euler', color='b')

            local_errory = self.improved_euler.local_error()
            local_error_fig.plot(impruved_eulerx, local_errory, color='b')

            global_errorx, global_errory = self.improved_euler.global_error(global_error_startn, global_error_finishn)
            global_error_fig.plot(global_errorx, global_errory, color='b')

        if self.rungeKutteButton.isChecked():
            runge_kuttax, runge_kuttay = self.rungekutta.plot()
            ax.plot(runge_kuttax, runge_kuttay, color='y')

            local_errory = self.rungekutta.local_error()
            local_error_fig.plot(runge_kuttax, local_errory, color='y')

            global_errorx, global_errory = self.rungekutta.global_error(global_error_startn, global_error_finishn)
            global_error_fig.plot(global_errorx, global_errory, color='y')

        if self.exactButton.isChecked():
            ex, ey = self.exact.plot()
            ax.plot(ex, ey, color='g')

        ax.grid(True, which='both')
        local_error_fig.grid(True, which='both')
        global_error_fig.grid(True, which='both')

        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        local_error_fig.axhline(y=0, color='k')
        local_error_fig.axvline(x=0, color='k')
        global_error_fig.axhline(y=0, color='k')
        global_error_fig.axvline(x=0, color='k')

        # refresh plotCanvas
        self.plotCanvas.draw()
        self.localErrorCanvas.draw()
        self.globalErrorCanval.draw()