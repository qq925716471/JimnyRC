import io
import cv2
import socket
import numpy as np
from PIL import Image


def showCam():
    try:
        # 建立 UDP 连接
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
        host_ip = '192.168.0.13' # 指定本机IP地址
        port = 8888 # 指定监听端口号
        server_socket.bind((host_ip, port))
        print("socket bind")
        # 循环接收数据
        while True:
            try:
                data, ip = server_socket.recvfrom(160000)
                print(1)
                bytes_stream = io.BytesIO(data)
                image = Image.open(bytes_stream)
                img = np.asarray(image)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                # 将接收到的字节流转换为帧数据
                # 显示帧数据
                cv2.imshow('Clent:', img)
                if cv2.waitKey(1) == ord('q'):
                    break
            except:
                pass

        # 关闭连接和窗口
        server_socket.close()
        cv2.destroyAllWindows()
    except:
        print("except")
showCam()