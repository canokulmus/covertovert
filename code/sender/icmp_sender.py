import scapy.all as scapy

TARGET_IP = "172.18.0.3"
REQUESTED_TTL = 1
ECHO_TYPE = 8

def createAndSendPkg():
    packet = scapy.IP(dst=TARGET_IP, ttl=REQUESTED_TTL) / scapy.ICMP(type=ECHO_TYPE)

    scapy.send(packet)

if __name__ == "__main__":
    createAndSendPkg()
