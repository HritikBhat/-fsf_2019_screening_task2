import sys,csv
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout,QAction,QMessageBox,QCheckBox,QLabel,QFileDialog,QTableWidgetItem,QTableWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget,QDialogButtonBox,QPushButton
from PyQt5.QtCore import QSize, Qt,pyqtSlot

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
        #Open a GUI which ease users to find a csv file
        name =QFileDialog.getOpenFileName(self, 'Open File')
        file=open(name[0],'r')

        #Reads a csv File
        csv_Reader= csv.reader(file)
        row=0
        myli=[]

        #Appending data into a list called myli
        for line in csv_Reader:
            col=len(line)
            myli.append(line)
            row=row+1

        try:
            central_widget = QWidget(self)
            # Install the central widget
            self.setCentralWidget(central_widget)
            
            # Create QGridLayout
            self.grid_layout = QGridLayout(self)
            
            # Set this layout in central widget
            central_widget.setLayout(self.grid_layout)   

            """
            For NOW, I have kept all connect function in buttons as exit so I will Update soon!
            """
            #To Plot Scatter Points
            self.btn=QPushButton("Plot scatter points",self)
            self.btn.clicked.connect(self.exit_File)
            self.btn.resize(50,40)
            self.btn.move(100,100)

            #To Plot scatter points with smooth lines
            self.btn2=QPushButton("Plot scatter points with smooth lines",self)
            self.btn2.clicked.connect(self.exit_File)
            self.btn2.resize(50,40)
            self.btn2.move(100,100)

            #To Plot Lines
            self.btn3=QPushButton("Plot Lines",self)
            self.btn3.clicked.connect(self.exit_File)
            self.btn3.resize(50,40)
            self.btn3.move(100,100)
            

            myli2=[]
            #Creates a table.
            self.table = QTableWidget(self)

            #Set columns and rows according to given csv file.
            self.table.setColumnCount(col)     
            self.table.setRowCount(row-1)
            
            for i in range(0,col):
                myli2.append(myli[0][i])

                
            #Create Headers for the table.
            self.table.setHorizontalHeaderLabels(myli2)

            #Display data on spreadsheet.
            for i in range(0,row-1):
                for j in range(0,col):
                    self.table.setItem(i,j, QTableWidgetItem(myli[i+1][j]))
                

            # Do the resize of the columns by content
            self.table.resizeColumnsToContents()

            self.grid_layout.addWidget(self.table,0,0)
            self.grid_layout.addWidget(self.btn)
            self.grid_layout.addWidget(self.btn2)
            self.grid_layout.addWidget(self.btn3)
            
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
        
        

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
