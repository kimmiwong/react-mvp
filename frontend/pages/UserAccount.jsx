
import { Link } from 'react-router-dom';
import {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';

function UserAccount () {
    const { userId } = useParams();
    const[userFavorites, setUserFavorites] = useState([])
    const[userReviews, setUserReviews] = useState([])
    const [userName, setUserName] = useState({})
    const apiHost = import.meta.env.VITE_API_HOST;

    useEffect(() => {
        async function fetchUserInfo() {

            try {
                const userResponse = await fetch (`${apiHost}/api/users/${userId}`);
                const name = await userResponse.json();
                setUserName(name);

                const response = await fetch (`${apiHost}/api/users/${userId}/favorites`);
                const favorites = await response.json();
                setUserFavorites(favorites);

                const res = await fetch (`${apiHost}/api/users/${userId}/reviews`);
                const reviews = await res.json();
                setUserReviews(reviews);
            }

            catch (error) {
                console.error("Error fetching user info:", error);
            }

        }
        fetchUserInfo();
    }, [userId]);

    return (
        <>
        <Link to="/">Go Home</Link>
        <div className = 'users-link-container'><Link to ='/users' className='users-link'>Users</Link> </div>
        <h2>{userName.username}'s Profile</h2>
        <div className = 'user-container'>
            <div className = 'user-review-list'>
                <h2>Reviews</h2>

                {userReviews.length > 0 ? (
                <ol>

                {
                userReviews.map((review) => (
                    <li key={review.review_id}>
                                    <h3><Link to ={`/${review.restaurant_id}`}>{review.restaurant_name}</Link></h3>

                                    <p>{review.rating}⭐</p>
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
                                <h3><Link to ={`/${favorite.restaurant_id}`}>{favorite.restaurant_name}</Link></h3>

                            </li>
                            ))
                        }

                    </ol>
                ): (

                    <p>No favorite restaurants have been selected yet.</p>
                )}

            </div>
        </div>
        </>
    )
}

export default UserAccount
