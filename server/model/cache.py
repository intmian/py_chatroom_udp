import os
from typing import *
from json import dump, load
import random


class Accounts:
    """
    {
        "account":[
            <name>
            <pwd_d>
        ]
    }
    """

    def __init__(self):
        self.__database = None
        self.__json_file = None
        if os.path.exists('user_info.json'):
            self.__load()
        else:
            self.__database: Dict[str:List] = {}
        self.__json_file = open('user_info.json', 'w', encoding='utf-8')  # 因为_del_里面不能有依赖项open...

    def __del__(self):
        self.dump()

    def dump(self):
        dump(self.__database, self.__json_file, ensure_ascii=False, indent=4)
        self.__json_file.close()

    def __load(self):
        fw = open('user_info.json', 'r', encoding='utf-8')
        self.__database = load(fw)
        fw.close()

    def new_user(self, acc: str, password_d: str, name: str) -> bool:
        for acc_ in self.__database:
            if acc == acc_ or name == self.__database[acc_][1]:
                return False
        self.__database[acc] = [name, password_d]
        return True

    def get_user(self, acc) -> (str, str):
        """
        :returns: 返回用户名和hash过的密码,没有就返回False
        """
        if acc not in self.__database:
            return None, None
        else:
            acc_ = self.__database[acc]
            return acc_[0], acc_[1]


class Cache:
    def __init__(self):
        self.__data: Dict[str:Any] = dict()
        self.__data["online"]: Set = {}

    def set(self, key: str, value: Any):
        self.__data[key] = value

    def get(self, key: str) -> Any:
        return self.__data[key]


class OnlineList:
    def __init__(self):
        self.users = set()
        self.sessions = dict()  # 对应用户端的cookie
        self.addrs = dict()  # name : ipport

    @staticmethod
    def new_cookie() -> str:
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        s = random.sample(seed, 10)
        return "".join(s)

    def add_user(self, user: AnyStr, addr: Tuple) -> str:
        """
        :param user:
        :return: cookie
        """
        self.users.add(user)
        cookie = self.new_cookie()
        self.sessions[cookie] = user
        self.addrs[user] = addr
        return cookie

    def remove_user(self, cookie: bytes) -> bool:
        if cookie not in self.sessions:
            return False
        else:
            user = self.sessions.pop(cookie)
            self.users.remove(user)
            return True


ACCOUNT = Accounts()
CACHE = Cache()
CACHE.set("onlineList", OnlineList())  # 在线名单
