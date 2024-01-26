import tkinter as tk
import tkinter.ttk as ttk
import random
import pyttsx3
import keyboard

# ... (rest of the script remains unchanged)

# Define a class for the popup window
class Popup:

    def __init__(self, master):
        # ... (existing code)

        self.close_popup()  # Automatically close the popup when it is created

    def close_popup(self):
        self.popup.destroy()  # Destroy the popup window
        # ... (existing code)

        if keyboard.is_pressed('e') and keyboard.is_pressed('n') and keyboard.is_pressed('d'):
            return  # Break out of the method if 'E', 'N', and 'D' are held down

        Popup(self.master)    # Create 2 new instances of the Popup class
        Popup(self.master)

        rate = motore.getProperty('rate')  # Get the current speech rate
        motore.setProperty('rate', rate)  # Set the speech rate

        motore.say(testi[random.randint(0, len(testi)-1)])  # Generate a random index and speak a random message from the list
        motore.runAndWait()  # Run the text-to-speech synthesis engine

# ... (rest of the script remains unchanged)

root = tk.Tk()  # Create the root window
root.withdraw()  # Hide the root window

popup = Popup(root)  # Create an instance of the Popup class with the root window

root.mainloop()  # Start the main event loop of the tkinter application
