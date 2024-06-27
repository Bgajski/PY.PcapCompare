import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class PcapComparisonPlotter:
    def __init__(self, protocol_list1, protocol_list2):
        self.protocol_list1 = protocol_list1
        self.protocol_list2 = protocol_list2

    def plot_protocol_comparison(self):
        # lists of dictionaries to DataFrames
        df1 = pd.DataFrame(self.protocol_list1)
        df2 = pd.DataFrame(self.protocol_list2)
        df1['File'] = 'File 1'
        df2['File'] = 'File 2'
        df = pd.concat([df1, df2], ignore_index=True)

        # form suitable for bar plot
        df_melted = df.melt(id_vars=['File'], var_name='Protocol', value_name='Presence')

        # Aggregate presence counts
        df_counts = df_melted[df_melted['Presence'] == True].groupby(['File', 'Protocol']).size().reset_index(name='Count')

        palette = {"File 1": "blue", "File 2": "red"}

        sns.set_theme(style="whitegrid")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.barplot(data=df_counts, x='Protocol', y='Count', hue='File', palette=palette, ax=ax)
        ax.set_title('Protocol Comparison Bar Plot')
        ax.set_ylabel('Count')
        ax.set_xlabel('Protocol')

        return fig
