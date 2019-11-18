# 显示方式	效果	字体色	背景色	颜色描述
# 0	终端默认设置	30	    40	    黑色
# 1	高亮显示	    31	    41	    红色
# 4	使用下划线	    32	    42	    绿色
# 5	闪烁	        33	    43	    黄色
# 7	反白显示	    34	    44	    蓝色
# 8	不可见	        35	    45	    紫红色
#                   36	    46	    青蓝色
#                   37	    47  	白色


def color_str(s: str, style: int = -1, font_color: int = -1, background: int = -1) -> str:
    tpl = r"\033[%sm%s\033[0m!"
    cmd = ""
    if style != -1:
        cmd += str(style)
    if font_color != -1:
        cmd += ";"
        cmd += str(font_color)
    if background != -1:
        cmd += ";"
        cmd += str(background)
    return tpl % (cmd, str)


def red_paint(s: str):
    print(color_str(s, font_color=31))


def blue_paint(s: str):
    print(color_str(s, font_color=34))


def green_paint(s: str):
    print(color_str(s, font_color=32))


def hint_paint(s: str):
    print(color_str(s, font_color=35))
