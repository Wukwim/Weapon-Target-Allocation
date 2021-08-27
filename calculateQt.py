import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from interface import Ui_Form
import numpy as np
import target_allocation

class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)
        # self.number.setAlignment(Qt.AlignCenter)  # 文本框居中
        # self.maxvalue.setAlignment(Qt.AlignCenter)
        # self.way.setAlignment(Qt.AlignCenter)

    def calculate_q(self):
        max_value, max_value_num = target_allocation.main_enumeration()
        self.way.setText('穷举法')
        self.number.setText(str(max_value_num))
        self.maxvalue.setText(str(max_value))

    def calculate_d(self):
        max_value, s_final = target_allocation.main_dynamic(np.array(target_allocation.values).transpose())
        self.way.setText('动态规划')
        self.number.setText(str(s_final))
        self.maxvalue.setText(str(max_value))

    def clear_all(self):
        self.way.clear()
        self.number.clear()
        self.maxvalue.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mypyqt_form = MyPyQT_Form()
    mypyqt_form.show()
    sys.exit(app.exec_())