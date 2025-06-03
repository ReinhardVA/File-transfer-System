import zlib
from protocol.packet import FilePacket

received_fragments = {}

def handle_packet(pkt):
    if FilePacket in pkt:
        frag = pkt[FilePacket]
        if zlib.crc32(frag.data) & 0xFFFFFFFF == frag.crc:
            received_fragments[frag.seq] = frag.data
            print(f"Received valid fragment {frag.seq} / {frag.total - 1}")
        else:
            print(f"Corrupt fragment {frag.seq} - CRC mismatch")
            return
        
        if len(received_fragments) == frag.total:
            output_path = "received_file.out"
            with open(output_path, "wb") as f:
                for i in range(frag.total):
                    f.write(received_fragments[i])
            print(f"File successfully reassembled to {output_path}.")