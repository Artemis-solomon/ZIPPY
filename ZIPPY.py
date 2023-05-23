import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import shutil
import tarfile
import os


def compress_file():
    source_file = source_file_entry.get()
    destination_file = destination_file_entry.get()

    if not source_file or not destination_file:
        messagebox.showerror("Error", "Please provide source and destination file paths.")
        return

    try:
        with tarfile.open(destination_file, "w:gz") as tar:
            tar.add(source_file, arcname=os.path.basename(source_file))

        messagebox.showinfo("Success", "File compressed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error compressing file: {str(e)}")


def decompress_file():
    source_file = source_file_entry.get()
    destination_file = destination_file_entry.get()

    if not source_file or not destination_file:
        messagebox.showerror("Error", "Please provide source and destination file paths.")
        return

    try:
        with tarfile.open(source_file, "r:gz") as tar:
            tar.extractall(path=destination_file)

        messagebox.showinfo("Success", "File decompressed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error decompressing file: {str(e)}")


def browse_source_file():
    file_path = filedialog.askopenfilename()
    source_file_entry.delete(0, tk.END)
    source_file_entry.insert(0, file_path)


def browse_destination_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".tar.gz")
    destination_file_entry.delete(0, tk.END)
    destination_file_entry.insert(0, file_path)


# Create the main window
window = tk.Tk()
window.title("File Compression Tool")

# Create the source file label and entry
source_file_label = tk.Label(window, text="Source File:")
source_file_label.grid(row=0, column=0, padx=10, pady=10)
source_file_entry = tk.Entry(window)
source_file_entry.grid(row=0, column=1, padx=10, pady=10)
browse_source_button = tk.Button(window, text="Browse", command=browse_source_file)
browse_source_button.grid(row=0, column=2, padx=10, pady=10)

# Create the destination file label and entry
destination_file_label = tk.Label(window, text="Destination File:")
destination_file_label.grid(row=1, column=0, padx=10, pady=10)
destination_file_entry = tk.Entry(window)
destination_file_entry.grid(row=1, column=1, padx=10, pady=10)
browse_destination_button = tk.Button(window, text="Browse", command=browse_destination_file)
browse_destination_button.grid(row=1, column=2, padx=10, pady=10)

# Create the compress and decompress buttons
compress_button = tk.Button(window, text="Compress", command=compress_file)
compress_button.grid(row=2, column=0, padx=10, pady=10)
decompress_button = tk.Button(window, text="Decompress", command=decompress_file)
decompress_button.grid(row=2, column=1, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
