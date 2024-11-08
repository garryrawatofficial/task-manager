import tkinter as tk
from tkinter import messagebox
import psutil

# Function to retrieve all running processes
def get_process_list():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_list.append((proc.info['pid'], proc.info['name']))
    return process_list

# Function to update the listbox with running processes
def update_process_list():
    # Clear the listbox before updating
    process_listbox.delete(0, tk.END)
    
    processes = get_process_list()
    for pid, name in processes:
        process_listbox.insert(tk.END, f"{pid} - {name}")

# Function to terminate a process
def terminate_process():
    try:
        selected_process = process_listbox.get(process_listbox.curselection())
        pid = int(selected_process.split(" ")[0])
        process = psutil.Process(pid)
        process.terminate()  # Terminate the selected process
        update_process_list()  # Update the list after termination
        messagebox.showinfo("Success", f"Process {pid} terminated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error terminating process: {e}")

# Create the main application window
root = tk.Tk()
root.title("Task Manager")

# Create a listbox to display the processes
process_listbox = tk.Listbox(root, width=60, height=20, font=("Arial", 12))
process_listbox.pack(pady=20)

# Button to refresh the process list
refresh_button = tk.Button(root, text="Refresh List", width=20, height=2, font=("Arial", 12), command=update_process_list)
refresh_button.pack(pady=10)

# Button to terminate selected process
terminate_button = tk.Button(root, text="Terminate Process", width=20, height=2, font=("Arial", 12), command=terminate_process)
terminate_button.pack(pady=10)

# Initialize the process list
update_process_list()

# Start the Tkinter event loop
root.mainloop()
