# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/User_ShopDetail.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 710)
        Dialog.setFixedSize(470, 710)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(235, 255, 235);")
        self.lbl_shop = QtWidgets.QLabel(Dialog)
        self.lbl_shop.setGeometry(QtCore.QRect(20, 20, 431, 61))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_shop.setFont(font)
        self.lbl_shop.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(0, 100, 76);\n"
                                    "font: 20pt \"Bai Jamjuree\";")
        self.lbl_shop.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_shop.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_shop.setObjectName("lbl_shop")
        self.btn_back = QtWidgets.QPushButton(Dialog)
        self.btn_back.setGeometry(QtCore.QRect(360, 660, 91, 31))
        self.btn_back.setStyleSheet("background-color:  rgba(0, 0, 0, 0);\n"
                                    "color: rgb(200, 9, 19);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "border-radius: 10px;\n"
                                    "border: 2px solid rgb(200, 9, 19);")
        self.btn_back.setObjectName("btn_back")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(40, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_14.setObjectName("label_14")
        self.lbl_phone = QtWidgets.QLabel(Dialog)
        self.lbl_phone.setGeometry(QtCore.QRect(40, 120, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Bai Jamjuree")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_phone.setFont(font)
        self.lbl_phone.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "font: 12pt \"Bai Jamjuree\";")
        self.lbl_phone.setObjectName("lbl_phone")
        self.lbl_email = QtWidgets.QLabel(Dialog)
        self.lbl_email.setGeometry(QtCore.QRect(40, 190, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Bai Jamjuree")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_email.setFont(font)
        self.lbl_email.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "font: 12pt \"Bai Jamjuree\";")
        self.lbl_email.setObjectName("lbl_email")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 160, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(40, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_16.setObjectName("label_16")
        self.tbro_address = QtWidgets.QTextBrowser(Dialog)
        self.tbro_address.setGeometry(QtCore.QRect(40, 260, 381, 81))
        self.tbro_address.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "font: 12pt \"Bai Jamjuree\";\n"
                                        "border: 0px;")
        self.tbro_address.setObjectName("tbro_address")
        self.tbro_detail = QtWidgets.QTextBrowser(Dialog)
        self.tbro_detail.setGeometry(QtCore.QRect(40, 370, 381, 201))
        self.tbro_detail.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "font: 12pt \"Bai Jamjuree\";\n"
                                       "border: 0px;")
        self.tbro_detail.setObjectName("tbro_detail")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(40, 340, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_17.setObjectName("label_17")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.this_dialog = Dialog
        self.SetShopDetail()

        self.btn_back.clicked.connect(self.BackToCreateParty)

    def __init__(self, passData):
        self.shopData = passData

    def SetShopDetail(self):
        self.lbl_shop.setText(self.shopData['shopName'])
        self.lbl_phone.setText(self.shopData['phone'])
        self.lbl_email.setText(self.shopData['email'])
        self.tbro_address.setText(self.shopData['address'])
        self.tbro_detail.setText(self.shopData['detail'])

    def BackToCreateParty(self):
        self.this_dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Board Game Community"))
        self.lbl_shop.setText(_translate("Dialog", "**SHOP NAME**"))
        self.btn_back.setText(_translate("Dialog", "Back"))
        self.label_14.setText(_translate("Dialog", "Telephone"))
        self.lbl_phone.setText(_translate("Dialog", "**0000000000**"))
        self.lbl_email.setText(_translate("Dialog", "**EMAIL**"))
        self.label_15.setText(_translate("Dialog", "Email"))
        self.label_16.setText(_translate("Dialog", "Address"))
        self.tbro_address.setHtml(_translate("Dialog",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'Bai Jamjuree\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">**ADDRESS</p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ADDRESS**</p></body></html>"))
        self.tbro_detail.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Bai Jamjuree\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">**DETAIL</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DETAIL**</p></body></html>"))
        self.label_17.setText(_translate("Dialog", "Detail"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
