from typing import Dict,AnyStr

from net_tool.netIo import NetIo, UDP_IO
from json import dumps


class SeniorNetIo:
    def __init__(self, protocol: NetIo = UDP_IO):
        self.__protocol = protocol
        self.__cookie = None
        self.__if_cookie = False

    def set_cookie(self, cookie: bytes):
        self.__cookie = cookie
        self.__if_cookie = True

    def remove_cookie(self):
        self.__cookie = None
        self.__if_cookie = False

    def send_json(self, addr, args: Dict[AnyStr, AnyStr]) -> bool:
        if self.__if_cookie:
            args["cookie"] = self.__cookie
        j = dumps(args)
        return self.__protocol.send(addr, j.encode("utf-8"))


UDP_SENIOR_IO = SeniorNetIo()
