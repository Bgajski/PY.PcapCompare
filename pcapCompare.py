import collections
import numpy as np
import matplotlib.pyplot as plt
import pyshark

# scrap pcap
pcapScrap1 = pyshark.FileCapture('static\images\file1.pcap', only_summaries=True)
protocolList1 = []
for packet in pcapScrap1:
    line = str(packet)
    formattedLine = line.split(" ")
    print(formattedLine)
    protocolList1.append(formattedLine[4])  
    pcapData1 = collections.Counter(protocolList1)
print(protocolList1)

pcapScrap2 = pyshark.FileCapture('static\images\tile2.pcap', only_summaries=True)
protocolList2 = []
for packet in pcapScrap2:
    line = str(packet)
    formattedLine = line.split(" ")
    print(formattedLine)
    protocolList2.append(formattedLine[4]) 
    pcapData2 = collections.Counter(protocolList2)
print(protocolList2)

# Show protocol list frequency
plt.style.use('ggplot')

x_pos = np.arange(len(list(pcapData1.keys())))
y_pos = np.arange(len(list(pcapData2.keys())))

plt.bar(x_pos, list(pcapData1.values()), align='center', alpha=0.5, color=['b', 'g', 'r', 'c', 'm'])
plt.xticks(x_pos, list(pcapData2.keys()))

plt.bar(y_pos, list(pcapData1.values()), align='center', alpha=0.5, color=['black'])
plt.xticks(y_pos, list(pcapData2.keys()))

plt.title("Packets comparison")
plt.ylabel("Frequency")
plt.xlabel("Protocol Name")
plt.savefig("static\graph\Pcap.png")
plt.show()
