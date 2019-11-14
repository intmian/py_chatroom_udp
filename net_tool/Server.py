import json

from net_tool.netIo import NetIo, UDP_IO
from typing import Callable, List, Tuple, NoReturn
from threading import Thread
from typing import *


class Router:
    def __init__(self, func_map: Dict[str, Callable[[Tuple[str, int], Dict[str, Any]], NoReturn]]):
        self.__map = func_map

    def route(self, addr, data):
        re = json.loads(data)
        self.__map[re["mode"]](addr, re)


class Server:
    def __init__(self, router: Router, protocol: NetIo = UDP_IO):
        """
        :param func: 回调函数
        :param protocol: 协议
        """
        self.__protocol = protocol
        self.__threads: List[Thread] = []
        self.__router = router

    def listen(self):
        while True:
            data, addr = self.__protocol.receive()
            t = Thread(target=self.__router.route(addr, data), args=(data, addr), daemon=True)
            self.__threads.append(t)
            t.start()

    def close(self):
        pass
        # 设为守护进程即可
        # for t in self.__threads:
        #     if t.is_alive():
        #         t.
