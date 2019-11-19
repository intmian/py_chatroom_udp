from client.setting import SETTING, ADDR
from net_tool.SeniorNetIo import UDP_SENIOR_IO
import client.color_paint as cp
import hashlib


def cmd():
    help_()
    while True:
        c = input()
        if c[0] == "#":
            args = c.split()
            mode = args[0][1:]
            if mode == "help":
                help_()
            elif mode == "login":
                login(args[1],args[2])
            elif mode == "signup":
                sign_up(args[1],args[2],args[3])
            elif mode == "list":
                list_()
            elif mode == "logout":
                logout()
            elif mode == "quit":
                exit(0)
            else:
                cp.red_paint("未知指令")
        elif c[0] == "@":
            args = c.split()
            msg(args[1],args[0][1:])
        else:
            msg(c)



def help_():
    cp.blue_paint(
        """命令列表
帮助 #help
登录 #login account password
注册 #signup account password name
在线名单 #list
登出 #logout
退出 #quit
私信 @name message
公屏发言 message"""
    )


def login(acc, pwd):
    pwd = hashlib.new('sha256', pwd.encode('UTF-8')).hexdigest()
    UDP_SENIOR_IO.send_json(ADDR, {
        "mode": "login",
        "account": acc,
        "pwd": pwd
    })


def sign_up(acc, pwd, name):
    pwd = hashlib.new('sha256', pwd.encode('UTF-8')).hexdigest()
    UDP_SENIOR_IO.send_json(ADDR, {
        "mode": "signUp",
        "account": acc,
        "pwd": pwd,
        "name": name
    })


def list_():
    UDP_SENIOR_IO.send_json(ADDR, {
        "mode": "getList",
    })


def msg(msg, to="", ):
    UDP_SENIOR_IO.send_json(ADDR, {
        "mode": "msg",
        "msg": msg,
        "to": to
    })

def logout():
    UDP_SENIOR_IO.send_json(ADDR, {
        "mode": "logout",
    })
    UDP_SENIOR_IO.remove_cookie()