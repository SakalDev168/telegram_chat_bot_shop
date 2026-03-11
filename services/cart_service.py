carts = {}

def add_to_cart(user_id, product):
    if user_id not in carts:
        carts[user_id] = []

    carts[user_id].append(product)

def get_cart(user_id):
    return carts.get(user_id, [])

def clear_cart(user_id):
    carts[user_id] = []