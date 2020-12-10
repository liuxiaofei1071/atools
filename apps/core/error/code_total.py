# _*_ coding:utf-8 _*_
# @Time:2020/11/6 17:42
# @Author:Cadman
# @File code_total.py

class ErrorCode:
    success = 0

    null_parameters = -1
    select_resource_null = -2
    not_user = -3
    request_params_error = -4
    user_passwd_error = -5
    secret_error = -6
    access_error = -7
    user_unknown_exception = -8
    select_already_exists = -10
    file_uploaded = -11
    file_not_supported = -12
    server_not_bind_services = -20


ErrorINFO = {
    0: "",
    -1: "请求参数为空",
    -2: "该资源不存在",
    -3: "用户不存在",
    -4: "请求参数错误",
    -5: "用户名密码错误",
    -6: "令牌有误,请您用正确方式登录!",
    -7: "校验访问码有误，请您用正确方式登录!",
    -8: "用户极端异常",
    -10: "该资源已存在",
    -11: "文件已上传",
    -12: "文件类型不被支持",
    -20: "服务器未绑定服务"

}
