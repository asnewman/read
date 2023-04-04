import pyttsx3
import tkinter as tk
import subprocess

result = None

def on_read_button_click():
    global result
    text = text_input.get("1.0", tk.END)
    result = subprocess.Popen(["python", "speak.py", text])

def on_stop_button_click():
    global result
    result.kill()

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Text Reader")

    # Create and pack the text input
    text_input = tk.Text(root, width=50, height=50)
    text_input.pack(pady=10)

    # Create and pack the Read button
    read_button = tk.Button(root, text="Read", command=on_read_button_click)
    read_button.pack(pady=5)

    # Create and pack the Read button
    stop_button = tk.Button(root, text="Stop", command=on_stop_button_click)
    stop_button.pack(pady=5)

    # Start the main event loop
    root.mainloop()
