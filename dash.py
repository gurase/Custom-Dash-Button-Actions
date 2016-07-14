import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import config
from wunderlistclient import WunderlistClient

def add_item(button_id):
    button = config.buttons[button_id]
    wunderlist = WunderlistClient(config.CLIENT_ID, config.ACCESS_TOKEN)
    wunderlist.create_task(button["list"], button["message"])
    
def udp_filter(pkt):
    options = pkt[DHCP].options
    for option in options:
        if isinstance(option, tuple):
            if 'requested_addr' in option:
                # we've found the IP address, which means its the second and final UDP request, so we can trigger our action
                add_item(pkt.src)
        
print "Waiting for a button press..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in list(config.buttons.keys()))