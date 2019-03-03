import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QAction,QMessageBox,QCheckBox,QProgressBar,QComboBox,QLabel,QStyleFactory,QFontDialog


class screening_task_main(QMainWindow):

    def __init__(self):

        super(screening_task_main,self).__init__()

        #Setting up my Window
        self.setGeometry(50,50,500,600)
        self.setWindowTitle("Main")

        #Setting up a menubar
        mainMenu = self.menuBar()

        #File option in menu 
        fileMenu = mainMenu.addMenu('&File')

        load_Action = QAction("&Load", self)
        load_Action.setShortcut("Ctrl+L")
        load_Action.setStatusTip('Loads a csv file.')
        load_Action.triggered.connect(self.load_File)
        fileMenu.addAction(load_Action)

        add_Data_Action = QAction("&Add Data", self)
        add_Data_Action.setShortcut("A")
        add_Data_Action.setStatusTip('Add new data to the table.')
        add_Data_Action.triggered.connect(self.add_File)
        fileMenu.addAction(add_Data_Action)

        exit_Action = QAction("&Exit", self)
        exit_Action.setShortcut("Esc")
        exit_Action.setStatusTip('Exit')
        exit_Action.triggered.connect(self.exit_File)
        fileMenu.addAction(exit_Action)

        #Edit option in menu
        editMenu = mainMenu.addMenu('&Edit')
        edit_Data_Action = QAction("&Edit Data", self)
        edit_Data_Action.setShortcut("E")
        edit_Data_Action.setStatusTip('Edit the existing data in the table.')
        edit_Data_Action.triggered.connect(self.edit_File)
        editMenu.addAction(edit_Data_Action)

        self.show()

    def load_File(self):
        print("Loads a csv!")

    def add_File(self):
        print("Add data in csv!")

    def edit_File(self):
        print("Edit data in csv!")

    def exit_File(self):
        sys.exit()

        
def run():        
    app = QApplication(sys.argv)
    GUI = screening_task_main()
    sys.exit(app.exec_())

run()
