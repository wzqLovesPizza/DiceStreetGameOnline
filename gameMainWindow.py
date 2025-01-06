from PyQt5 import QtCore, QtGui, QtWidgets
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import Qt, pyqtSignal
import struct
import threading
import json
from ShopWindow_dataDisplay import ShopWindow_display
from ShopWindow import ShopWindow
from PyQt5.QtGui import QFont
import ast



class GameMainWindow(QWidget):

    raiseShopWindow = pyqtSignal(dict)
    updatePlayerListSignal = pyqtSignal(list)
    raisePlayerdataSignal = pyqtSignal(dict)
    rollTwoPermissionSignal = pyqtSignal()
    raiseThrowConfirmWindowSignal = pyqtSignal()
    updateEventSignal = pyqtSignal(str)
    updateChatSignal = pyqtSignal(str)
    updateWhoseTurnSignal = pyqtSignal(str)

    def __init__(self, ip, port, name):

        super().__init__()

        self.raiseShopWindow.connect(self.raiseShopWindowfunc)
        self.updatePlayerListSignal.connect(self.updatePlayerList)
        self.raisePlayerdataSignal.connect(self.updatePlayerData)
        self.rollTwoPermissionSignal.connect(self.divideRollButtonIntoTwo)
        self.raiseThrowConfirmWindowSignal.connect(self.raiseThrowConfirmWindow)
        self.updateEventSignal.connect(self.updateEvent)
        self.updateChatSignal.connect(self.updateChat)
        self.updateWhoseTurnSignal.connect(self.WhoseTurn)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client_socket.connect((ip, port))
            register_name = self.sendPreprocess(name)
            self.client_socket.send(register_name)
        except Exception as e:
            
            QMessageBox.critical(self, '错误', f'连接服务器失败: {e}')
            self.client_socket.close()
            return
        

        self.setObjectName(name)
        self.setWindowTitle(name)
        self.resize(1920, 1080)
#         Form.setStyleSheet("QWidget {\n"
# "    background-image: url(C:/Windows/Web/Wallpaper/ThemeD/img32.jpg); /* 设置背景图像 */\n"
# "    background-repeat: no-repeat; /* 不重复 */\n"
# "    background-position: center; /* 居中显示 */\n"
# "    background-attachment: fixed; /* 背景固定 */\n"
# "}")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(770, 380, 351, 151))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 630, 301, 211))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(1610, 650, 301, 191))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 940, 161, 91))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 450, 1051, 20))
#         self.frame.setStyleSheet("QFrame {\n"
# "    background-color: #000000; /* 设置为黑色 */\n"
# "    height: 2px; /* 调整高度以控制线条粗细 */\n"
# "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(1600, 920, 121, 131))
#         self.pushButton_5.setStyleSheet("QPushButton {\n"
# "    background-color: #3498db; /* 按钮背景色 */\n"
# "    border: 2px solid #2980b9; /* 边框颜色和宽度 */\n"
# "    border-radius: 25px; /* 设置圆角半径，确保足够大以形成圆形 */\n"
# "    width: 50px; /* 按钮宽度 */\n"
# "    height: 50px; /* 按钮高度 */\n"
# "    color: white; /* 文字颜色 */\n"
# "}\n"
# "QPushButton:hover {\n"
# "    background-color: #2980b9; /* 鼠标悬停时的背景色 */\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "    background-color: #1c6691; /* 按钮按下时的背景色 */\n"
# "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(30, 150, 601, 391))
        font = QFont('微软雅黑', 15)
        font.setFamily("Arial")
        font.setBold(True)
        self.textEdit.setFont(font)
#         self.textEdit.setStyleSheet("QTextEdit {\n"
# "    background-color: #f5f5f5; /* 背景色 */\n"
# "    color: #333333; /* 文本颜色 */\n"
# "    font-family: Arial; /* 字体 */\n"
# "    font-size: 12px; /* 字体大小 */\n"
# "    padding: 10px; /* 内边距 */\n"
# "}\n"
# "QTextEdit {\n"
# "    border: 1px solid #ccc; /* 边框颜色和宽度 */\n"
# "    border-radius: 5px; /* 圆角半径 */\n"
# "    background-color: #f9f9f9; /* 背景色 */\n"
# "    color: #222; /* 文本颜色 */\n"
# "    padding: 5px; /* 内边距 */\n"
# "}\n"
# "QTextEdit::selection {\n"
# "    background-color: #2980b9; /* 选中时的背景色 */\n"
# "    color: white; /* 选中时的文字颜色 */\n"
# "}\n"
# "QTextEdit QScrollBar:vertical {\n"
# "    border: none; /* 去掉边框 */\n"
# "    background: #f5f5f5; /* 滚动条背景 */\n"
# "    width: 10px; /* 滚动条宽度 */\n"
# "}\n"
# "\n"
# "QTextEdit QScrollBar::handle:vertical {\n"
# "    background: #ccc; /* 滚动条滑块背景 */\n"
# "    border-radius: 5px; /* 圆角 */\n"
# "}\n"
# "\n"
# "QTextEdit QScrollBar::handle:vertical:hover {\n"
# "    background: #bbb; /* 滚动条滑块悬停颜色 */\n"
# "}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(1240, 150, 651, 391))
        self.textEdit_2.setFont(font)
