import asyncio
from bleak import BleakClient,BleakScanner

address = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
MODEL_NBR_UUID = "2A24"

async def main():
    devices = await BleakScanner.discover()
    for d in devices:  # d为类，其属性有：d.name为设备名称，d.address为设备地址
        print(d)

asyncio.run(main())