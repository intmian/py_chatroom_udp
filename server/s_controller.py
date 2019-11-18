# Callable[Tuple[str, int], Dict[str, Any]
from server.model.cache import ACCOUNT, CACHE, OnlineList
from net_tool.SeniorNetIo import UDP_SENIOR_IO
from typing import *


def verify_cookie(cookie: bytes) -> tuple[bool, Any]:
    """
    :param cookie:
    :return: if_success, user_name
    """
    o: OnlineList = CACHE["onlineList"]
    if cookie in o.sessions:
        return True, o.sessions[cookie]
    else:
        return False, None


def test(addr, args):
    print("from ", addr)
    print(args)


def sign_up(addr, args):
    suc = ACCOUNT.new_user(args["account"], args["pwd"], args["name"])
    if suc:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replySighUp",
            "type": True,
            "hit": ""
        })
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replySighUp",
            "type": False,
            "hit": "账号名或用户名重复"
        })


def login(addr, args):
    name, hash_d = ACCOUNT.get_user(args["account"])
    if hash_d == args["pwd"]:
        o: OnlineList = CACHE["onlineList"]
        cookie = o.add_user(name)
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogin",
            "success": True,
            "cookie": cookie
        })
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogin",
            "success": False,
            "cookie": ""
        })


def get_list(addr, args):
    cookie = args["cookie"]
    flag, name = verify_cookie(cookie)
    o: OnlineList = CACHE["onlineList"]
    if flag:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyList",
            "status": True,
            "list": o.users
        })
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyList",
            "status": True,
            "list": None
        })

def send_msg(addr:Tuple[str,int],msg:str,from_name:str):
    UDP_SENIOR_IO.send_json(addr,{
        g
    })

def msg(addr, args):
    pass


def logout(addr, args):
    pass
