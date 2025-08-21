# Azralithia Finance Tracker (CLI)

A command-line based personal finance tracker with SQLite integration,
CSV export, and simple reporting.\
Built as part of the **Azralithia** suite of projects.

------------------------------------------------------------------------

## ✨ Features

-   💾 **SQLite Database**\
    Automatically creates `finance.db` on first run.

-   ➕ **Add Transactions**\
    Record income or expenses with amount and category.

-   📊 **View Transactions**\
    Filter by category or show all entries.

-   📜 **Export to CSV**\
    Save transaction history to a CSV file.

-   📈 **Summary Reports**\
    See income, expenses, and net balance at a glance.

-   🔍 **Search & Filters**\
    View subsets of your data for better insights.

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

-   Choose an option by number.\
-   Transactions are stored in `finance.db`.\
-   Export create files with a unique timestamped filename, like `transactions_2025-08-20_14-32-10.csv`

------------------------------------------------------------------------

## 🛠️ Requirements

-   Python 3.10+\
-   SQLite (built-in, no extra install needed)

------------------------------------------------------------------------

## 🔮 Future Improvements

-   TUI/GUI integration (see [Azralithia Finance Tracker
    (GUI)](https://github.com/Azralithia/azralithia-finance-tracker-gui))\
-   Budget alerts
-   Data visualization (charts, graphs)

------------------------------------------------------------------------

## 📜 License

This project is licensed under the [MIT License](LICENSE.md).

------------------------------------------------------------------------

## 🏷️ Credits

Developed by **Azralithia**.
