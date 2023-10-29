# coding:utf-8
import pygame
import socket
import struct
import _thread

# 模块初始化
pygame.init()
pygame.joystick.init()

# 若只连接了一个手柄，此处带入的参数一般都是0
joystick = pygame.joystick.Joystick(0)
# 手柄对象初始化a
joystick.init()

done = False
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.4.1' # 指定接收端IP地址
port = 9999 # 指定接收端端口号
client_socket.connect((host_ip, port))
#_thread.start_new_thread(client.showCam, ())
last_cmd = "0"

def process(param):
    global last_cmd
    if param != last_cmd:
        print(param)
        last_cmd = param
        param=param.encode("utf-8")
        message_size = struct.pack("i", len(param))
        client_socket.sendall(message_size+param)

while not done:
    for event_ in pygame.event.get():
        # 退出事件
        if event_.type == pygame.QUIT:
            done = True
        # 按键按下或弹起事件
        elif event_.type == pygame.JOYBUTTONDOWN or event_.type == pygame.JOYBUTTONUP:
            # 获取按键状态信息
            button = event_.button
            value = joystick.get_button(button)
            if (button == 3):
                if value == 1:
                    process("turnOn")
                elif (value == 0):
                    process("turnOff")
            elif button == 9:
                if value == 1:
                    process("back:0.5")
                elif value == 0:
                    process("stop")

            elif button == 10:
                print(value)
                if value == 1:
                    process("forword:0.8")
                elif value == 0:
                    process("stop")

        # 轴转动事件
        elif event_.type == pygame.JOYAXISMOTION:
            if (event_.axis == 0):
                if (event_.value > 0.3):
                    process("turnRight:0.5")
                elif (event_.value > 0.8):
                    process("turnRight:1")
                elif (event_.value < -0.3 ):
                    process("turnLeft:0.5")
                elif (event_.value > 0.8):
                    process("turnLeft:1")

                else:
                    process("turnForward")

pygame.quit()