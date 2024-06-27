import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from PcapCompare.PcapDriver import PcapDriver
from PcapCompare.PcapComparisonPlotter import PcapComparisonPlotter

class PcapCompareGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PCAP Compare GUI")
        self.root.geometry("1280x720")  # Adjusted window size to 1280x720
        self.root.configure(bg='lightblue')

        # Set font style
        self.font_style = ("Tahoma", 10)

        # Create the main frames
        self.browse_frame = tk.Frame(root, bg='lightblue')
        self.browse_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.control_frame = tk.Frame(root, bg='lightblue')
        self.control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        self.plot_frame = tk.Frame(root, bg='lightblue')
        self.plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

        # Create UI elements in browse frame
        self.button1 = tk.Button(self.browse_frame, text="Browse", command=self.load_file1, bg='lightgreen', font=self.font_style, width=10, height=2)
        self.button1.grid(row=0, column=0, padx=10, pady=5)
        self.label1 = tk.Label(self.browse_frame, text="Select first PCAP file:", bg='lightblue', font=self.font_style)
        self.label1.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.button2 = tk.Button(self.browse_frame, text="Browse", command=self.load_file2, bg='lightgreen', font=self.font_style, width=10, height=2)
        self.button2.grid(row=1, column=0, padx=10, pady=5)
        self.label2 = tk.Label(self.browse_frame, text="Select second PCAP file:", bg='lightblue', font=self.font_style)
        self.label2.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Create UI elements in control frame
        self.compare_button = tk.Button(self.control_frame, text="Compare", command=self.compare_files, bg='lightgreen', font=self.font_style, width=10, height=2)
        self.compare_button.grid(row=0, column=0, padx=10, pady=5)

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset, bg='yellow', font=self.font_style, width=10, height=2)
        self.reset_button.grid(row=0, column=1, padx=10, pady=5)

        self.exit_button = tk.Button(self.control_frame, text="Exit", command=self.exit_program, bg='red', font=self.font_style, width=10, height=2)
        self.exit_button.grid(row=0, column=2, padx=10, pady=5)

        self.file1 = None
        self.file2 = None
        self.canvas = None
        self.toolbar = None

    def load_file1(self):
        self.file1 = filedialog.askopenfilename(title="Select first PCAP file")
        if self.file1:
            self.label1.config(text=f"First PCAP file: {self.file1}")

    def load_file2(self):
        self.file2 = filedialog.askopenfilename(title="Select second PCAP file")
        if self.file2:
            self.label2.config(text=f"Second PCAP file: {self.file2}")

    def compare_files(self):
        if not self.file1 or not self.file2:
            messagebox.showerror("Error", "Please select both PCAP files")
            return

        try:
            pcap_processor1 = PcapDriver(self.file1)
            pcap_processor2 = PcapDriver(self.file2)

            protocol_list1 = pcap_processor1.driver_pcap()
            protocol_list2 = pcap_processor2.driver_pcap()

            plotter = PcapComparisonPlotter(protocol_list1, protocol_list2)
            fig = plotter.plot_protocol_comparison()

            if self.canvas:
                self.canvas.get_tk_widget().pack_forget()
            if self.toolbar:
                self.toolbar.pack_forget()

            self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)
            self.toolbar.update()
            self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def reset(self):
        self.file1 = None
        self.file2 = None
        self.label1.config(text="Select first PCAP file:")
        self.label2.config(text="Select second PCAP file:")
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()
            self.canvas = None
        if self.toolbar:
            self.toolbar.pack_forget()
            self.toolbar = None
        messagebox.showinfo("Reset", "All selections have been reset.")

    def exit_program(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PcapCompareGUI(root)
    root.mainloop()
