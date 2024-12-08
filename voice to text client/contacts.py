import tkinter as tk
import streaming

class ContactApp(tk.Tk):
    server = None
    def __init__(self, data, server):
        super().__init__()
        self.data = data
        ContactApp.server = server
        self.title("Contact List")
        self.geometry("400x600")  # Initial size
        self.resizable(True, True)  # Allow resizing
        self.configure(bg="#1E1E1E")
        
        # Header
        self.header = tk.Frame(self, bg="#4CAF50")
        self.header.pack(fill=tk.X)
        self.header_label = tk.Label(self.header, text="Contact List", font=("Segoe UI", 18, "bold"), bg="#4CAF50", fg="white")
        self.header_label.pack(pady=10)

        # Create a frame for contact cards
        self.cards_frame = tk.Frame(self, bg="#1E1E1E")
        self.cards_frame.pack(expand=True, fill=tk.BOTH)

        # Create and place contact cards in a grid layout
        self.create_contact_cards()

    def create_contact_cards(self):
        # Calculate the number of cards and layout
        num_cards = len(self.data)
        num_columns = 1  # You can change this to set the number of columns
        for index, contact_info in enumerate(self.data):
            card = self.ContactCard(self.cards_frame, contact_info)  # Use inner class for contact card
            card.grid(row=index // num_columns, column=index % num_columns, pady=10, padx=20, sticky="ew")  # Use grid for flexible layout

        # Configure grid to make it responsive
        for i in range(num_cards):
            self.cards_frame.grid_rowconfigure(i, weight=1)  # Allow rows to expand
        self.cards_frame.grid_columnconfigure(0, weight=1)  # Allow column to expand

        # Update window size based on the number of cards
        self.update_window_size(num_cards)

    def update_window_size(self, num_cards):
        # Calculate the required height based on the number of rows
        num_rows = (num_cards + 1) // 1  # Assuming 1 column for simplicity
        card_height = 100  # Approximate height of each card
        header_height = 50  # Height of the header
        new_height = header_height + (num_rows * card_height) + 20  # Add some padding
        new_width = 400  # Fixed width for the window
        self.geometry(f"{new_width}x{new_height}")  # Update window size

    class ContactCard(tk.Frame):
        def __init__(self, master, contact_info):
            super().__init__(master, bd=2, relief=tk.RAISED, padx=20, pady=20, bg="#2C2C2C", width=354)
            self.contact_info = contact_info
            
            # Name label
            self.name_label = tk.Label(self, text=contact_info[0], font=("Segoe UI", 16, "bold"), bg="#2C2C2C", fg="#FFFFFF")
            self.name_label.pack(side=tk.LEFT, padx=(0, 10), pady=(0, 5))  # Align to the left with padding

            # Call button
            self.call_button = tk.Button(self, text="📞 Call", command=self.call_contact, bg="#4CAF50", fg="white", 
                                          font=("Segoe UI", 16), borderwidth=0, relief=tk.FLAT, height=1, width=10)
            self.call_button.pack(side=tk.RIGHT, pady=(0, 5))  # Align to the right
            self.call_button.bind("<Enter>", lambda e: self.call_button.config(bg="#45a049"))
            self.call_button.bind("<Leave>", lambda e: self.call_button.config(bg="#4CAF50"))

        def call_contact(self):
            # Print contact information to the console
            ContactApp.server.pop = False
            client = streaming.TextCameraClient(self.contact_info[1], self.contact_info[2])
            client.start_stream()
            print(f"Calling {self.contact_info[0]}...")
            print(f"IP Address: {self.contact_info[1]}")
            print(f"Port: {self.contact_info[2]}")

# Example usage:
if __name__ == "__main__":
    contacts = [
        ("Alice", "192.168.1.1", 8000),
        ("Bob", "192.168.1.2", 8001),
        ("Charlie", "192.168.1.3", 8002)
    ]
    app = ContactApp(contacts)
    app.mainloop()