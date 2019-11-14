from tool.netIo import NetIo, UDP_IO
from json import dumps


class SeniorNetIo:
    def __init__(self, protocol: NetIo = UDP_IO):
        self.protocol = protocol
        self.cookie = None

    def set_cookie(self, cookie: bytes):
        self.cookie = cookie

    def send_json(self, addr, args: dict[str:str]) -> bool:
        args["cookie"] = self.cookie
        j = dumps(args)
        return self.protocol.send(addr, j)


UDP_SENIOR_IO = SeniorNetIo()
