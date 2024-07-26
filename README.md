# PCAP Compare 
Python protocol comparison gui program for Wireshark PCAPs

# Description
This project provides a GUI application for comparing network protocols from two PCAP files. Built with Python, it uses Tkinter for the GUI, Matplotlib for visualizing protocol comparisons, Pandas for data manipulation, Seaborn for creating statistical plots, and Pyshark for parsing PCAP files. This tool offers a user-friendly way to analyze and visualize differences in network protocol usage between two PCAP files.

# Code Overview
PCAP Compare GUI: The main GUI application for selecting PCAP files and displaying protocol comparison plots
PCAP Driver: Class for loading and parsing PCAP files using Pyshark
PCAP Packet Driver: Class for extracting protocol information from individual packets
PCAP Protocol Extractor: Base class for protocol-specific extractors
PCAP Comparison Plotter: Class for generating protocol comparison plots using Matplotlib and Seaborn

# Required Libraries
tkinter: Creating the GUI application
matplotlib: Generating the bar plots
seaborn: Enhancing the visual appeal of the plots
pandas: Data manipulation and analysis
pyshark: Parsing and extracting data from PCAP files

# License
This project is licensed under the MIT License.
