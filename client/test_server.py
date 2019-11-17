import sys

sys.path.append('../')
from net_tool.netIo import UdpIo

u = UdpIo(1029)

addr = input("addr")
port = input("port")
u.send((addr, int(port)), "this is a test".encode("utf-8"))
