from json import load


class Setting:
    def __init__(self):
        f = open("setting.json", "w")
        self.set = load(f)
        self.set["cookie"] = ""


SETTING = Setting()
