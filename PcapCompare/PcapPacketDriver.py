from .PcapProtocolExtractor import TCP, UDP, SSL

class PcapPacketDriver:
    def __init__(self, packet):
        self.packet = packet
        self.protocol_extractor = [TCP, UDP, SSL]

    def packet_driver(self):
        protocol_data = {extractor.__name__: extractor(self.packet).extract() for extractor in self.protocol_extractor}
        return protocol_data
