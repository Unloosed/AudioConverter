import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Supported audio formats
SUPPORTED_FORMATS = ["wav", "mp3", "ogg", "flac", "aac"]

def convert_audio(files, output_format):
    for input_file in files:
        try:
            audio = AudioSegment.from_file(input_file)
            output_file = os.path.splitext(input_file)[0] + f".{output_format}"
            audio.export(output_file, format=output_format)
            print(f"Converted {input_file} to {output_file}")
        except CouldntDecodeError:
            print(f"Could not decode {input_file}. Skipping...")
        except Exception as e:
            print(f"An error occurred with {input_file}: {e}")

def reencode_audio(files, output_format):
    for input_file in files:
        try:
            audio = AudioSegment.from_file(input_file)
            output_file = os.path.join(os.path.dirname(input_file), "reencoded_" + os.path.splitext(os.path.basename(input_file))[0] + f".{output_format}")
            audio.export(output_file, format=output_format)
            print(f"Re-encoded {input_file} to {output_file}")
        except CouldntDecodeError:
            print(f"Could not decode {input_file}. Skipping...")
        except Exception as e:
            print(f"An error occurred with {input_file}: {e}")

def revert_reencode_name(folder_path):
    for filename in os.listdir(folder_path):
        if filename.startswith("reencoded_"):
            new_filename = filename[len("reencoded_"):]
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)

            if os.path.exists(new_file):
                print(f"Cannot rename {old_file} to {new_file} because the target file already exists. Skipping...")
            else:
                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} to {new_file}")

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.wav *.mp3 *.ogg *.flac *.aac")])
    if not files:
        messagebox.showerror("Error", "No files selected. Please select valid audio files.")
        return None
    return files

def perform_action(action):
    files = select_files()
    if not files:
        return

    output_format = output_format_var.get()
    if output_format not in SUPPORTED_FORMATS:
        messagebox.showerror("Error", "Unsupported format. Please choose from the supported formats.")
        return

    if action == 'convert':
        convert_audio(files, output_format)
        messagebox.showinfo("Info", "Conversion complete!")
    elif action == 'reencode':
        reencode_audio(files, output_format)
        messagebox.showinfo("Info", "Re-encoding complete!")
    elif action == 'revert':
        folder_path = filedialog.askdirectory()
        if not folder_path:
            messagebox.showerror("Error", "Invalid folder path. Please select a valid directory.")
            return
        revert_reencode_name(folder_path)
        messagebox.showinfo("Info", "Renaming complete!")

# GUI setup
root = tk.Tk()
root.title("Audio Processor")

# Output format selection
tk.Label(root, text="Select Output Format:").grid(row=0, column=0, padx=10, pady=10, columnspan=2)
output_format_var = tk.StringVar(value=SUPPORTED_FORMATS[0])
for i, format in enumerate(SUPPORTED_FORMATS):
    tk.Radiobutton(root, text=format, variable=output_format_var, value=format).grid(row=1, column=i, padx=5, pady=10)

# Action buttons
tk.Button(root, text="Convert", command=lambda: perform_action('convert')).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Re-encode", command=lambda: perform_action('reencode')).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Revert", command=lambda: perform_action('revert')).grid(row=2, column=2, padx=10, pady=10)
tk.Button(root, text="Quit", command=root.quit).grid(row=2, column=3, padx=10, pady=10)

# Add padding to the main window
for widget in root.winfo_children():
    widget.grid_configure(padx=10, pady=10)

root.mainloop()
