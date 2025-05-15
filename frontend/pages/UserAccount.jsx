
import { Link } from 'react-router-dom';
import {useState, useEffect, useContext} from 'react';
import { useParams } from 'react-router-dom';

function UserAccount () {
    const { userId } = useParams();
    const[userFavorites, setUserFavorites] = useState([])
    const[userReviews, setUserReviews] = useState([])

    useEffect(() => {
        async function fetchUserInfo() {

            try {
                const response = await fetch (`http://localhost:8000/api/users/${userId}/favorites`)
                const favorites = await response.json()
                setUserFavorites(favorites)

                const res = await fetch (`http://localhost:8000/api/users/${userId}/reviews`)
                const reviews = await res.json()
                setUserReviews(reviews)





            }

            catch { console.error(Error)


            }


        }
        fetchUserInfo()
    }, [])

return (
<>
<Link to="/">Go Home</Link>
<div className = 'user-container'>
    <div className = 'user-review-list'>
        <h2>Reviews</h2>

        {userReviews.length > 0 ? (
        <ol>

        {
        userReviews.map((review) => (
            <li key={review.review_id}>
                            <h3>{review.restaurant_id}</h3>

                            <p>Rating: {review.rating}/5 Stars</p>
                            <p>{review.comment}</p>
            </li>))



        }

        </ol>
        ) : (
            <p>No reviews have been published yet.</p>
        )

        }
        </div>

    <div className = 'user-favorite-list'>
        <h2>Favorite Restaurants</h2>

        {userFavorites.length > 0 ? (


            <ol>

                {
                    userFavorites.map((favorite) => (
                    <li key={favorite.favorite_id}>
                        <h3>{favorite.restaurant_id}</h3>

                    </li>
                    ))


                }


            </ol>
        ): (

            <p>No favorite restaurants has been selected yet.</p>
        )}


    </div>

</div>
</>
)
}

export default UserAccount
