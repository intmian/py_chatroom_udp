from net_tool.Server import Server, Router

# 路径
udp_map = {

}


def main():
    udp_router = Router(udp_map)
    chat_server = Server(udp_router)
    chat_server.listen()


if __name__ == 'main':
    main()
