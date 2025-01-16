import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import tempfile
import sys


class OrbitIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Orbit IDE")
        self.create_widgets()

    def create_widgets(self):
        # Create menu bar
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_command(label="Exit", command=self.exit_ide)
        menu_bar.add_cascade(label="File", menu=file_menu)

        run_menu = tk.Menu(menu_bar, tearoff=0)
        run_menu.add_command(label="Run", command=self.run_orbit_code)
        menu_bar.add_cascade(label="Run", menu=run_menu)

        self.root.config(menu=menu_bar)

        # Create text editor
        self.text_editor = tk.Text(self.root, wrap=tk.WORD)
        self.text_editor.pack(fill=tk.BOTH, expand=1)

    def open_file(self):
        """Open a .orbit file."""
        file_path = filedialog.askopenfilename(filetypes=[("Orbit Files", "*.orbit")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, content)
                self.root.title(f"Orbit IDE - {os.path.basename(file_path)}")
                self.current_file_path = file_path
            except Exception as e:
                messagebox.showerror("Error", f"Cannot open file: {e}")

    def save_file(self):
        """Save the current file."""
        if hasattr(self, 'current_file_path') and self.current_file_path:
            try:
                with open(self.current_file_path, 'w') as file:
                    file.write(self.text_editor.get(1.0, tk.END).strip())
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot save file: {e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        """Save the current file as a new file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".orbit", filetypes=[("Orbit Files", "*.orbit")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_editor.get(1.0, tk.END).strip())
                self.current_file_path = file_path
                self.root.title(f"Orbit IDE - {os.path.basename(file_path)}")
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot save file: {e}")

    def run_orbit_code(self):
        """Run the Orbit code from the editor."""
        orbit_code = self.text_editor.get(1.0, tk.END).strip()
        if not orbit_code:
            messagebox.showerror("Error", "No code to run.")
            return

        # Run Orbit code by writing it to a temp file and calling main.py
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".orbit") as temp_file:
                temp_file.write(orbit_code.encode('utf-8'))
                temp_file.close()

                # Use sys.executable to dynamically find the correct Python executable
                result = subprocess.run(
                    [sys.executable, 'main.py', temp_file.name],
                    text=True,
                    capture_output=True
                )
                if result.returncode == 0:
                    messagebox.showinfo("Orbit Output", result.stdout)
                else:
                    messagebox.showerror("Orbit Error", result.stderr)

            # Clean up temp file
            os.remove(temp_file.name)

        except Exception as e:
            messagebox.showerror("Error", f"Cannot run code: {e}")

    def exit_ide(self):
        """Exit the IDE."""
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = OrbitIDE(root)
    root.mainloop()

