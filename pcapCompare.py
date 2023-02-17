import collections
import numpy as np
import matplotlib.pyplot as plt
import pyshark

def read_pcap(file_path):
    protocol_list = []
    pcap_scrap = pyshark.FileCapture(file_path, only_summaries=True)
    for packet in pcap_scrap:
        line = str(packet)
        formatted_line = line.split(" ")
        protocol_list.append(formatted_line[4])
    return collections.Counter(protocol_list), protocol_list

pcap_data1, protocol_list1 = read_pcap('static/images/file1.pcap')
pcap_data2, protocol_list2 = read_pcap('static/images/file2.pcap')

# Show protocol list frequency
plt.style.use('ggplot')

x_pos = np.arange(len(list(pcap_data1.keys())))
y_pos = np.arange(len(list(pcap_data2.keys())))

plt.bar(x_pos, list(pcap_data1.values()), align='center', alpha=0.5, color=['b', 'g', 'r', 'c', 'm'])
plt.xticks(x_pos, list(pcap_data1.keys()))

plt.bar(y_pos, list(pcap_data2.values()), align='center', alpha=0.5, color=['black'])
plt.xticks(y_pos, list(pcap_data2.keys()))

plt.title("Packets comparison")
plt.ylabel("Frequency")
plt.xlabel("Protocol Name")
plt.savefig("static/graph/Pcap.png")
plt.show()
