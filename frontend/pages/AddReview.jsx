
import { Link, useNavigate } from 'react-router-dom';
import {useState, useEffect, useContext} from 'react';
import { useParams } from 'react-router-dom';


function AddReview () {


const { id } = useParams();
const [email, setEmail] = useState ('')
const [username, setUsername] = useState ('')
const [password, setPassword] = useState('')
const [rating, setRating] = useState(1)
const [reviewText, setReviewText] = useState ('')
const [favorite, setFavorite] = useState(false)
const [restaurantName, setRestaurantName] = useState('')
const navigate = useNavigate();

useEffect(()=> {
const fetchRestaurantName = async () => {
        const restaurantResponse = await fetch (`http://localhost:8000/api/restaurants/${id}`)
        const restaurantInfo = await restaurantResponse.json()
        setRestaurantName(restaurantInfo)

}
fetchRestaurantName()

}, [id])

const handleSubmit = async(e) => {

    e.preventDefault();




    try{

        let userId;

        const userLookUp = await fetch(`http://localhost:8000/api/users?username=${username}`)
        const existingUsers = await userLookUp.json()

        if(userLookUp.ok && existingUsers.length >0) {
            userId=existingUsers[0].user_id
        } else {


        const userResponse = await fetch("http://localhost:8000/api/users", {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                username,
                email,
                password

        })
        })

        if (!userResponse.ok) throw new Error ("Failed to create user")
        const newUser = await userResponse.json();
        userId = newUser.user_id;
        }



        const restaurantResponse = await fetch (`http://localhost:8000/api/restaurants/${id}`)
        const reviewResponse = await fetch (`http://localhost:8000/api/restaurants/${id}/reviews`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                user_id: userId,
                restaurant_id: parseInt(id), // from useParams()
                rating: parseFloat(rating),
                comment: reviewText

        })
        })

        if (favorite) {
            const response = await fetch (`http://localhost:8000/api/users/${userId}`)
            const favoriteResponse = await fetch (`http://localhost:8000/api/users/${userId}/favorites`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify ( {
                    restaurant_id: id

            })
            })
        }
        navigate(-1);


    }
    catch(error) {console.error("Error adding review:", error);

    }
}

return (
<>

<Link to="/">Go Home</Link>


<div className='add-review-container'>
    <h2>Add Review for {restaurantName.name}</h2>
   <form className = 'review' onSubmit={handleSubmit}>
        <div className = "review">
            <div>
                <label>Enter your email: </label>
                <input type = "email" value = {email} onChange={e => setEmail(e.target.value)}/>
            </div>
            <div>
                <label>Enter your username: </label>
                <input type = "text" value = {username} onChange={e => setUsername(e.target.value)}/>
            </div>
            <div>
                <label>Enter your password: </label>
                <input type = "text" value = {password} onChange={e => setPassword(e.target.value)}/>
            </div>
        </div>

            <div>
                <label htmlFor = "rating">Select rating</label>
                <select name = "rating" id = "rating" value = {rating} onChange={e => setRating(e.target.value)}>
                    <option value = "1">1</option>
                    <option value = "1.5">1.5</option>
                    <option value = "2">2</option>
                    <option value = "2.5">2.5</option>
                    <option value = "3">3</option>
                    <option value = "3.5">3.5</option>
                    <option value = "4">4</option>
                    <option value = "4.5">4.5</option>
                    <option value = "5">5</option>


                </select>
            </div>
            <div>
                <label  htmlFor = "review-text">Write a review: </label>
                <br></br>
                <textarea id = "review-text" name = "review-text" value = {reviewText} onChange={e => setReviewText(e.target.value)}></textarea>
            </div>

            <div>
                <label>Would you like to favorite this restaurant?</label>
                <input type = "checkbox" value = {favorite} onChange={e => setFavorite(!favorite)}/>
            </div>

            <div>
                <button id= "submit-review-button" type = "submit">Submit Review</button>
            </div>

   </form>
</div>
</>
)
}

export default AddReview
