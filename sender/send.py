import argparse
from sender.fragmenter import fragment_file
from scapy.all import send


def main():
    parser = argparse.ArgumentParser(description="Send a file over the network using custom packets.")
    parser.add_argument("file", help="Path to the file to send")
    parser.add_argument("dst_ip", help="Destination IP address")
    parser.add_argument("--chunk_size", type=int, default=1024, help="Size of each packet in bytes")

    args = parser.parse_args()

    packets = fragment_file(args.file, args.dst_ip, args.chunk_size)

    for pkt in packets:
        send(pkt)
    
    print(f"Sent {len(packets)} packets successfully")

if __name__ == "__main__":
    main()