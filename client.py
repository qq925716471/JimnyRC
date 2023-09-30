import cv2
import socket
import pickle
import struct

# 建立 TCP 连接
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1' # 指定本机IP地址
port = 9999 # 指定监听端口号
server_socket.bind((host_ip, port))
server_socket.listen(5)

# 接受连接请求并建立连接
client_socket, addr = server_socket.accept()
data = b""
payload_size = struct.calcsize("L")

# 循环接收数据
while True:
    while len(data) < payload_size:
        data += client_socket.recv(4096)
    
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    # 将接收到的字节流转换为帧数据
    frame = pickle.loads(frame_data)
    
    # 显示帧数据
    cv2.imshow('Clent:', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# 关闭连接和窗口
server_socket.close()
cv2.destroyAllWindows()