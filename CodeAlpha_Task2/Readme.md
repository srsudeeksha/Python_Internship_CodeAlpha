# 📊 Stock Portfolio Tracker - CodeAlpha Task 2

A comprehensive stock portfolio management system that tracks investments and calculates portfolio values.

## 🎯 Project Overview
This project was developed as part of the **CodeAlpha Python Programming Internship - Task 2**.

## ✨ Features
- **10 Predefined Stocks** with current market prices
- **Portfolio Management** - Buy stocks and track quantities
- **Investment Calculations** - Automatic value calculations
- **Portfolio Analytics** - Holdings breakdown with percentages
- **Transaction History** - Complete purchase log with timestamps
- **File Export** - Save portfolio to CSV and TXT formats
- **Data Import** - Load previously saved portfolios
- **Professional Interface** - Menu-driven system with validation

## 💼 Available Stocks
| Symbol | Company | Price |
|--------|---------|-------|
| AAPL | Apple Inc. | $185.50 |
| TSLA | Tesla Inc. | $248.75 |
| GOOGL | Alphabet Inc. | $138.25 |
| MSFT | Microsoft Corp. | $348.50 |
| AMZN | Amazon.com Inc. | $142.80 |
| NVDA | NVIDIA Corp. | $458.20 |
| META | Meta Platforms Inc. | $285.40 |
| NFLX | Netflix Inc. | $432.15 |
| PYPL | PayPal Holdings Inc. | $58.90 |
| DIS | The Walt Disney Co. | $91.30 |

## 🔧 Key Concepts Used
- **Dictionary** - Stock prices and portfolio storage
- **Input/Output** - User interaction and data display
- **Basic Arithmetic** - Investment value calculations
- **File Handling** - CSV and TXT file operations
- **Object-oriented programming** - Portfolio class structure
- **Data validation** - Input verification and error handling

## 🚀 How to Run
```bash
python CodeAlpha_StockPortfolio.py
```

## 📋 Main Features

### 1. 📈 Buy Stocks
- Select from available stocks
- Enter desired quantities
- Real-time cost calculation
- Purchase confirmation

### 2. 📊 View Portfolio
- Current holdings display
- Individual stock values
- Portfolio weights (percentages)
- Total portfolio value

### 3. 💰 Portfolio Summary
- Total investment value
- Number of different stocks
- Largest and smallest holdings
- Portfolio analytics

### 4. 📋 Transaction History
- Complete purchase log
- Timestamps for all transactions
- Detailed transaction records

### 5. 💾 Save/Load Portfolio
- Export to CSV format
- Save readable TXT summaries
- Import from previous saves

## 📊 Sample Output
```
📊 YOUR PORTFOLIO
======================================================================
Stock    Shares   Price        Value           Weight  
----------------------------------------------------------------------
AAPL     10       $185.50      $1855.00        59.9%
TSLA     5        $248.75      $1243.75        40.1%
----------------------------------------------------------------------
TOTAL                           $3098.75
======================================================================
```

## 📁 File Formats

### CSV Output
```csv
Symbol,Shares,Price_Per_Share,Total_Value
AAPL,10,185.5,1855.0
TSLA,5,248.75,1243.75
TOTAL,,,3098.75
```

### TXT Summary
```
STOCK PORTFOLIO SUMMARY
==================================================
Generated on: 2025-08-31 15:30:45

Stock    Shares   Price        Value          
--------------------------------------------------
AAPL     10       $185.50      $1855.00      
TSLA     5        $248.75      $1243.75      
--------------------------------------------------
TOTAL                           $3098.75
```

## 🏆 CodeAlpha Requirements Met
✅ User inputs stock names and quantity  
✅ Hardcoded dictionary for stock prices  
✅ Displays total investment value  
✅ Saves results to .txt and .csv files  
✅ Uses dictionary, input/output, arithmetic, file handling  

## 🎯 Technical Implementation
- **Menu-driven interface** for easy navigation
- **Input validation** prevents invalid stock symbols and quantities
- **Portfolio analytics** including weights and statistics
- **File operations** with error handling and timestamps
- **Transaction logging** for complete audit trail

## 📁 Files
- `CodeAlpha_StockPortfolio.py` - Main portfolio tracker implementation
- `Readme.md` - Project documentation

## 👨‍💻 Author
**CodeAlpha Python Programming Intern**

## 📧 Contact
- GitHub: https://github.com/srsudeeksha/Python_Internship_CodeAlpha/tree/main/CodeAlpha_Task2
- LinkedIn: www.linkedin.com/in/ranga-sudeeksha

---
*This project is part of the CodeAlpha Python Programming Internship program.*
