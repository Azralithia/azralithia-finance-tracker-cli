transactions = []

def main():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Show Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip().lower()

        if choice.startswith('1') or choice.startswith('exp'):
            try:
                expense = float(input("Enter expense details (amount): "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            transactions.append(("expense", expense))
            print(f"Expense added: {expense}\n")

        elif choice.startswith('2') or choice.startswith('inc'):
            try:
                income = float(input("Enter income details (amount): "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            transactions.append(("income", income))
            print(f"Income added: {income}\n")

        elif choice.startswith('3') or choice.startswith('sum'):
            total_expense = sum(amount for type_, amount in transactions if type_ == "expense")
            total_income = sum(amount for type_, amount in transactions if type_ == "income")
            balance = total_income - total_expense
            print("\n=== Summary ===")
            print(f"Income: {total_income:.2f}, Expense: {total_expense:.2f}, Balance: {balance:.2f}\n")

        elif choice in ['4', 'exit', 'quit']:
            print("Exiting the program.")
            break

        else:
            print(f"Choice {choice} does not exist. Please try again.")

if __name__ == "__main__":
    main()