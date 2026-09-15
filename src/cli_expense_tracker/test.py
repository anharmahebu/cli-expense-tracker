import questionary
import cli_expense_tracker.category.check_category as check_category


data = check_category.read_category()
data = [category['name'] for category in data]

print(data)
choice = questionary.select(
    "Pilih Kategori: ",
    choices=data
).ask()

print(choice)
 