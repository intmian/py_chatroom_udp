from typing import *
import json


def router(addr, data):
    r_map: Dict[str, Callable[[Tuple[str, int], bytes], NoReturn]] = {

    }

    re = json.loads(data)
    r_map[re["mode"]](addr, data)
