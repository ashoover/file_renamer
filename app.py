import os
import tkinter as tk
from tkinter import filedialog, messagebox


class FolderRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Renamer")

        self.base_path = tk.StringVar()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for folder path input
        tk.Label(self.root, text="Select Folder:").grid(row=0, column=0, padx=10, pady=5)
        self.folder_entry = tk.Entry(self.root, width=50, textvariable=self.base_path, state='readonly')
        self.folder_entry.grid(row=0, column=1, padx=10, pady=5)

        # Button to select folder
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=0, column=2, padx=10, pady=5)

        # Text widget for preview window
        self.preview_text = tk.Text(self.root, width=80, height=15)
        self.preview_text.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Button to apply changes
        self.go_button = tk.Button(self.root, text="Go", command=self.apply_changes)
        self.go_button.grid(row=2, column=0, columnspan=3, pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.base_path.set(folder_selected)
            self.show_preview()

    def show_preview(self):
        self.preview_text.delete(1.0, tk.END)  # Clear previous preview
        base_path = self.base_path.get()
        changes = []

        for root, dirs, files in os.walk(base_path):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                for filename in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, filename)

                    if os.path.isfile(file_path):
                        ext = os.path.splitext(filename)[1]
                        new_filename = directory + ext
                        changes.append(f"Renaming: {file_path} to {os.path.join(dir_path, new_filename)}")

        self.preview_text.insert(tk.END, "\n".join(changes))

    def apply_changes(self):
        base_path = self.base_path.get()
        if not os.path.isdir(base_path):
            messagebox.showerror("Error", "Please select a valid folder.")
            return

        for root, dirs, files in os.walk(base_path):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                for filename in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, filename)

                    if os.path.isfile(file_path):
                        ext = os.path.splitext(filename)[1]
                        new_filename = directory + ext
                        new_file_path = os.path.join(dir_path, new_filename)
                        try:
                            os.rename(file_path, new_file_path)
                        except Exception as e:
                            messagebox.showerror("Error", f"Failed to rename {file_path}: {e}")

        messagebox.showinfo("Success", "Files have been renamed successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FolderRenamerApp(root)
    root.mainloop()
