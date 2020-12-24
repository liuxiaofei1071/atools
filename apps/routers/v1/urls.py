# _*_ coding:utf-8 _*_
# @Time:2020/11/4 11:13
# @Author:Cadman
# @File urls.py

"""APP v1 接口路由"""
from fastapi import APIRouter

from apps.controller.v1 import (
    content_type,
    files_manager,
    music,
    user,
    host_server,
    test_api,
    hardware_kind,
    interesting_iq,
    agent,
)

router = APIRouter()

# test测试
router.put("/items/{item_id}", summary="[工欲善其事,必先利其器] 测", tags=["测试接口"])(test_api.update_item)
# router.post("/token",summary="[浮世万千,吾爱有三,日月与卿;] 测",tags=["测试接口"])(test_api.token)
router.get("/test/about/token", summary="[日为朝,月为暮,卿为朝朝暮暮.] 测", tags=["测试接口"])(test_api.test_user)

# 文件类型模块
router.post("/content/type/create", summary="[有一美人兮，见之不忘]增", tags=["content_type"])(content_type.create_content_type)
router.get("/content/type", summary="[一日不见兮，思之如狂] 单查", tags=["content_type"], )(content_type.get_content_type)
router.get("/content/type/list", summary="[情不知所起，一往而深] 全查", tags=["content_type"], )(content_type.get_content_type_list)
router.delete("/content/type/delete", summary="[衣带渐宽终不悔，为伊消得人憔悴] 单删", tags=["content_type"], )(
    content_type.del_content_type)

# 文件上传
router.post("/upload/", summary="[世间安得双全法，不负如来不负卿] 上传", status_code=201, tags=["文件上传"])(
    files_manager.create_upload_file)

# 音乐模块
router.post("/song/create", summary="[举世皆浊我独清,众人皆醉我独醒] 增", tags=["歌曲"])(music.create_song)
router.get("/song", summary="[新沐者必弹冠,新浴者必振衣.] 单查", tags=["歌曲"])(music.get_song)
router.get("/song/list", summary="[安能以身之察察,受物之汶汶者乎?] 全查", tags=["歌曲"])(music.get_song_list)
router.delete("/song", summary="[安能以皓皓之白，而蒙世俗之尘埃乎?] 单删", tags=["歌曲"], )(music.del_song)
router.put("/song", summary="[蒹葭苍苍,白露为霜,所谓伊人,在水一方.] 更新", tags=["歌曲"])(music.update_song)

# 书籍模块

# 用户模块 登陆|注册
router.get("/secret", summary="[空山新雨后，天气晚来秋] 获取公钥", tags=["用户-秘钥"])(user.rsa)
router.get("/code/list", summary="[蜀道难，难于上青天] 全查", tags=["用户"])(user.get_sec_code_list)
router.post("/user/code", summary="[面朝大海，春暖花开] 增（sec）", tags=["用户"])(user.create_sec_code)
router.post("/login", summary="[十重秘钥] 增（sec）", tags=["用户"])(user.login)
# router.post("/register",summary="[安全加倍] 增（sec）",tags=["用户"])(user.register)

# 服务器模块
router.get("/host/server/list", summary="[几度风霜绕残阳] 全查", tags=["服务器"])(host_server.get_host_server_list)
router.get("/host/server", summary="[一城烟雨渡众生] 查", tags=["服务器"])(host_server.get_host_server)
router.post("/host/server", summary="[先天下之忧而忧,后天下之乐而乐] 增", tags=["服务器"])(host_server.create_host_server)
router.delete("/host/server", summary="[余忆童稚时,能张目对日,明察秋毫] 单删", tags=["服务器"], )(host_server.del_host_server)
router.put("/host/server", summary="[天下难事,皆在人为] 更新", tags=["服务器"])(host_server.update_host_server)
router.post("/bind/service", summary="[孤独的根号3] 绑定", tags=["服务器"])(host_server.bind_service)

# 服务模块

# 发布模块

# 硬件类型模块
router.get("/hardware/first/list", summary="[你若花开,蝴蝶自来] 全查(第一子类)", tags=["硬件库"])(hardware_kind.get_hardware_first_list)
router.get("/hardware/second/list", summary="[自古中秋月最明,凉风届候夜弥清] 全查(第二子类)", tags=["硬件库"])(
    hardware_kind.get_hardware_second_list)
router.get("/hardware/list", summary="[人生固有一死,或重于泰山,或轻于鸿毛] 全查", tags=["硬件库"])(hardware_kind.get_hardware_list)
router.post("/hardware/create", summary="[待到秋来九月八,我花开罢百花杀] 增", tags=["硬件库"])(hardware_kind.hardware_create)


#其他模块
router.post("/iq/validate", summary="[熟读唐诗三百首,不会做诗也会吟] 增", tags=["其他-IQ"])(interesting_iq.create_validate)
router.get("/iq/validate", summary="[山有桥松,隰有游龙] 查", tags=["其他-IQ"])(interesting_iq.get_validate)
router.get("/iq/question", summary="[熟读唐诗三百首,不会做诗也会吟] 查", tags=["其他-IQ"])(interesting_iq.get_question)
router.post("/iq/answer", summary="[熟读唐诗三百首,不会做诗也会吟] 校验", tags=["其他-IQ"])(interesting_iq.answer_validate)
router.get("/iq/validate/list", summary="[读万卷书,行万里里] 全查", tags=["其他-IQ"])(interesting_iq.get_validate_list)
router.delete("/iq/validate", summary="[天涯地角有穷时,只有相思无尽处] 单删", tags=["其他-IQ"], )(interesting_iq.del_validate)
router.put("/ip/validate", summary="[多情只有春庭月,犹为离人照落花] 更新", tags=["其他-IQ"])(interesting_iq.update_validate)

#驱动模块
#agent 子模块
router.get("/script/list", summary="[] 全查", tags=["驱动-script"])(agent.get_script_list)
router.get("/script/code", summary="[] 全查", tags=["驱动-script"])(agent.get_script_code)
router.post("/script", summary="[] 增", tags=["驱动-script"])(agent.create_script)
router.put("/script", summary="[] 改", tags=["驱动-script"])(agent.update_script)