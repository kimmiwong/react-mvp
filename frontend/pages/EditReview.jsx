import { Link, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function EditReview() {
  const { id, reviewId } = useParams();
  const [rating, setRating] = useState(1);
  const [reviewText, setReviewText] = useState('');
  const [restaurantName, setRestaurantName] = useState('');
  const navigate = useNavigate();
  const apiHost = import.meta.env.VITE_API_HOST;

  useEffect(() => {
    const fetchRestaurantName = async () => {
      const restaurantResponse = await fetch(`${apiHost}/api/restaurants/${id}`);
      const restaurantInfo = await restaurantResponse.json();
      setRestaurantName(restaurantInfo.name);
    };

    const fetchReview = async () => {
      const res = await fetch(`${apiHost}/api/restaurants/${id}/reviews/${reviewId}`);
      if (res.ok) {
        const review = await res.json();
        setRating(review.rating);
        setReviewText(review.comment);
      } else {
        console.error;
      }
    };

    fetchRestaurantName();
    fetchReview();
  }, [id, reviewId]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`${apiHost}/api/restaurants/${id}/reviews/${reviewId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          rating: parseFloat(rating),
          comment: reviewText,
        }),
      });

      if (!response.ok) throw new Error('Failed to update review');

      navigate(-1);
    } catch (error) {
      console.error('Error updating review:', error);
    }
  };

  return (
    <>
      <Link to="/">Go Home</Link>

      <div className="edit-review-container">
        <h2>Edit Review for {restaurantName}</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="rating">Select rating</label>
            <select
              name="rating"
              id="rating"
              value={rating}
              onChange={(e) => setRating(e.target.value)}
            >
              {[...Array(9)].map((_, i) => {
                const val = 1 + i * 0.5;
                return (
                  <option key={val} value={val}>
                    {val}
                  </option>
                );
              })}
            </select>
          </div>

          <div>
            <label htmlFor="review-text">Write a review: </label>
            <br />
            <textarea
              id="review-text"
              name="review-text"
              value={reviewText}
              onChange={(e) => setReviewText(e.target.value)}
            ></textarea>
          </div>

          <div>
            <button type="submit">Update Review</button>
          </div>
        </form>
      </div>
    </>
  );
}

export default EditReview;
