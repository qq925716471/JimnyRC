# coding:utf-8
import pygame
import platform
from bleak import BleakClient, BleakScanner
import asyncio

# 模块初始化
pygame.init()
pygame.joystick.init()

# 若只连接了一个手柄，此处带入的参数一般都是0
joystick = pygame.joystick.Joystick(0)
# 手柄对象初始化a
joystick.init()

done = False
last_cmd = "0"
device=None

mac_addr = (
    "34:85:18:70:34:46"
    if platform.system() != "Darwin"
    else "A1BBC8EA-21D2-84A0-62EE-84C3601D36A6"
)
async def initBlueTooth():
    global mac_addr
    global device
    device = await BleakScanner.find_device_by_address(mac_addr)


async def send(cmd):
    global device
    async with BleakClient(device) as client:
         if (cmd != "0"):
              await client.write_gatt_char("6e400002-b5a3-f393-e0a9-e50e24dcca9e", bytes(last_cmd, 'UTF-8'))

def process(param):
    global last_cmd
    if param != last_cmd:
        print(param)
        last_cmd = param
        asyncio.run(send(param))

asyncio.run(initBlueTooth())

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
                elif (event_.value >0.8):
                    process("turnLeft:1")
                elif (event_.value < -0.3):
                    process("turnLeft:0.5")
                elif (event_.value > 0.8):
                    process("turnLeft:1")
                else:
                    process("turnForward")


pygame.quit()
