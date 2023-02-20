import pyshark
import collections
import numpy as np
import matplotlib.pyplot as plt


def read_pcap(file_path):
    protocol_attrs = {
        'TCP': 'tcp',
        'UDP': 'udp',
        'SSL/TLS': 'ssl',
        'HTTP': 'http',
        'SMTP': 'smtp'
    }
    protocol_list = []
    with pyshark.FileCapture(file_path) as pcap_scrap:
        for packet in pcap_scrap:
            try:
                protocol_search = packet.transport_layer
            except AttributeError:
                # Ignore packets that don't contain transport layer information
                pass
            else:
                protocol_list.append(protocol_search)

            for protocol_name, protocol_attr in protocol_attrs.items():
                try:
                    protocol_search = getattr(packet, protocol_attr)
                    protocol_list.append(protocol_name)
                except AttributeError:
                    pass

    return protocol_list


pcap_file1 = 'static/pcap/file1.pcapng'
pcap_file2 = 'static/pcap/file2.pcapng'

protocol_list1 = read_pcap(pcap_file1)
protocol_list2 = read_pcap(pcap_file2)

pcap_data1 = collections.Counter(protocol_list1)
pcap_data2 = collections.Counter(protocol_list2)

# Combine the keys from both dictionaries and remove duplicates
keys = list(set(list(pcap_data1.keys()) + list(pcap_data2.keys())))


# Show protocol list frequency
plt.style.use('ggplot')

x_pos = np.arange(len(list(pcap_data1.keys())))
y_pos = np.arange(len(list(pcap_data2.keys())))

bar_width = 0.35

fig, ax = plt.subplots()

graph1 = ax.bar(x_pos, list(pcap_data1.values()), bar_width, alpha=0.5, color='b', label='PCAP File 1')
graph2 = ax.bar(y_pos + bar_width, list(pcap_data2.values()), bar_width, alpha=0.5, color='r', label='PCAP File 2')

ax.set_xticks(x_pos + bar_width / 2)
ax.set_xticklabels(keys)

ax.legend()

plt.title("Packets comparison")
plt.ylabel("Frequency")
plt.xlabel("Protocol Name")
plt.savefig("static/graph/Pcap.png")
plt.show()
