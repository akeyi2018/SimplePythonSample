import uuid

node=uuid.getnode()
mac = uuid.UUID(int=node)
addr = mac.hex[-12:]
print(addr)
