import json

from net_tool.netIo import NetIo, UDP_IO
from typing import Callable, List, Tuple, NoReturn
from threading import Thread
from typing import *


class Router:
    def __init__(self, func_map: Dict[str, Callable[[Tuple[str, int], Dict[str, Any]], NoReturn]],
                 if_log: bool = False):
        self.__map = func_map
        self.__log = if_log

    def route(self, addr, data):
        re = json.loads(data)
        if "mode" not in re.keys():  # 过滤一下扫描的
            print("[log](%s %d) %s" % (addr[0], addr[1], "错误调用"))
            return
        if self.__log:
            print("[log](%s %d) %s" % (addr[0], addr[1], re["mode"]))
        if re["mode"] not in self.__map:
            print("[log](%s %d) %s" % (addr[0], addr[1], "错误调用"))
            return
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
            t = Thread(target=self.__router.route, args=(addr, data), daemon=True)
            self.__threads.append(t)
            t.start()

    def close(self):
        pass
        # 设为守护进程即可
        # for t in self.__threads:
        #     if t.is_alive():
        #         t.
