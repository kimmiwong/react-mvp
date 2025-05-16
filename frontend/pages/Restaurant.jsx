
import { Link } from 'react-router-dom';
import {useState, useEffect, useContext} from 'react';
import { useParams } from 'react-router-dom';


function Restaurant () {

       const { id } = useParams();
       const[restaurantInfo, setRestaurantInfo] = useState([])
       const [reviewList, setReviewList] = useState([])

    useEffect(()=> {
        async function fetchRestaurantInfo() {

            try {

                const response = await fetch (`http://localhost:8000/api/restaurants/${id}`)
                const restaurant = await response.json()
                setRestaurantInfo(restaurant)

                const res = await fetch (`http://localhost:8000/api/restaurants/${id}/reviews`)
                const reviews = await res.json()
                setReviewList(reviews)

            }

            catch { console.error(Error)


            }
        }
        fetchRestaurantInfo()
    }, [])




return (
<>

<Link to="/">Go Home</Link>
<div className = "restaurant-container"  >
    <div className = 'restaurant-details'>
        <h1>{restaurantInfo.name}</h1>
        <h3>{restaurantInfo.address}</h3>
    </div>
    <h2  style={{ textDecoration: 'underline' }}>Reviews</h2>
    <div className = "review-list">
            {reviewList.length > 0 ? (
                <ol>

                {reviewList.map((review)=> (


                    <li key={review.review_id}>
                        <p>Rating: {review.rating}/5 Stars</p>
                        <p>{review.comment}</p>
                        <h6>Posted by <Link to={`/${review.user_id}/useraccount`}>{review.username}</Link></h6>
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
