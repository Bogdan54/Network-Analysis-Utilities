import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class IPAnalysisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("IP Analysis Tool")

        self.ip_addresses = tk.StringVar()
        self.file_path = tk.StringVar()

        tk.Label(master, text="Enter IP Addresses (one per line):").pack(pady=10)
        self.ip_text = tk.Text(master, height=5, width=40)
        self.ip_text.pack(pady=10)

        tk.Button(master, text="Choose File", command=self.choose_file).pack(pady=10)
        tk.Button(master, text="Run Analysis", command=self.run_analysis).pack(pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_path.set(file_path)

    def run_analysis(self):
        ip_addresses = self.ip_text.get("1.0", "end-1c").strip()  # Get the content of the Text widget
        file_path = self.file_path.get()

        if not ip_addresses or not file_path:
            messagebox.showerror("Error", "Please enter IP addresses and choose a file.")
            return

        # Write IP addresses to the file
        with open(file_path, 'w') as file:
            file.write(ip_addresses)

        # Run the analysis script using bash
        script_command = f"python3 script.py {file_path}"
        try:
            result = subprocess.run(script_command, shell=True, check=True, capture_output=True, text=True)
            output = result.stdout.strip()

            # Display the results in a dialog box
            self.show_results_dialog(output)

        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error occurred while running the analysis script:\n{e}")

    def show_results_dialog(self, output):
        # Split the output into lines
        lines = output.split('\n')

        # Extract the best IP, results, and IPs list
        best_ip = lines[0]
        results = lines[1:]
        
        # Create a dialog box to display the results
        results_dialog = tk.Toplevel(self.master)
        results_dialog.title("Analysis Results")

        tk.Label(results_dialog, text="Best IP:").pack(pady=5)
        tk.Label(results_dialog, text=best_ip).pack(pady=5)

        tk.Label(results_dialog, text="Results:").pack(pady=5)
        
        # Display a list of IPs and results
        listbox = tk.Listbox(results_dialog, selectmode=tk.BROWSE, height=len(results), width=40)
        listbox.pack(pady=5)

        for result in results:
            listbox.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = IPAnalysisApp(root)
    root.mainloop()
