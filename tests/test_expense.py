import cli_expense_tracker.expense as expense

def test_expense():
    expense.write_expense("Ayam", 15000, "Makan")
    expense.write_expense("Aqua", 5000, "Minum")
    expense.write_expense("Nasi", 5000, "Makan")

