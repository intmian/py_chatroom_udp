import tool.UdpServer
import server.s_router as rout


def main():
    chat_server = tool.UdpServer.Server(rout.router)
    chat_server.listen()


if __name__ == 'main':
    main()
