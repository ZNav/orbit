import tkinter as tk
from tkinter import messagebox
import subprocess

# Orbit interpreter function (we will use the previous code for parsing and execution)
def run_orbit_code(code):
    try:
        # Save the code to a temporary .orbit file
        with open("temp.orbit", "w") as f:
            f.write(code)

        # Execute the orbit interpreter script (assuming main.py is in the same directory)
        result = subprocess.run(['python3', 'main.py', 'temp.orbit'], capture_output=True, text=True)

        # Check if there was any error in the execution
        if result.returncode != 0:
            return result.stderr
        else:
            return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"


# Simple syntax highlighting for Orbit code
def highlight_syntax(event=None):
    code = code_text.get("1.0", "end-1c")
    
    # Simple example of syntax highlighting for operators (add more as needed)
    code_text.tag_remove("keyword", "1.0", "end")
    code_text.tag_add("keyword", "1.0", "end")
    for keyword in ['p', 's', 'g', '=', '+', '-', '/', '*', '|', '&', '^', '0', '1', '\\']:
        start_idx = "1.0"
        while True:
            start_idx = code_text.search(keyword, start_idx, stopindex="end")
            if not start_idx: break
            end_idx = f"{start_idx}+{len(keyword)}c"
            code_text.tag_add("keyword", start_idx, end_idx)
            start_idx = end_idx

    # Update color for syntax highlighting
    code_text.tag_configure("keyword", foreground="blue")


# Run the Orbit code when the "Run" button is clicked
def on_run_button_click():
    code = code_text.get("1.0", "end-1c")
    if not code.strip():
        messagebox.showwarning("Warning", "Please enter some Orbit code.")
        return

    output = run_orbit_code(code)
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("Orbit IDE")
root.geometry("800x600")

# Code editor section
code_text = tk.Text(root, wrap=tk.WORD, height=20, width=80, font=("Courier", 12))
code_text.pack(pady=10)

# Add syntax highlighting trigger
code_text.bind("<KeyRelease>", highlight_syntax)

# Run button
run_button = tk.Button(root, text="Run", command=on_run_button_click, width=20, height=2, bg="green", fg="white")
run_button.pack(pady=10)

# Output console section
output_label = tk.Label(root, text="Output:", font=("Courier", 14))
output_label.pack()

output_text = tk.Text(root, wrap=tk.WORD, height=10, width=80, font=("Courier", 12), bg="black", fg="white")
output_text.pack(pady=10)
output_text.config(state=tk.DISABLED)

# Start the Tkinter main loop
root.mainloop()

