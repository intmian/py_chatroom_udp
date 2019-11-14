from tool.netIo import NetIo, UDP_IO
from typing import Callable, List
from threading import Thread


class Server:
    def __init__(self, func: Callable, protocol: NetIo = UDP_IO):
        self.callback = func
        self.protocol = protocol
        self.threads: List[Thread] = []

    def set_callback(self, callback: Callable):
        self.callback = callback

    def listen(self):
        while True:
            data, addr = self.protocol.receive()
            t = Thread(target=self.callback, args=(data, addr), daemon=True)
            self.threads.append(t)
            t.start()

    def close(self):
        pass
        # 设为守护进程即可
        # for t in self.threads:
        #     if t.is_alive():
        #         t.
