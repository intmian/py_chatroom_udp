# Callable[Tuple[str, int], Dict[str, Any]
from server.model.cache import ACCOUNT, CACHE
from net_tool.SeniorNetIo import UDP_SENIOR_IO

def test(addr, args):
    print("from ", addr)
    print(args)


def sign_up(addr, args):
    suc = ACCOUNT.new_user(args["account"], args["pwd"], args["name"])
    if suc:
        UDP_SENIOR_IO.send_json(args, {
            "mode": "replySighUp",
            "type": True,
            "hit": ""
        })
    else:
        UDP_SENIOR_IO.send_json(args, {
            "mode": "replySighUp",
            "type": False,
            "hit": "账号名或用户名重复"
        })

