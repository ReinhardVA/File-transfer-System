from protocol.packet import FilePacket
from scapy.all import IP
import zlib

def fragment_file(file_path, dest_ip, chunk_size = 1024):
    with open(file_path, "rb") as f:
        file_bytes = f.read()
    
    fragments = [file_bytes[i:i + chunk_size] for i in range(0, len(file_bytes), chunk_size)]
    packets = []
    total = len(fragments)

    for seq, data in enumerate(fragments):
        pkt = IP(dst=dest_ip, proto=250) / FilePacket(
            seq = seq,
            total = total,
            length = len(data),
            crc = zlib.crc32(data) & 0xFFFFFFFF,
            data = data
        )
        packets.append(pkt)
    
    return packets