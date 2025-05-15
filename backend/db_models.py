from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class DBUsers(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


class DBRestaurants(Base):
    __tablename__ = "restaurants"

    restaurant_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)


class DBFavoriteRestaurants(Base):
    __tablename__ = "favorite_restaurants"

    favorite_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'), nullable=False)

    restaurant = relationship("DBRestaurants")


class DBReviews(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'), nullable=False)
    rating = Column(Float)
    comment = Column(String)

    user = relationship("DBUsers")
    restaurant = relationship("DBRestaurants")
