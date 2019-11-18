from typing import Dict,AnyStr

from net_tool.netIo import NetIo, UDP_IO
from json import dumps


class SeniorNetIo:
    def __init__(self, protocol: NetIo = UDP_IO):
        self.__protocol = protocol
        self.__cookie = None
        self.__if

    def set_cookie(self, cookie: bytes):
        self.__cookie = cookie

    def send_json(self, addr, args: Dict[AnyStr, AnyStr]) -> bool:
        args["cookie"] = self.__cookie
        j = dumps(args)
        return self.__protocol.send(addr, j.encode("utf-8"))


UDP_SENIOR_IO = SeniorNetIo()
