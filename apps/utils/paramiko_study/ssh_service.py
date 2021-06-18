# _*_ coding:utf-8 _*_
# @Time:2021/2/23 15:44
# @Author:Cassie·Lau
# @File ssh_service.py
import time
import paramiko
import scpclient

def ssh_for_us():
    start = time.time()
    # 实例化SSHClient
    client = paramiko.SSHClient()

    # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接SSH服务端，以用户名和密码进行认证
    client.connect(hostname='172.16.16.222', port=22, username='root', password='hksoft.cn')

    # 打开一个Channel并执行命令
    stdin, stdout, stderr = client.exec_command('cd /opt/jar && ls -la')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

    # 打印执行结果
    print(stdout.read().decode('utf-8'))

    # 关闭SSHClient
    client.close()
    diff = time.time() - start
    print(f"执行时间为:{diff}")

def ssh_for_transport():
    start = time.time()
    transport = paramiko.Transport('172.16.16.222:22')
    transport.connect(username="root",password="hksoft.cn")

    ssh = paramiko.SSHClient()
    ssh._transport = transport
    stdin,stdout,stderr = ssh.exec_command("systemctl restart mysqld")
    print(f"stdin:{stdin}")
    print(f"stdout:{stdout.read().decode()}")
    print(f"stderr:{stderr.read().decode()}")
    transport.close()
    diff = time.time()-start
    print(f"执行时间为:{diff}")

ssh_for_transport()


