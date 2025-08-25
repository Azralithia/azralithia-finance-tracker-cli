# Azralithia Finance Tracker (CLI)

A command-line based personal finance tracker with SQLite integration,
CSV export, and summary reporting.

------------------------------------------------------------------------

## ✨ Features

-   Add income and expenses with categories and dates.

-   View monthly summaries with income, expenses, and balance.

-   Browse transaction history with pagination (10 per page).

-   Apply filters (type, category, date, amount, ID).

-   Edit or delete existing transactions.

-   Export transactions to CSV with timestamped filenames.

-   Persistent SQLite database storage.

------------------------------------------------------------------------

## 🚀 Installation

``` bash
git clone https://github.com/Azralithia/azralithia-finance-tracker-cli.git
cd azralithia-finance-tracker-cli
python finance_tracker_cli.py
```

------------------------------------------------------------------------

## 📑 Usage

When you run the program, you'll see a simple menu:
<pre>=== Personal Finance Tracker ===
1. Add Expense
2. Add Income
3. Show Monthly Summary
4. Show Transaction History
5. Exit</pre>

(Note: **Transaction History** menu includes *filtering, editing, deleting, and CSV export*)
-   Choose an option by number.
-   Transactions are stored in `transactions.db`.
-   Exports create files with a unique timestamped filename, like `transactions_2025-08-20_14-32-10.csv`

------------------------------------------------------------------------

## 🛠️ Requirements

-   Python 3.10+
-   SQLite (built-in, no extra install needed)

------------------------------------------------------------------------

## 🔮 Future Improvements

-   TUI/GUI integration (see [Azralithia Finance Tracker
    (GUI)](https://github.com/Azralithia/azralithia-finance-tracker-gui))
-   Budget alerts
-   Data visualization (charts, graphs)
-   Better summary reporting (weekly/yearly/custom date ranges)

------------------------------------------------------------------------

## 📜 License

This project is licensed under the [MIT License](LICENSE.md).

------------------------------------------------------------------------

## 🏷️ Credits

Built as part of the **Azralithia** suite of projects.
