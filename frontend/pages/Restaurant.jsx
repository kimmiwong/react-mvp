
import { Link } from 'react-router-dom';
import {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';


function Restaurant () {

    const { id } = useParams();
    const [restaurantInfo, setRestaurantInfo] = useState({});
    const [reviewList, setReviewList] = useState([]);
    const [avgRating, setAvgRating] = useState(0);
    const [isLoading, setIsLoading] = useState(false);
    const apiHost = import.meta.env.VITE_API_HOST;

    async function deleteReview(review_id) {
        try {
            const response = await fetch (
                `${apiHost}/api/restaurants/${id}/reviews/${review_id}`,
                {
                    method: "DELETE",
                }
            );

            if (!response.ok) throw new Error ("Failed to delete review");

            await fetchRestaurantInfo();

        }

        catch (error) {
            console.error("Error deleting review", error);

        }
    }


    async function fetchRestaurantInfo() {

        try {
            setIsLoading(true);
            const response = await fetch (`${apiHost}/api/restaurants/${id}`);
            const restaurant = await response.json();
            setRestaurantInfo(restaurant);
            setAvgRating(restaurant.average_rating);

            const res = await fetch (`${apiHost}/api/restaurants/${id}/reviews`);
            const reviews = await res.json();
            setReviewList(reviews);

        }

        catch (error) {
            console.error("Error fetching restaurant info:", error);

        } finally {
            setIsLoading(false);
        }
    }
    useEffect(()=> {
        fetchRestaurantInfo();
    }, [id]);

    if (isLoading) {
        return <p>Loading...</p>;
    }

    return (
        <>
        <Link to="/">Go Home</Link>
        <div className = "restaurant-container"  >
            <div className = 'restaurant-details'>
                <h1>{restaurantInfo.name} </h1>
                <h3>
                {avgRating ? `${avgRating} ⭐` : "No ratings yet"}
                </h3>
                <h3>{restaurantInfo.address}</h3>

            </div>
            <h2  style={{ textDecoration: 'underline' }}>Reviews</h2>
            <div className = "review-list">
                    {reviewList.length > 0 ? (
                        <ol>

                        {reviewList.map((review)=> (


                            <li key={review.review_id}>
                                <p>{review.rating}⭐</p>
                                <p>{review.comment}</p>
                                <h6>Posted by <Link to={`/${review.user_id}/useraccount`}>{review.username}</Link></h6>
                                <button className = "review-button" onClick={() => deleteReview(review.review_id)}>Delete Review</button>
                                <Link to={`/${id}/${review.review_id}/editreview`}><button className = "review-button">Edit Review</button></Link>


                            </li>


                        ))}
                        </ol>
                    ): (

                            <p>No reviews yet!</p>

                        )}

            </div>

            <div className = "add-review-button">
                <Link to={`/${id}/addreview`} >
                <button>Add review</button>
                </Link>
            </div>
        </div>
        </>
    )
}

export default Restaurant
