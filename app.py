import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    # Update every 1000 ms (1 second)
    root.after(1000, update_time)

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Label to display time
label = tk.Label(root, font=("Arial", 48), bg="black", fg="lime")
label.pack(pady=20)

# Start updating time
update_time()

root.mainloop()
