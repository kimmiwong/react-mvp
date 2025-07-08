# Project Title

NYC Restaurant Finder - A full stack app that allows users to discover local restaurants, leave reviews and ratings, favorite restaurants, and view user profiles.


## Description

This was a 3 day project and my first full stack app. The app integrates with the Foursquare API to show 50 restaurants based on zip code and supports user-generated content through a custom backend.

Users can:
- View 50 restaurants in the 11215 zip code
- Click on a restaurant to view ratings and reviews
- Add, edit, and delete reviews with ratings
- Favorite restaurants
- View user profiles that show user's reviews and favorite restaurants


## Technology Stack

- Frontend: React, JavaScript, React Router
- Backend: FastAPI, Python, SQLAlchemy
- Database: PostgreSQL
- APIs: Foursquare Places API
- DevOps: Docker, Render


## Getting Started

### Dependencies

Found in the requirements.txt, package.json, and package-lock.json files

### Installing

Database:

- Start Docker: `docker compose up -d`
- Access PostgreSQL container: `docker exec -it postgres_db psql -U postgres`
- Connect to database: `\c mvp`
- Load schema: `\i data/mvp.sql`

Backend:
- Navigate to the backend directory from root directory: `cd backend`
- Install from requirements: `pip install -r requirements.txt`
- Run dev server: `fastapi dev main.py` or `uvicorn main:app --reload`

Frontend:
- Navigate to the frontend directory from root directory: `cd frontend`
- Install dependencies: `npm install`
- Start dev server: `npm run dev`

### Environment Variables
Backend:
- Create a .env file in the /backend directory with the following content:
    - FOUR_SQUARE_API_KEY=your_foursquare_api_key (Create an account at https://foursquare.com/developer/, create a new project, and generate an api key)
    - DATABASE_URL="postgresql+psycopg2://postgres:postgres@localhost:5432/mvp"
    - PORT=8000

Frontend:
- Create a .env file in the /frontend directory with the following content:
    - VITE_API_HOST = http://localhost:8000


### Executing program

View page at http://localhost:5173/


## Author
- Kimmi Wong/
  kimmiwong94@gmail.com/
  https://github.com/kimmiwong
