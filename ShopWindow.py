from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal


class ShopWindow(QWidget):

    dataSent = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi()
        

    def setupUi(self):
        self.setObjectName("Form")
        self.setWindowTitle('购买界面')
        self.resize(1041, 630)
        self.pushButton_11 = QtWidgets.QPushButton(self)
        self.pushButton_11.setGeometry(QtCore.QRect(560, 510, 101, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 10, 551, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_3.addWidget(self.pushButton_15)
        self.layoutWidget1 = QtWidgets.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 380, 551, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.layoutWidget2 = QtWidgets.QWidget(self)
        self.layoutWidget2.setGeometry(QtCore.QRect(160, 100, 511, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_5.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_5.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_5.addWidget(self.pushButton_20)
        self.layoutWidget3 = QtWidgets.QWidget(self)
        self.layoutWidget3.setGeometry(QtCore.QRect(140, 290, 551, 61))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.layoutWidget4 = QtWidgets.QWidget(self)
        self.layoutWidget4.setGeometry(QtCore.QRect(260, 200, 291, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_4.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_4.addWidget(self.pushButton_17)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        
        self.broadcastTower = QtWidgets.QLabel(self)
        self.broadcastTower.setFont(font)
        self.broadcastTower.setGeometry(QtCore.QRect(170, 70, 70, 20))
        self.broadcastTower.setObjectName("broadcastTower")
        
        self.amusementpark = QtWidgets.QLabel(self)
        self.amusementpark.setFont(font)
        self.amusementpark.setGeometry(QtCore.QRect(310, 70, 70, 21))
        self.amusementpark.setObjectName("amusementpark")
        
        self.shoppingmall = QtWidgets.QLabel(self)
        self.shoppingmall.setFont(font)
        self.shoppingmall.setGeometry(QtCore.QRect(450, 70, 70, 20))
        self.shoppingmall.setObjectName("shoppingmall")
        
        self.trainstation = QtWidgets.QLabel(self)
        self.trainstation.setFont(font)
        self.trainstation.setGeometry(QtCore.QRect(580, 70, 70, 21))
        self.trainstation.setObjectName("trainstation")
        
        self.commercial = QtWidgets.QLabel(self)
        self.commercial.setFont(font)
        self.commercial.setGeometry(QtCore.QRect(213, 162, 61, 20))
        self.commercial.setObjectName("commercial")
        
        self.tvstation = QtWidgets.QLabel(self)
        self.tvstation.setFont(font)
        self.tvstation.setGeometry(QtCore.QRect(383, 162, 61, 20))
        self.tvstation.setObjectName("tvstation")
        
        self.gym = QtWidgets.QLabel(self)
        self.gym.setFont(font)
        self.gym.setGeometry(QtCore.QRect(553, 162, 61, 20))
        self.gym.setObjectName("gym")
        
        self.westernres = QtWidgets.QLabel(self)
        self.westernres.setFont(font)
        self.westernres.setGeometry(QtCore.QRect(293, 251, 71, 31))
        self.westernres.setObjectName("westernres")
        
        self.cafe = QtWidgets.QLabel(self)
        self.cafe.setFont(font)
        self.cafe.setGeometry(QtCore.QRect(450, 250, 61, 21))
        self.cafe.setObjectName("cafe")
        
        self.fruitmall = QtWidgets.QLabel(self)
        self.fruitmall.setFont(font)
        self.fruitmall.setGeometry(QtCore.QRect(160, 350, 71, 31))
        self.fruitmall.setObjectName("fruitmall")
        
        self.bakery = QtWidgets.QLabel(self)
        self.bakery.setFont(font)
        self.bakery.setGeometry(QtCore.QRect(280, 350, 61, 21))
        self.bakery.setObjectName("bakery")
        
        self.grocery = QtWidgets.QLabel(self)
        self.grocery.setFont(font)
        self.grocery.setGeometry(QtCore.QRect(390, 350, 61, 21))
        self.grocery.setObjectName("grocery")
        
        self.cheesefac = QtWidgets.QLabel(self)
        self.cheesefac.setFont(font)
        self.cheesefac.setGeometry(QtCore.QRect(500, 350, 61, 20))
        self.cheesefac.setObjectName("cheesefac")
        
        self.furniturefac = QtWidgets.QLabel(self)
        self.furniturefac.setFont(font)
        self.furniturefac.setGeometry(QtCore.QRect(603, 351, 61, 21))
        self.furniturefac.setObjectName("furniturefac")
        
        self.mine = QtWidgets.QLabel(self)
        self.mine.setFont(font)
        self.mine.setGeometry(QtCore.QRect(170, 450, 71, 31))
        self.mine.setObjectName("mine")
        
        self.orchard = QtWidgets.QLabel(self)
        self.orchard.setFont(font)
        self.orchard.setGeometry(QtCore.QRect(280, 460, 61, 21))
        self.orchard.setObjectName("orchard")
        
        self.field = QtWidgets.QLabel(self)
        self.field.setFont(font)
        self.field.setGeometry(QtCore.QRect(380, 460, 61, 21))
        self.field.setObjectName("field")
        
        self.farm = QtWidgets.QLabel(self)
        self.farm.setFont(font)
        self.farm.setGeometry(QtCore.QRect(493, 452, 61, 20))
        self.farm.setObjectName("farm")
        
        self.forest = QtWidgets.QLabel(self)
        self.forest.setFont(font)
        self.forest.setGeometry(QtCore.QRect(610, 460, 61, 20))
        self.forest.setObjectName("forest")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 520, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(250, 520, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(360, 520, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(420, 520, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(710, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(820, 120, 180, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(610, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(730, 200, 291, 80))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(710, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(820, 310, 180, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.pushButton.clicked.connect(self.mineButton)
        self.pushButton_2.clicked.connect(self.orchardButton)
        self.pushButton_3.clicked.connect(self.fieldButton)
        self.pushButton_4.clicked.connect(self.farmButton)
        self.pushButton_5.clicked.connect(self.forestButton)
        self.pushButton_6.clicked.connect(self.fruitmallButton)
        self.pushButton_7.clicked.connect(self.bakeryButton)
        self.pushButton_8.clicked.connect(self.groceryButton)
        self.pushButton_9.clicked.connect(self.cheesefacButton)
        self.pushButton_10.clicked.connect(self.furniturefacButton)
        self.pushButton_11.clicked.connect(self.cancelButton)
        self.pushButton_12.clicked.connect(self.broadcastTowerButton)
        self.pushButton_13.clicked.connect(self.amusementparkButton)
        self.pushButton_14.clicked.connect(self.shoppingmallButton)
        self.pushButton_15.clicked.connect(self.trainstationButton)
        self.pushButton_16.clicked.connect(self.westernresButton)
        self.pushButton_17.clicked.connect(self.cafeButton)
        self.pushButton_18.clicked.connect(self.commercialButton)
        self.pushButton_19.clicked.connect(self.tvstationButton)
        self.pushButton_20.clicked.connect(self.gymButton)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.installEventFilter(self)
        self.pushButton_2.installEventFilter(self)
        self.pushButton_3.installEventFilter(self)
        self.pushButton_4.installEventFilter(self)
        self.pushButton_5.installEventFilter(self)
        self.pushButton_6.installEventFilter(self)
        self.pushButton_7.installEventFilter(self)
        self.pushButton_8.installEventFilter(self)
        self.pushButton_9.installEventFilter(self)
        self.pushButton_10.installEventFilter(self)
        self.pushButton_11.installEventFilter(self)
        self.pushButton_12.installEventFilter(self)
        self.pushButton_13.installEventFilter(self)
        self.pushButton_14.installEventFilter(self)
        self.pushButton_15.installEventFilter(self)
        self.pushButton_16.installEventFilter(self)
        self.pushButton_17.installEventFilter(self)
        self.pushButton_18.installEventFilter(self)
        self.pushButton_19.installEventFilter(self)
        self.pushButton_20.installEventFilter(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_11.setText(_translate("Form", "取消"))
        self.pushButton_12.setText(_translate("Form", "广播塔"))
        self.pushButton_13.setText(_translate("Form", "游乐园"))
        self.pushButton_14.setText(_translate("Form", "购物中心"))
        self.pushButton_15.setText(_translate("Form", "火车站"))
        self.pushButton.setText(_translate("Form", "矿场"))
        self.pushButton_2.setText(_translate("Form", "果园"))
        self.pushButton_3.setText(_translate("Form", "麦田"))
        self.pushButton_4.setText(_translate("Form", "农场"))
        self.pushButton_5.setText(_translate("Form", "林场"))
        self.pushButton_18.setText(_translate("Form", "商业中心"))
        self.pushButton_19.setText(_translate("Form", "电视台"))
        self.pushButton_20.setText(_translate("Form", "体育馆"))
        self.pushButton_6.setText(_translate("Form", "果蔬超市"))
        self.pushButton_7.setText(_translate("Form", "面包房"))
        self.pushButton_8.setText(_translate("Form", "便利店"))
        self.pushButton_9.setText(_translate("Form", "奶酪工厂"))
        self.pushButton_10.setText(_translate("Form", "家具工厂"))
        self.pushButton_16.setText(_translate("Form", "西餐厅"))
        self.pushButton_17.setText(_translate("Form", "咖啡馆"))
        self.broadcastTower.setText(_translate("Form", "TextLabel"))
        self.amusementpark.setText(_translate("Form", "TextLabel"))
        self.shoppingmall.setText(_translate("Form", "TextLabel"))
        self.trainstation.setText(_translate("Form", "TextLabel"))
        self.commercial.setText(_translate("Form", "TextLabel"))
        self.tvstation.setText(_translate("Form", "TextLabel"))
        self.gym.setText(_translate("Form", "TextLabel"))
        self.westernres.setText(_translate("Form", "TextLabel"))
        self.cafe.setText(_translate("Form", "TextLabel"))
        self.fruitmall.setText(_translate("Form", "TextLabel"))
        self.bakery.setText(_translate("Form", "TextLabel"))
        self.grocery.setText(_translate("Form", "TextLabel"))
        self.cheesefac.setText(_translate("Form", "TextLabel"))
        self.furniturefac.setText(_translate("Form", "TextLabel"))
        self.mine.setText(_translate("Form", "TextLabel"))
        self.orchard.setText(_translate("Form", "TextLabel"))
        self.field.setText(_translate("Form", "TextLabel"))
        self.farm.setText(_translate("Form", "TextLabel"))
        self.forest.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "玩家名字："))
        self.label_3.setText(_translate("Form", "金钱："))
        self.label_5.setText(_translate("Form", "触发点数"))
        self.label_7.setText(_translate("Form", "卡片说明"))
        self.label_9.setText(_translate("Form", "购买价格"))
        

    def updatePlayerData(self, json_data):
        replacement_dict = {
            0: '未激活',
            1: '已激活'
        }
        json_dataWhetheractivate = {k: replacement_dict.get(v, str(v)) for k, v in json_data.items()}
        json_data = {k: str(v) for k, v in json_data.items()}
        self.broadcastTower.setText(json_dataWhetheractivate['broadcastTower'])
        self.amusementpark.setText(json_dataWhetheractivate['amusementpark'])
        self.shoppingmall.setText(json_dataWhetheractivate['shoppingmall'])
        self.trainstation.setText(json_dataWhetheractivate['trainstation'])
        self.commercial.setText(json_data['commercial'])
        self.tvstation.setText(json_data['tvstation'])
        self.gym.setText(json_data['gym'])
        self.westernres.setText(json_data['westernres'])
        self.cafe.setText(json_data['cafe'])
        self.fruitmall.setText(json_data['fruitmall'])
        self.bakery.setText(json_data['bakery'])
        self.grocery.setText(json_data['grocery'])
        self.cheesefac.setText(json_data['cheesefac'])
        self.furniturefac.setText(json_data['furniturefac'])
        self.mine.setText(json_data['mine'])
        self.orchard.setText(json_data['orchard'])
        self.field.setText(json_data['field'])
        self.farm.setText(json_data['farm'])
        self.forest.setText(json_data['forest'])
        self.label_2.setText(json_data['name'])
        self.label_4.setText(json_data['money'])
    
    def broadcastTowerButton(self):
        message = '/buy' + 'broadcastTower'
        self.dataSent.emit(message)
        print(message)
    
    def amusementparkButton(self):
        message = '/buy' + 'amusementpark'
        self.dataSent.emit(message)
        print(message)

    def shoppingmallButton(self):
        message = '/buy' + 'shoppingmall'
        self.dataSent.emit(message)
        print(message)

    def trainstationButton(self):
        message = '/buy' + 'trainstation'
        self.dataSent.emit(message)
        print(message)

    def commercialButton(self):
        message = '/buy' + 'commercial'
        self.dataSent.emit(message)
        print(message)

    def tvstationButton(self):
        message = '/buy' + 'tvstation'
        self.dataSent.emit(message)
        print(message)

    def gymButton(self):
        message = '/buy' + 'gym'
        self.dataSent.emit(message)
        print(message)

    def westernresButton(self):
        message = '/buy' + 'westernres'
        self.dataSent.emit(message)
        print(message)

    def cafeButton(self):
        message = '/buy' + 'cafe'
        self.dataSent.emit(message)
        print(message)

    def fruitmallButton(self):
        message = '/buy' + 'fruitmall'
        self.dataSent.emit(message)
        print(message)

    def bakeryButton(self):
        message = '/buy' + 'bakery'
        self.dataSent.emit(message)
        print(message)

    def groceryButton(self):
        message = '/buy' + 'grocery'
        self.dataSent.emit(message)
        print(message)

    def cheesefacButton(self):
        message = '/buy' + 'cheesefac'
        self.dataSent.emit(message)
        print(message)

    def furniturefacButton(self):
        message = '/buy' + 'furniturefac'
        self.dataSent.emit(message)
        print(message)

    def mineButton(self):
        message = '/buy' + 'mine'
        self.dataSent.emit(message)
        print(message)

    def orchardButton(self):
        message = '/buy' + 'orchard'
        self.dataSent.emit(message)
        print(message)

    def fieldButton(self):
        message = '/buy' + 'field'
        self.dataSent.emit(message)
        print(message)

    def farmButton(self):
        message = '/buy' + 'farm'
        self.dataSent.emit(message)
        print(message)

    def forestButton(self):
        message = '/buy' + 'forest'
        self.dataSent.emit(message)
        print(message)

    def cancelButton(self):
        message = '/buy' + 'cancel'
        self.dataSent.emit(message)
        print(message)
    
    def eventFilter(self, source, event):
        if event.type() == event.Enter:
            if source == self.pushButton:
                self.label_6.setText("点数9")
                self.label_8.setText('所有玩家每拥有一个矿场就获得5金币')
                self.label_10.setText('6')
            elif source == self.pushButton_2:
                self.label_6.setText("点数10")
                self.label_8.setText('所有玩家每拥有一个果园就获得3金币')
                self.label_10.setText('3')
            elif source == self.pushButton_3:
                self.label_6.setText("点数1")
                self.label_8.setText('所有玩家每拥有一个麦田就获得1金币')
                self.label_10.setText('1')
            elif source == self.pushButton_4:
                self.label_6.setText("点数2")
                self.label_8.setText('所有玩家每拥有一个农场就获得1金币')
                self.label_10.setText('1')
            elif source == self.pushButton_5:
                self.label_6.setText("点数5")
                self.label_8.setText('所有玩家每拥有一个林场就获得1金币')
                self.label_10.setText('3')
            elif source == self.pushButton_6:
                self.label_6.setText("点数11或12")
                self.label_8.setText('当前掷骰子的玩家每拥有一个\n果园或麦田就获得2金币')
                self.label_10.setText('2')
            elif source == self.pushButton_7:
                self.label_6.setText("点数2或3")
                self.label_8.setText('当前掷骰子的玩家每拥有一间\n面包房就获得1金币')
                self.label_10.setText('1')
            elif source == self.pushButton_8:
                self.label_6.setText("点数4")
                self.label_8.setText('当前掷骰子的玩家每拥有一个\n便利店就获得3金币')
                self.label_10.setText('2')
            elif source == self.pushButton_9:
                self.label_6.setText("点数7")
                self.label_8.setText('当前掷骰子的玩家每拥有一个\n奶酪工厂就获得3金币')
                self.label_10.setText('5')
            elif source == self.pushButton_10:
                self.label_6.setText("点数8")
                self.label_8.setText('当前掷骰子的玩家每拥有一个\n家具工厂就获得3金币')
                self.label_10.setText('3')
            elif source == self.pushButton_11:
                self.label_6.setText("")
                self.label_8.setText('取消')
                self.label_10.setText('')
            elif source == self.pushButton_12:# 
                self.label_6.setText("增益卡牌，无触发点数")
                self.label_8.setText('当玩家拥有广播塔时，\n可自由选择是否重新掷骰')
                self.label_10.setText('22')
            elif source == self.pushButton_13:
                self.label_6.setText("增益卡牌，无触发点数")
                self.label_8.setText('当玩家拥有游乐园时，掷得的两个\n骰子点数相同，则下回合依旧是该玩家的回合')
                self.label_10.setText('16')
            elif source == self.pushButton_14:
                self.label_6.setText("增益卡牌，无触发点数")
                self.label_8.setText('当玩家拥有购物中心时，从‘西餐厅’‘咖啡馆’\n‘面包房’‘便利店’的收益均增加1金币')
                self.label_10.setText('10')
            elif source == self.pushButton_15:
                self.label_6.setText("增益卡牌，无触发点数")
                self.label_8.setText('当玩家拥有火车站时，可以自由选择掷1个或者2个骰子')
                self.label_10.setText('4')
            elif source == self.pushButton_16:
                self.label_6.setText("点数9或10")
                self.label_8.setText('玩家每拥有一家西餐厅就从\n掷到9或10的玩家那里收取2金币')
                self.label_10.setText('3')
            elif source == self.pushButton_17:
                self.label_6.setText("点数3")
                self.label_8.setText('玩家每拥有一家咖啡馆就从\n掷到3的玩家那里收取1金币')
                self.label_10.setText('2')
            # elif source == self.pushButton_18:
            #     self.label_6.setText("你悬浮在按钮 1 上了")
            #     self.label_8.setText('')
            #     self.label_10.setText('')
            # elif source == self.pushButton_19:
            #     self.label_6.setText("你悬浮在按钮 1 上了")
            #     self.label_8.setText('')
            #     self.label_10.setText('')
            elif source == self.pushButton_20:
                self.label_6.setText("点数6")
                self.label_8.setText('当前掷骰子的玩家从其他所有玩家那里每人收取2金币')
                self.label_10.setText('6')
        elif event.type() == event.Leave:
            if source in [self.pushButton,
                          self.pushButton_2,
                          self.pushButton_3,
                          self.pushButton_4,
                          self.pushButton_5,
                          self.pushButton_6,
                          self.pushButton_7,
                          self.pushButton_8,
                          self.pushButton_9,
                          self.pushButton_10,
                          self.pushButton_11,
                          self.pushButton_12,
                          self.pushButton_13,
                          self.pushButton_14,
                          self.pushButton_15,
                          self.pushButton_16,
                          self.pushButton_17,
                          self.pushButton_18,
                          self.pushButton_19,
                          self.pushButton_20]:
                self.label_6.setText('')
                self.label_8.setText("悬浮鼠标查看卡牌明细")
                self.label_10.setText('')

        return super().eventFilter(source, event)


