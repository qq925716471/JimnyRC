import cv2
import socket
import pickle
import struct

# 建立 TCP 连接
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.0.11' # 指定接收端IP地址
port = 9999 # 指定接收端端口号
client_socket.connect((host_ip, port))

# 打开摄像头
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    # 将帧数据序列化为字节流
    data = pickle.dumps(frame)
    # 获取字节流长度并将其打包为固定长度的二进制数据
    message_size = struct.pack("L", len(data))
    # 发送消息大小和帧数据
    client_socket.sendall(message_size + data)

# 关闭连接和摄像头
client_socket.close()
cap.release()
cv2.destroyAllWindows()