# Callable[Tuple[str, int], Dict[str, Any]
from server.model.cache import ACCOUNT, CACHE


def test(addr, args):
    print("from ", addr)
    print(args)


def sign_up(addr, args):
    pass
