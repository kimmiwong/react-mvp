
import { Link } from 'react-router-dom';

function AddReview () {

return (
<>

<Link to="/">Go Home</Link>


<div className='add-review-container'>
    <h2>Add Review</h2>
   <form className = 'review'>
        <div className = "review">
            <div>
                <label>Enter your email: </label>
                <input type = "email"/>
            </div>
            <div>
                <label>Enter your username: </label>
                <input type = "text"/>
            </div>
            <div>
                <label>Enter your password: </label>
                <input type = "text"/>
            </div>
        </div>

            <div>
                <label htmlFor = "rating">Select rating</label>
                <select name = "rating" id = "rating">
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
                <textarea id = "review-text" name = "review-text"></textarea>
            </div>

            <div>
                <label>Would you like to favorite this restaurant?</label>
                <input type = "checkbox"/>
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
