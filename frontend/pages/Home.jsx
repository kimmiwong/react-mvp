import { Link } from 'react-router-dom';
import {useState, useEffect} from 'react';


function Home () {

    const [restaurantList, setRestaurantList] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const apiHost = import.meta.env.VITE_API_HOST;



    useEffect(() => {
        async function fetchRestaurantList() {
            try {
                setIsLoading(true);
                const response = await fetch(`${apiHost}/api/restaurants`);
                if (!response.ok) throw new Error("Failed to fetch restaurants");

                const restaurants = await response.json();
                setRestaurantList(restaurants);

            }

            catch(error) {
                console.error("Error fetching restaurants:", error);

            } finally {
                setIsLoading(false);
            }
        }
        fetchRestaurantList()
    }, []);

    if (isLoading) {
        return <p>Loading...</p>;
    }

    return (
        <div >
            <div className = 'users-link-container'><Link to ='/users' className='users-link'>Users</Link> </div>
            <h1>NYC Restaurant Finder</h1>
            <div className = 'restaurant-list'>
            {
                restaurantList.length === 0 ? <p>No restaurants found.</p>
                : restaurantList.map((restaurant) => {
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
