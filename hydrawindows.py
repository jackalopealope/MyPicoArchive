# ... (existing code)

class Popup:
    def __init__(self, master):
        # ... (existing code)

        # Store a reference to the popup window
        self.popup = tk.Toplevel(master)
        # ... (existing code)

        self.close_popup()  # Automatically close the popup when it is created

    def close_popup(self):
        if hasattr(self, 'popup') and self.popup.winfo_exists():  # Check if 'popup' attribute exists and window still exists
            self.popup.destroy()  # Destroy the popup window

        # ... (existing code)

# ... (rest of the script remains unchanged)
