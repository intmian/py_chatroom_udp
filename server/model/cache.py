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
        if os.path.exists('user_info.json'):
            self.__load()
        else:
            self.__database: Dict[str:List] = {}

    def __del__(self):
        self.dump()

    def dump(self):
        fw = open('user_info.json', 'w', encoding='utf-8')
        dump(self.__database, fw, ensure_ascii=False, indent=4)

    def __load(self):
        fw = open('user_info.json', 'w', encoding='utf-8')
        self.__database = load(fw, ensure_ascii=False, indent=4)

    def new_user(self, acc: str, password_d: str, name: str) -> bool:
        for acc_ in self.__database:
            if acc == acc_ or name == self.__database[acc_][1]:
                return False
        self.__database[acc] = [name, password_d]

    def get_user(self, acc) -> (str, str):
        """
        :rtype: 返回用户名和hash过的密码,没有就返回False
        """
        if str not in self.__database:
            return False
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
        self.users = Set()
        self.sessions = Dict()  # 对应用户端的cookie

    @staticmethod
    def new_cookie() -> bytes:
        seed = b"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
        s = random.sample(seed, 10)
        return s

    def add_user(self, user: AnyStr) -> bytes:
        """
        :param user:
        :return: cookie
        """
        self.users.add(user)
        cookie = self.new_cookie()
        self.sessions[cookie] = user
        return cookie

    def remove_user(self, user: AnyStr, cookie: bytes) -> bool:
        if self.sessions[cookie] != user:
            return True
        else:
            self.sessions.pop(cookie)
            self.users.remove(user)
            return False


ACCOUNT = Accounts()
CACHE = Cache()

seed = b"this is a A"
CACHE.set("randB", random.shuffle(seed))  # 设置服务器端随机数用于登录时校验
CACHE.set("onlineList", OnlineList())  # 在线名单
