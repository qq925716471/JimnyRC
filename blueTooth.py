import asyncio
import platform

from bleak import BleakClient, BleakScanner


async def print_services(mac_addr: str):
    device = await BleakScanner.find_device_by_address(mac_addr)
    async with BleakClient(device) as client:
        await client.write_gatt_char("6e400002-b5a3-f393-e0a9-e50e24dcca9e", bytes("hello turnRight", 'UTF-8'))


mac_addr = (
    "34:85:18:70:34:46"
    if platform.system() != "Darwin"
    else "A1BBC8EA-21D2-84A0-62EE-84C3601D36A6"
)
loop = asyncio.get_event_loop()
loop.run_until_complete(print_services(mac_addr))
