import netifaces

for iface_name in netifaces.interfaces():
    iface_data = netifaces.ifaddresses(iface_name)
    print(iface_data.get(netifaces.AF_INET))
    
