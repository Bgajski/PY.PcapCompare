PCAP Compare GUI

# Description
This project provides a GUI application for comparing network protocols from two PCAP files. Built with Python, it uses Tkinter for the GUI, Matplotlib for visualizing protocol comparisons, Pandas for data manipulation, Seaborn for creating statistical plots, and Pyshark for parsing PCAP files. This tool offers a user-friendly way to analyze and visualize differences in network protocol usage between two PCAP files.

# Features
Load PCAP Files: Select two PCAP files using the "Browse" buttons

Compare Protocols: Analyze the selected PCAP files and display a bar plot comparing the protocols

Reset and Exit: Clear selections and the plot with "Reset", and close the application with "Exit"

# Required Libraries

tkinter: For creating the GUI application

matplotlib: For generating the bar plots

seaborn: For enhancing the visual appeal of the plots

pandas: For data manipulation and analysis

pyshark: For parsing and extracting data from PCAP files

# Code Overview

PCAP Compare GUI: The main GUI application for selecting PCAP files and displaying protocol comparison plots

PCAP Driver: Class for loading and parsing PCAP files using Pyshark

PCAP Packet Driver: Class for extracting protocol information from individual packets

PCAP Protocol Extractor: Base class for protocol-specific extractors

PCAP Comparison Plotter: Class for generating protocol comparison plots using Matplotlib and Seaborn

# License
This project is licensed under the MIT License.


