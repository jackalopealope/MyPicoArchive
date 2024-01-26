import tkinter as tk
import tkinter.ttk as ttk
import random
import pyttsx3
import keyboard

def create_popup(master):
    popup = tk.Toplevel(master)
    popup.title("Try to catch me!")

    popup.protocol("WM_DELETE_WINDOW", lambda: close_popup(popup, master))
    popup.bind("<Unmap>", lambda event, p=popup: clone_popup(p))

    message_label = ttk.Label(popup, text="Try to catch me!", font=("Helvetica", 18, "bold"), foreground="white", background="black")
    message_label.pack(pady=20)

    close_button = ttk.Button(popup, text="Catch!", command=lambda p=popup: catch_popup(p, master))
    close_button.pack(pady=10)

    popup.style = ttk.Style(popup)
    popup.style.configure("Popup.TFrame", background="black")
    popup.style.configure("TButton", background="white", font=("Helvetica", 14))
    popup.style.configure("TLabel", foreground="white", background="black", font=("Helvetica", 14))

    popup_frame = ttk.Frame(popup, style="Popup.TFrame", width=200)
    popup_frame.pack_propagate(0)
    popup_frame.pack()

    x = random.randint(0, master.winfo_screenwidth() - 200)
    y = random.randint(0, master.winfo_screenheight() - 100)
    popup.geometry("+{}+{}".format(x, y))

    popup.lift()  # Bring the popup to the front

def clone_popup(popup):
    create_popup(popup.master)

def catch_popup(popup, master):
    close_popup(popup, master)
    duplicate_popups(master, count=2)

def duplicate_popups(master, count):
    for _ in range(count):
        create_popup(master)

def close_all_popups(master):
    for popup in master.winfo_children():
        if isinstance(popup, tk.Toplevel):
            close_popup(popup, master)

def close_popup(popup, master):
    popup.destroy()
    duplicate_popups(master, count=2)

def main():
    root = tk.Tk()
    root.withdraw()

    create_popup(root)  # Create a popup on startup

    button = ttk.Button(root, text="Create Popup", command=lambda: create_popup(root))
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
