# _*_coding: utf-8_*_
# @Time: 2020/12/6 15:48
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: rsa.py

import base64

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

class OperateRSA:

    RANDOM_GENERATOR = Random.new().read

    @staticmethod
    def b64_encode(var):
        return base64.b64encode(var)

    @staticmethod
    def b64_decode(args):
        return base64.b64decode(args)

    @property
    def generate_rsa(self):
        # rsa算法生成实例
        rsa = RSA.generate(1024, self.RANDOM_GENERATOR)
        # a的秘钥对的生成,存储文件
        self.private_key = rsa.exportKey().decode()
        # with open('a-private.pem', 'w') as f:
        #     f.write(PRIVATE_PEM)

        self.public_key = rsa.publickey().exportKey().decode()

        # with open('a-public.pem', 'w') as f:
        #     f.write(PUBLIC_PEM)
        return self.public_key,self.private_key


    def pubic_key2b64(self,msg,pub_key):
        rsa_key = RSA.importKey(pub_key)

        cipher = Cipher_pkcs1_v1_5.new(rsa_key)
        #加密的时候选择base64加密
        _info = cipher.encrypt(msg.encode())
        cipher_info = self.b64_encode(_info).decode()

        return cipher_info


    def private_b64(self,cipjer,private_key):

        rsa_key = RSA.importKey(private_key)
        cipher = Cipher_pkcs1_v1_5.new(rsa_key)
        b64_bytes = self.b64_decode(cipjer.encode())
        password = cipher.decrypt(b64_bytes,None)

        if isinstance(password,bytes):
            result = password.decode()
        else:
            result = False
        return result

"""
#[rsa] 配合测试
start = time.time()
msg = "liuxiaofei"
rsa_obj = OperateRSA()

cipher_info = rsa_obj.pubic_key2b64(msg)
res = rsa_obj.private_b64(cipher_info)
print(res)
print(f"当前加密和解密合计耗时:{time.time()-start}")
"""

