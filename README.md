# Personal Finance Tracker 💰

A simple command-line finance tracker built in Python with SQLite.
Track your income and expenses, categorize them, view monthly summaries, and review your transaction history.

## ✨ Features ✨

- Add expenses and income with category + date

- View all transactions (ID, type, category, and date)

- View monthly summary (income, expenses, balance)

- Validates dates (leap years, invalid months/days)

- Clean and consistent error handling

- Data stored in SQLite database (`finance.db`)


## 🛠️ Technologies

Python 3

SQLite3 (built-in, no external dependencies)


## 🚀 Setup

Clone the repo:
```bash
git clone https://github.com/Azralithia/finance-tracker.git 
cd finance-tracker
```

Run the program:
```bash 
python finance_tracker.py
```
⚠️ Note: The database file (`finance.db`) is created automatically when you run the program.
It is ignored with `.gitignore` 👍

## 📖 Usage
Main Menu
<pre>=== Personal Finance Tracker ===
1. Add Expense
2. Add Income
3. Show Monthly Summary
4. Show Transaction History
5. Exit</pre>
Input:

1 / exp → Add expense

2 / inc → Add income

3 / sum / mon → Show monthly summary

4 / tra / his → Show all transactions

5 / exit / quit → Exit the program

<pre>Enter expense amount: 50
Enter category (e.g., Food, Rent, Salary): Food
Enter year (YYYY): 2025
Enter month (MM): 08
Enter day (DD): 17
Is this correct? 17-08-2025 (y/n): y

Expense added: 50.00 | Category: Food | Date: 2025-08-17
</pre>

## 🔮 Future Improvements

- Edit transactions by ID

- Delete transactions by ID

- Category-based summaries (e.g., Food: 200, Rent: 500)

- Export transactions/summary to CSV

- Running balance view

## 📌 Notes

- Works on Linux, Windows, and macOS (Python 3 required).

- Designed as a portfolio project to demonstrate Python, SQLite, and CLI programming.
