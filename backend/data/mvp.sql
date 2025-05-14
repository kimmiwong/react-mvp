CREATE TABLE restaurants (
 restaurant_id SERIAL PRIMARY KEY,
 name TEXT NOT NULL,
 address TEXT NOT NULL,
 cuisine_type TEXT NOT NULL,
 yelp_rating FLOAT,
 internal_avg_rating FLOAT
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(15)

);

CREATE TABLE favorite_restaurants (
    favorite_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    restaurant_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) ON DELETE CASCADE
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    restaurant_id INT NOT NULL,
    rating float,
    comment TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) ON DELETE CASCADE
);


INSERT INTO users (username, email, password)
VALUES
('kimmiwong', 'kimmi@me.com', 'moshi3');

ALTER TABLE restaurants
DROP COLUMN cuisine_type,
DROP COLUMN yelp_rating,
DROP COLUMN internal_avg_rating;
