import uuid,re

#Get Macaddress
mac = format(uuid.getnode(),"x")

#split macaddress and trim list
splitedStr = re.split("(..)",mac)[1::2]

#join character
res = '-'.join(splitedStr)

#print(mac)
#print(splitedStr)
#print(res)

#Write it in a row
res2 = "-".join(re.split('(..)', format(uuid.getnode(), 'x'))[1::2])

print(res2)
