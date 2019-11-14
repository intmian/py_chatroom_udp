from tool.netIo import NetIo, UDP_IO
from typing import Callable, List, Tuple, NoReturn
from threading import Thread


class Server:
    def __init__(self, func: Callable[[bytes, Tuple[str, int]], NoReturn], protocol: NetIo = UDP_IO):
        """
        :param func: 回调函数
        :param protocol: 协议
        """
        self.__callback = func
        self.__protocol = protocol
        self.__threads: List[Thread] = []

    def set_callback(self, callback: Callable):
        self.__callback = callback

    def listen(self):
        while True:
            data, addr = self.__protocol.receive()
            t = Thread(target=self.__callback, args=(data, addr), daemon=True)
            self.__threads.append(t)
            t.start()

    def close(self):
        pass
        # 设为守护进程即可
        # for t in self.__threads:
        #     if t.is_alive():
        #         t.
