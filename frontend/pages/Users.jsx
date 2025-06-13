import { Link } from 'react-router-dom';
import {useState, useEffect} from 'react';


function Users () {


    const [userList, setUserList] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const apiHost = import.meta.env.VITE_API_HOST;

    useEffect(()=> {

        async function fetchUserList()  {

            try {
                setIsLoading(true);
                const response = await fetch (`${apiHost}/api/users`);
                const users = await response.json();
                setUserList(users);
            }

            catch (error) {
                console.error("Error fetching users:", error);
            } finally {
                setIsLoading(false);
            }
        }

        fetchUserList();

     }, []);

    if (isLoading) {
        return <p>Loading...</p>;
    }

    return (
        <>
        <Link to="/">Go Home</Link>
        <div className = 'users-list'>
        <h2>Users</h2>

        {userList.length > 0 ? (
        <ol>

        {
        userList.map((user) => (
            <li key={user.user_id}>
                            <h3><Link to ={`/${user.user_id}/useraccount`}>{user.username}</Link></h3>


            </li>))
        }

        </ol>
        ) : (
            <p>No users exist.</p>
        )
        }
        </div>
        </>
     )
}

export default Users
