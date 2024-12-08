import tkinter as tk

class CallReceiverApp:
    def __init__(self, root, data, connection):
        self.data = data
        self.root = root
        self.connection = connection
        self.root.title("Company Call Receiver")
        self.root.geometry("400x200")
        self.root.configure(bg="#2E2E2E")  # Dark background

        # Create a card-like frame for the incoming call
        self.card_frame = tk.Frame(root, bg="#3E3E3E", bd=2, relief=tk.RAISED)
        self.card_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Incoming Call Label
        self.caller_name_label = tk.Label(
            self.card_frame, text="No Incoming Call", font=("Arial", 16), bg="#3E3E3E", fg="white"
        )
        self.caller_name_label.pack(pady=20)

        # Buttons for attending or declining the call
        self.button_frame = tk.Frame(self.card_frame, bg="#3E3E3E")
        self.button_frame.pack(pady=10)

        self.attend_button = tk.Button(
            self.button_frame, text="Attend", command=self.attend_call, bg="#4CAF50", fg="white", width=10
        )
        self.attend_button.pack(side=tk.LEFT, padx=10)

        self.decline_button = tk.Button(
            self.button_frame, text="Decline", command=self.decline_call, bg="#F44336", fg="white", width=10
        )
        self.decline_button.pack(side=tk.RIGHT, padx=10)

        # Simulate an incoming call
        self.simulate_incoming_call()

    def simulate_incoming_call(self):
        self.caller_name_label.config(text=f"Incoming Call From: {self.data[0]}")

    def attend_call(self):
        caller_name = self.caller_name_label.cget("text").replace("Incoming Call From: ", "")
        print(f"Attending call from: {caller_name}")
        from streaming import TextCameraClient
        client = TextCameraClient(self.data[1], self.data[2])
        client.start_stream()
        self.root.destroy()

    def decline_call(self):
        self.root.destroy()
        self.connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = CallReceiverApp(root)
    root.mainloop()