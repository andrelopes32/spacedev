import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%Y-%m-%d %H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Live Timestamp")

# Create and pack the label
label = tk.Label(root, font=('Helvetica', 40), fg='blue')
label.pack(padx=20, pady=20)

# Start the time update loop
update_time()

# Run the application
root.mainloop()
