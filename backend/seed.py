import requests
from db import SessionLocal, add_restaurant
from db_models import DBRestaurants
from dotenv import load_dotenv
import os
from schemas import RestaurantIn

load_dotenv()
api_key = os.getenv("FOUR_SQUARE_API_KEY")


def seed_restaurant_data():
    db = SessionLocal()
    try:
        if db.query(DBRestaurants).count() > 0:
            print("Restaurants already seeded.")
            return

        url = "https://api.foursquare.com/v3/places/search?categories=13000&near=Brooklyn%2C%20NY&limit=50"

        headers = {
            "accept": "application/json",
            "Authorization": api_key
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        restaurant_data = data.get('results', [])
        if not restaurant_data:
            print("No restaurant data found")
            return

        for restaurant in restaurant_data:
            name = restaurant.get("name")
            address = restaurant.get("location").get("formatted_address")
            if name and address:
                restaurant_in = RestaurantIn(name=name, address=address)
                add_restaurant(restaurant_in)

        print("Seeding complete")

    except Exception as e:
        print(f"Error seeding data:{e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_restaurant_data()
