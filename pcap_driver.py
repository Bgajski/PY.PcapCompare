# Network protocol extraction driver

import pyshark
from protocol_extractor import *


class PacketDataDriver:
    def __init__(self, packet):
        self.packet = packet
        self.protocol_extractor = [
            TCP, UDP, SSL
        ]

    def packet_driver(self):
        protocol_data = {extractor.__name__: extractor(self.packet).extract()
                         for extractor in self.protocol_extractor}
        return protocol_data


class PcapDriver:
    def __init__(self, file_path):
        self.file_path = file_path

    def driver_pcap(self):
        protocol_list = []
        try:
            with pyshark.FileCapture(self.file_path) as pcap_scrap:
                for packet in pcap_scrap:
                    driver = PacketDataDriver(packet)
                    protocol_data = driver.packet_driver()
                    protocol_list.append(protocol_data)
        except Exception as e:
            print(f"Error processing pcap file: {e}")
        return protocol_list
