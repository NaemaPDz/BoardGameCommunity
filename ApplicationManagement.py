from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import pymongo
import dns

from _datetime import datetime
import re
from bson import ObjectId
from hashlib import md5

connection = "mongodb+srv://patavee:YWb3af6rhzUytOWy@cluster0.pynoh.mongodb.net/<dbname>?retryWrites=true&w=majority"
conn = pymongo.MongoClient(connection)
database = conn.get_database('BoardGameCommunity')


############## Useable Function ##############
def ToMD5(text):
    return md5(text.encode("utf-8")).hexdigest()


def ToObjectId(text):
    return ObjectId(text)


def IsPhoneNumber(phone):
    checkPhone = False

    if phone.__len__() != 10:
        checkPhone = False
    elif not phone.isnumeric():
        checkPhone = False
    elif phone[0] != "0":
        checkPhone = False
    else:
        checkPhone = True

    return checkPhone


def IsEmail(email):
    checkEmail = False
    emailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if not re.search(emailRegex, email):
        checkEmail = False
    else:
        checkEmail = True

    return checkEmail


############## UI Management ##############
def ChangeWindowDialog(this_dialog, new_dialog, passData=None):
    try:
        dialog = QtWidgets.QDialog()
        if passData is not None:
            ui = new_dialog.Ui_Dialog(passData=passData)
        else:
            ui = new_dialog.Ui_Dialog()
        ui.setupUi(dialog)
        this_dialog.close()
        dialog.exec_()
    except Exception as e:
        ShowMessageBox("System", "Unexpected Error !!", QMessageBox.Critical)
        print("ERROR : {}".format(e))


def OpenNewWindowDialog(new_dialog, passData=None):
    try:
        dialog = QtWidgets.QDialog()
        if passData is not None:
            ui = new_dialog.Ui_Dialog(passData=passData)
        else:
            ui = new_dialog.Ui_Dialog()
        ui.setupUi(dialog)
        dialog.exec_()
    except Exception as e:
        ShowMessageBox("System", "Unexpected Error !!", QMessageBox.Critical)
        print("ERROR : {}".format(e))


def ShowMessageBox(title, text, icon):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(icon)
    msg.setStyleSheet("font: 12pt \"Bai Jamjuree\";")
    msg.exec_()


def ShowConfirmBox(title, text, icon=QMessageBox.Question):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setStyleSheet("font: 12pt \"Bai Jamjuree\";")
    reply = msg.question(msg,
                         title,
                         text,
                         QMessageBox.Ok | QMessageBox.Cancel,
                         QMessageBox.Cancel)
    confirmation = False
    if reply == QMessageBox.Ok:
        confirmation = True
    else:
        confirmation = False

    return confirmation


######################################## New Account ########################################

## Player ##
def CheckNewPlayerData(playerData: dict):
    checkPlayerData = False
    checkDetail = ""
    checkEmailPlayerUsed = database.Players.count_documents({'email': playerData['email']})
    checkEmailShopOwnerUsed = database.ShopOwners.count_documents({'email': playerData['email']})

    if playerData['fullname'] == "" or playerData['username'] == "" \
            or playerData['phone'] == "" or playerData['email'] == "" \
            or playerData['password'] == "" or playerData['confirmPassword'] == "":
        checkPlayerData = False
        checkDetail += "Error !!\nPlease Input All Field !!"
    else:
        if not IsPhoneNumber(playerData['phone']):
            checkPlayerData = False
            checkDetail += "Error !!\nPhone Number Incorrect !!"
        elif not IsEmail(playerData['email']):
            checkPlayerData = False
            checkDetail += "Error !!\nEmail Pattern Incorrect !!"
        elif playerData['password'] != playerData['confirmPassword']:
            checkPlayerData = False
            checkDetail += "Error !!\nPassword Confirmation Doesn't Match !!"
        elif checkEmailPlayerUsed == 1 or checkEmailShopOwnerUsed == 1:
            checkPlayerData = False
            checkDetail += "Error !!\nEmail was Used !!"
        else:
            checkPlayerData = True
            checkDetail += "Create New Player Successful !!"

    return checkPlayerData, checkDetail


def InsertNewPlayer(playerData: dict):
    insertedPlayerData = playerData
    del insertedPlayerData['confirmPassword']
    insertedPlayerData['createdTime'] = datetime.now().__str__()
    currentID = database.Players.insert_one(insertedPlayerData)
    print("New Record [_id] : {}".format(currentID.inserted_id))


