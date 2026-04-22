"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart.keys():
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart
    
def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        cart[item] = 1
    return cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    sorted_dict = dict(sorted(cart.items()))
    return sorted_dict

def send_to_store(cart, aisle_mapping):
    """
    Create a fulfillment cart combining quantity, aisle, and refrigeration information.

    :param cart: dict - User's shopping cart with item names as keys and quantities as values.
    :param aisle_mapping: dict - Mapping of items to [aisle number, refrigeration needed] lists.
    :return: dict - Fulfillment cart sorted in reverse alphabetical order with [quantity, aisle, refrigeration].
    """
    fulfillment_cart = {}

    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle, refrigeration = aisle_mapping[item]
            fulfillment_cart[item] = [quantity, aisle, refrigeration]
        else:
            fulfillment_cart[item] = [quantity, None, None]
    sorted_keys = sorted(fulfillment_cart.keys(), reverse=True)
    sorted_fulfillment_cart = {key: fulfillment_cart[key] for key in sorted_keys}
    return sorted_fulfillment_cart

def update_store_inventory(fulfillment_cart, store_inventory):
    """
    Update store inventory levels with user order.

    :param fulfillment_cart: dict - Fulfillment cart to send to store.
    :param store_inventory: dict - Store available inventory.
    :return: dict - Updated store inventory.
    """
    for item in fulfillment_cart:
        if item in store_inventory:
            # Subtract the quantity (index 0 in fulfillment_cart value)
            store_inventory[item][0] -= fulfillment_cart[item][0]

            # Check if inventory is out of stock
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = "Out of Stock"
    return store_inventory
