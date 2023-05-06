from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from PyQt5.QtCore import QCoreApplication
from app_layout import *
from main_layout import *
#from data import *

def main():
    main_window.show()
    test_window.hide()

def start():
    main_window.hide()
    test_window.show()

exit_btn.clicked.connect(QCoreApplication.instance().quit)
start_btn.clicked.connect(start)
menu_btn.clicked.connect(main)

#answer_btn.setStyleSheet("background: rgb(255,255, 255);")
#group_box2.setStyleSheet("background: rgb(255,255, 255);")
#group_box.setStyleSheet("background: rgb(255,255, 255);")
start_btn.setStyleSheet("background: rgb(255,255, 255);")
exit_btn.setStyleSheet("background: rgb(255,255, 255);")
#menu_btn.setStyleSheet("background: rgb(255,255, 255);")
#qlb.setStyleSheet("background: rgb(255,255, 255);")

main_window = QWidget()
main_window.setStyleSheet("background-image: url(M:/Python/Memory Card [My Project]/Additional Files/Image/background.png);")
main_window.setWindowTitle("English Tester")
main_window.setLayout(main_line)
main_window.resize(1000, 563)
main_window.show()

test_window = QWidget()
test_window.setStyleSheet("background-image: url(M:/Python/Memory Card [My Project]/Additional Files/Image/background.png);")
test_window.setWindowTitle("English Tester")
test_window.setLayout(layout_app)
test_window.resize(1000, 563)

app.exec_()