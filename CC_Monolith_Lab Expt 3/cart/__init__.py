import json
from cart import dao


def get_cart(username: str):
    try:
        cart_details = dao.get_cart(username)
        if not cart_details:
            return []
        
        items = [
            item
            for cart_detail in cart_details
            for item in json.loads(cart_detail.get('contents', '[]')) if item
        ]

        from products import get_product  # Lazy import to avoid circular dependency
        return [get_product(item) for item in items]
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error in get_cart: {e}")
        return []


def add_to_cart(username: str, product_id: int):
    try:
        dao.add_to_cart(username, product_id)
    except Exception as e:
        print(f"Error in add_to_cart: {e}")


def remove_from_cart(username: str, product_id: int):
    try:
        dao.remove_from_cart(username, product_id)
    except Exception as e:
        print(f"Error in remove_from_cart: {e}")


def delete_cart(username: str):
    try:
        dao.delete_cart(username)
    except Exception as e:
        print(f"Error in delete_cart: {e}")

