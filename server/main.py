import sys

sys.path.append('../')
from threading import Thread

from server.model.cache import ACCOUNT

from net_tool.Server import Server, Router
from server.s_router import udp_map


def main():
    udp_router = Router(udp_map, True)
    chat_server = Server(udp_router)
    t = Thread(target=chat_server.listen, daemon=True)
    t.start()
    input()
    ACCOUNT.dump()


if __name__ == '__main__':
    main()
