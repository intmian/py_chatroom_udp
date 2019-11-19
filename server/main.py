import sys
from threading import Thread

sys.path.append('../')

from net_tool.Server import Server, Router
from server.s_router import udp_map


def main():
    udp_router = Router(udp_map, True)
    chat_server = Server(udp_router)
    t = Thread(target=chat_server.listen, daemon=True)
    t.start()
    input()


if __name__ == '__main__':
    main()
