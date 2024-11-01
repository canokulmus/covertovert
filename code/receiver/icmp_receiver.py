import scapy.all as scapy

REQUESTED_TTL = 1
ECHO_TYPE = 8

def showIcmp(pkg):
    if pkg.haslayer(scapy.ICMP) and pkg[scapy.ICMP].type == ECHO_TYPE and pkg[scapy.IP].ttl == REQUESTED_TTL:
        pkg.show()

def sniffPacket():
    scapy.sniff(
        filter="icmp", 
        prn=showIcmp,
        count=1
    )

if __name__ == "__main__":
    sniffPacket()