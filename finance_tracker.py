import sqlite3
import csv
from datetime import datetime

class FinanceTracker:
    def __init__(self, db_name="finance.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.counter = 0
        self.filters = []
        self.filtered_transactions = "WHERE id IS NOT NULL"
        self._setup_db()

    def _setup_db(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT,
            date DATETIME NOT NULL
        )
        """)
        self.conn.commit()

    def _format_category(self, category):
        return category if category else "Uncategorized"
    
    def _active_filters_text(self):
        return " AND ".join(self.filters) if self.filters else "None"
    
    def _get_transaction_id(self, action):
        # prompt user for transaction ID to edit or delete
        while True:
            try:
                t_id = int(input(f"Enter transaction ID to {action} (type 0 to cancel): ").strip())
                if t_id == 0:
                    print(f"{action.capitalize()} cancelled.")
                    return None
                return t_id
            except ValueError:
                print("Invalid ID. Try again.")
    
    def _build_filter_string(self):
        if self.filters:
            self.filtered_transactions = "WHERE " + " AND ".join(self.filters)
        else:
            self.filtered_transactions = "WHERE id IS NOT NULL"

    def export_to_csv(self):
        self._build_filter_string()
        query = f"SELECT * FROM transactions {self.filtered_transactions} ORDER BY date, id"
        self.cursor.execute(query)
        transactions = self.cursor.fetchall()

        if not transactions:
            print("No transactions to export.\n")
            return

        # Create filename with timestamp
        filename = f"transactions_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

        # Write to CSV
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Header row
            writer.writerow(["ID", "Type", "Amount", "Category", "Date"])
            # Data rows
            writer.writerows(transactions)

        print(f"Transactions exported successfully to {filename}\n")

    def get_date(self):
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

    def add_transaction(self, type_):
        # Checking if the amount is a valid float
        try:
            amount = float(input(f"Enter {type_} amount: "))
        except ValueError:
            print("Invalid input. Must be a number.")
            return
        
        category = input("Enter category (e.g., Food, Rent, Salary): ").strip()
        
        # Call function to get a valid date
        date_value = self.get_date()

        # Insert the transaction into the database
        self.cursor.execute(
            "INSERT INTO transactions (type, amount, category, date) VALUES (?,?,?,?)",
            (type_, amount, category, date_value)
        )
        self.conn.commit()
        print(f"{type_.capitalize()} added: {amount:.2f} | Category: {category} | Date: {date_value}\n")

    def show_monthly(self):
        # Year input: looped until user enters a valid year
        while True:
            raw_year = input("Enter year (YYYY): ").strip()[:4]
            try:
                year = int(raw_year)
                break
            except ValueError:
                print("Invalid input. Must be numbers only.\n")

        # Month input: looped until user enters a valid month
        while True:
            raw_month = input("Enter month (MM): ").strip()[:2]
            try:
                month = int(raw_month)
                if 1 <= month <= 12:
                    break
                else:
                    print("Invalid month. Must be between 01 and 12.\n")
            except ValueError:
                print("Invalid input. Must be numbers only.\n")

        year_str = f"{year:04d}"
        month_str = f"{month:02d}"

        # Fetch transactions for the specified month and year
        self.cursor.execute("""
            SELECT type, amount FROM transactions
            WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?
        """, (year_str, month_str))
        transactions = self.cursor.fetchall()

        if not transactions:
            print(f"No transactions found for {month_str}/{year_str}.")
            return 0, 0, 0

        # Balance calculation
        total_expense = sum(amount for type_, amount in transactions if type_ == "expense")
        total_income = sum(amount for type_, amount in transactions if type_ == "income")
        balance = total_income - total_expense

        return total_income, total_expense, balance

    def apply_filters(self):
        while True:
            print("\n=== Filter Transactions ===")
            print("1. Type (expense/income)")
            print("2. Category")
            print("3. Date")
            print("4. Amount")
            print("5. ID")
            print("6. Clear filters")
            print("7. Back")

            choice = input("Choose filter: ").strip().lower()

            if choice.startswith('1') or choice.startswith('typ') or choice.startswith('exp') or choice.startswith('inc'):
                type_filter = input("Enter 1 for expense or 2 for income: ").strip().lower()
                if type_filter in ['1', '2', 'expense', 'income']:
                    if type_filter == '1' or type_filter == 'expense':
                        self.filters.append("type = 'expense'")
                        return
                    elif type_filter == '2' or type_filter == 'income':
                        self.filters.append("type = 'income'")
                        return
                else:
                    print("Invalid type. Please enter '1' or '2'.")
            
            elif choice.startswith('2') or choice.startswith('cat'):
                category_filter = input("Enter category: ").strip()
                self.filters.append(f"category LIKE '%{category_filter}%'")
                return

            elif choice.startswith('3') or choice.startswith('dat'):
                date_value = self.get_date()
                self.filters.append(f"date = '{date_value}'")
                return

            elif choice.startswith('4') or choice.startswith('amo'):
                try:
                    amount_filter = float(input("Enter amount: "))
                    self.filters.append(f"amount = {amount_filter}")
                    return
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")

            elif choice.startswith('5') or choice.startswith('id'):
                try:
                    id_filter = int(input("Enter transaction ID: "))
                    self.filters.append(f"id = {id_filter}")
                    return
                except ValueError:
                    print("Invalid ID. Please enter a valid number.")

            elif choice.startswith('6') or choice.startswith('cle') or choice.startswith('erase'):
                self.filters.clear()
                self.counter = 0  # Reset counter when clearing filters
                print("Filters cleared.")
                print("Active Filters:", self._active_filters_text())

            elif choice.startswith('7') or choice.startswith('bac'):
                break

    def show_transactions(self):
        while True:
            # Call the function to build the filter string
            self._build_filter_string()

            # Limited the number of transactions displayed per page to 10 for better readability
            query = f"SELECT * FROM transactions {self.filtered_transactions} ORDER BY date, id LIMIT 10 OFFSET ?"
            self.cursor.execute(query, (self.counter,))
            transactions = self.cursor.fetchall()

            if not transactions:
                if self.counter > 0:
                    print("No more transactions on this page. Going back one page.\n")
                    self.counter = max(0, self.counter - 10)
                    continue
                else:
                    print("\nNo transactions found\n")
                    input("Press Enter to return to the main menu...")
                    return
                
            print("\n=== All Transactions ===\n")
            print("Active Filters:", self._active_filters_text())
            print("\n============================================================\n\n")
            
            for data in transactions:
                category = self._format_category(data[3])
                print(f"ID: {data[0]} | {data[1].capitalize()}: {data[2]:.2f} | Category: {category} | Date: {data[4]}")
            
            print("\n1. Next Page")
            if self.counter >= 10:
                print("2. Previous Page")
            else:
                print("2. Previous Page (disabled)")
            print("3. Filter transactions")
            print("4. Edit transaction")
            print("5. Delete transaction")
            print("6. Export transactions to CSV")
            print("7. Back to main menu")

            choice = input("Choose: ").strip().lower()

            if choice.startswith('1') or choice.startswith('nex'):
                self.counter += 10 # Next page worth of 10 IDs
                continue
            
            elif choice.startswith('2') or choice.startswith('pre'):
                if self.counter >= 10:
                    self.counter -= 10
                else:
                    print("No previous page available.\n")
                continue

            elif choice.startswith('3') or choice.startswith('fil'):
                self.apply_filters()
                self.counter = 0  # Reset counter when applying filters
            
            elif choice.startswith('4') or choice.startswith('edi'):
                t_id = self._get_transaction_id("edit")
                if t_id: 
                    self.edit_transaction(t_id)
                continue
                                
            elif choice.startswith('5') or choice.startswith('del'):
                t_id = self._get_transaction_id("delete")
                if t_id: 
                    self.delete_transaction(t_id)
                continue

            elif choice.startswith('6') or choice.startswith('exp') or choice.startswith('csv'):
                self.export_to_csv()
                continue

            elif choice.startswith('7') or choice.startswith('exi') or choice.startswith('bac'):
                return
            
            else:
                print(f"Choice {choice} does not exist. Please try again.")
                continue

    def edit_transaction(self, t_id):
        # Fetch transaction first
        self.cursor.execute("SELECT * FROM transactions WHERE id = ?", (t_id,))
        transaction = self.cursor.fetchone()
        if not transaction:
            print(f"No transaction found with ID {t_id}")
            return


        transaction = list(transaction)
        current_category = self._format_category(transaction[3])

        # Display current transaction details
        print("\nEditing Transaction:")
        print(f"ID: {transaction[0]} | {transaction[1].capitalize()}: {transaction[2]:.2f} | Category: {current_category} | Date: {transaction[4]}")

    # Ask user what to update
        while True:
            # Amount
            new_amount = input(f"Enter new amount (Press Enter to keep {transaction[2]}): ").strip()
            if new_amount:
                try:
                    transaction[2] = float(new_amount)
                except ValueError:
                    print("Invalid amount. Try again.")
                    continue  # restart loop from top

            # Category
            new_category = input(f"Enter new category (Press Enter to keep {current_category}): ").strip()
            if new_category:
                transaction[3] = new_category

            # Date
            change_date = input("Change date? (y/n): ").strip().lower()
            if change_date == 'y':
                transaction[4] = self.get_date()

            # Confirmation
            print("\nPlease confirm the changes:")
            print(f"Amount: {transaction[2]:.2f}")
            print(f"Category: {transaction[3] if transaction[3] else 'Uncategorized'}")
            print(f"Date: {transaction[4]}")
            confirm = input("Apply these changes? (y/n/r (r = retry)): ").strip().lower()
            
            if confirm == 'y':
                print("Edit confirmed.\n")
                # Update DB
                self.cursor.execute("""
                    UPDATE transactions SET amount = ?, category = ?, date = ?
                    WHERE id = ?
                """, (transaction[2], transaction[3], transaction[4], transaction[0]))
                self.conn.commit()
                print("Transaction updated successfully! (Note: Filters remain active!)\n")
                print("Active Filters:", self._active_filters_text(), "\n")
                return  # Finished, back to transaction list
            
            elif confirm == 'r':
                print("Let's try again.\n")
                continue  # restart edit process
            
            else:
                print("Edit cancelled.")
                return

        

    def delete_transaction(self, t_id):
        self.cursor.execute("SELECT * FROM transactions WHERE id = ?", (t_id,))
        transaction = self.cursor.fetchone()
        if not transaction:
            print(f"No transaction found with ID {t_id}")
            return

        current_category = self._format_category(transaction[3])

        print(f"ID: {transaction[0]} | {transaction[1].capitalize()}: {transaction[2]:.2f} | Category: {current_category} | Date: {transaction[4]}")
        confirm = input(f"Are you sure you want to delete transaction {t_id}? (y/n): ").strip().lower()
        if confirm == 'y':
            self.cursor.execute("DELETE FROM transactions WHERE id = ?", (t_id,))
            self.conn.commit()
            print("Transaction deleted successfully! (Note: Filters remain active!)\n")
            print("Active Filters:", self._active_filters_text(), "\n")
        else:
            print("Delete cancelled.\n")

    def run(self):
        while True:
            print("\n=== Personal Finance Tracker ===")
            print("1. Add Expense")
            print("2. Add Income")
            print("3. Monthly Summary")
            print("4. Transactions")
            print("5. Exit")

            choice = input("Choose: ").strip().lower()

            if choice.startswith('1') or choice.startswith('exp'):
                self.add_transaction("expense")

            elif choice.startswith('2') or choice.startswith("inc"):
                self.add_transaction("income")

            elif choice.startswith('3') or choice.startswith('sum') or choice.startswith('mon'):
                total_income, total_expense, balance = self.show_monthly()
                if total_income == total_expense == balance == 0:
                    pass  # already told user "no transactions"
                else:
                    print("\n=== Summary ===")
                    print(f"Income: {total_income:.2f}, Expense: {total_expense:.2f}, Balance: {balance:.2f}\n")

            elif choice.startswith('4') or choice.startswith('tra') or choice.startswith('his'):
                self.show_transactions()

            elif choice.startswith('5') or choice.startswith('exi') or choice.startswith('qui'):
                print("Exiting the program.")
                self.conn.close()
                break

            else:
                print(f"Choice {choice} does not exist. Please try again.")

if __name__ == "__main__":
    app = FinanceTracker()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\nExiting the program (Keyboard Interrupt).")
        app.conn.close()
