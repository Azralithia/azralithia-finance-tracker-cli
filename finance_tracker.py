import sqlite3
from datetime import datetime

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT,
    date DATETIME NOT NULL
)
""")

def get_date():
    while True:
        # Year input
        date_year = input("Enter year (YYYY): ").strip()[:4]
        try:
            year= int(date_year)
        except ValueError:
            print("Invalid input. Must be numbers only.\n")
            continue

        # Month input: looped until user enters a valid month
        while True:
            date_month = input("Enter month (MM): ").strip()[:2]
            try:
                month = int(date_month)
                if 1 <= month <= 12:
                    break
                else:
                    print("Invalid month. Must be between 01 and 12.\n")
            except ValueError:
                print("Invalid input. Must be numbers only.\n")

        # Day input: looped until user enters a valid day
        while True:
            date_day = input("Enter day (DD): ").strip()[:2]
            try:
                day = int(date_day)
                if 1 <= day <= 31:
                    break
                else:
                    print("Invalid day. Must be between 01 and 31.\n")
            except ValueError:
                print("Invalid input. Must be numbers only.\n")

        # Checking if the date is real (handles Feb 30, leap years, etc.)
        try:
            date_obj = datetime(year, month, day)
            date_value = date_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("That date doesn’t exist. Try again.\n")
            continue

        # Confirm
        confirm = input(f"Is this correct? {date_obj.strftime('%d-%m-%Y')} (y/n): ").strip()[:1].lower()
        if confirm == 'y':
            return date_value
        else:
            print("Let's try again.\n")

def add_transaction(type_):
        # Checking if the amount is a valid float
        try:
            amount = float(input(f"Enter {type_} amount: "))
        except ValueError:
            print("Invalid input. Must be a number.")
            return
        
        category = input("Enter category (e.g., Food, Rent, Salary): ").strip()

        # Call function to get a valid date
        date_value = get_date()
            
        # Insert the transaction into the database
        cursor.execute(
            "INSERT INTO transactions (type, amount, category, date) VALUES (?,?,?,?)",
            (type_, amount, category, date_value)
        )
        conn.commit()
        print(f"{type_.capitalize()} added: {amount:.2f} | Category: {category} | Date: {date_value}\n")

def show_monthly():
    while True:
        # User input for year and month
        choice_year = input("Enter year (YYYY): ").strip()[:4]
        choice_month = input("Enter month (MM): ").strip()[:2].zfill(2)

        # Validate input
        try:
            year = int(choice_year)
            month = int(choice_month)
        except ValueError:
            print("Invalid input. Please enter only valid numbers.")
            continue

        if not (1 <= month <= 12):
            print("Invalid month. Must be between 01 and 12.")
            continue

        # Fetch transactions for the specified month and year
        cursor.execute("""
            SELECT type, amount FROM transactions
            WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?
        """, (choice_year, choice_month))
        transactions = cursor.fetchall()
        if not transactions:
            print(f"No transactions found for {choice_month}/{choice_year}.")
            return 0, 0, 0
        
        # Balance calculation
        total_expense = sum(amount for type_, amount in transactions if type_ == "expense")
        total_income = sum(amount for type_, amount in transactions if type_ == "income")
        balance = total_income - total_expense

        return total_income, total_expense, balance

def show_transactions():
    cursor.execute("SELECT * FROM transactions ORDER BY date")
    transactions = cursor.fetchall()
    if not transactions:
        print("\nNo transactions found\n")
    else:
        print("\n=== All Transactions ===\n")
        for data in transactions:
            print(f"ID: {data[0]} | {data[1].capitalize()}: {data[2]:.2f} | Category: {data[3].capitalize()} | Date: {data[4]}")
        print()

def main():
    while True:
        # Display the options menu
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Show Monthly Summary")
        print("4. Show Transaction history")
        print("5. Exit")

        choice = input("Choose an option: ").strip().lower()

        if choice.startswith('1') or choice.startswith('exp'):
            add_transaction("expense")

        elif choice.startswith('2') or choice.startswith("inc"):
            add_transaction("income")

        elif choice.startswith('3') or choice.startswith('sum') or choice.startswith('mon'):
            total_income, total_expense, balance = show_monthly()
            if total_income == total_expense == balance == 0:
                pass  # already told user "no transactions"
            else:
                print("\n=== Summary ===")
                print(f"Income: {total_income:.2f}, Expense: {total_expense:.2f}, Balance: {balance:.2f}\n")

        elif choice.startswith('4') or choice.startswith('tra') or choice.startswith('his'):
            show_transactions()

        elif choice in ['5', 'exit', 'quit']:
            print("Exiting the program.")
            conn.close()
            break

        else:
            print(f"Choice {choice} does not exist. Please try again.")

if __name__ == "__main__":
    main()