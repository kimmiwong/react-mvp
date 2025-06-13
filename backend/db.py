from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from db_models import DBRestaurants, DBFavoriteRestaurants, DBReviews, DBUsers
from schemas import RestaurantIn, RestaurantOut, UserIn, UserOut, FavRestaurantIn, FavRestaurantOut, ReviewIn, ReviewOut, ReviewUpdate, ReviewWithUser, UserReviewWithRestaurant, FavoriteWithRestaurant
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def add_restaurant(restaurant: RestaurantIn) -> RestaurantOut:
    db = SessionLocal()
    db_restaurant = DBRestaurants(**restaurant.model_dump())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    restaurant = RestaurantOut(
        restaurant_id=db_restaurant.restaurant_id,
        name=db_restaurant.name,
        address=db_restaurant.address,
        average_rating=db_restaurant.average_rating

    )
    db.close()
    return restaurant


def get_restaurants() -> list[RestaurantOut]:
    db = SessionLocal()
    db_restaurants = db.query(DBRestaurants).all()
    restaurants = []
    for db_restaurant in db_restaurants:
        restaurants.append(RestaurantOut(
            restaurant_id=db_restaurant.restaurant_id,
            name=db_restaurant.name,
            address=db_restaurant.address,
            average_rating=db_restaurant.average_rating
        ))
    db.close()
    return restaurants


def get_restaurant(restaurant_id: int) -> RestaurantOut:
    db = SessionLocal()
    db_restaurant = db.query(DBRestaurants).filter(DBRestaurants.restaurant_id == restaurant_id).first()
    db.close()
    return RestaurantOut(
        restaurant_id=db_restaurant.restaurant_id,
        name=db_restaurant.name,
        address=db_restaurant.address,
        average_rating=db_restaurant.average_rating

    )


def get_review(review_id: int) -> ReviewOut:
    db = SessionLocal()
    db_review = db.query(DBReviews).filter(DBReviews.review_id == review_id).first()
    db.close()
    return ReviewOut(
        review_id=db_review.review_id,
        user_id=db_review.user_id,
        restaurant_id=db_review.restaurant_id,
        rating=db_review.rating,
        comment=db_review.comment

    )


def get_reviews(restaurant_id: int) -> list[ReviewWithUser]:
    db = SessionLocal()
    db_reviews = db.query(DBReviews).filter(DBReviews.restaurant_id == restaurant_id).join(DBUsers).all()
    reviews = []
    for db_review in db_reviews:
        reviews.append(ReviewWithUser(
            review_id=db_review.review_id,
            user_id=db_review.user_id,
            username=db_review.user.username,
            rating=db_review.rating,
            comment=db_review.comment

        ))
    db.close()
    return reviews


def get_user_reviews(user_id: int) -> list[UserReviewWithRestaurant]:
    db = SessionLocal()
    db_reviews = db.query(DBReviews).filter(DBReviews.user_id == user_id).join(DBRestaurants).all()
    user_reviews = []
    for db_review in db_reviews:
        user_reviews.append(UserReviewWithRestaurant(
            review_id=db_review.review_id,
            restaurant_id=db_review.restaurant_id,
            restaurant_name= db_review.restaurant.name,
            rating=db_review.rating,
            comment=db_review.comment

        ))
    db.close()
    return user_reviews

def update_average_rating(db, restaurant_id: int):
    avg_rating = db.query(func.avg(DBReviews.rating)).filter(DBReviews.restaurant_id == restaurant_id).scalar()
    db_restaurant = db.query(DBRestaurants).filter(DBRestaurants.restaurant_id == restaurant_id).first()

    if db_restaurant:
        if avg_rating is not None:
            db_restaurant.average_rating = round(avg_rating, 1)
        else:
            db_restaurant.average_rating = None
        db.commit()


def create_review(restaurant_id: int, review: ReviewIn) -> ReviewOut:
    db = SessionLocal()
    db_review = DBReviews(restaurant_id=restaurant_id, **review.model_dump())
    db.add(db_review)
    db.commit()

    update_average_rating(db, restaurant_id)

    db.refresh(db_review)
    review = ReviewOut(
        review_id=db_review.review_id,
        user_id=db_review.user_id,
        restaurant_id=restaurant_id,
        rating=db_review.rating,
        comment=db_review.comment

    )
    db.close()
    return review


def delete_review(review_id: int) -> bool:
    db = SessionLocal()
    db_review = db.query(DBReviews).filter(DBReviews.review_id == review_id).first()
    restaurant_id = db_review.restaurant_id

    db.delete(db_review)
    db.commit()

    update_average_rating(db, restaurant_id)
    db.close()
    return True


def update_review(review_id: int, review: ReviewUpdate) -> ReviewOut:
    db = SessionLocal()
    db_review = db.query(DBReviews).filter(DBReviews.review_id == review_id).first()
    restaurant_id = db_review.restaurant_id

    if review.user_id is not None:
        db_review.user_id = review.user_id
    if review.rating is not None:
        db_review.rating = review.rating
    if review.comment is not None:
        db_review.comment = review.comment

    db.commit()
    update_average_rating(db, restaurant_id)
    db.refresh(db_review)
    db.close()

    return ReviewOut(
        review_id=review_id,
        user_id=db_review.user_id,
        restaurant_id=db_review.restaurant_id,
        rating=db_review.rating,
        comment=db_review.comment
    )


def get_users() -> list[UserOut]:
    db = SessionLocal()
    db_users = db.query(DBUsers).all()
    users = []
    for db_user in db_users:
        users.append(UserOut(
            user_id=db_user.user_id,
            username=db_user.username,
            email=db_user.email,
        ))
    db.close()
    return users


def get_user(user_id: int) -> UserOut:
    db = SessionLocal()
    db_user = db.query(DBUsers).filter(DBUsers.user_id == user_id).first()
    db.close()
    return UserOut(
        user_id=db_user.user_id,
        username=db_user.username,
        email=db_user.email
    )


def add_user(user: UserIn) -> UserOut:
    db = SessionLocal()
    existing_user = db.query(DBUsers).filter(DBUsers.username == user.username).first()
    if existing_user:
        return UserOut(
        user_id=existing_user.user_id,
        username=existing_user.username,
        email=existing_user.email,
    )
    db_user = DBUsers(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return UserOut(
        user_id=db_user.user_id,
        username=db_user.username,
        email=db_user.email,

    )


def get_favorites(user_id: int) -> list[FavoriteWithRestaurant]:
    db = SessionLocal()
    db_favorites = db.query(DBFavoriteRestaurants).filter(DBFavoriteRestaurants.user_id==user_id).join(DBRestaurants).all()
    favorites = []
    for db_favorite in db_favorites:
        favorites.append(FavoriteWithRestaurant(
            favorite_id=db_favorite.favorite_id,
            restaurant_id=db_favorite.restaurant_id,
            restaurant_name = db_favorite.restaurant.name


        ))
    db.close()
    return favorites


def add_favorite(user_id: int, favorite: FavRestaurantIn) -> FavRestaurantOut:
    db = SessionLocal()
    db_favorite = DBFavoriteRestaurants(user_id=user_id, **favorite.model_dump())
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    favorite = FavRestaurantOut(
        favorite_id=db_favorite.favorite_id,
        user_id=user_id,
        restaurant_id=db_favorite.restaurant_id


    )
    db.close()
    return favorite
