# _*_ coding:utf-8 _*_
# @Time:2021/1/7 16:26
# @Author:Cadman
# @File biamp_telnet.py

import time
import socket
import logging
import telnetlib



tn = telnetlib.Telnet()

class TelnetResponse:

    class _Tags:
        a = 1
        b = 2
        c = 3

    @staticmethod
    def recv_ready(ip,port):
        try:
            tn.open(ip,port)
            tn.read_until("Welcome to the Tesira Text Protocol Server...\r\n".encode('utf-8'))
            time.sleep(2)
            #话筒1,2,3,4
            tn.write("AudioIn01 subscribe levels AudioIn01 100\n".encode('utf-8'))  # mic1,2,3,4
            tn.read_until("+OK".encode("utf-8"))
            time.sleep(0.3)
            #播放器1,2
            tn.write("AudioIn05 subscribe levels AudioIn05 100\n".encode('utf-8'))  # 播放器1,2 其他(3,4)
            tn.read_until("+OK".encode("utf-8"))
            time.sleep(0.3)
            #扬声器1,2,other1,2
            tn.write("AudioOut01 subscribe levels AudioOut01 100\n".encode('utf-8'))  # 扬声器,1,2
            tn.read_until("+OK".encode("utf-8"))
            time.sleep(0.3)
            #TV1,2
            tn.write("AudioOut06 subscribe levels AudioOut06 100\n".encode('utf-8'))  # 扬声器,1,2
            tn.read_until("+OK".encode("utf-8"))
            time.sleep(0.3)

        except socket.gaierror:
            logging.error("socket.gaierror: [Errno 11004] getaddrinfo failed,Unable to connect device")
            tn.close()

