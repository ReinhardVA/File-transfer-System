from scapy.all import Packet, IntField, StrLenField, bind_layers, IP

class FilePacket(Packet):
    name = "FilePacket"
    fields_desc = [
        IntField("seq", 0),
        IntField("total", 0),
        IntField("length", 0),
        IntField("crc", 0),
        StrLenField("data", b"", length_from=lambda pkt: pkt.length)
    ]
bind_layers(IP, FilePacket, proto=250)