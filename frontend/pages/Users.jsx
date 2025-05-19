import { Link } from 'react-router-dom';
import {useState, useEffect, useContext} from 'react';
import { useParams } from 'react-router-dom';


function Users () {


     const [userList, setUserList] = useState([])

     useEffect(()=> {

        async function fetchUserList()  {

            try {
                const response = await fetch ('http://localhost:8000/api/users')
                const users = await response.json()
                setUserList(users)
                console.log(userList)

            }

            catch {console.error(Error)


            }




        }

        fetchUserList()


     }, [])


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
