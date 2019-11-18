import sys

sys.path.append('../')

from net_tool.Server import Server, Router
from client.c_router import udp_map
from threading import Thread
from client.cmd import cmd


def main():
    udp_router = Router(udp_map, True)
    listen_server = Server(udp_router)
    t = Thread(target=listen_server.listen, daemon=True)
    t.start()
    cmd()


if __name__ == '__main__':
    main()
