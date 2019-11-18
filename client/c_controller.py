import client.color_paint as cp
from client.setting import SETTING


# Callable[Tuple[str, int], Dict[str, Any]
# 系统信息 蓝色
# 全体信息 白色
# 私信     绿色
# 失败     红色
def reply_sign_up(addr, args):
    type_ = args["type"]
    if type_:
        cp.blue_paint("注册成功")
    else:
        cp.red_paint("注册失败:" + args["hint"])


def reply_login(addr, args):
    suc = args["success"]
    if suc:
        cp.blue_paint("登录成功")
        SETTING.set["cookie"] = args["cookie"]
    else:
        cp.red_paint("登录失败")


def reply_list(addr, args):
    status, list_ = args["status", "list"]
    if status:
        cp.blue_paint("在线名单：")
        for name in list_:
            cp.blue_paint("  " + name)
    else:
        cp.red_paint("请先登录")


def reply_msg(addr, args):
    if not args["type"]:
        cp.red_paint("信息发送失败")


def get_msg(addr, args):
    from_, private, msg = args["from"], args["private"], args["msg"]
    if private:
        cp.green_paint(from_ + ":" + msg)
    else:
        print(from_ + ":" + msg)


def reply_logout(addr, args):
    t = args["type"]
    if not t:
        cp.red_paint("退出登录失败")
