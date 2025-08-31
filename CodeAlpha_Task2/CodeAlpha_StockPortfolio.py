"""
Stock Portfolio Tracker - CodeAlpha Task 2
A simple stock portfolio tracker that calculates total investment based on predefined stock prices.

Author: [Your Name]
Project: CodeAlpha Python Programming Internship
Task: Task 2 - Stock Portfolio Tracker
"""

import csv
import os
from datetime import datetime

class StockPortfolioTracker:
    """A comprehensive stock portfolio tracking system"""
    
    def __init__(self):
        """Initialize the tracker with predefined stock prices"""
        
        # Hardcoded stock prices as per requirements
        self.stock_prices = {
            "AAPL": 185.50,    # Apple Inc.
            "TSLA": 248.75,    # Tesla Inc.
            "GOOGL": 138.25,   # Alphabet Inc.
            "MSFT": 348.50,    # Microsoft Corp.
            "AMZN": 142.80,    # Amazon.com Inc.
            "NVDA": 458.20,    # NVIDIA Corp.
            "META": 285.40,    # Meta Platforms Inc.
            "NFLX": 432.15,    # Netflix Inc.
            "PYPL": 58.90,     # PayPal Holdings Inc.
            "DIS": 91.30       # The Walt Disney Co.
        }
        
        self.portfolio = {}
        self.transaction_history = []
    
    def display_welcome(self):
        """Display welcome message and available stocks"""
        print("📊 STOCK PORTFOLIO TRACKER - CodeAlpha Task 2")
        print("=" * 60)
        print("Welcome to your personal stock portfolio tracker!")
        print("\n📈 Available Stocks and Current Prices:")
        print("-" * 60)
        
        for stock, price in self.stock_prices.items():
            print(f"{stock:<6} - ${price:>8.2f}")
        
        print("-" * 60)
        print("💡 You can buy stocks, view your portfolio, and track your investments!")
        print("=" * 60)
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n🎯 MAIN MENU")
        print("-" * 30)
        print("1. 📈 Buy Stocks")
        print("2. 📊 View Portfolio")
        print("3. 💰 Portfolio Summary")
        print("4. 📋 Transaction History")
        print("5. 💾 Save Portfolio to File")
        print("6. 📂 Load Portfolio from File")
        print("7. ❌ Exit")
        print("-" * 30)
    
    def validate_stock_symbol(self, symbol):
        """Validate if stock symbol exists in our database"""
        return symbol.upper() in self.stock_prices
    
    def validate_quantity(self, quantity_str):
        """Validate and convert quantity to integer"""
        try:
            quantity = int(quantity_str)
            if quantity > 0:
                return quantity
            else:
                print("❌ Quantity must be a positive number!")
                return None
        except ValueError:
            print("❌ Please enter a valid number!")
            return None
    
    def buy_stocks(self):
        """Handle stock purchase functionality"""
        print("\n📈 BUY STOCKS")
        print("-" * 40)
        
        while True:
            # Get stock symbol
            symbol = input("Enter stock symbol (or 'back' to return): ").upper().strip()
            
            if symbol.lower() == 'back':
                return
            
            if not self.validate_stock_symbol(symbol):
                print(f"❌ '{symbol}' is not available. Please choose from the available stocks.")
                continue
            
            # Get quantity
            quantity_str = input(f"Enter quantity for {symbol}: ").strip()
            quantity = self.validate_quantity(quantity_str)
            
            if quantity is None:
                continue
            
            # Calculate cost
            price = self.stock_prices[symbol]
            total_cost = price * quantity
            
            # Confirm purchase
            print(f"\n📋 Purchase Summary:")
            print(f"Stock: {symbol}")
            print(f"Quantity: {quantity} shares")
            print(f"Price per share: ${price:.2f}")
            print(f"Total cost: ${total_cost:.2f}")
            
            confirm = input("\nConfirm purchase? (y/n): ").lower().strip()
            
            if confirm in ['y', 'yes']:
                # Add to portfolio
                if symbol in self.portfolio:
                    self.portfolio[symbol] += quantity
                else:
                    self.portfolio[symbol] = quantity
                
                # Add to transaction history
                self.transaction_history.append({
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'action': 'BUY',
                    'symbol': symbol,
                    'quantity': quantity,
                    'price': price,
                    'total': total_cost
                })
                
                print(f"✅ Successfully purchased {quantity} shares of {symbol}!")
                
                # Ask if user wants to buy more
                more = input("\nBuy more stocks? (y/n): ").lower().strip()
                if more not in ['y', 'yes']:
                    break
            else:
                print("❌ Purchase cancelled.")
    
    def view_portfolio(self):
        """Display current portfolio holdings"""
        print("\n📊 YOUR PORTFOLIO")
        print("=" * 70)
        
        if not self.portfolio:
            print("📭 Your portfolio is empty. Start by buying some stocks!")
            return
        
        print(f"{'Stock':<8} {'Shares':<8} {'Price':<12} {'Value':<15} {'Weight':<8}")
        print("-" * 70)
        
        total_value = 0
        
        for symbol, quantity in self.portfolio.items():
            price = self.stock_prices[symbol]
            value = price * quantity
            total_value += value
        
        for symbol, quantity in self.portfolio.items():
            price = self.stock_prices[symbol]
            value = price * quantity
            weight = (value / total_value) * 100 if total_value > 0 else 0
            
            print(f"{symbol:<8} {quantity:<8} ${price:<11.2f} ${value:<14.2f} {weight:<7.1f}%")
        
        print("-" * 70)
        print(f"{'TOTAL':<37} ${total_value:.2f}")
        print("=" * 70)
    
    def portfolio_summary(self):
        """Display detailed portfolio summary with analytics"""
        print("\n💰 PORTFOLIO SUMMARY")
        print("=" * 50)
        
        if not self.portfolio:
            print("📭 No holdings to summarize.")
            return
        
        total_value = 0
        total_shares = 0
        stock_count = len(self.portfolio)
        
        # Calculate totals
        for symbol, quantity in self.portfolio.items():
            price = self.stock_prices[symbol]
            value = price * quantity
            total_value += value
            total_shares += quantity
        
        # Find largest and smallest holdings
        largest_holding = max(self.portfolio.items(), 
                            key=lambda x: x[1] * self.stock_prices[x[0]])
        smallest_holding = min(self.portfolio.items(), 
                             key=lambda x: x[1] * self.stock_prices[x[0]])
        
        # Display summary
        print(f"📈 Total Portfolio Value: ${total_value:,.2f}")
        print(f"🏢 Number of Different Stocks: {stock_count}")
        print(f"📊 Total Shares Owned: {total_shares:,}")
        print(f"💵 Average Value per Stock: ${total_value/stock_count:,.2f}")
        
        largest_value = largest_holding[1] * self.stock_prices[largest_holding[0]]
        smallest_value = smallest_holding[1] * self.stock_prices[smallest_holding[0]]
        
        print(f"\n🔝 Largest Holding: {largest_holding[0]} (${largest_value:,.2f})")
        print(f"🔻 Smallest Holding: {smallest_holding[0]} (${smallest_value:,.2f})")
        
        print("=" * 50)
    
    def view_transaction_history(self):
        """Display transaction history"""
        print("\n📋 TRANSACTION HISTORY")
        print("=" * 80)
        
        if not self.transaction_history:
            print("📭 No transactions yet.")
            return
        
        print(f"{'Date':<20} {'Action':<6} {'Symbol':<8} {'Shares':<8} {'Price':<12} {'Total':<12}")
        print("-" * 80)
        
        for transaction in self.transaction_history:
            print(f"{transaction['date']:<20} {transaction['action']:<6} "
                  f"{transaction['symbol']:<8} {transaction['quantity']:<8} "
                  f"${transaction['price']:<11.2f} ${transaction['total']:<11.2f}")
        
        print("=" * 80)
    
    def save_portfolio_to_file(self):
        """Save portfolio data to CSV and TXT files"""
        if not self.portfolio:
            print("❌ No portfolio data to save!")
            return
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Save to CSV file
            csv_filename = f"portfolio_{timestamp}.csv"
            with open(csv_filename, 'w', newline='') as csvfile:
                fieldnames = ['Symbol', 'Shares', 'Price_Per_Share', 'Total_Value']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                total_value = 0
                
                for symbol, quantity in self.portfolio.items():
                    price = self.stock_prices[symbol]
                    value = price * quantity
                    total_value += value
                    
                    writer.writerow({
                        'Symbol': symbol,
                        'Shares': quantity,
                        'Price_Per_Share': price,
                        'Total_Value': value
                    })
                
                # Add total row
                writer.writerow({
                    'Symbol': 'TOTAL',
                    'Shares': '',
                    'Price_Per_Share': '',
                    'Total_Value': total_value
                })
            
            # Save to TXT file
            txt_filename = f"portfolio_summary_{timestamp}.txt"
            with open(txt_filename, 'w') as txtfile:
                txtfile.write("STOCK PORTFOLIO SUMMARY\n")
                txtfile.write("=" * 50 + "\n")
                txtfile.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                txtfile.write(f"{'Stock':<8} {'Shares':<8} {'Price':<12} {'Value':<15}\n")
                txtfile.write("-" * 50 + "\n")
                
                total_value = 0
                for symbol, quantity in self.portfolio.items():
                    price = self.stock_prices[symbol]
                    value = price * quantity
                    total_value += value
                    txtfile.write(f"{symbol:<8} {quantity:<8} ${price:<11.2f} ${value:<14.2f}\n")
                
                txtfile.write("-" * 50 + "\n")
                txtfile.write(f"{'TOTAL':<29} ${total_value:.2f}\n")
            
            print(f"✅ Portfolio saved successfully!")
            print(f"📄 CSV file: {csv_filename}")
            print(f"📄 TXT file: {txt_filename}")
            
        except Exception as e:
            print(f"❌ Error saving files: {e}")
    
    def load_portfolio_from_file(self):
        """Load portfolio from a CSV file"""
        print("\n📂 LOAD PORTFOLIO FROM FILE")
        print("-" * 40)
        
        # List available CSV files
        csv_files = [f for f in os.listdir('.') if f.startswith('portfolio_') and f.endswith('.csv')]
        
        if not csv_files:
            print("❌ No portfolio files found in current directory.")
            return
        
        print("Available portfolio files:")
        for i, filename in enumerate(csv_files, 1):
            print(f"{i}. {filename}")
        
        try:
            choice = int(input("\nEnter file number to load (0 to cancel): "))
            
            if choice == 0:
                return
            
            if 1 <= choice <= len(csv_files):
                filename = csv_files[choice - 1]
                
                # Confirm overwrite
                if self.portfolio:
                    confirm = input("⚠️  This will overwrite your current portfolio. Continue? (y/n): ")
                    if confirm.lower() not in ['y', 'yes']:
                        return
                
                # Load from CSV
                new_portfolio = {}
                with open(filename, 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['Symbol'] != 'TOTAL' and row['Symbol'] in self.stock_prices:
                            new_portfolio[row['Symbol']] = int(row['Shares'])
                
                self.portfolio = new_portfolio
                print(f"✅ Portfolio loaded successfully from {filename}!")
                
            else:
                print("❌ Invalid choice!")
                
        except ValueError:
            print("❌ Please enter a valid number!")
        except Exception as e:
            print(f"❌ Error loading file: {e}")
    
    def run(self):
        """Main program loop"""
        self.display_welcome()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.buy_stocks()
                elif choice == '2':
                    self.view_portfolio()
                elif choice == '3':
                    self.portfolio_summary()
                elif choice == '4':
                    self.view_transaction_history()
                elif choice == '5':
                    self.save_portfolio_to_file()
                elif choice == '6':
                    self.load_portfolio_from_file()
                elif choice == '7':
                    print("\n👋 Thank you for using Stock Portfolio Tracker!")
                    print("💰 Happy investing!")
                    break
                else:
                    print("❌ Invalid choice! Please enter 1-7.")
                
                # Pause before showing menu again
                if choice in ['1', '2', '3', '4', '5', '6']:
                    input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")

def display_project_info():
    """Display project information"""
    print("\n" + "=" * 70)
    print("PROJECT INFORMATION")
    print("=" * 70)
    print("Project: Stock Portfolio Tracker")
    print("Task: CodeAlpha Task 2")
    print("Description: Track stock investments with predefined prices")
    print("Features:")
    print("• 10 predefined stocks with current prices")
    print("• Buy stocks and track quantities")
    print("• Portfolio summary and analytics")
    print("• Transaction history")
    print("• Save/load portfolio to/from CSV and TXT files")
    print("• Input validation and error handling")
    print("Key Concepts: dictionary, input/output, arithmetic, file handling")
    print("=" * 70)

def main():
    """Main function to start the stock portfolio tracker"""
    try:
        # Display project information
        display_project_info()
        input("\nPress Enter to start the Stock Portfolio Tracker...")
        
        # Create and run tracker
        tracker = StockPortfolioTracker()
        tracker.run()
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please restart the program.")

if __name__ == "__main__":
    main()