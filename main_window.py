from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt

app=QApplication([])

q=QLabel("Введіть запитання:")
q_red=QLineEdit()
a=QLabel("Введіть вірну відповідь:")
a_red=QLineEdit()
w1=QLabel("Введіть першу хибну відповідь:")
w1_red=QLineEdit()
w2=QLabel("Введіть другу хибну відповідь:")
w2_red=QLineEdit()
w3=QLabel("Введіть третю хибну відповідь:")
w3_red=QLineEdit()

btn_add=QPushButton("Додати запитання:")
btn_clear=QPushButton("Очистити:")

line1_menu.addWidget(q)
line1_menu.addWidget(a)
line1_menu.addWidget(w1)
line1_menu.addWidget(w2)
line1_menu.addWidget(w3)

line1_menu.addWidget(q_red)
line1_menu.addWidget(a_red)
line1_menu.addWidget(w1_red)
line1_menu.addWidget(w2_red)
line1_menu.addWidget(w3_red)

line_hor=QHBoxLayout()
line1_hourQHBoxLayout()

line_hor.addLayout(line1_menu)
line2_hor.addLayout(line2_menu)

line2_hor.addWidget(btn_add)
line2_hor.addWidger(btn_clear)

line_menu.addLayout(line_hor)
line_menu.addLayout(line2_hour)

line_menu.addWidget(stat)
line_menu.addWidget(stat_info)
line_menu.addWidget(btn_back)

menu_win=QWidget()
menu_win=.setLayout(line_menu)
menu.show()
