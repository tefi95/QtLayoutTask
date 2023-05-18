# QtLayoutTask
#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton 

app = QApplication([])
win = QWidget()
win.show()

main_layout = QHBoxLayout() #V - вертикальная направляющая
win.setLayout(main_layout) #устанаваливаем окну win layout - main_layout

b1 = QPushButton("кто")
main_layout.addWidget(b1)

b2 = QPushButton('читает')
main_layout.addWidget(b2)

b3 = QPushButton('тот лучший')
main_layout.addWidget(b3)

app.exec_()
