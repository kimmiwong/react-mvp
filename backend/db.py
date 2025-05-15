from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import DBRestaurants, DBFavoriteRestaurants, DBReviews, DBUsers
from schemas import RestaurantIn, RestaurantOut, UserIn, UserOut, FavRestaurantIn, FavRestaurantOut, ReviewIn, ReviewOut, ReviewWithUser, UserReviewWithRestaurant, FavoriteWithRestaurant

DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/mvp"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def add_restaurant(restaurant: RestaurantIn) -> RestaurantOut:
    db = SessionLocal()
    db_restaurant = DBRestaurants(**restaurant)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    restaurant = RestaurantOut(
        restaurant_id=db_restaurant.restaurant_id,
        name=db_restaurant.name,
        address=db_restaurant.address

    )
    db.close()
    return restaurant

def get_restaurants() -> list[RestaurantOut]:
    db=SessionLocal()
    db_restaurants = db.query(DBRestaurants).all()

    restaurants = []
    for db_restaurant in db_restaurants:
        restaurants.append(RestaurantOut(
            restaurant_id=db_restaurant.restaurant_id,
            name=db_restaurant.name,
            address=db_restaurant.address
        ))
    db.close()
    return restaurants

def get_restaurant(restaurant_id: int) -> RestaurantOut:
    db=SessionLocal()
    db_restaurant = db.query(DBRestaurants).filter(DBRestaurants.restaurant_id == restaurant_id).first()
    db.close()
    return RestaurantOut(
        restaurant_id=db_restaurant.restaurant_id,
        name=db_restaurant.name,
        address=db_restaurant.address

    )

def get_reviews(restaurant_id: int) -> list[ReviewWithUser]:
    db=SessionLocal()
    db_reviews = db.query(DBReviews).filter(DBReviews.restaurant_id==restaurant_id).join(DBUsers).all()

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
    db_reviews = db.query(DBReviews).filter(DBReviews.user_id==user_id).join(DBRestaurants).all()

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

def create_review(restaurant_id: int, review: ReviewIn) -> ReviewOut:
    db = SessionLocal()
    db_review = DBReviews(restaurant_id=restaurant_id,
        **review.model_dump()
        )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    review = ReviewOut(
        review_id=db_review.review_id,
        user_id=db_review.user_id,
        restaurant_id=restaurant_id,
        rating=db_review.rating,
        comment=db_review.comment

    )
    return review


def get_users() -> list[UserOut]:
    db = SessionLocal()
    db_users = db.query(DBUsers).all()

    users = []
    for db_user in db_users:
        users.append(UserOut(
            user_id=db_user.user_id,
            username=db_user.username,
            email=db_user.email,
            password=db_user.password

        ))
    db.close()
    return users


def get_user(user_id: int) -> UserOut:
    db=SessionLocal()
    db_user = db.query(DBUsers).filter(DBUsers.user_id==user_id).first()
    db.close()
    return UserOut(
        user_id=db_user.user_id,
        username=db_user.username,
        email=db_user.email,
        password=db_user.password

    )

def get_user_by_username(username: str):
    db=SessionLocal()
    db_user = db.query(DBUsers).filter(DBUsers.username==username).first()
    db.close()
    return db_user

def add_user(user: UserIn) -> UserOut:
    db = SessionLocal()
    db_user = DBUsers(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    user = UserOut(
        user_id=db_user.user_id,
        username=db_user.username,
        email=db_user.email,
        password=db_user.password
    )
    return user

def get_favorites(user_id: int) -> list[FavoriteWithRestaurant]:
    db=SessionLocal()
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
    db_favorite = DBFavoriteRestaurants(user_id=user_id,
        **favorite.model_dump()
        )
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    favorite = FavRestaurantOut(
        favorite_id=db_favorite.favorite_id,
        user_id=user_id,
        restaurant_id=db_favorite.restaurant_id


    )
    return favorite
