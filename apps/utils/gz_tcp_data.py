import time

local_time = time.localtime(time.time())
s_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
print(s_time)

class CommandYIS:
    pass

class TCPClient:
    RESPONSE_STRING_SET = {"switch","humidity", "curtain", "mode", "light", "Temp"}
    DUIYING = {
        "humidity":"humidity_val",
        "mode":"current_mode",
        "curtain":"curtain_val",
        "switch-frontlight1":"front_light1_status",
        "switch-frontlight2":"front_light2_status",
        "switch-backlight2":"back_light1_status",
        "switch-backlight1":"back_light2_status",
        "switch-exhausefan":"fan_status",
        "light":"light_status",
        "Temp":"temp_status",
        "switch-1-1":"xx_status",
        "switch-1-2":"xx_status",
        "switch-1-3":"xx_status",
        "switch-1-4":"xx_status",
        "switch-1-5":"xx_status",
        "switch-1-6":"xx_status",
        "switch-1-7":"xx_status",
        "switch-1-8":"xx_status",
        "switch-2-1":"xx_status",
        "switch-2-2":"xx_status",
        "switch-2-3":"xx_status",
        "switch-2-4":"xx_status",
        "switch-2-5":"xx_status",
        "switch-2-6":"xx_status",
        "switch-2-7":"xx_status",
        "switch-2-8":"xx_status",
    }

    def __init__(self):
        pass

    def parse_data(self, args=None):
        # for item  in self.RESPONSE_STRING:
        #     if item in args
        args = """humidity_63.3
mode_systemclose
curtain_0
switch-frontlight2_off
switch-frontlight1_off
switch-backlight2_off
switch-backlight1_off
switch-exhausefan_off
switch-1-1_off
switch-1-2_off
switch-1-3_off
switch-1-4_off
switch-1-5_off
switch-1-6_off
switch-1-7_off
switch-1-8_off
switch-2-1_off
switch-2-2_off
switch-2-3_off
switch-2-4_off
switch-2-5_off
switch-2-6_off
switch-2-7_off
switch-2-8_off
light_auto
Temp_23.2
        """
        _dict = {}
        ret = args.split("\n")
        for i in ret[:-1]:
            key,val = i.split("_")
            _dict[self.DUIYING[key]] = val
        print(_dict)

TCPClient().parse_data()