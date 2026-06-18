from fastapi import FastAPI

from inventory import get_inventory
from inventory import get_expiring_items

from recipe_agent import suggest_recipes

from sample_data import load_sample_inventory

app = FastAPI(
    title="EcoCart FreshFlow"
)

# load example data when app starts
load_sample_inventory()


@app.get("/")
def home():

    return {
        "project": "EcoCart FreshFlow",
        "status": "active development"
    }


@app.get("/inventory")
def view_inventory():

    inventory = get_inventory()

    return [
        {
            "name": item.name,
            "quantity": item.quantity,
            "expiry_date": item.expiry_date
        }
        for item in inventory
    ]


@app.get("/expiring")
def view_expiring_items():

    items = get_expiring_items()

    return [
        {
            "name": item.name,
            "days_remaining": item.days_until_expiry()
        }
        for item in items
    ]


@app.get("/recipes")
def get_recipe_suggestions():

    inventory = get_inventory()

    suggestions = suggest_recipes(
        inventory
    )

    return suggestions