#         self.textEdit_2.setStyleSheet("QTextEdit {\n"
# "    background-color: #f5f5f5; /* 背景色 */\n"
# "    color: #333333; /* 文本颜色 */\n"
# "    font-family: Arial; /* 字体 */\n"
# "    font-size: 12px; /* 字体大小 */\n"
# "    padding: 10px; /* 内边距 */\n"
# "}\n"
# "QTextEdit {\n"
# "    border: 1px solid #ccc; /* 边框颜色和宽度 */\n"
# "    border-radius: 5px; /* 圆角半径 */\n"
# "    background-color: #f9f9f9; /* 背景色 */\n"
# "    color: #222; /* 文本颜色 */\n"
# "    padding: 5px; /* 内边距 */\n"
# "}\n"
# "QTextEdit::selection {\n"
# "    background-color: #2980b9; /* 选中时的背景色 */\n"
# "    color: white; /* 选中时的文字颜色 */\n"
# "}\n"
# "QTextEdit QScrollBar:vertical {\n"
# "    border: none; /* 去掉边框 */\n"
# "    background: #f5f5f5; /* 滚动条背景 */\n"
# "    width: 10px; /* 滚动条宽度 */\n"
# "}\n"
# "\n"
# "QTextEdit QScrollBar::handle:vertical {\n"
# "    background: #ccc; /* 滚动条滑块背景 */\n"
# "    border-radius: 5px; /* 圆角 */\n"
# "}\n"
# "\n"
# "QTextEdit QScrollBar::handle:vertical:hover {\n"
# "    background: #bbb; /* 滚动条滑块悬停颜色 */\n"
# "}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 100, 301, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(310, 950, 901, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(1290, 960, 101, 61))
#         self.pushButton_6.setStyleSheet("QPushButton {\n"
# "    background-color: #3498db; /* 按钮背景色 */\n"
# "    border: 2px solid #2980b9; /* 边框颜色和宽度 */\n"
# "    border-radius: 10px; /* 圆角半径，调整这个值以控制圆润程度 */\n"
# "    padding: 10px; /* 内边距，增加按钮内部空间 */\n"
# "    color: white; /* 文字颜色 */\n"
# "    font-size: 16px; /* 文字大小 */\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "    background-color: #2980b9; /* 鼠标悬停时的背景色 */\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "    background-color: #1c6691; /* 按钮按下时的背景色 */\n"
# "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(1520, 70, 201, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(710, 650, 571, 191))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(790, 40, 641, 91))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.retranslateUi()

        self.textEdit.setReadOnly(True)
        self.textEdit_2.setReadOnly(True)
        self.pushButton_6.clicked.connect(self.send)
        self.lineEdit.returnPressed.connect(self.send)
        self.pushButton_5.clicked.connect(self.throw_dice)
        self.pushButton.clicked.connect(self.getPlayer1Data)
        self.pushButton_2.clicked.connect(self.getPlayer2Data)
        self.pushButton_3.clicked.connect(self.getPlayer3Data)
        self.pushButton_4.clicked.connect(self.getPlayerMySelf)

        
        # QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "玩家1"))
        self.pushButton_2.setText(_translate("Form", "玩家2"))
        self.pushButton_3.setText(_translate("Form", "玩家3"))
        self.pushButton_4.setText(_translate("Form", "你"))
        self.pushButton_5.setText(_translate("Form", "掷骰子"))
        self.label.setText(_translate("Form", "系统"))
        self.pushButton_6.setText(_translate("Form", "发送"))
        self.label_2.setText(_translate("Form", "聊天"))

        threading.Thread(target=self.receive_message_Thread, daemon=True).start()

    def throw_dice(self):
        message = '/throw_dice'
        message = self.sendPreprocess(message)
        self.client_socket.send(message)


    def sendPreprocess(self, item):
        if isinstance(item, str):
            item_bytes = item.encode('utf-8')
            item_length = struct.pack('!I', len(item_bytes))
            item = item_length + item_bytes
            return item
        elif isinstance(item, bytes):
            item_length = struct.pack('!I', len(item))
            item = item_length + item
            return item
        else:
            raise TypeError("item must be str or bytes")


    def receivePreprocess(self, client_socket):
        header = client_socket.recv(4)

        if not header:
            return -1
        
        item_length = struct.unpack('!I', header)[0]
        item = client_socket.recv(item_length)
        return item


    def send(self):

        message = '/chat' + self.lineEdit.text()

        if message:
            message = self.sendPreprocess(message)
            self.client_socket.send(message)
            self.lineEdit.clear()


    def receive_message_Thread(self):
        while True:
            message = self.receivePreprocess(self.client_socket)
            if message == -1:
                break
            else:
                message = message.decode('utf-8')

                if message.startswith('/playerdata'):
                    message = message[11:]
                    playerdata = json.loads(message)
                    self.raisePlayerdataSignal.emit(playerdata)

                if message.startswith('/raiseThrowConfirmWindow'):
                    self.raiseThrowConfirmWindowSignal.emit()
                
                if message.startswith('/playerlist'):
                    message = message[11:]
                    playerlist = ast.literal_eval(message)
                    self.updatePlayerListSignal.emit(playerlist)

                if message.startswith('/raiseClientShopWindow'):
                    print('已收到唤出商店窗口的指令')
                    buyPlayer_info = json.loads(message[22:])
                    self.raiseShopWindow.emit(buyPlayer_info)
                    
                # if message.startswith('/rolldata'):
                #     message = message[9:]
                #     # 搞点骰子gif，暂时以播报文字代替

                if message.startswith('/event'):
                    message = message[6:]

                    self.updateEventSignal.emit(message)

                if message.startswith('/chat'):
                    message = message[5:]
                    self.updateChatSignal.emit(message)
                    
                if message.startswith('/rollTwoPermission'):
                    print('获得掷两个骰子权限，按钮分裂！')
                    self.rollTwoPermissionSignal.emit()
                
                if message.startswith('/turn'):
                    message = message[5:]
                    self.updateWhoseTurnSignal.emit(message)
                    


    def divideRollButtonIntoTwo(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_5.setText(_translate("Form", "掷1个骰子"))
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(1600, 920, 121, 131))
        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(1730, 920, 121, 131))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: #3498db; /* 按钮背景色 */\n"
