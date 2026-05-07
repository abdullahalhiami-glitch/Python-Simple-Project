expenses = [{"desc": "Coffee", "amount": 500, "category": "Food"}]


def add_expense(desc, amount, category):
    """Add a new expense dictionary to the main expense list."""
    if not isinstance(desc, str) or not desc:
        raise ValueError("Description must be a non-empty string")
    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("Amount must be a non-negative number")
    if not isinstance(category, str) or not category:
        raise ValueError("Category must be a non-empty string")

    expense = {
        "desc": desc,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    return expense


def get_all_expenses():
    """Return all recorded expenses."""
    return list(expenses)


def calculate_total_spent():
    """Return the sum of all expense amounts."""
    total = 0
    for item in expenses:
        total += item.get("amount", 0)
    return total


def get_expenses_by_category(target_category):
    """Return expenses that belong to the specified category."""
    return [item for item in expenses if item.get("category") == target_category]


def calculate_category_total(target_category):
    """Return the total amount spent in the requested category."""
    total = 0
    for item in expenses:
        if item.get("category") == target_category:
            total += item.get("amount", 0)
    return total


def get_highest_expense():
    """Return the expense with the highest amount."""
    if not expenses:
        return None
    return max(expenses, key=lambda item: item.get("amount", 0))


def delete_expense(index):
    """Delete an expense by index from the main list."""
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index >= len(expenses):
        raise IndexError("Expense index out of range")
    return expenses.pop(index)


def check_budget_warning(budget_limit):
    """Return True if the total expense exceeds the provided budget limit."""
    if not isinstance(budget_limit, (int, float)):
        raise ValueError("Budget limit must be a number")
    return calculate_total_spent() > budget_limit
