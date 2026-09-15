import cli_expense_tracker.category.check_category as check_category
import questionary

print("CLI Expense Tracke Apps")

def main():
    if not check_category.check_file():
        print("Tidak ada kategori, mohon memasukkan minimal 1 kategori terlebih dahulu.")
        input_category()

    categories = check_category.read_category()
    categories = [category['name'] for category in categories]

    print(f"Berikut adalah category yang tersedia: {", ".join(categories)}")

    choices = ["Input Pengeluaran", "Tambah Kategori", "Lihat Report", "Exit"]

    while True:
        choice = questionary.select(
            "Pilih Menu: ", choices=choices
        ).ask()
        
        if choice == "Input Pengeluaran":
            pass
        elif choice == "Tambah Kategori":
            input_category()
        else:
            break

def input_category():
    while True:
        category = input("Masukkan nama category (quit/exit untuk keluar dari input category): ")

        if category.lower() == "quit" or category.lower() == "exit":
            break

        check_category.write_category(category)

        
main()