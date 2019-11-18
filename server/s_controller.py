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


def send_msg(addr: Tuple[str, int], msg: str, from_name: str):
    UDP_SENIOR_IO.send_json(addr, {
        "mode": "getMsg",
        "from": from_name,
        "msg": msg
    })


def msg(addr, args):
    to, msg, cookie = args["to"], args["msg"], args["cookie"]
    flag, name = verify_cookie(cookie)
    if not flag:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyMsg",
            "type": False
        })
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyMsg",
            "type": True
        })
        if to == "":
            o: OnlineList = CACHE["onlineList"]
            for user in o.users:
                send_msg(addr, msg, user)
        else:
            send_msg(addr, msg, name)


def logout(addr, args):
    cookie = args["cookie"]
    flag, name = verify_cookie(cookie)
    if flag:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogout",
            "type": True
        })
        o: OnlineList = CACHE["onlineList"]
        o.remove_user(cookie)
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogout",
            "type": False
        })
