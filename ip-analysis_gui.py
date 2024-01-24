import tkinter as tk
from tkinter import filedialog
import subprocess

class IPAnalysisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("IP Analysis Tool")

        self.ip_addresses = tk.StringVar()
        self.file_path = tk.StringVar()

        tk.Label(master, text="Enter IP Addresses (comma-separated):").pack(pady=10)
        self.ip_entry = tk.Entry(master, textvariable=self.ip_addresses, width=40)
        self.ip_entry.pack(pady=10)

        tk.Button(master, text="Choose File", command=self.choose_file).pack(pady=10)
        tk.Button(master, text="Run Analysis", command=self.run_analysis).pack(pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_path.set(file_path)

    def run_analysis(self):
        ip_addresses = self.ip_addresses.get()
        file_path = self.file_path.get()

        if not ip_addresses or not file_path:
            tk.messagebox.showerror("Error", "Please enter IP addresses and choose a file.")
            return

        # Write IP addresses to the file
        with open(file_path, 'w') as file:
            file.write(ip_addresses)

        # Run the analysis script using a shell
        script_command = f"sh /home/bogdan54/Documents/Projects/ip_test/script.sh {file_path}"
        try:
            subprocess.run(script_command, shell=True, check=True)
            tk.messagebox.showinfo("Success", "Analysis completed successfully!")
        except subprocess.CalledProcessError:
            tk.messagebox.showerror("Error", "Error occurred while running the analysis script.")

if __name__ == "__main__":
    root = tk.Tk()
    app = IPAnalysisApp(root)
    root.mainloop()
