from abc import abstractmethod, ABCMeta
import socket
from typing import Any


class NetIo:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, addr: tuple[str, int], content: bytes) -> bool:
        pass

    @abstractmethod
    def receive(self, buff_size: int = 1024) -> ((str, int), bytes):
        pass


class UdpIo(NetIo):

    def __init__(self, port: int = 23333):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(('127.0.0.1', port))

    def send(self, addr: tuple[str, int], content: bytes) -> bool:
        data_len = self.__socket.sendto(content, addr)
        return len(content) == data_len

    def receive(self, buff_size: int = 1024) -> tuple[bytes, Any]:
        return self.__socket.recvfrom(buff_size)


UDP_IO = UdpIo()
