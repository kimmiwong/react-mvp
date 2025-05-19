from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import requests
from schemas import RestaurantIn, RestaurantOut, ReviewIn, ReviewOut, UserIn, UserOut, FavRestaurantOut, FavRestaurantIn, ReviewWithUser, FavoriteWithRestaurant, UserReviewWithRestaurant
from db import add_restaurant, get_restaurants, get_restaurant, get_reviews, create_review, get_user, add_user, get_users, get_favorites, add_favorite, get_user_reviews, get_avg_rating


app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8000/api/restaurants",
    "http://localhost:5173",
    "http://localhost:8000/api/restaurants/{restaurant_id}",
    "http://localhost:5173/{restaurant_id}/addreview",
    "http://localhost:5173/{user_id}/useraccount",
    "http://localhost:5173/{restaurant_id}"
    "http://localhost:8000/api/users",
    "http://localhost:8000/api/restaurants/{restaurant_id}/reviews",
    "http://localhost:8000/api/users/{user_id}",
    "http://localhost:8000/api/users/{user_id}/reviews",
    "http://localhost:8000/api/users/{user_id}/favorites"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/api/restaurants/")
# async def get_restaurants():
#     url ="https://api.foursquare.com/v3/places/search?categories=13000&near=Brooklyn%2C%20NY&limit=50"

#     headers = {
#     "accept": "application/json",
#     "Authorization": "fsq3UbovOEIxmJ9RRnfHCFQkShWXrl3K242e+wZsNEynLXs="
# }

#     response = requests.get(url, headers=headers)

#     data = response.json()
#     restaurant_data = data.get('results')
#     results = []

#     for restaurant in restaurant_data:
#         new_dict = {
#             "name": restaurant.get("name"),
#             "address": restaurant.get("location").get("address")
#         }
#         results.append(new_dict)

#     for restaurant in results:
#         restaurant = await create_restaurant(restaurant)





# @app.post("/api/restaurants")
# async def create_restaurant(restaurant: RestaurantIn):
#     restaurant = add_restaurant(restaurant)
#     return restaurant

@app.get("/api/restaurants")
async def list_restaurants():
    return get_restaurants()


@app.get("/api/restaurants/{restaurant_id}")
async def get_restaurant_details(restaurant_id: int) -> RestaurantOut:
    restaurant = get_restaurant(restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail='Restaurant not found')
    return restaurant


@app.get("/api/restaurants/{restaurant_id}/reviews")
async def get_restaurant_reviews(restaurant_id: int) -> list[ReviewWithUser] | None:
    reviews = get_reviews(restaurant_id)
    return reviews


@app.post("/api/restaurants/{restaurant_id}/reviews")
async def create_restaurant_review(restaurant_id: int, review: ReviewIn) -> ReviewOut:
    return create_review(restaurant_id, review)

@app.get("/api/restaurants/{restaurant_id}/avgrating")
async def get_avg_restaurant_rating(restaurant_id: int):
    return get_avg_rating(restaurant_id)


@app.get("/api/users")
async def get_restaurant_users() -> list[UserOut]:
    return get_users()



@app.get("/api/users/{user_id}")
async def get_restaurant_user(user_id: int) -> UserOut:
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user



@app.post("/api/users")
async def add_restaurant_user(user: UserIn) -> UserOut:
    new_user = add_user(user)
    return new_user


@app.get("/api/users/{user_id}/favorites")
async def get_restaurant_favorites(user_id: int) -> list[FavoriteWithRestaurant]:
    return get_favorites(user_id)


@app.post("/api/users/{user_id}/favorites")
async def add_favorite_restaurant(user_id: int, favorite: FavRestaurantIn) -> FavRestaurantOut:
    return add_favorite(user_id, favorite)


@app.get("/api/users/{user_id}/reviews")
async def get_user_restaurant_reviews(user_id: int) -> list[UserReviewWithRestaurant]:
    return get_user_reviews(user_id)
