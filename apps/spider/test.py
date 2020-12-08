# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 10:53
# @Author  : wangyk
# @File    : test.py

import subprocess
import time

import uiautomation

# from pykeyboard import PyKeyboard

print(uiautomation.GetRootControl())
subprocess.Popen(r'D:\Apps\TencentMeeting\wemeetapp.exe')
# kb = PyKeyboard()


def enter_meeting():
    """
    未登录状态下腾讯视频会议加入会议！
    :return:
    """
    window1 = uiautomation.WindowControl(searchDepth=1, Name='腾讯会议(LoadingWnd)')
    print(window1.Name)
    window1.SetActive()
    # 首页点击登录
    login = window1.ButtonControl(searchDepth=5, Name='注册/登录')
    print(login.Name)
    login.Click()
    # 跳转后输入用户名，密码
    login_user = window1.EditControl(Name='PhoneNumberEdit')
    print(login_user.Name)
    login_user.SendKeys('17610379173', interval=0.1)
    login_pwd = window1.EditControl(Name='Account_login_password_input')
    print(login_pwd.Name)
    login_pwd.Click()
    login_pwd.SendKeys('Wgd123456', interval=0.1)
    # 点击登录按钮
    login_but = window1.ButtonControl(Name='登录')
    login_but.Click()
    # 默认为企业直接点击确定
    determine_but = window1.ButtonControl(Name='确定')
    determine_but.Click()
    # 增加阻塞等待跳转，可使用 auto.uiautomation.SetGlobalSearchTimeout(15)  设置全局搜索超时 15秒
    time.sleep(2)
    enter_meeting_but = window1.ButtonControl(Name='加入会议')
    print(enter_meeting_but.Name)
    enter_meeting_but.Click()
    time.sleep(2)

    # 获取腾讯会议加入会议页面
    window2 = uiautomation.PaneControl(Name='ClientArea')
    enter_meeting_input = window2.EditControl(Name='Join_meeting_meeting_number')
    print(enter_meeting_input.Name)
    enter_meeting_input.Click()
    enter_meeting_input.SendKeys('792342214', interval=0.1)
    # 勾选麦克风，摄像头
    mic_check_box = window2.CheckBoxControl(Name='自动连接音频')
    camera_check_box = window2.CheckBoxControl(Name='入会开启摄像头')
    # mic_check_box.GetTogglePattern().ToggleState 属性可判断是否勾选 返回 int 0,1
    # 判断是否勾选
    if mic_check_box.GetTogglePattern().ToggleState == 0:
        mic_check_box.Click()
    if camera_check_box.GetTogglePattern().ToggleState == 0:
        camera_check_box.Click()
    # 加入会议
    join_meeting_but = window2.ButtonControl(Name='Join_meeting_Join_meeting')
    join_meeting_but.Click()

    # 获取视频会议选择音频接入方式弹窗
    try:
        window3 = uiautomation.WindowControl(Name='(AudioSelectWndNew)')
        pc_audio_but = window3.ButtonControl(Name='使用电脑音频')
        audio_check = window3.CheckBoxControl(Name='入会时使用电 脑音频')
        print(audio_check.GetTogglePattern().ToggleState)
        if audio_check.GetTogglePattern().ToggleState == 0:
            audio_check.Click()
        time.sleep(1)
        pc_audio_but.Click()
    except Exception as e:
        print(e)

    # 获取视频会议主页面
    window4 = uiautomation.WindowControl(Name='腾讯会议(InMeetingWnd)')
    window4.Maximize()


# def start():
#     logined = uiautomation.WindowControl(Name='腾讯会议(LoadingWnd)')
#     logined.SetActive()
#     logout = logined.ImageControl()
#     if not logout.Name:
#         logout.Click()
#         time.sleep(1)
#         # 获取登录信息下拉菜单
#         for i in range(13):
#             kb.press_key(kb.tab_key)
#             kb.release_key(kb.tab_key)
#         time.sleep(1)
#         kb.tap_key(kb.enter_key)
#         # 关闭应用，重新入会
#         try:
#             kb.press_key(kb.alt_key)
#             kb.tap_key(115)  # 115为键盘“F4”键码
#             kb.release_key(kb.alt_key)
#         except:
#             kb.release_key(kb.alt_key)
#         enter_meeting()
#     else:
#         enter_meeting()


if __name__ == '__main__':
    enter_meeting()