"    border: 2px solid #2980b9; /* 边框颜色和宽度 */\n"
"    border-radius: 25px; /* 设置圆角半径，确保足够大以形成圆形 */\n"
"    width: 50px; /* 按钮宽度 */\n"
"    height: 50px; /* 按钮高度 */\n"
"    color: white; /* 文字颜色 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* 鼠标悬停时的背景色 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c6691; /* 按钮按下时的背景色 */\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText(_translate("Form", "掷2个骰子"))
        self.pushButton_7.show()
        self.pushButton_7.clicked.connect(self.throw_two_dice)


    def throw_two_dice(self):
        message = '/throw_dice2'
        message = self.sendPreprocess(message)
        self.client_socket.send(message)
    

    def ShopWindowBackmessage(self, data):
        data = self.sendPreprocess(data)
        self.client_socket.send(data)
        self.shopwindow.hide()
        print('商店窗口已关闭')
    

    def updatePlayerList(self, playerlist):
        self.pushButton.setText(playerlist[0])
        self.pushButton_2.setText(playerlist[1])
        self.pushButton_3.setText(playerlist[2])


    def raiseThrowConfirmWindow(self):
        reply = QMessageBox.question(self, '提示', '是否重新掷骰子？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            action = self.sendPreprocess('/chooseThrowTwice')
            self.client_socket.send(action)
        else:
            action = self.sendPreprocess('/chooseNotThrowTwice')
            self.client_socket.send(action)


    def raiseShopWindowfunc(self,player_info):
        self.shopwindow = ShopWindow()
        self.shopwindow.updatePlayerData(player_info)
        self.shopwindow.dataSent.connect(self.ShopWindowBackmessage)
        self.shopwindow.show()
        print('已唤出商店窗口')


    def updatePlayerData(self, player_data):
        self.shopwindow_display = ShopWindow_display()
        self.shopwindow_display.updatePlayerData(player_data)
        # QtCore.QMetaObject.invokeMethod(self.shopwindow, "show", QtCore.Qt.QueuedConnection)
        self.shopwindow_display.show()
    

    def updateEvent(self, event):
        message = f'系统:{event}'
        self.textEdit.append(message)
        self.textEdit.verticalScrollBar().setValue(self.textEdit.verticalScrollBar().maximum())

    def updateChat(self, message):
        self.textEdit_2.append(message)
        self.textEdit_2.verticalScrollBar().setValue(self.textEdit_2.verticalScrollBar().maximum())

    def getPlayer1Data(self):
        player = self.pushButton.text()
        message = '/getPlayer' + player
        self.client_socket.send(self.sendPreprocess(message))


    def getPlayer2Data(self):
        player = self.pushButton_2.text()
        message = '/getPlayer' + player
        self.client_socket.send(self.sendPreprocess(message))


    def getPlayer3Data(self):
        player = self.pushButton_3.text()
        message = '/getPlayer' + player
        self.client_socket.send(self.sendPreprocess(message))
    

    def getPlayerMySelf(self):
        player = 'self'
        message = '/getPlayer' + player
        self.client_socket.send(self.sendPreprocess(message))
    

    def WhoseTurn(self,player):
        message = f'==={player} 的回合==='
        self.label_4.setText(message)
