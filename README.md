# Personal Finance Tracker 💰

A simple command-line finance tracker built in Python with SQLite.  
Track your income and expenses, categorize them, edit or delete entries, view monthly summaries, apply filters, and export your data.

## ✨ Features ✨

- Add expenses and income with category + date

- Edit and delete transactions by ID

- View all transactions (ID, type, category, and date)

- Paginated transaction history (10 per page)

- Filter transactions (by type, category, date, amount, or ID)

- View monthly summary (income, expenses, balance)

- Validates dates (leap years, invalid months/days)

- Export transactions to CSV (auto-generated filename with timestamp)

- Clean and consistent error handling

- Data stored in SQLite database (`finance.db`)

## 🛠️ Technologies

- Python 3  

- SQLite3 (built-in, no external dependencies)

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

5 / exi / qui → Exit the program

<pre>Enter expense amount: 50
Enter category (e.g., Food, Rent, Salary): Food
Enter year (YYYY): 2025
Enter month (MM): 08
Enter day (DD): 17
Is this correct? 17-08-2025 (y/n): y

Expense added: 50.00 | Category: Food | Date: 2025-08-17
</pre>

## 🔮 Future Improvements

- Category-based summaries (e.g., All food expenses of a month → Food: 200)

- Running balance view

- GUI (Graphical user interface)

- TUI (Text-based UI)

## 📌 Notes

- Works on Linux, Windows, and macOS (Python 3 required).

- Designed as a portfolio project to demonstrate Python, SQLite, and CLI programming.

## 📤 Export to CSV

You can export your transactions to a CSV file.  
This will include all applied filters (if any) and export the currently visible data.

Steps:
1. Go to **Transactions** (`4` in the main menu).  
2. Apply any filters you want (optional).  
3. Select **Export transactions to CSV**.  
4. The program will automatically export with a unique timestamped filename, like `transactions_2025-08-20_14-32-10.csv`

Example:
<pre>
Choose: 4
=== All Transactions ===
...
Choose: 6 (Export transactions to CSV)

Transactions exported successfully to transactions_2025-08-20_14-32-10.csv
</pre>

The file will be saved in the same directory as the program, and can be opened in Excel, Google Sheets, or any text editor.

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.