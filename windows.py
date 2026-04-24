from root import Root
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QRadioButton, QGroupBox, QLabel, QButtonGroup, QPushButton, QTextEdit, QLineEdit, QListWidget

class Win_00(QWidget,Root):
    def __init__(self):
        super().__init__()
        self.resize(1000, 700)
        self.setWindowTitle(self.setup.txt('title'))
        self.setUI()
        self.setCMD()

    def setUI(self):
        txt = self.setup.txt
        self.v_00 = QVBoxLayout()
        self.v_01 = QVBoxLayout()
        self.h_00 = QHBoxLayout()
        self.h_01 = QHBoxLayout()
        self.h_02 = QHBoxLayout()
    
        self.h_00.addLayout(self.v_00)
        self.h_00.addLayout(self.v_01)
        self.v_01.addLayout(self.h_01)
        self.v_01.addLayout(self.h_02)
        self.setLayout(self.h_00)

        self.b_00 = QPushButton(txt('left'))
        self.b_01 = QPushButton(txt('right'))
        self.b_02 = QPushButton(txt('mirror'))
        self.b_03 = QPushButton(txt("sharpness"))
        self.b_04 = QPushButton(txt('blur'))
        self.b_05 = QPushButton(txt('contrast'))
        self.b_06 = QPushButton(txt('gray'))
        self.b_07 = QPushButton(txt('cancel'))
        self.b_08 = QPushButton(txt('delete'))
        self.b_09 = QPushButton(txt("save"))
        self.b_10 = QPushButton(txt('folder'))
        self.t_00 = QLabel(txt('picture'))
        self.lst_00 = QListWidget()

        self.v_00.addWidget(self.b_10)
        self.v_00.addWidget(self.lst_00)
        self.h_01.addWidget(self.t_00)
        self.h_02.addWidget(self.b_00)
        self.h_02.addWidget(self.b_01)
        self.h_02.addWidget(self.b_02)
        self.h_02.addWidget(self.b_03)
        self.h_02.addWidget(self.b_04)
        self.h_02.addWidget(self.b_05)
        self.h_02.addWidget(self.b_06)
        self.h_02.addWidget(self.b_07)
        self.h_02.addWidget(self.b_08)
        self.h_02.addWidget(self.b_09)

    def setCMD(self):
        send = self.controller.command
        self.b_10.clicked.connect(lambda : send(('press_folder', )))
        self.lst_00.itemClicked.connect(lambda : send(('select_file', self.lst_00.selectedItems()[0].text())))
        self.b_00.clicked.connect(lambda : send(('left',)))
        self.b_01.clicked.connect(lambda : send(('right',)))
        self.b_02.clicked.connect(lambda : send(('mirror',)))
        self.b_03.clicked.connect(lambda : send(('sharpness',)))
        self.b_04.clicked.connect(lambda : send(('blur',)))
        self.b_05.clicked.connect(lambda : send(('contrast',)))
        self.b_06.clicked.connect(lambda : send(('gray',)))
        self.b_07.clicked.connect(lambda : send(('cancel',)))
        self.b_08.clicked.connect(lambda : send(('delete_ok',)))
        self.b_09.clicked.connect(lambda : send(('save',)))
        


        # self.b_05.clicked.connect(lambda : send(('find_notes', self.l_00.text())))
        
    def stage_00(self):
        self.show()

    def stage_01(self, files, file=None):
        self.lst_00.clear() 
        self.lst_00.addItems(files)
        if file:
            for index in range(self.lst_00.count()):
                item = self.lst_00.item(index)
                if item.text() == file:
                    self.lst_00.setCurrentRow(index)
                    break

    def stage_02(self, picture):
        w = self.t_00.width()
        h = self.t_00.height()
        picture = picture.scaled(w, h, Qt.KeepAspectRatio)
        self.t_00.setPixmap(picture)

    def stage_03(self):
        self.t_00.setText(self.setup.txt('picture'))

