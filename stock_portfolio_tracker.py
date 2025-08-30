08.30 10:48 AM
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Portfolio file ---
PORTFOLIO_FILE = "portfolio.csv"

# --- Load or create portfolio ---
def load_portfolio():
    if os.path.exists(PORTFOLIO_FILE):
        return pd.read_csv(PORTFOLIO_FILE)
    else:
        df = pd.DataFrame(columns=["Symbol", "Quantity", "Buy Price"])
        df.to_csv(PORTFOLIO_FILE, index=False)
        return df

def save_portfolio(df):
    df.to_csv(PORTFOLIO_FILE, index=False)

# --- Add stock ---
def add_stock(symbol, quantity, buy_price):
    df = load_portfolio()
    new_row = pd.DataFrame([[symbol.upper(), quantity, buy_price]],
                           columns=["Symbol", "Quantity", "Buy Price"])
    df = pd.concat([df, new_row], ignore_index=True)
    save_portfolio(df)

# --- Remove stock ---
def remove_stock(symbol):
    df = load_portfolio()
    df = df[df["Symbol"] != symbol.upper()]
    save_portfolio(df)

# --- Get stock performance ---
def get_stock_data():
    portfolio = load_portfolio()
    data = []

    for _, stock in portfolio.iterrows():
        ticker = yf.Ticker(stock["Symbol"])
        try:
            current_price = ticker.history(period="1d")["Close"].iloc[-1]
        except Exception:
            current_price = stock["Buy Price"]  # fallback if data unavailable

        invested = stock["Quantity"] * stock["Buy Price"]
        current_value = stock["Quantity"] * current_price
        profit_loss = current_value - invested
        percent_change = (profit_loss / invested) * 100 if invested > 0 else 0

        data.append({
            "Symbol": stock["Symbol"],
            "Quantity": stock["Quantity"],
            "Buy Price": stock["Buy Price"],
            "Current Price": round(current_price, 2),
            "Invested": round(invested, 2),
            "Current Value": round(current_value, 2),
            "P/L": round(profit_loss, 2),
            "P/L %": round(percent_change, 2)
        })

    return pd.DataFrame(data)

# --- Show portfolio summary ---
def show_portfolio():
    df = get_stock_data()
    if df.empty:
        print("\n Portfolio is empty. Add stocks first!\n")
        return

    print("\n===  Stock Portfolio Tracker ===\n")
    print(df.to_string(index=False))

    print("\n Total Invested:", round(df["Invested"].sum(), 2))
    print(" Current Value :", round(df["Current Value"].sum(), 2))
    print(" Total P/L     :", round(df["P/L"].sum(), 2), 
          f"({round((df['Current Value'].sum()-df['Invested'].sum())/df['Invested'].sum()*100,2)}%)")

    # Plot portfolio allocation
    df.plot.pie(y="Current Value", labels=df["Symbol"], autopct="%1.1f%%", figsize=(5,5))
    plt.title("Portfolio Allocation")
    plt.ylabel("")  # Hide ylabel
    plt.show()

# --- Main Menu ---
def main():
    while True:
        print("\n===== MENU =====")
        print("1. Show Portfolio")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_portfolio()
        elif choice == "2":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            qty = int(input("Enter quantity: "))
            buy = float(input("Enter buy price: "))
            add_stock(symbol, qty, buy)
            print(f"✅ {symbol} added to portfolio.")
        elif choice == "3":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
            print(f"❌ {symbol} removed from portfolio.")
        elif choice == "4":
            print(" Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
​    main()

