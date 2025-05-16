from pydantic import BaseModel


class UserIn(BaseModel):
    username: str
    email: str
    password: str


class UserOut(UserIn):
    user_id: int


class RestaurantIn(BaseModel):
    name: str
    address: str


class RestaurantOut(RestaurantIn):
    restaurant_id: int | None


class FavRestaurantIn(BaseModel):
    restaurant_id: int


class FavRestaurantOut(FavRestaurantIn):
    favorite_id: int
    user_id: int


class ReviewIn(BaseModel):
    user_id: int
    rating: float
    comment: str


class ReviewOut(ReviewIn):
    review_id: int
    restaurant_id: int


class ReviewWithUser(BaseModel):
    review_id: int
    user_id: int
    username: str
    rating: float
    comment: str


class UserReviewWithRestaurant(BaseModel):
    review_id: int
    restaurant_id: int
    restaurant_name: str
    rating: float
    comment: str


class FavoriteWithRestaurant(BaseModel):
    favorite_id: int
    restaurant_id: int
    restaurant_name: str
