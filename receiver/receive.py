from scapy.all import sniff

from receiver.assembler import handle_packet

def main():
    print("Listening for incoming packets...")
    sniff(filter="ip proto 250", prn=handle_packet)
if __name__ == "__main__":
    main()