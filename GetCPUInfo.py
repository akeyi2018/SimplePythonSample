import psutil

print("CPU Core:" + str(psutil.cpu_count()))

print("CPU Percent: " + str(psutil.cpu_percent(interval=1)))

print("Memory Used: " + str(psutil.virtual_memory().percent))

#mac = psutil.net_if_addrs()["eth0"][-1][1]

mac = psutil.net_if_addrs()["lo"][-1][1]

print("Mac Address: " + str(mac))
