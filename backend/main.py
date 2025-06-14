from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from seed import seed_restaurant_data
from schemas import RestaurantIn, RestaurantOut, ReviewIn, ReviewOut, ReviewUpdate, UserIn, UserOut, FavRestaurantOut, FavRestaurantIn, ReviewWithUser, FavoriteWithRestaurant, UserReviewWithRestaurant
from db import add_restaurant, get_restaurants, get_restaurant, get_reviews, get_review, create_review, get_user, add_user, get_users, get_favorites, add_favorite, get_user_reviews, delete_review, update_review


origins = [
    "http://localhost:5173",
    "https://restaurant-finder-frontend.onrender.com/"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/restaurants")
async def create_restaurant(restaurant: RestaurantIn):
    restaurant = add_restaurant(restaurant)
    return restaurant


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



@app.get("/api/restaurants/{restaurant_id}/reviews/{review_id}", response_model=ReviewOut)
async def get_restaurant_review(restaurant_id: int, review_id: int):
    review = get_review(review_id)
    if not review or review.restaurant_id != restaurant_id:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@app.put("/api/restaurants/{restaurant_id}/reviews/{review_id}")
async def update_restaurant_review(review_id: int, review: ReviewUpdate) -> ReviewOut:
    updated_review = update_review(review_id, review)
    if not updated_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return updated_review


@app.delete("/api/restaurants/{restaurant_id}/reviews/{review_id}")
async def delete_restaurant_review(review_id: int):
    deleted_review = delete_review(review_id)
    if not deleted_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return True


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
