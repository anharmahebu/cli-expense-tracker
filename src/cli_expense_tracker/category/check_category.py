from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "category.json"

def check_file() -> bool:
    file = Path(file_path)

    if file.exists():
        return True
    else:
        return False

def write_category(category: str):
    data = {
        "name": category
    }

    if not check_file():
        list_data = [data]
        with open(file_path, "w") as file:
            json.dump(list_data, file, indent=4)
    else:
        list_data = read_category()

        list_data.append(data)

        with open(file_path, 'w') as file:
            json.dump(list_data, file, indent=4)
         
def read_category() -> list[dict]:
    with open(file_path, 'r') as file:
        data: list[dict] = json.load(file)

    return data


    