from data.products import products


def get_categories():
    return list(products.keys())


def get_products(category):
    return products.get(category, [])


def get_product_by_id(pid):

    for category in products.values():
        for product in category:
            if product["id"] == pid:
                return product