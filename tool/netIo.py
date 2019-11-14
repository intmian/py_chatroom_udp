from abc import abstractmethod, ABCMeta
import socket
from typing import Any


class NetIo:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, address_port: (str, int), content: bytes) -> bool:
        pass

    @abstractmethod
    def receive(self, buff_size: int = 1024) -> ((str, int), bytes):
        pass


class UdpIo(NetIo):

    def __init__(self, port: int = 23333):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 绑定 客户端口和地址:
        self.s.bind(('127.0.0.1', port))

    def send(self, address_port: (str, int), content: bytes) -> bool:
        data_len = self.s.sendto(content, address_port)
        return len(content) == data_len

    def receive(self, buff_size: int = 1024) -> tuple[bytes, Any]:
        return self.s.recvfrom(buff_size)


UDP_IO = UdpIo()
