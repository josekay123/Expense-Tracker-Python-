import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.expenses = []
        self.filename = filename
        self.load_expenses()

    def add_expense(self, amount, category, description, date=None):
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        expense = {
            "amount": float(amount),
            "category": category,
            "description": description,
            "date": date
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print(f"{'Date':<12} {'Amount':<10} {'Category':<15} {'Description':<20}")
        print("-" * 60)
        for expense in self.expenses:
            print(f"{expense['date']:<12} {expense['amount']:<10.2f} {expense['category']:<15} {expense['description']:<20}")

    def summarize_by_category(self):
        if not self.expenses:
            print("No expenses to summarize.")
            return

        summary = {}
        for expense in self.expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']

        print(f"{'Category':<15} {'Total Amount':<10}")
        print("-" * 30)
        for category, total in summary.items():
            print(f"{category:<15} {total:<10.2f}")

    def save_expenses(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category", "description", "date"])
            writer.writeheader()
            writer.writerows(self.expenses)

    def load_expenses(self):
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                self.expenses = [row for row in reader]
                for expense in self.expenses:
                    expense["amount"] = float(expense["amount"])
        except FileNotFoundError:
            print("No previous expenses found. Starting fresh.")

    def menu(self):
        while True:
            print("\nExpense Tracker Menu")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Summarize by Category")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = input("Enter amount: ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.summarize_by_category()
            elif choice == "4":
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
