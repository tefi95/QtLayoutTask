from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton 

app = QApplication([])
main_win = QWidget()
main_win.show()

main_layout = QHBoxLayout()             

b1 = QHBoxLayout()
b2 = QHBoxLayout()
b3 = QHBoxLayout()

main_v_line = QVBoxLayout()

b1 = QPushButton("1")            
b2 = QPushButton("2")    
b3 = QPushButton('3')
b4 = QPushButton("4")  
b5 = QPushButton("5")   

main_layout.addWidget(b1)           
main_layout.addLayout(main_v_line)            
main_layout.addWidget(b2)          
main_v_line.addWidget(b3)

main_v_line.addWidget(b4)        
             
main_v_line.addWidget(b5)        




main_win.setLayout(main_layout)
app.exec_()
