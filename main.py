# -*- coding: utf-8 -*-
import requests
import multiprocessing
import time
def loginwork(username,password):
    while True:
        try:
            if "Modify Password" in requests.get("http://baidu.com/").text:
                print(time.strftime("%H-%M-%S",time.localtime(time.time()))," 无网络，开始认证网络...")
                result = requests.post("http://10.44.1.20/", data={"DDDDD": username, "upass": password, "0MKKey": ""})
                if "You have successfully logged into our system" in result.text:
                    print(time.strftime("%H-%M-%S",time.localtime(time.time()))," 您已成功登录到上网系统")
                else:
                    print(time.strftime("%H-%M-%S",time.localtime(time.time()))," 您无法正常登录到上网系统...")
        except:
            pass
        time.sleep(10)
if __name__=='__main__':
    multiprocessing.freeze_support()
    print(
        "欢迎使用hbucvc网络自动重连服务\n",
        "请先连接 hbucvc-work 无线网络"
    )
    print("现在请登录您的上网账号:")
    username = input("请输入账号:")
    password = input("请输入密码:")
    print("当前已开始监听...")
    process1 = multiprocessing.Process(target=loginwork,args=(username,password))
    process1.start()
