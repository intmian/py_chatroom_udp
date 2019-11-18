from abc import abstractmethod, ABCMeta
import socket
from typing import Any, Tuple


class NetIo:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, addr: Tuple[str, int], content: bytes) -> bool:
        pass

    @abstractmethod
    def receive(self, buff_size: int = 1024) -> ((str, int), bytes):
        pass


class UdpIo(NetIo):

    def __init__(self, port: int = 0):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(('127.0.0.1', port))

    def send(self, addr: Tuple[str, int], content: bytes) -> bool:
        data_len = self.__socket.sendto(content, addr)
        return len(content) == data_len

    def receive(self, buff_size: int = 1024) -> Tuple[bytes, Any]:
        return self.__socket.recvfrom(buff_size)


def net_is_used(port, ip='127.0.0.1'):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        return True
    except:
        return False


UDP_IO = None
try:
    UDP_IO = UdpIo(23333)
except:
    UDP_IO = UdpIo(0)
