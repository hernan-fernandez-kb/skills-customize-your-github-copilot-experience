import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    r = requests.get(f"{BASE_URL}/")
    print("Root endpoint:", r.json())

def test_create_item():
    item = {"id": 1, "name": "Book", "price": 12.99}
    r = requests.post(f"{BASE_URL}/items", json=item)
    print("Create item:", r.json())

def test_get_items():
    r = requests.get(f"{BASE_URL}/items")
    print("Get items:", r.json())

def test_get_item():
    r = requests.get(f"{BASE_URL}/items/1")
    print("Get item by ID:", r.json())

def test_update_item():
    updated = {"id": 1, "name": "Notebook", "price": 15.99}
    r = requests.put(f"{BASE_URL}/items/1", json=updated)
    print("Update item:", r.json())

def test_delete_item():
    r = requests.delete(f"{BASE_URL}/items/1")
    print("Delete item:", r.json())

if __name__ == "__main__":
    test_root()
    test_create_item()
    test_get_items()
    test_get_item()
    test_update_item()
    test_delete_item()
