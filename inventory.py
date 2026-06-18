from datetime import datetime


class InventoryItem:

    def __init__(self, name, quantity, expiry_date):

        self.name = name
        self.quantity = quantity
        self.expiry_date = expiry_date

    def days_until_expiry(self):

        expiry = datetime.strptime(
            self.expiry_date,
            "%Y-%m-%d"
        )

        today = datetime.now()

        difference = expiry - today

        return difference.days


inventory = []


def add_item(name, quantity, expiry_date):

    item = InventoryItem(
        name,
        quantity,
        expiry_date
    )

    inventory.append(item)


def get_inventory():

    return inventory

def get_expiring_items(days=3):

    expiring_items = []

    for item in inventory:

        if item.days_until_expiry() <= days:
            expiring_items.append(item)

    return expiring_items
