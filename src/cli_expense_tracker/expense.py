from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "data" / "expense.json"

def check_file() -> bool:
    file = Path(file_path)

    if file.exists():
        return True
    else:
        return False

def write_expense(nama:str, jumlah:int, category: str):
    data = {
        "name": nama,
        "jumlah": jumlah,
        "category": category
    }

    if not check_file():
        list_data = [data]
        with open(file_path, "w") as file:
            json.dump(list_data, file, indent=4)
    else:
        list_data = read_expense()

        list_data.append(data)

        with open(file_path, 'w') as file:
            json.dump(list_data, file, indent=4)
         
def read_expense() -> list[dict]:
    with open(file_path, 'r') as file:
        data: list[dict] = json.load(file)

    return data

def get_total_by_category(category: str):
    data = read_expense()
    return sum([int(currentData['jumlah']) for currentData in data if str(currentData['category']).lower() == category.lower()])