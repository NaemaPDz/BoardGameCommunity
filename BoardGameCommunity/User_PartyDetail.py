# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/User_PartyDetail.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import ApplicationManagement as am
import User_PartyList, User_ShopDetail, User_MemberList


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
        self.lbl_title = QtWidgets.QLabel(Dialog)
        self.lbl_title.setGeometry(QtCore.QRect(20, 20, 431, 61))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "color: rgb(0, 100, 76);\n"
                                     "font: 16pt \"Bai Jamjuree\";\n")
        self.lbl_title.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 100, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                   "color: rgb(0, 100, 76);")
        self.label_9.setObjectName("label_9")
        self.btn_back = QtWidgets.QPushButton(Dialog)
        self.btn_back.setGeometry(QtCore.QRect(360, 660, 91, 31))
        self.btn_back.setStyleSheet("background-color:  rgba(0, 0, 0, 0);\n"
                                    "color: rgb(200, 9, 19);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "border-radius: 10px;\n"
                                    "border: 2px solid rgb(200, 9, 19);")
        self.btn_back.setObjectName("btn_back")
        self.btn_viewShop = QtWidgets.QPushButton(Dialog)
        self.btn_viewShop.setGeometry(QtCore.QRect(330, 130, 111, 41))
        self.btn_viewShop.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                        "color: rgb(0, 154, 49);\n"
                                        "border-radius: 10px;\n"
                                        "border: 2px solid rgb(0, 154, 49);")
        self.btn_viewShop.setObjectName("btn_viewShop")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 380, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 170, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(40, 240, 211, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(40, 310, 211, 31))
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
        self.lbl_shop = QtWidgets.QLabel(Dialog)
        self.lbl_shop.setGeometry(QtCore.QRect(40, 130, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Bai Jamjuree")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_shop.setFont(font)
        self.lbl_shop.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"Bai Jamjuree\";")
        self.lbl_shop.setObjectName("lbl_shop")
        self.lbl_date = QtWidgets.QLabel(Dialog)
        self.lbl_date.setGeometry(QtCore.QRect(40, 200, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Bai Jamjuree")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_date.setFont(font)
        self.lbl_date.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"Bai Jamjuree\";")
        self.lbl_date.setObjectName("lbl_date")
        self.lbl_time = QtWidgets.QLabel(Dialog)
        self.lbl_time.setGeometry(QtCore.QRect(40, 270, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Bai Jamjuree")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_time.setFont(font)
        self.lbl_time.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"Bai Jamjuree\";")
        self.lbl_time.setObjectName("lbl_time")
        self.lbl_member = QtWidgets.QLabel(Dialog)
        self.lbl_member.setGeometry(QtCore.QRect(40, 340, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Bai Jamjuree")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_member.setFont(font)
        self.lbl_member.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                      "font: 12pt \"Bai Jamjuree\";")
        self.lbl_member.setObjectName("lbl_member")
        self.tbro_description = QtWidgets.QTextBrowser(Dialog)
        self.tbro_description.setGeometry(QtCore.QRect(40, 410, 381, 101))
        self.tbro_description.setStyleSheet("font: 12pt \"Bai Jamjuree\";\n"
                                            "background-color: rgba(255, 255, 255, 0);\n"
                                            "border: 0px;")
        self.tbro_description.setObjectName("tbro_description")
        self.btn_viewMember = QtWidgets.QPushButton(Dialog)
        self.btn_viewMember.setGeometry(QtCore.QRect(330, 340, 111, 41))
        self.btn_viewMember.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                          "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                          "color: rgb(0, 154, 49);\n"
                                          "border-radius: 10px;\n"
                                          "border: 2px solid rgb(0, 154, 49);")
        self.btn_viewMember.setObjectName("btn_viewMember")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(40, 520, 101, 31))
        font = QtGui.QFont()
        font.setFamily("ZCOOL QingKe HuangYou")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                    "color: rgb(0, 100, 76);")
        self.label_13.setObjectName("label_13")
        self.lbl_owner = QtWidgets.QLabel(Dialog)
        self.lbl_owner.setGeometry(QtCore.QRect(40, 550, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Bai Jamjuree")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbl_owner.setFont(font)
        self.lbl_owner.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                     "font: 12pt \"Bai Jamjuree\";")
        self.lbl_owner.setObjectName("lbl_owner")

        self.btn_partyAction = QtWidgets.QPushButton(Dialog)
        self.btn_partyAction.setGeometry(QtCore.QRect(40, 600, 391, 41))
        self.btn_partyAction.setObjectName("btn_partyAction")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.this_dialog = Dialog
        self.ShowPartyDetail()
        self.SetPartyActionButton()

        self.btn_viewShop.clicked.connect(self.ViewShop)
        self.btn_viewMember.clicked.connect(self.ViewPartyMember)
        self.btn_back.clicked.connect(self.BackToPlayerParty)

    def __init__(self, passData):
        self.userData = passData['userData']
        partyList = am.FetchPartyList({'_id': passData['partyID']})
        self.partyData: None
        for i in partyList:
            self.partyData = i
            break

    def ShowPartyDetail(self):
        self.lbl_title.setText(self.partyData['partyName'])
        self.lbl_shop.setText(self.partyData['shopName'])
        self.lbl_date.setText(self.partyData['date'])
        self.lbl_time.setText("{} - {}".format(self.partyData['startTime'], self.partyData['endTime']))
        self.lbl_member.setText("{} / {}".format(self.partyData['currentPlayer'], self.partyData['maxPlayer']))
        self.tbro_description.setText(self.partyData['description'])
        self.lbl_owner.setText(self.partyData['creatorUsername'])

    def SetPartyActionButton(self):
        if self.userData['_id'] == self.partyData['creatorID']:
            self.btn_partyAction.setText("Cancel Party")
            self.btn_partyAction.setStyleSheet("background-color: rgb(200, 9, 19);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                               "border-radius: 10px;\n"
                                               "border: 2px solid rgb(200, 9, 19);")
            self.btn_partyAction.clicked.connect(self.CancelParty)
        elif self.userData['_id'] in self.partyData['joinedPlayerID']:
            self.btn_partyAction.setText("Leave This Party")
            self.btn_partyAction.setStyleSheet("background-color: rgb(200, 9, 19);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                               "border-radius: 10px;\n"
                                               "border: 2px solid rgb(200, 9, 19);")
            self.btn_partyAction.clicked.connect(self.LeaveParty)
        elif self.partyData['currentPlayer'] >= self.partyData['maxPlayer']:
            self.btn_partyAction.setText("Party Full")
            self.btn_partyAction.setDisabled(True)
            self.btn_partyAction.setStyleSheet("background-color: rgb(133, 133, 133);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                               "border-radius: 10px;\n"
                                               "border: 2px solid rgb(133, 133, 133);")
        else:
            self.btn_partyAction.setText("Join This Party")
            self.btn_partyAction.setStyleSheet("background-color: rgb(0, 154, 49);\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "font: 12pt \"ZCOOL QingKe HuangYou\";\n"
                                                   "border-radius: 10px;\n"
                                                   "border: 2px solid rgb(0, 154, 49);")
            self.btn_partyAction.clicked.connect(self.JoinParty)

    def ViewShop(self):
        shopList = am.FetchShopList({'_id': self.partyData['shopID']})
        shopData: None
        for i in shopList:
            shopData = i
            break
        am.OpenNewWindowDialog(User_ShopDetail, passData=shopData)

    def ViewPartyMember(self):
        partyData = {'eventName': self.partyData['partyName'],
                     'maxPlayer': self.partyData['maxPlayer'],
                     'joinedPlayerID': self.partyData['joinedPlayerID']}
        am.OpenNewWindowDialog(User_MemberList, passData=partyData)

    def JoinParty(self):
        reply = am.ShowConfirmBox("Join Party",
                                  "Joining Party [{}].\nAre you sure ?".format(self.partyData['partyName']))
        if reply:
            joinedPlayerID = self.partyData['joinedPlayerID']
            joinedPlayerID.append(self.userData['_id'])
            updatePartyData = {'joinedPlayerID': joinedPlayerID}
            try:
                am.UpdatePartyMember(updatePartyData, self.partyData['_id'])
                am.ShowMessageBox("Join Party",
                                  "Join Party [{}]\nSuccessful !!".format(self.partyData['partyName']),
                                  QMessageBox.Information)
                self.BackToPlayerParty()
            except:
                am.ShowMessageBox("Join Party",
                                  "Join Party [{}]\nFailed !!\nPlease try again !!".format(self.partyData['partyName']),
                                  QMessageBox.Critical)

    def LeaveParty(self):
        reply = am.ShowConfirmBox("Leave Party",
                                  "Leaving Party [{}].\nAre you sure ?".format(self.partyData['partyName']))
        if reply:
            joinedPlayerID = self.partyData['joinedPlayerID']
            joinedPlayerID.remove(self.userData['_id'])
            updatePartyData = {'joinedPlayerID': joinedPlayerID}
            try:
                am.UpdatePartyMember(updatePartyData, self.partyData['_id'])
                am.ShowMessageBox("Leave Party",
                                  "Leave Party [{}]\nSuccessful !!".format(self.partyData['partyName']),
                                  QMessageBox.Information)
                self.BackToPlayerParty()
            except:
                am.ShowMessageBox("Leave Party",
                                  "Leave Party [{}]\nFailed !!\nPlease try again !!".format(
                                      self.partyData['partyName']),
                                  QMessageBox.Critical)

    def CancelParty(self):
        reply = am.ShowConfirmBox("Cancel Party",
                                  "Cancel Party [{}].\nAre you sure ?".format(self.partyData['partyName']))

        if reply:
            try:
                am.DeleteParty(self.partyData['_id'])
                am.ShowMessageBox("Cancel Party",
                                  "Cancel Party [{}]\nSuccessful !!".format(self.partyData['partyName']),
                                  QMessageBox.Information)
                self.BackToPlayerParty()
            except:
                am.ShowMessageBox("Cancel Party",
                                  "Cancel Party [{}]\nFailed !!\nPlease try again !!".format(
                                      self.partyData['partyName']),
                                  QMessageBox.Critical)

    def BackToPlayerParty(self):
        am.ChangeWindowDialog(self.this_dialog, User_PartyList, passData=self.userData)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Board Game Community"))
        self.lbl_title.setText(_translate("Dialog", "**PARTY NAME**"))
        self.label_9.setText(_translate("Dialog", "Shop Party Location"))
        self.btn_back.setText(_translate("Dialog", "Back"))
        self.btn_viewShop.setText(_translate("Dialog", "View Shop"))
        self.label_10.setText(_translate("Dialog", "Description"))
        self.label_11.setText(_translate("Dialog", "Date and Time"))
        self.label_12.setText(_translate("Dialog", "Time"))
        self.label_14.setText(_translate("Dialog", "Member"))
        self.lbl_shop.setText(_translate("Dialog", "**SHOP NAME**"))
        self.lbl_date.setText(_translate("Dialog", "**DD-MMM-YY**"))
        self.lbl_time.setText(_translate("Dialog", "**00.00 - 00.00**"))
        self.lbl_member.setText(_translate("Dialog", "**00 / 00**"))
        self.tbro_description.setHtml(_translate("Dialog",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Bai Jamjuree\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">**DESCRIPTION</p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DESCRIPTION**</p></body></html>"))
        self.btn_viewMember.setText(_translate("Dialog", "View Member"))
        self.label_13.setText(_translate("Dialog", "Party Owner"))
        self.lbl_owner.setText(_translate("Dialog", "**OWNER USERNAME**"))
        self.btn_partyAction.setText(_translate("Dialog", "**ACTION BUTTON**"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
