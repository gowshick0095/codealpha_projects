import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class StockPortfolioTracker:
    
    def __init__(self, master):
        self.master = master
        self.master.config(bg="LightYellow")
        self.master.title("Stock Portfolio Tracker")

        self.portfolio = {}  # Dictionary to store stock holdings (symbol: quantity)
        self.create_widgets()


    def create_widgets(self):
        self.instruction_label = tk.Label(self.master, text="Enter stock symbol and quantity", font=('Arial', 30),fg="red4",bg="LightYellow")
        self.instruction_label.place(x=500,y=65)

        self.symbol_label = tk.Label(self.master, text="Symbol  :" , font=('Arial', 30),fg="gray1",bg="LightYellow")
        self.symbol_label.place(x=50,y=210)

        self.symbol_entry = tk.Entry(self.master , font=('Arial', 20),fg="gray1",bg="LightYellow")
        self.symbol_entry.place(x=230,y=220)
        
        self.quantity_label = tk.Label(self.master, text="Quantity :" , font=('Arial', 30),fg="gray1",bg="LightYellow")
        self.quantity_label.place(x=50,y=265)

        self.quantity_entry = tk.Entry(self.master ,font=('Arial', 20),fg="gray1",bg="LightYellow")
        self.quantity_entry.place(x=230,y=280)

        self.add_button = tk.Button(self.master, text="Add to Portfolio", command=self.add_stock , font=('Arial', 30),fg="white",bg="SlateGray4")
        self.add_button.place(x=150,y=330)

        
    def add_stock(self):
        symbol = self.symbol_entry.get().upper()
        quantity = self.quantity_entry.get()

        if not symbol or not quantity.isdigit():
            messagebox.showerror("Invalid Input", "Please enter valid stock symbol and quantity.")
            return

        self.portfolio[symbol] = int(quantity)
        messagebox.showinfo("Success", f"{symbol} added to portfolio!")

        # Clear input fields

        self.symbol_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.view_portfolio()

    def view_portfolio(self):
        if not self.portfolio:
            messagebox.showinfo("Portfolio Empty", "Your portfolio is empty.")
        else:
            symbols = list(self.portfolio.keys())
            quantities = list(self.portfolio.values())
    
            # Plotting code (using matplotlib)

            self.fig = Figure(figsize=(5, 4), dpi=100)
            self.fig.clear()
            ax = self.fig.add_subplot(111)
            ax.bar(symbols, quantities)
            ax.set_xlabel('Stock Symbol')
            ax.set_ylabel('Quantity')
            ax.set_title('Stock Portfolio')
    
            # Embedding the graph in Tkinter        
                
            canvas = FigureCanvasTkAgg(self.fig, master= self.master)  
            canvas.draw()
            canvas.get_tk_widget().place(x=700,y=200)


if __name__ == "__main__":
    root = tk.Tk()
    stock_tracker = StockPortfolioTracker(root)
    root.mainloop()
