import bluetooth


def get_locol_address():
    print("本机蓝牙MAC地址:", bluetooth.read_local_bdaddr())


def find_buletooth(target_name):
    nearby_devices = bluetooth.discover_devices()
    target_address = None

    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name(bdaddr):
            target_address = bdaddr
        break

    if target_address is not None:
        print("found target bluetooth device with address ", target_address)
        return 1
    else:
        print("could not find target bluetooth device nearby")
        return 0


def san_bluetooth():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in nearby_devices:
        print(" %s - %s" % (addr, name))

    services = bluetooth.find_service(address=addr)
    for svc in services:
        print("Service Name: %s" % svc["name"])
        print(" Host: %s" % svc["host"])
        print(" Description: %s" % svc["description"])
        print(" Provided By: %s" % svc["provider"])
        print(" Protocol: %s" % svc["protocol"])
        print(" channel/PSM: %s" % svc["port"])
        print(" svc classes: %s " % svc["service-classes"])
        print(" profiles: %s " % svc["profiles"])
        print(" service id: %s " % svc["service-id"])
        print("")
    return


def socket_client(bd_addr, port):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()
    return


# find_buletooth("GZSOAIY")
# san_bluetooth()
# socket_client("41:42:C5:BF:2C:32", 1)
get_locol_address()
# bluetooth.bt.connect("41:42:C5:BF:2C:32", 1)


