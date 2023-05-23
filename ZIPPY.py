#Written by: Aertemis Solomon
#ZIPPY: Python .tar File Compressor and File Extraction

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
#function is triggered when the "Compress" button is clicked, and the `decompress_file()` function is triggered when the "Decompress" button is clicked.

#In the `compress_file()` function:
#1. The source file and destination file paths are obtained from the entry fields.
#2. It checks if both the source and destination file paths are provided. If either is missing, an error message is displayed.
#3. If both paths are provided, it tries to compress the file using the `tarfile` module. The source file is added to a tar archive with the specified destination file path.
#4. If any errors occur during compression, an error message is displayed.

#In the `decompress_file()` function:
#1. The source file and destination file paths are obtained from the entry fields.
#2. It checks if both the source and destination file paths are provided. If either is missing, an error message is displayed.
#3. If both paths are provided, it tries to decompress the file using the `tarfile` module. The contents of the tar archive are extracted to the specified destination folder.
#4. If any errors occur during decompression, an error message is displayed.

#The `browse_source_file()` and `browse_destination_file()` functions open file dialogs to allow the user to browse and select the source and destination files respectively.

#The program creates a graphical user interface (GUI) window using Tkinter's widgets such as labels, entry fields, and buttons. The GUI provides an intuitive way for users to input file paths and trigger the compression or decompression process.

#To run the program, ensure you have Python and Tkinter installed. Save the code to a Python file (e.g., `compression_tool.py`) and execute it using `python compression_tool.py` in your terminal or command prompt.

#Upon running the program, a window will appear with fields to enter the source file path, destination file path, and buttons to compress or decompress the file. Clicking the "Browse" buttons allows you to select the files using a file dialog. After providing the necessary file paths, click the "Compress" or "Decompress" button to perform the corresponding operation.

#Error handling is incorporated to display informative error messages if any issues occur during compression or decompression.

#This Python program provides beginners with a basic understanding of how to create a file compression tool with a GUI using Tkinter. Feel free to explore and enhance the program based on your requirements and preferences.

