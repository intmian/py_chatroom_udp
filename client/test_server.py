import sys

sys.path.append('../')
from net_tool.SeniorNetIo import UDP_SENIOR_IO

addr = input("addr")
port = 23333
UDP_SENIOR_IO.set_cookie("test")
UDP_SENIOR_IO.send_json((addr, port), {
    "mode": "test",
    "aaa": "bbb"
})
