import pyshark
from .PcapPacketDriver import PcapPacketDriver

class PcapDriver:
    def __init__(self, file_path):
        self.file_path = file_path

    def driver_pcap(self):
        protocol_list = []
        try:
            with pyshark.FileCapture(self.file_path) as pcap_scrap:
                for packet in pcap_scrap:
                    driver = PcapPacketDriver(packet)
                    protocol_data = driver.packet_driver()
                    protocol_list.append(protocol_data)
        except Exception as e:
            print(f"Error processing pcap file: {e}")
        print(f"Processed {len(protocol_list)} packets from {self.file_path}")
        return protocol_list
