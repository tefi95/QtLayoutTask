from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton 

app = QApplication([])
main_win = QWidget()
main_win.show()

main_layout = QHBoxLayout()
main_layout_2 = QHBoxLayout()        
main_v_layout = QVBoxLayout()

b1 = QPushButton('1')
b2 = QPushButton('2')
b3 = QPushButton('3')
b4 = QPushButton('4')
b5 = QPushButton('5')        

main_v_layout.addLayout(main_layout)
main_v_layout.addLayout(main_layout_2)
main_layout.addWidget(b1)
main_layout.addWidget(b2)
main_layout.addWidget(b3)
main_layout_2.addWidget(b4)
main_layout_2.addWidget(b5)

main_win.setLayout(main_v_layout)
app.exec_()
