# Network protocol comparison CLI program

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pcap_driver import PcapDriver


def plot_comparisons(file1, file2, output_path_protocol):
    pcap_processor1 = PcapDriver(file1)
    pcap_processor2 = PcapDriver(file2)

    protocol_list1 = pcap_processor1.driver_pcap()
    protocol_list2 = pcap_processor2.driver_pcap()

    plot_protocol_comparison(protocol_list1, protocol_list2, output_path_protocol)


def plot_protocol_comparison(protocol_list1, protocol_list2, output_path_protocol):
    # set DataFrame grid
    df1 = pd.DataFrame(protocol_list1)
    df2 = pd.DataFrame(protocol_list2)
    df1['File'] = 'File 1'
    df2['File'] = 'File 2'
    df = pd.concat([df1, df2], ignore_index=True)
    df_melted = df.melt(id_vars=['File'], var_name='Protocol', value_name='Presence')

    # set Seaborn graph
    sns.set_theme(style="whitegrid")
    sns.set(rc={'figure.figsize': (12, 8)})
    ax = sns.countplot(data=df_melted, x='Protocol', hue='File')
    ax.set_title('Protocol Comparison')
    ax.set_ylabel('Metric')
    ax.set_xlabel('Protocol')

    # save and close
    os.makedirs(os.path.dirname(output_path_protocol), exist_ok=True)
    plt.savefig(output_path_protocol)
    plt.close()


if __name__ == "__main__":
    pcap_file1 = "static/pcap/file1.pcapng"
    pcap_file2 = "static/pcap/file2.pcapng"
    output_graph_protocol = "static/graph/pcap_protocol_comparison.png"
    plot_comparisons(pcap_file1, pcap_file2, output_graph_protocol)
