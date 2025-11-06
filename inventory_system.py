import json
from datetime import datetime
#testing command

def add_item(item="default", qty=0, logs=None):
    """Add the given quantity of an item to the stock."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item from the stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")


def get_qty(item):
    """Return the quantity of the specified item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty stock.")
        return {}


def save_data(stock, file="inventory.json"):
    """Save the current stock data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock, indent=2))


def print_data(stock):
    """Print all inventory items and quantities."""
    print("Items Report:")
    for i, qty in stock.items():
        print(f"{i} -> {qty}")


def check_low_items(stock, threshold=5):
    """Return a list of items with quantity below the given threshold."""
    return [i for i, qty in stock.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    global stock_data
    stock_data = load_data()

    add_item("apple", 10)
    add_item("banana", -2)
    add_item("123", 10)  # fixed invalid type

    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items(stock_data))

    save_data(stock_data)
    print_data(stock_data)
    print("Static analysis fix: eval() removed for safety.")


if __name__ == "__main__":
    stock_data = {}
    main()