## Shop Owner ##
def CheckNewShopOwnerData(shopOwnerData: dict):
    checkShopOwnerData = False
    checkDetail = ""
    checkEmailPlayerUsed = database.Players.count_documents({'email': shopOwnerData['email']})
    checkEmailShopOwnerUsed = database.ShopOwners.count_documents({'email': shopOwnerData['email']})

    if shopOwnerData['shopName'] == "" or shopOwnerData['phone'] == "" \
            or shopOwnerData['address'] == "" or shopOwnerData['email'] == "" \
            or shopOwnerData['password'] == "" or shopOwnerData['confirmPassword'] == "":
        checkShopOwnerData = False
        checkDetail += "Error !!\nPlease Input All Field !!"
    else:
        if not IsPhoneNumber(shopOwnerData['phone']):
            checkShopOwnerData = False
            checkDetail += "Error !!\nPhone Number Incorrect !!"
        elif not IsEmail(shopOwnerData['email']):
            checkShopOwnerData = False
            checkDetail += "Error !!\nEmail Pattern Incorrect !!"
        elif shopOwnerData['password'] != shopOwnerData['confirmPassword']:
            checkShopOwnerData = False
            checkDetail += "Error !!\nPassword Confirmation Doesn't Match !!"
        elif checkEmailPlayerUsed == 1 or checkEmailShopOwnerUsed == 1:
            checkShopOwnerData = False
            checkDetail += "Error !!\nEmail was Used !!"
        else:
            checkShopOwnerData = True
            checkDetail += "Create New Shop Owner Successful !!"

    return checkShopOwnerData, checkDetail


def InsertNewShopOwner(shopOwnerData: dict):
    insertedShopOwnerData = shopOwnerData
    del insertedShopOwnerData['confirmPassword']
    insertedShopOwnerData['detail'] = ""
    insertedShopOwnerData['createdTime'] = datetime.now().__str__()
    currentID = database.ShopOwners.insert_one(insertedShopOwnerData)
    print("New Record [_id] : {}".format(currentID.inserted_id))


######################################## Log In ########################################
def CheckLogin(email, password):
    conditional = {'$and': [{'email': email}, {'password': password}]}
    checkLogin = "NotFound"
    userData = None
    playerFound = database.Players.count_documents(conditional)
    shopOwnerFound = database.ShopOwners.count_documents(conditional)

    if playerFound == 1:
        checkLogin = "Player"
        playerCursor = database.Players.find(conditional)
        for i in playerCursor:
            userData = i
            break
    elif shopOwnerFound == 1:
        checkLogin = "ShopOwner"
        shopOwnerCursor = database.ShopOwners.find(conditional)
        for i in shopOwnerCursor:
            userData = i
            break
    else:
        checkLogin = "Not Found"
        userData = None

    return checkLogin, userData


######################################## User ########################################
##################### Fetching Data #####################
def FetchShopList(conditional):
    shopCursor = database.ShopOwners.find(conditional)
    shopList = []
    for i in shopCursor:
        shopList.append(i)
    return shopList


def FetchPartyList(conditional):
    sorting = [('createdTime', -1)]
    partyCursor = database.Parties.find(conditional).sort(sorting)
    partyList = []
    for i in partyCursor:
        partyDetail = i
        partyDetail['currentPlayer'] = partyDetail['joinedPlayerID'].__len__()
        partyCreator = database.Players.find({'_id': i['creatorID']})
        for j in partyCreator:
            partyDetail['creatorUsername'] = j['username']
        shopLocation = database.ShopOwners.find({'_id': i['shopID']})
        for j in shopLocation:
            partyDetail['shopName'] = j['shopName']
        partyList.append(partyDetail)

    return partyList


def FetchActivityList(conditional):
    sorting = [('createdTime', -1)]
    activityCursor = database.Activities.find(conditional).sort(sorting)
    activityList = []
    for i in activityCursor:
        activityDetail = i
        activityDetail['currentPlayer'] = activityDetail['joinedPlayerID'].__len__()
        shopLocation = database.ShopOwners.find({'_id': i['shopID']})
        for j in shopLocation:
            activityDetail['shopName'] = j['shopName']
        activityList.append(activityDetail)

    return activityList


def FetchPlayerList(conditional):
    playerCursor = database.Players.find(conditional)
    playerList = []
    for i in playerCursor:
        playerList.append(i)
    return playerList


