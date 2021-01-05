# _*_ coding:utf-8 _*_
# @Time:2020/11/6 17:42
# @Author:Cadman
# @File code_total.py

class StatusCode:
    """
    状态码合集
    """
    #公共码
    C10000 = {"code":10000,"msg":"成功"}
    C10001 = {"code":10001,"msg":"新增数据失败"}
    C10002 = {"code":10002,"msg":"更新数据失败"}
    C10003 = {"code":10003,"msg":"删除数据失败"}
    C10004 = {"code":10004,"msg":"查询数据失败"}
    C10005 = {"code":10005,"msg":"查询数据[MORE]失败"}

    #资源
    R20001 = {"code":20001,"msg":"检测到资源已存在"}
    R20002 = {"code":20002,"msg":"资源不存在"}
    R20003 = {"code":20003,"msg":"文件类型不支持"}
    R20004 = {"code":20004,"msg":"文件已上传"}
    R20005 = {"code":20005,"msg":"文件路径有误"}
    R20006 = {"code":20006,"msg":"非法ID探测资源"}

    # 登陆/注册模块
    L30001 = {"code":30001,"msg":"用户名或密码错误"}
    L30002 = {"code":30002,"msg":"检测到非法操作"}
    L30003 = {"code":30003,"msg":"缺省参数"}
    L30004 = {"code":30004,"msg":"用户被限制，请联系管理员处理"}
    L30005 = {"code":30005,"msg":"用户被锁定，请联系管理员处理"}
    L30006 = {"code":30006,"msg":"令牌有误，请正常登陆"}
    L30007 = {"code":30007,"msg":"用户名不合法"}

    # 用户相关
    P40001 = {"code":40001,"msg":"非法用户"}
    P40002 = {"code":40002,"msg":"未获取到有效数据"}



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
    sql_execute_error = -9
    select_already_exists = -10
    file_uploaded = -11
    file_not_supported = -12
    no_resources = -13
    py_resources_error = -14
    server_not_bind_services = -20
    IQ_verification_failed = -30

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
    -9: "操作数据执行有误",
    -10: "该资源已存在",
    -11: "文件已上传",
    -12: "文件类型不被支持",
    -13:"选择的资源不存在",
    -14:"选择py资源错误",
    -20: "服务器未绑定服务",
    -30:"IQ校验未通过"
}

