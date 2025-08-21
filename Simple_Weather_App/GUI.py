import tkinter as tk #the most common libary for GUIs
import WeatherApp as wa
root = tk.Tk()
root.title("Weather App")

# --- Fixed size and center ---
window_width = 500
window_height = 300

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# Set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Prevent resizing
root.resizable(False, False)

frame = tk.Frame(root, padx = 30, pady = 30)
frame.pack(expand = True)

prompt_label = tk.Label(frame, text="Enter a city:", font=("Arial", 15))
prompt_label.pack()

entry = tk.Entry(frame, width = 30, font=("Arial", 12))
entry.pack(pady = 10)

button = tk.Button(frame, text="Submit", command=wa.get_input, font=("Arial", 12),highlightbackground= "lightblue")
button.pack(pady=5)

label = tk.Label(frame, text="",wraplength = 450, justify = "left", font=("Arial", 12))
label.pack()

root.mainloop() #keeps the window open and responsive 