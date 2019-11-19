# Callable[Tuple[str, int], Dict[str, Any]
from server.model.cache import ACCOUNT, CACHE, OnlineList
from net_tool.SeniorNetIo import UDP_SENIOR_IO
from typing import *


def verify_cookie(cookie: bytes) -> Tuple[bool, Any]:
    """
    :param cookie:
    :return: if_success, user_name
    """
    o: OnlineList = CACHE.get("onlineList")
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
            "mode": "replySignUp",
            "type": True,
            "hint": ""
        })
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replySignUp",
            "type": False,
            "hint": "账号名或用户名重复"
        })


def login(addr, args):
    name, hash_d = ACCOUNT.get_user(args["account"])
    if hash_d == args["pwd"]:
        o: OnlineList = CACHE.get("onlineList")
        cookie = o.add_user(name, addr)
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogin",
            "success": True,
            "cookie": cookie,
            "name": name
        })
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogin",
            "success": False,
            "cookie": "",
            "name": ""
        })


def get_list(addr, args):
    if "cookie" not in args:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyList",
            "status": False,
            "list": None
        })
        return
    cookie = args["cookie"]
    flag, name = verify_cookie(cookie)
    o: OnlineList = CACHE.get("onlineList")
    if flag:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyList",
            "status": True,
            "list": list(o.users)
        })
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyList",
            "status": False,
            "list": None
        })


def send_msg(addr: Tuple[str, int], msg: str, from_name: str, private: bool):
    UDP_SENIOR_IO.send_json(addr, {
        "mode": "getMsg",
        "from": from_name,
        "msg": msg,
        "private": private
    })


def msg(addr, args):
    if "cookie" not in args:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyList",
            "status": True,
            "list": None
        })
        return
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
            o: OnlineList = CACHE.get("onlineList")
            for user in o.users:
                send_msg(o.addrs[user], msg, user, False)
        else:
            o: OnlineList = CACHE.get("onlineList")
            send_msg(o.addrs[to], msg, name, True)


def logout(addr, args):
    if "cookie" not in args:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyList",
            "status": True,
            "list": None
        })
        return
    cookie = args["cookie"]
    flag, name = verify_cookie(cookie)
    if flag:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogout",
            "type": True
        })
        o: OnlineList = CACHE.get("onlineList")
        o.remove_user(cookie)
    else:
        UDP_SENIOR_IO.send_json(addr, {
            "mode": "replyLogout",
            "type": False
        })
