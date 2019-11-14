from tool.netIo import NetIo, UDP_IO
from json import dumps


class SeniorNetIo:
    def __init__(self, protocol: NetIo = UDP_IO):
        self.__protocol = protocol
        self.__cookie = None

    def set_cookie(self, cookie: bytes):
        self.__cookie = cookie

    def send_json(self, addr, args: dict[str:str]) -> bool:
        args["cookie"] = self.__cookie
        j = dumps(args)
        return self.__protocol.send(addr, j)


UDP_SENIOR_IO = SeniorNetIo()
