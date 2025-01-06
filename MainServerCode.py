"""
Copyright (c) 2025 Zequan Wang

This project is a digital implementation inspired by the original tabletop game "Dice Street".
All rights reserved. Redistribution or modification for commercial purposes is prohibited.

Licensed under Creative Commons Attribution-NonCommercial 4.0 International License.
http://creativecommons.org/licenses/by-nc/4.0/
"""


import socket
import threading
import random
import time
# import pandas as pd
# import sys
import struct
import json
from datetime import datetime

def sendPreprocess(item):
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


def recvPreprocess(client_socket):

    header = client_socket.recv(4)

    if not header:
        return -1
    
    item_length = struct.unpack('!I', header)[0]
    item = client_socket.recv(item_length)
    return item


def send_info(client_socket, info):
    client_socket.send(sendPreprocess(info))


clients = []
clients_name = []
player_list = []
class Player:
    def __init__(self, name, farm=0, bakery=1, forest=0, field=1, orchard=0, miningSite=0, fruitMall=0, grocery=0, cheeseFac=0, furnitureFac=0, TVStation=0, gym=0, commercialCenter=0, westernRes=0, cafe=0, broadcastTower=False, trainStation=False, shoppingMall=False, amusementPark=False, money=5):
        self.name = name

        self.farm = farm
        self.bakery = bakery
        self.forest = forest
        self.field = field
        self.orchard = orchard
        self.miningSite = miningSite

        self.fruitMall = fruitMall
        self.grocery = grocery
        self.cheeseFac = cheeseFac
        self.furnitureFac = furnitureFac
        self.TVStation = TVStation
        self.gym = gym
        self.commercialCenter = commercialCenter
        self.westernRes = westernRes
        self.cafe = cafe

        self.broadcastTower = broadcastTower
        self.trainStation = trainStation
        self.shoppingMall = shoppingMall
        self.amusementPark = amusementPark

        self.money = money


    def buy_farm(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 1:
            self.money -= 1
            self.farm += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 农场 ，ta现在有 {self.farm} 个农场')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买农场，农场需要 1 金钱")
    
    def buy_bakery(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 1:
            self.money -= 1
            self.bakery += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 面包店 ，ta现在有 {self.bakery} 个面包店')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买面包店，面包店需要 1 金钱")
    
    def buy_forest(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 3:
            self.money -= 3
            self.forest += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 森林 ，ta现在有 {self.forest} 个林场')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买森林，森林需要 3 金钱")

    def buy_field(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 1:
            self.money -= 1
            self.field += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 农田 ，ta现在有 {self.field} 个农田!')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买农田，农田需要 1 金钱")
    
    def buy_orchard(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 3:
            self.money -= 3
            self.orchard += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 果园 ，ta现在有 {self.orchard} 个果园')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买果园，果园需要 3 金钱")

    def buy_miningSite(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 6:
            self.money -= 6
            self.miningSite += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 矿山 ，ta现在有 {self.miningSite} 个矿山')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买矿山，矿山需要 6 金钱")

    def buy_fruitMall(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 2:
            self.money -= 2
            self.fruitMall += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 水果商场 ，ta现在有 {self.fruitMall} 个水果商场')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买水果商场，水果商场需要 2 金钱")

    def buy_grocery(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 2:
            self.money -= 2
            self.grocery += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 杂货店 ，ta现在有 {self.grocery} 个杂货店')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买杂货店，杂货店需要 2 金钱")

    def buy_cheeseFac(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 5:
            self.money -= 5
            self.cheeseFac += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 奶酪工厂 ，ta现在有 {self.cheeseFac} 个奶酪工厂')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买奶酪工厂，奶酪工厂需要 5 金钱")

    def buy_furnitureFac(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 3:
            self.money -= 3
            self.furnitureFac += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 家具工厂 ，ta现在有 {self.furnitureFac} 个家具工厂')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买家具工厂，家具工厂需要 3 金钱")

    def buy_TVStation(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 7:
            self.money -= 7
            self.TVStation += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 电视台 ，ta现在有 {self.TVStation} 个电视台')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买电视台，电视台需要 7 金钱")
    
    def buy_commercialCenter(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 8:
            self.money -= 8
            self.commercialCenter += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 商业中心 ，ta现在有 {self.commercialCenter} 个商业中心')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买商业中心，商业中心需要 8 金钱")

    def buy_cafe(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 2:
            self.money -= 2
            self.cafe += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 咖啡馆 ，ta现在有 {self.cafe} 个咖啡馆')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买咖啡馆，咖啡馆需要 2 金钱")
    
    def buy_westernRes(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 3:
            self.money -= 3
            self.westernRes += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 西餐厅 ，ta现在有 {self.westernRes} 个西餐厅')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买西餐厅，西餐厅需要 3 金钱")
    
    def buy_gym(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 6:
            self.money -= 6
            self.gym += 1
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 健身房 ，ta现在有 {self.gym} 个健身房')
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买健身房，健身房需要 6 金钱")

    def buy_broadcastTower(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 22:
            if self.broadcastTower == False:
                self.money -= 22
                self.broadcastTower = True
                broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 广播塔 ，ta的广播塔现在已经 激活！')
            else:
                send_info(current_socket, f"/event你已经有一个广播塔了")
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买广播塔，广播塔需要 22 金钱")

    def buy_trainStation(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 4:
            if self.trainStation == False:
                self.money -= 4
                self.trainStation = True
                broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 火车站 ，ta的火车站现在已经 激活！')
                send_info(current_socket, '/rollTwoPermission')
            else:
                send_info(current_socket, f"/event你已经有一个火车站了")
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买火车站，火车站需要 4 金钱")

    def buy_shoppingMall(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 10:
            if self.shoppingMall == False:
                self.money -= 10
                self.shoppingMall = True
                broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 购物中心 ，ta的购物中心现在已经 激活！')
            else:
                send_info(current_socket, f"/event你已经有一个购物中心了")
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买购物中心，购物中心需要 10 金钱")

    def buy_amusementPark(self):
        current_socket = clients[turnNum % maxPlayers]
        if self.money >= 16:
            if self.amusementPark == False:
                self.money -= 16
                self.amusementPark = True
                broadcastMessage(f'{player_list[turnNum % maxPlayers].name}购买了一个 游乐场 ，ta的游乐场现在已经 激活！')
            else:
                send_info(current_socket, f"/event你已经有一个游乐场了")
        else:
            send_info(current_socket, f"/event你没有足够的钱来购买游乐场，游乐场需要 16 金钱")


    def __str__(self):
        data = {'broadcastTower': self.broadcastTower,
                'amusementpark': self.amusementPark,
                'shoppingmall': self.shoppingMall,
                'trainstation': self.trainStation,
                'commercial': self.commercialCenter,
                'tvstation': self.TVStation,
                'gym': self.gym,
                'westernres': self.westernRes,
                'cafe': self.cafe,
                'fruitmall': self.fruitMall,
                'bakery': self.bakery,
                'grocery': self.grocery,
                'cheesefac': self.cheeseFac,
                'furniturefac': self.furnitureFac,
                'mine': self.miningSite,
                'orchard': self.orchard,
                'field': self.field,
                'farm': self.farm,
                'forest': self.forest,
                'money': self.money,
                'name': self.name
                }
        
        return data
        
        # df = pd.DataFrame(data)
        
        # result = f"{self.name}的设施统计：\n"
        
        # result += df.to_string(index=False)
        
        # return result


playerxx = Player('example')
i = 0

def ChatBroadcastMessage(message):
    for client in clients:
        send_info(client, message)


def broadcastMessage(message):
    message = '/event' + message
    for client in clients:
        send_info(client, message)

def broadcastMessageHeadLight(message):
    message = '/turn' + message
    for client in clients:
        send_info(client, message)


def broadcast_join(name):
    for client in clients:
        send_info(client, f"/event{name}上线了")
        send_info(client, f'/event在线玩家：{clients_name}')


def server():
    global clients, clients_name, turnNum, player_list, maxPlayers
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    server_socket.bind((ip, 8888))
    server_socket.listen(5)

    print("服务器启动，等待连接...")
    print(ip)

    onlines = 0
    maxPlayers = 4
    
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        name = recvPreprocess(client_socket).decode('utf-8')
        print(name)
        clients_name.append(name)
        print(f"有用户连接：{name}")
        broadcast_join(name)
        print(f'在线用户：{clients_name}')
        print(client_address, "连接成功")
        onlines += 1
        if onlines == maxPlayers:
            break
        send_info(client_socket, f"/event欢迎来到游戏，你的名字是{name}, 请等待其他玩家加入游戏")

    for i in range(onlines):
        player_list.append(Player(clients_name[i]))
    for each in clients:
        other_player = [x for x in clients_name if x != player_list[clients.index(each)].name]
        send_info(each, f"/playerlist{other_player}")
    Player_quit = False
    

    def efarm():
        for player in player_list:
            before_balance = player.money
            player.money += player.farm * 1
            after_balance = player.money
            broadcastMessage(f"事件处理完成，玩家{player.name}获得{after_balance-before_balance}金钱")
            time.sleep(1)

    def efield():
        for player in player_list:
            before_balance = player.money
            player.money += player.field * 1
            after_balance = player.money
            broadcastMessage(f"麦田事件处理完成，玩家{player.name}获得{after_balance-before_balance}金钱")
            time.sleep(1)

    def eorchard():
        for player in player_list:
            before_balance = player.money
            player.money += player.orchard * 3
            after_balance = player.money
            broadcastMessage(f"果园事件处理完成，玩家{player.name}获得{after_balance-before_balance}金钱")
            time.sleep(1)

    def eminingSite():
        for player in player_list:
            before_balance = player.money
            player.money += player.miningSite * 5
            after_balance = player.money
            broadcastMessage(f"矿场事件处理完成，玩家{player.name}获得{after_balance-before_balance}金钱")
            time.sleep(1)

    def eforest():
        for player in player_list:
            before_balance = player.money
            player.money += player.forest * 1
            after_balance = player.money
            broadcastMessage(f"森林事件处理完成，玩家{player.name}获得{after_balance-before_balance}金钱")
            time.sleep(1)

    def ebakery():
        if player_list[turnNum % maxPlayers].shoppingMall == 0:
            before_balance = player_list[turnNum % maxPlayers].money
            player_list[turnNum % maxPlayers].money += player_list[turnNum % maxPlayers].bakery * 1
            after_balance = player_list[turnNum % maxPlayers].money
            broadcastMessage(f'面包房事件处理完成，玩家{player_list[turnNum % maxPlayers].name}获得{after_balance - before_balance}金钱')
            time.sleep(0.1)
        else:
            before_balance = player_list[turnNum % maxPlayers].money
            player_list[turnNum % maxPlayers].money += player_list[turnNum % maxPlayers].bakery * 2
            after_balance = player_list[turnNum % maxPlayers].money
            broadcastMessage(f'面包房事件处理完成，玩家{player_list[turnNum % maxPlayers].name}获得{after_balance - before_balance}金钱')
            time.sleep(0.1)

    def efurnitureFac():
        before_balance = player_list[turnNum % maxPlayers].money
        player_list[turnNum % maxPlayers].money += (player_list[turnNum % maxPlayers].forest + player_list[turnNum % maxPlayers].miningSite) * player_list[turnNum % maxPlayers].furnitureFac * 3
        after_balance = player_list[turnNum % maxPlayers].money
        broadcastMessage(f'家具厂事件处理完成，玩家{player_list[turnNum % maxPlayers].name}获得{after_balance - before_balance}金钱')
        time.sleep(0.1)

    def echeeseFac():
        before_balance = player_list[turnNum % maxPlayers].money
        player_list[turnNum % maxPlayers].money += player_list[turnNum % maxPlayers].farm * player_list[turnNum % maxPlayers].cheeseFac * 3
        after_balance = player_list[turnNum % maxPlayers].money
        broadcastMessage(f'奶酪厂事件处理完成，玩家{player_list[turnNum % maxPlayers].name}获得{after_balance - before_balance}金钱')
        time.sleep(0.1)

    def egrocery():
        if player_list[turnNum % maxPlayers].shoppingMall == 0:
            before_balance = player_list[turnNum % maxPlayers].money
            player_list[turnNum % maxPlayers].money += player_list[turnNum % maxPlayers].grocery * 3
            after_balance = player_list[turnNum % maxPlayers].money
            broadcastMessage(f'便利店事件处理完成，玩家{player_list[turnNum % maxPlayers].name}获得{after_balance - before_balance}金钱')
            time.sleep(0.1)
        else:
            before_balance = player_list[turnNum % maxPlayers].money
            player_list[turnNum % maxPlayers].money += player_list[turnNum % maxPlayers].grocery * 4
            after_balance = player_list[turnNum % maxPlayers].money
            broadcastMessage(f'便利店事件处理完成，玩家{player_list[turnNum % maxPlayers].name}获得{after_balance - before_balance}金钱')
            time.sleep(0.1)

    def efruitMall():
        before_balance = player_list[turnNum % maxPlayers].money
        player_list[turnNum % maxPlayers].money += (player_list[turnNum % maxPlayers].orchard + player_list[turnNum % maxPlayers].field) * player_list[turnNum % maxPlayers].fruitMall * 2
        after_balance = player_list[turnNum % maxPlayers].money
        broadcastMessage(f'水果店事件处理完成，玩家{player_list[turnNum % maxPlayers].name}获得{after_balance - before_balance}金钱')
        time.sleep(0.1)

    def ecafe():
        for player in player_list:
            if player.shoppingMall == 0:
                if player.cafe > player_list[turnNum % maxPlayers].money:
                    before_balance = player.money
                    player.money += player_list[turnNum % maxPlayers].money
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money = 0
                    broadcastMessage(f'咖啡馆事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers]}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)
                    broadcastMessage(f'玩家{player_list[turnNum % maxPlayers].name}没钱了！')
                    time.sleep(0.1)

                else:
                    before_balance = player.money
                    player.money += player.cafe * 1
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money -= player.cafe
                    broadcastMessage(f'咖啡馆事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers].name}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)
            else:
                if player.cafe * 2 > player_list[turnNum % maxPlayers].money:
                    before_balance = player.money
                    player.money += player_list[turnNum % maxPlayers].money
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money = 0
                    broadcastMessage(f'咖啡馆事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers]}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)
                    broadcastMessage(f'玩家{player_list[turnNum % maxPlayers].name}没钱了！')
                    time.sleep(0.1)

                else:
                    before_balance = player.money
                    player.money += player.cafe * 2
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money -= player.cafe * 2
                    broadcastMessage(f'咖啡馆事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers].name}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)

    def ewesternRes():
        for player in player_list:
            if player.shoppingMall == 0:
                if player.westernRes * 2 > player_list[turnNum % maxPlayers].money:
                    before_balance = player.money
                    player.money += player_list[turnNum % maxPlayers].money
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money = 0
                    broadcastMessage(f'西部餐厅事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers].name}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)
                    broadcastMessage(f'玩家{player_list[turnNum % maxPlayers].name}没钱了！')
                    time.sleep(0.1)
                else:
                    before_balance = player.money
                    player.money += player.westernRes * 2
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money -= player.westernRes * 2
                    broadcastMessage(f'西部餐厅事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers].name}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)
            else:
                if player.westernRes * 3 > player_list[turnNum % maxPlayers].money:
                    before_balance = player.money
                    player.money += player_list[turnNum % maxPlayers].money
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money = 0
                    broadcastMessage(f'西部餐厅事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers].name}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)
                    broadcastMessage(f'玩家{player_list[turnNum % maxPlayers].name}没钱了！')
                    time.sleep(0.1)
                else:
                    before_balance = player.money
                    player.money += player.westernRes * 3
                    after_balance = player.money
                    player_list[turnNum % maxPlayers].money -= player.westernRes * 3
                    broadcastMessage(f'西部餐厅事件处理完成，玩家{player.name}向{player_list[turnNum % maxPlayers].name}收取了{after_balance - before_balance}金钱')
                    time.sleep(0.1)

    def egym():
        for player in player_list:
            if player_list[turnNum % maxPlayers].gym * 2 > player.money:
                before_balance = player_list[turnNum % maxPlayers].money
                player_list[turnNum % maxPlayers].money += player.money
                after_balance = player_list[turnNum % maxPlayers].money
                player.money = 0
                broadcastMessage(f'健身房事件处理完成，玩家{player_list[turnNum % maxPlayers].name}向{player.name}收取了{after_balance - before_balance}金钱')
                time.sleep(0.1)
                broadcastMessage(f'玩家{player.name}没钱了！')
                time.sleep(0.1)
                
            else:
                before_balance = player_list[turnNum % maxPlayers].money
                player_list[turnNum % maxPlayers].money += player_list[turnNum % maxPlayers].gym * 2
                after_balance = player_list[turnNum % maxPlayers].money
                player.money -= player_list[turnNum % maxPlayers].gym * 2
                broadcastMessage(f'健身房事件处理完成，玩家{player_list[turnNum % maxPlayers].name}向{player.name}收取了{after_balance - before_balance}金钱')
                time.sleep(0.1)

    def eTVStation():
        while True:
            time.sleep(0.1)
            broadcastMessage(f"广播电视塔触发: 玩家{player_list[turnNum % maxPlayers].name}正在进行偷取金钱...")
            time.sleep(0.1)
            clients[turnNum % maxPlayers].send(f'你的电视广播塔卡牌触发了，请选择你要偷取金钱的玩家，输入/表示该回合不使用此事件'.encode('utf-8'))
            target_player = clients[turnNum % maxPlayers].recv(1024).decode('utf-8')
            if target_player != '/':
                if target_player in player_list:
                    before_balance = player_list[turnNum % maxPlayers].money
                    target_player.money -= player_list[turnNum % maxPlayers].TVStation * 5
                    if target_player.money < 0:
                        target_player.money = 0
                        after_balance = player_list[turnNum % maxPlayers].money
                        player_list[turnNum % maxPlayers].money += target_player.money
                        broadcastMessage(f"广播电视塔事件处理完成，玩家{player_list[turnNum % maxPlayers].name}偷取了{target_player.name}的{after_balance - before_balance}金钱")
                        time.sleep(0.1)
                        broadcastMessage(f'玩家{target_player.name}没钱了！')
                        time.sleep(0.1)
                    else:
                        player_list[turnNum % maxPlayers].money += player_list[turnNum % maxPlayers].TVStation * 5
                        after_balance = player_list[turnNum % maxPlayers].money
                        broadcastMessage(f"广播电视塔事件处理完成，玩家{player_list[turnNum % maxPlayers].name}偷取了{target_player.name}的{after_balance - before_balance}金钱")
                        time.sleep(0.1)
                    break
                else:
                    clients[turnNum % maxPlayers].send("请输入正确的玩家名".encode('utf-8'))
                    continue
            else:
                broadcastMessage("广播电视塔事件未被使用")

    def ecommercialCenter():
        cant_be_exchange_card = ['commercialCenter',
                                'TVStation',
                                'gym',
                                'broadcastTower',
                                'amusementPark',
                                'shoppingMall',
                                'trainStation']
        while True:
            broadcastMessage(f"商业中心触发: 玩家{player_list[turnNum % maxPlayers].name}正在进行交换...")
            clients[turnNum % maxPlayers].send(f'你的商业中心卡牌触发了，请选择你要交换卡牌的玩家'.encode('utf-8'))
            target_player = input('Enter the name of the player you want to exchange from, or input \'/\' to mean that you don\'t want to use this for now: ')
            if target_player != '/':
                if target_player in player_list:
                    broadcastMessage(target_player)
                    broadcastMessage('-----------------------------------------------')
                    target_card = input('Enter the name of the card you want to exchange, or input \'/\' to mean that you don\'t want to use this for now: ')
                    if target_card != '/':
                        if target_card in target_player.__dict__:
                            if target_card not in cant_be_exchange_card:
                                src_card = input('Enter the name of the card you want to exchange with, or input \'/\' to mean that you don\'t want to use this for now: ')
                                if src_card != '/':
                                    if src_card in player_list[turnNum % maxPlayers].__dict__:
                                        if player_list[turnNum % maxPlayers].__dict__[src_card] > 0:
                                            player_list[turnNum % maxPlayers].__dict__[target_card] += 1
                                            player_list[turnNum % maxPlayers].__dict__[src_card] -= 1
                                            target_player.__dict__[target_card] -= 1
                                            target_player.__dict__[src_card] += 1
                                            broadcastMessage(f"Commercial Center event: {player_list[turnNum % maxPlayers].name} exchanged {src_card} with {target_card} from {target_player.name}.")
                                            break
                                    else:
                                        broadcastMessage("Invalid card name. Please try again.")
                                else:
                                    broadcastMessage('Commercial Center event not used.')
                                    break
                            else:
                                broadcastMessage("You can't exchange this card.")
                        else:
                            broadcastMessage("Invalid card name. Please try again.")
                    else:
                        broadcastMessage('Commercial Center event not used.')
                        break
                else:
                    broadcastMessage("Invalid player name. Please try again.")
            else:
                broadcastMessage('Commercial Center event not used.')
                break

    def buy(buy_command):
        if buy_command == 'field':
            player_list[turnNum % maxPlayers].buy_field()
        elif buy_command == 'farm':
            player_list[turnNum % maxPlayers].buy_farm()
        elif buy_command == 'cafe':
            player_list[turnNum % maxPlayers].buy_cafe()
        elif buy_command == 'grocery':
            player_list[turnNum % maxPlayers].buy_grocery()
        elif buy_command == 'forest':
            player_list[turnNum % maxPlayers].buy_forest()
        elif buy_command == 'gym':
            player_list[turnNum % maxPlayers].buy_gym()
        elif buy_command == 'cheesefac':
            player_list[turnNum % maxPlayers].buy_cheeseFac()
        elif buy_command == 'furniturefac':
            player_list[turnNum % maxPlayers].buy_furnitureFac()
        elif buy_command == 'mine':
            player_list[turnNum % maxPlayers].buy_miningSite()
        elif buy_command == 'westernres':
            player_list[turnNum % maxPlayers].buy_westernRes()
        elif buy_command == 'orchard':
            player_list[turnNum % maxPlayers].buy_orchard()
        elif buy_command == 'fruitmall':
            player_list[turnNum % maxPlayers].buy_fruitMall()
        elif buy_command == 'trainstation':
            player_list[turnNum % maxPlayers].buy_trainStation()
        elif buy_command == 'broadcastTower':
            print('啊啊啊啊啊')
            player_list[turnNum % maxPlayers].buy_broadcastTower()
        elif buy_command == 'shoppingmall':
            player_list[turnNum % maxPlayers].buy_shoppingMall()
        elif buy_command == 'amusementpark':
            player_list[turnNum % maxPlayers].buy_amusementPark()
        elif buy_command == 'tvstation':
            player_list[turnNum % maxPlayers].buy_TVStation()
        elif buy_command == 'commercial':
            player_list[turnNum % maxPlayers].buy_commercialCenter()
        elif buy_command == 'bakery':
            player_list[turnNum % maxPlayers].buy_bakery()
        elif buy_command == 'cancel':
            return -1
        

    event_number = {'1': [efield],
                    '2': [efarm, ebakery],
                    '3': [ebakery, ecafe,],
                    '4': [egrocery],
                    '5': [eforest],
                    '6': [egym],
                    '7': [echeeseFac],
                    '8': [efurnitureFac],
                    '9': [eminingSite, ewesternRes],
                    '10': [ewesternRes, eorchard],
                    '11': [efruitMall],
                    '12': [efruitMall]}
    
    
    turnNum = 0
    threads = []


    def dailyProcess(response):
        if response.decode('utf-8').startswith('/getPlayer'):
            player = response.decode('utf-8')[10:]
            if player == 'self':
                player = player_list[turnNum % maxPlayers].name
            for i in player_list:
                if i.name == player:
                    message = '/playerdata' + json.dumps(i.__str__())
                    send_info(current_player, message)

        if response.decode('utf-8').startswith('/chat'):
            message = response.decode('utf-8')[5:]
            Whosaid = player_list[turnNum % maxPlayers].name
            theTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f'/chat{theTime} {Whosaid} : {message}'
            print(f'转发聊天{message}')
            ChatBroadcastMessage(message)

    
    def dailyProcessNotMainCharacter(response, client_socket):
        if response.decode('utf-8').startswith('/getPlayer'):
            player = response.decode('utf-8')[10:]
            if player == 'self':
                player = player_list[clients.index(client_socket)].name
            for i in player_list:
                if i.name == player:
                    message = '/playerdata' + json.dumps(i.__str__())
                    send_info(current_player, message)

        if response.decode('utf-8').startswith('/chat'):
            message = response.decode('utf-8')[5:]
            Whosaid = player_list[clients.index(client_socket)].name
            theTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f'/chat{theTime} {Whosaid} : {message}'
            print(f'转发聊天{message}')
            ChatBroadcastMessage(message)
    

    def throw_one_dice():
        global total_num, amusementPark_event
        amusementPark_event = False
        dice1 = random.randint(1,6)
        total_num = dice1
        broadcastMessage(f'{player_list[turnNum % maxPlayers].name} 掷出了 {dice1} !')
        broadcastMessage(f' {player_list[turnNum % maxPlayers].name} 总共掷出了 {total_num} !')

    
    def throw_two_dice():
        global total_num, dice1, dice2, amusementPark_event
        amusementPark_event = False
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total_num = dice1 + dice2
        broadcastMessage(f'{player_list[turnNum % maxPlayers].name} 掷出了 {dice1} 和 {dice2} !')
        time.sleep(0.5)
        broadcastMessage(f' {player_list[turnNum % maxPlayers].name} 总共掷出了 {total_num} !')


    while True:
        amusementPark_event = False
        print(clients)
        print(len(clients))
        stop_event = threading.Event()

        def handle_client(client_socket):
            time.sleep(1.5)
            send_info(client_socket, '/event现在不是你的回合，但你可以点击玩家的按钮来查看他们的背包')
            client_socket.setblocking(False)
            while not stop_event.is_set():
                try:
                    message = recvPreprocess(client_socket)
                    if message:
                        dailyProcessNotMainCharacter(message, client_socket)

                    if message.decode('utf-8') == '/throw_dice':
                        send_info(client_socket, '/event尚未到你的回合')

                    if message.decode('utf-8') == '/throw_dice2':
                        send_info(client_socket, '/event尚未到你的回合')

                    if message.decode('utf-8').startswith('/buy'):
                        send_info(client_socket, '/event尚未到你的回合')

                except BlockingIOError:
                    continue

        for i in range(len(clients)):
            if clients[i] == clients[turnNum % maxPlayers]:
                continue
            thread = threading.Thread(target=handle_client, args=(clients[i],))
            threads.append(thread)
            thread.start()
            print(f'玩家{player_list[i].name} 已进入输入控制')

        clients[turnNum % maxPlayers].setblocking(True)
        broadcastMessage(f'轮到 {player_list[turnNum % maxPlayers].name} 了')
        broadcastMessage(f'请 {player_list[turnNum % maxPlayers].name} 掷骰子')
        broadcastMessageHeadLight(player_list[turnNum % maxPlayers].name)
        time.sleep(0.5)

        current_player = clients[turnNum % maxPlayers]
        if not player_list[turnNum % maxPlayers].trainStation:
            send_info(current_player, f'/event请你掷骰子')
            while True:
                dice_command = recvPreprocess(current_player)
                if dice_command == -1:
                    broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 退出了游戏')
                    Player_quit = True
                    break
                elif dice_command:
                    if dice_command.decode('utf-8') == '/throw_dice':
                        throw_one_dice()
                        break
                    dailyProcess(dice_command)
            if Player_quit:
                break

        else:
            send_info(current_player, f'/event请你掷骰子')
            send_info(current_player, '/event因为你有火车站，你可以自由选择掷1个或者2个骰子')
            while True:
                dice_command = recvPreprocess(current_player)
                if dice_command == -1:
                    broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 退出了游戏')
                    Player_quit = True
                    break
                elif dice_command:
                    if dice_command.decode('utf-8') == '/throw_dice':
                        throw_one_dice()
                        break
                    elif dice_command.decode('utf-8') == '/throw_dice2':
                        throw_two_dice()
                        if dice1 == dice2:
                            amusementPark_event = True
                        break
                    dailyProcess(dice_command)
            if Player_quit == True:
                break


        if player_list[turnNum % maxPlayers].broadcastTower == True:
            send_info(current_player, '/event因为你有广播塔，你可以重新掷一次骰子也可以选择本次不掷')
            send_info(current_player, '/raiseThrowConfirmWindow')
            while True:
                dice_command = recvPreprocess(current_player)
                if dice_command == -1:
                    broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 退出了游戏')
                    Player_quit = True
                    break

                if dice_command.decode('utf-8') == '/chooseThrowTwice':
                    broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 有了广播塔，可以重新掷骰子')
                    if not player_list[turnNum % maxPlayers].trainStation:
                        send_info(current_player, f'请你掷骰子')
                        while True:
                            dice_command = recvPreprocess(current_player)
                            if dice_command == -1:
                                broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 退出了游戏')
                                Player_quit = True
                                break
                            elif dice_command:
                                if dice_command.decode('utf-8') == '/throw_dice':
                                    throw_one_dice()
                                    break
                                dailyProcess(dice_command)
                        # if Player_quit:
                        break

                    else:
                        send_info(current_player, f'/event请你掷骰子')
                        send_info(current_player, '/event因为你有火车站，你可以自由选择掷1个或者2个骰子')
                        while True:
                            dice_command = recvPreprocess(current_player)
                            if dice_command == -1:
                                broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 退出了游戏')
                                Player_quit = True
                                break
                            elif dice_command:
                                if dice_command.decode('utf-8') == '/throw_dice':
                                    throw_one_dice()
                                    break

                                elif dice_command.decode('utf-8') == '/throw_dice2':
                                    throw_two_dice()
                                    amusementPark_event = True
                                    break
                                
                                dailyProcess(dice_command)

                        # if Player_quit:
                        break

                elif dice_command.decode('utf-8') == '/chooseNotThrowTwice':
                    broadcastMessage(f'{player_list[turnNum % maxPlayers].name} 选择不掷第二次')
                    time.sleep(0.5)
                    break

                dailyProcess(dice_command)

            if Player_quit:
                break

        
        for func in event_number[str(total_num)]:
            broadcastMessage(f'{func.__name__} 事件触发！!')
            func()
            time.sleep(1)
        


        buyPlayer_info = json.dumps(player_list[turnNum % maxPlayers].__str__())
        
        # send_info(current_player, '是否需要购买什么？')
        send_info(current_player, f'/raiseClientShopWindow{buyPlayer_info}')
        print('已发出唤出商店窗口指令')

        while True:
            buy_command = recvPreprocess(current_player)
            if buy_command == -1:
                broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 退出了游戏')
                Player_quit = True
                break
            elif buy_command:
                # print(f'{buy_command.decode('utf-8')}-814')
                
                dailyProcess(buy_command)

                buy_command = buy_command.decode('utf-8')

                if buy_command.startswith('/buy'):
                    target = buy_command[4:]
                    print(f'{target}-822')
                    before_money = player_list[turnNum % maxPlayers].money
                    buy_result = buy(target)
                    if buy_result == -1:
                        broadcastMessage(f'玩家 {player_list[turnNum % maxPlayers].name} 取消了购买')
                        broadcastMessage(f'{player_list[turnNum % maxPlayers].name}的账户余额是${player_list[turnNum % maxPlayers].money}！')
                        break
                    after_money = player_list[turnNum % maxPlayers].money

                    if before_money == after_money:
                        send_info(current_player, f'/raiseClientShopWindow{buyPlayer_info}')
                        continue
                    else:
                        break

        if Player_quit == True:                
            break

        build_list = [player_list[turnNum % maxPlayers].broadcastTower, player_list[turnNum % maxPlayers].trainStation, player_list[turnNum % maxPlayers].shoppingMall, player_list[turnNum % maxPlayers].amusementPark]
        if all(build_list):
            broadcastMessage(f'所有建筑建成，游戏结束')
            broadcastMessage(f'{player_list[turnNum % maxPlayers].name}赢得了这场游戏!')
            break

        if not amusementPark_event:
            turnNum += 1
        elif player_list[turnNum % maxPlayers].amusementPark:
            broadcastMessage(f'因为玩家{player_list[turnNum % maxPlayers].name}在当前回合的最终掷出点数一样，且他拥有游乐场卡牌，所以下回合依旧是该玩家的回合')
            turnNum += maxPlayers
            time.sleep(3)

        stop_event.set()

        for thread in threads:
            thread.join()

    
if __name__ == '__main__':
    server()


        
        
