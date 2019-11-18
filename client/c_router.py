import client.c_controller as controller

udp_map = {
    "replySignUp": controller.reply_sign_up,
    "replyLogin": controller.reply_login,
    "replyList": controller.reply_list,
    "replyMsg": controller.reply_msg,
    "getMsg": controller.get_msg,
    "replyLogout" : controller.reply_logout
}
