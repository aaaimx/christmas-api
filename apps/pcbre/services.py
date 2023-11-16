from smbus import SMBus
from time import sleep
addrs = (8,9)
ledstates = (0,1)
bus = SMBus(1) 
#numb = 1

'''
while True:
    try:
        for addr in addrs:
            for ledstate in ledstates:
                bus.write_byte(addr,ledstate)
                print(addr,ledstate)
                sleep(1/100 )
    except:
        print("opps!")
'''

def on_led():
    for add in addrs:
        for status in ledstates:
            bus.write_byte(addr,ledstate)
        