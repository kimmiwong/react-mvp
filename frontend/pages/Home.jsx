import { Link } from 'react-router-dom';
import {useState, useEffect, useContext} from 'react';


function Home () {

    const [restaurantList, setRestaurantList] = useState([])


    useEffect(() => {
        async function fetchRestaurantList() {
            try {

                const response = await fetch ('http://localhost:8000/api/restaurants')
                const restaurants = await response.json()
                setRestaurantList(restaurants)

            }

            catch {


            }
        }
        fetchRestaurantList()
    }, [])

return (
<div >
    <div className = 'users-link-container'><Link to ='/users' className='users-link'>Users</Link> </div>
    <h1>NYC Restaurant Finder</h1>
    <div className = 'restaurant-list'>
    {
        restaurantList.map((restaurant) => {
            return (
                <div className = "restaurant-name" key={restaurant.restaurant_id}>
                <p><Link to ={`/${restaurant.restaurant_id}`}>{restaurant.name}</Link></p>
                </div>
            )
        })
    }
    </div>
</div>
)
}

export default Home
