from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np


class basic_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_opendir=os.getcwd()

        #signal and slot
        self.ui.actionOpen.triggered.connect(self.showdialog)

        #figure
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        self.canvas.move(0,0)
        self.toolbar=NavigationToolbar(self.canvas,self)

        #add widgets
        self.ui.gridLayout.addWidget(self.toolbar)
        self.ui.gridLayout.addWidget(self.canvas)
    
    def showdialog(self):
        fname=QtWidgets.QFileDialog.getOpenFileName(self,"Open file", self.current_opendir)
        if len(fname[0])==0:
            pass
        else:
            self.x=np.loadtxt(fname[0],delimiter="\t")
            x1=self.x[:,0]
            y1=self.x[:,1]
            self.graph_plot(x1,y1,"r","x","y")
    
    def graph_plot(self,x,y,color,xlabel,ylabel):
        self.ax=self.figure.add_subplot(1,1,1,xlabel=xlabel,ylabel=ylabel)
        self.ax.plot(x,y,c=color)
        
        plt.tight_layout()
        self.canvas.draw()


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    w=basic_window()
    w.show()
    sys.exit(app.exec())