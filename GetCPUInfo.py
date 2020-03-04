import psutil

print("CPU Core:" + str(psutil.cpu_count()))

print("CPU Percent: " + str(psutil.cpu_percent(interval=1)))

print("Memory Used: " + str(psutil.virtual_memory().percent))
