import os
from typing import *
from json import dump, load


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


ACCOUNT = Accounts()
CACHE = Cache()
