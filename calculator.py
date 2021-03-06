# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 310)
        Form.setMinimumSize(QtCore.QSize(360, 310))
        Form.setMaximumSize(QtCore.QSize(360, 310))
        self.output_display = QtWidgets.QLabel(Form)
        self.output_display.setGeometry(QtCore.QRect(10, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.output_display.setFont(font)
        self.output_display.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.output_display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output_display.setMidLineWidth(0)
        self.output_display.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.output_display.setObjectName("output_display")

        # PERCENTAGE BUTTON
        self.percent_btn = QtWidgets.QPushButton(Form)
        self.percent_btn.setGeometry(QtCore.QRect(10, 60, 81, 41))
        self.percent_btn.clicked.connect(self.calculate_percentage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.percent_btn.setFont(font)
        self.percent_btn.setObjectName("percent_btn")

        # CLEAR BTN
        self.clear_btn = QtWidgets.QPushButton(Form)
        self.clear_btn.setGeometry(QtCore.QRect(100, 60, 81, 41))
        self.clear_btn.clicked.connect(self.clear_output)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.arrow_btn = QtWidgets.QPushButton(Form)
        self.arrow_btn.setGeometry(QtCore.QRect(190, 60, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # ARROW BTN
        self.arrow_btn.setFont(font)
        self.arrow_btn.setObjectName("arrow_btn")
        self.divide_btn = QtWidgets.QPushButton(Form)
        self.divide_btn.setGeometry(QtCore.QRect(280, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # DIVIDE BTN
        self.divide_btn.setFont(font)
        self.divide_btn.setObjectName("divide_btn")
        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(190, 110, 81, 41))
        self.divide_btn.clicked.connect(lambda: self.display_btn_val("/"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # BTN 9
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_9.clicked.connect(lambda: self.display_btn_val("9"))

        # MULTIPLY BTN
        self.multiply_btn = QtWidgets.QPushButton(Form)
        self.multiply_btn.setGeometry(QtCore.QRect(280, 110, 71, 41))
        self.multiply_btn.clicked.connect(lambda: self.display_btn_val("*"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.multiply_btn.setFont(font)
        self.multiply_btn.setObjectName("multiply_btn")

        # BTN 7
        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(10, 110, 81, 41))
        self.btn_7.clicked.connect(lambda: self.display_btn_val("7"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")

        # BTN 8
        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(100, 110, 81, 41))
        self.btn_8.clicked.connect(lambda: self.display_btn_val("8"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")

        # BTN 6
        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(190, 160, 81, 41))
        self.btn_6.clicked.connect(lambda: self.display_btn_val("6"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")

        # MINUS BTN
        self.minus_btn = QtWidgets.QPushButton(Form)
        self.minus_btn.setGeometry(QtCore.QRect(280, 160, 71, 41))
        self.minus_btn.clicked.connect(lambda: self.display_btn_val("-"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.minus_btn.setFont(font)
        self.minus_btn.setObjectName("minus_btn")

        # BTN 4
        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(10, 160, 81, 41))
        self.btn_4.clicked.connect(lambda: self.display_btn_val("4"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")

        # BTN 5
        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(100, 160, 81, 41))
        self.btn_5.clicked.connect(lambda: self.display_btn_val("5"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")

        # BTN 3
        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(190, 210, 81, 41))
        self.btn_3.clicked.connect(lambda: self.display_btn_val("3"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")

        # PLUS BTN
        self.plus_btn = QtWidgets.QPushButton(Form)
        self.plus_btn.setGeometry(QtCore.QRect(280, 210, 71, 41))
        self.plus_btn.clicked.connect(lambda: self.display_btn_val("+"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.plus_btn.setFont(font)
        self.plus_btn.setObjectName("plus_btn")

        # BTN 1
        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(10, 210, 81, 41))
        self.btn_1.clicked.connect(lambda: self.display_btn_val("1"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")

        # BTN 2
        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(100, 210, 81, 41))
        self.btn_2.clicked.connect(lambda: self.display_btn_val("2"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")

        # BTN 0
        self.btn_0 = QtWidgets.QPushButton(Form)
        self.btn_0.setGeometry(QtCore.QRect(10, 260, 81, 41))
        self.btn_0.clicked.connect(lambda: self.display_btn_val("0"))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")

        # PINT BTN
        self.point_btn = QtWidgets.QPushButton(Form)
        self.point_btn.setGeometry(QtCore.QRect(100, 260, 81, 41))
        self.point_btn.clicked.connect(lambda: self.display_btn_val("."))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.point_btn.setFont(font)
        self.point_btn.setObjectName("point_btn")

        # EQUAL TO BTN
        self.equal_btn = QtWidgets.QPushButton(Form)
        self.equal_btn.setGeometry(QtCore.QRect(190, 260, 161, 41))
        self.equal_btn.clicked.connect(self.calculate_output_display_val)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.equal_btn.setFont(font)
        self.equal_btn.setObjectName("equal_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    # Gets the value of the btn and display it on the output_display
    def display_btn_val(self, btn_val):
        if self.output_display.text() == "0" or self.output_display.text() == "Math Error":
            self.output_display.setText(btn_val)
        else:
            self.output_display.setText(f"{self.output_display.text()}{btn_val}")
        return

    # Evaluate the the value in the output display and display in the output display
    def calculate_output_display_val(self):
        try:
            self.output_display.setText(str(eval(self.output_display.text())))
        except:
            self.output_display.setText("Math Error")
        return

    # Get the percentage of the current value in the output display
    def calculate_percentage(self):
        try:
            self.output_display.setText(str((float(self.output_display.text()))/100))
        except:
            self.output_display.setText("Math Error")

    #  clears the output of the screen
    def clear_output(self):
        self.output_display.setText("0")
        return

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.output_display.setText(_translate("Form", "0"))
        self.percent_btn.setText(_translate("Form", "%"))
        self.clear_btn.setText(_translate("Form", "C"))
        self.arrow_btn.setText(_translate("Form", "<<"))
        self.divide_btn.setText(_translate("Form", "/"))
        self.btn_9.setText(_translate("Form", "9"))
        self.multiply_btn.setText(_translate("Form", "*"))
        self.btn_7.setText(_translate("Form", "7"))
        self.btn_8.setText(_translate("Form", "8"))
        self.btn_6.setText(_translate("Form", "6"))
        self.minus_btn.setText(_translate("Form", "-"))
        self.btn_4.setText(_translate("Form", "4"))
        self.btn_5.setText(_translate("Form", "5"))
        self.btn_3.setText(_translate("Form", "3"))
        self.plus_btn.setText(_translate("Form", "+"))
        self.btn_1.setText(_translate("Form", "1"))
        self.btn_2.setText(_translate("Form", "2"))
        self.btn_0.setText(_translate("Form", "0"))
        self.point_btn.setText(_translate("Form", "."))
        self.equal_btn.setText(_translate("Form", "="))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