##################### Player #####################
## Create New Party ##
def CheckCreateParty(partyData: dict):
    print(partyData)
    checkPartyData = False
    checkDetail = ""

    if partyData['partyName'] == "":
        checkPartyData = False
        checkDetail += "Error !!\nPlease Enter Title !! !!"
    else:
        if partyData['startTime'] >= partyData['endTime']:
            checkPartyData = False
            checkDetail += "Error !!\nThe End Time must bt Later than The Start Time !!"
        else:
            checkPartyData = True
            checkDetail += "Create New Party Successful !!"

    return checkPartyData, checkDetail


def InsertNewParty(partyData: dict):
    insertedPartyData = partyData
    insertedPartyData['joinedPlayerID'] = [insertedPartyData['creatorID']]
    insertedPartyData['date'] = insertedPartyData['date'].strftime("%d-%b-%Y")
    insertedPartyData['startTime'] = insertedPartyData['startTime'].__str__()
    insertedPartyData['endTime'] = insertedPartyData['endTime'].__str__()
    insertedPartyData['createdTime'] = datetime.now().__str__()
    currentID = database.Parties.insert_one(insertedPartyData)
    print("New Record [_id] : {}".format(currentID.inserted_id))


## Update Party ##
def UpdatePartyMember(partyData: dict, _id):
    updatedData = {'$set': partyData}
    conditional = {'_id': _id}
    result = database.Parties.update_one(conditional, updatedData)
    print("MATCH : {}\nUPDATE : {}".format(result.matched_count, result.modified_count))


## Delete Party ##
def DeleteParty(partyID):
    conditional = {'_id': partyID}
    result = database.Parties.delete_one(conditional)
    print("DELETE : {}".format(result.deleted_count))


## Update Activity ##
def UpdateActivityMember(activityData: dict, _id):
    updatedData = {'$set': activityData}
    conditional = {'_id': _id}
    result = database.Activities.update_one(conditional, updatedData)
    print("MATCH : {}\nUPDATE : {}".format(result.matched_count, result.modified_count))


## Delete Activity ##
def DeleteActivity(activityID):
    conditional = {'_id': activityID}
    result = database.Activities.delete_one(conditional)
    print("DELETE : {}".format(result.deleted_count))


##################### Shop Owner #####################
## Edit Shop ##
def CheckEditShopData(shopData: dict):
    checkShopData = False
    checkDetail = ""

    if shopData['phone'] == "" or shopData['address'] == "" or shopData['confirmPassword'] == "":
        checkShopData = False
        checkDetail += "Error !!\nPlease Input All Field !!"
    else:
        if not IsPhoneNumber(shopData['phone']):
            checkShopData = False
            checkDetail += "Error !!\nPhone Number Incorrect !!"
        elif shopData['password'] != shopData['confirmPassword']:
            checkShopData = False
            checkDetail += "Error !!\nConfirm Password Incorrect !!"
        else:
            checkShopData = True
            checkDetail += " Edit Shop Successful !!"

    return checkShopData, checkDetail


def EditShopOwner(shopOwnerData: dict, _id):
    editedShopData = shopOwnerData
    del editedShopData['confirmPassword']
    updatedData = {'$set': editedShopData}
    conditional = {'_id': _id}
    result = database.ShopOwners.update_one(conditional, updatedData)
    print("MATCH : {}\nUPDATE : {}".format(result.matched_count, result.modified_count))


def GetNewShopUserData(_id):
    conditional = {'_id': _id}
    newShopDataList = FetchShopList(conditional)
    newShopData = newShopDataList[0]
    return newShopData


## Create New Activity ##
def CheckCreateActivity(activityData: dict):
    print(activityData)
    checkActivityData = False
    checkDetail = ""

    if activityData['activityName'] == "":
        checkActivityData = False
        checkDetail += "Error !!\nPlease Enter Title !! !!"
    else:
        if activityData['startTime'] >= activityData['endTime']:
            checkActivityData = False
            checkDetail += "Error !!\nThe End Time must bt Later than The Start Time !!"
        else:
            checkActivityData = True
            checkDetail += "Create New Party Successful !!"

    return checkActivityData, checkDetail


def InsertNewActivity(activityData: dict):
    insertedActivityData = activityData
    insertedActivityData['joinedPlayerID'] = []
    insertedActivityData['date'] = insertedActivityData['date'].strftime("%d-%b-%Y")
    insertedActivityData['startTime'] = insertedActivityData['startTime'].__str__()
    insertedActivityData['endTime'] = insertedActivityData['endTime'].__str__()
    insertedActivityData['createdTime'] = datetime.now().__str__()
    currentID = database.Activities.insert_one(insertedActivityData)
    print("New Record [_id] : {}".format(currentID.inserted_id))
