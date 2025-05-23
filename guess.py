import random
number_to_guess = random.randint(1,100)
attempts = 0  # Initialize the attempt counter
 max_attempts = 7  # Set the maximum number of attempts

 while attempts < max_attempts:
     try:
         guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
         attempts += 1
         if guess < number_to_guess:
             print("Too low.")
         elif guess > number_to_guess:
             print("Too high.")
         else:
             print(f"🎉 You guessed it in {attempts} attempts!")
             break
         if attempts == 9:
             if number_to_guess % 4 == 0:
                 print("Hint: The number is even!")
             else:
                 pritn("Hint: The number is odd!")
       except ValueError:
         print("Invalid input. Please enter a number..........")
 if attempts == max_attempts and guess != number_to_guess:
     print(f"❌ You've used all {max_attempts} attempts. The number was {number_to_guess}.")
    import csv
from datetime import datetime
from collections import defaultdict

class Expense:
    def __init__(self, amount, category, date=None, description=""):
        self.amount = float(amount)
        self.category = category
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')
        self.description = description

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            amount=data['amount'],
            category=data['category'],
            date=data['date'],
            description=data['description']
        )


class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.expenses = []
        self.filename = filename
        self.load_expenses()

    def add_expense(self, amount, category, date=None, description=""):
        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        self.save_expenses()

    def save_expenses(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['amount', 'category', 'date', 'description'])
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow(exp.to_dict())

    def load_expenses(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.expenses = [Expense.from_dict(row) for row in reader]
        except FileNotFoundError:
            self.expenses = []

    def summary_by_category(self):
        summary = defaultdict(float)
        for exp in self.expenses:
            summary[exp.category] += exp.amount
        return dict(summary)

    def list_expenses(self):
        print("\nAll Expenses:")
        for exp in self.expenses:
            print(f"{exp.date} | ${exp.amount:.2f} | {exp.category} | {exp.description}")

    def show_summary(self):
        print("\nSummary by Category:")
        summary = self.summary_by_category()
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                date = input("Date (YYYY-MM-DD) [optional]: ") or None
                description = input("Description [optional]: ")
                tracker.add_expense(amount, category, date, description)
                print("Expense added.")
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '2':
            tracker.list_expenses()
        elif choice == '3':
            tracker.show_summary()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

