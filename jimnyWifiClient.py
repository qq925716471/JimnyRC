import wifi
netrworks = wifi.Cell.all('wlan0')
for nw in netrworks:
    print(nw.ssid)