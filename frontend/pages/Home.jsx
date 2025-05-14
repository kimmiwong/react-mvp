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
    <h1>NYC Restaurant Finder</h1>
    {
        restaurantList.map((restaurant) => {
            return (
                <div className = "restaurant-list" key={restaurant.restaurant_id}>
                <p><Link to ={`/${restaurant.restaurant_id}`}>{restaurant.name}</Link></p>
                </div>
            )
        })
    }
</div>
)
}

export default Home
