import requests
import tkinter as tk
from tkinter import PhotoImage

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set background color of the main window
        self.configure(bg='Red')

        self.title("Cardano Price")
        self.geometry("300x200")
        self.resizable(width=False, height=False)



        # Add an Image
        img = PhotoImage('141506.png')
        self.image_label = tk.Label(self, image=img)
        self.image_label.pack()

        # Add label to show the current price of Cardano
        self.price_label = tk.Label(self, text="Cardano: Loading...", font=("Arial", 24), fg='white', bg='Red')
        self.price_label.pack()

        self.update_price()

    def update_price(self):
        url = "https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=gbp"
        response = requests.get(url)
        print(response.text)  # Log the API response to see what data is being returned
        data = response.json()
        ada_price = data["cardano"]["gbp"]
        self.price_label.config(text=f"Price: £{ada_price:.2f}")
        self.after(1000, self.update_price)


if __name__ == "__main__":
    app = App()
    app.mainloop()






