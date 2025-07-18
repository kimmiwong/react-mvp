import { useState } from 'react'
import './App.css'
import { Routes, Route } from 'react-router-dom'
import Home from '../pages/Home'
import Restaurant from '../pages/Restaurant'
import UserAccount from '../pages/UserAccount'
import AddReview from '../pages/AddReview'
import Users from '../pages/Users'
import EditReview from '../pages/EditReview'


const App = () => {
  return (

    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/users" element={<Users />} />
      <Route path="/:id" element={<Restaurant/>} />
      <Route path="/:id/addreview" element={<AddReview />} />
      <Route path="/:userId/useraccount" element={<UserAccount />}/>
      <Route path ="/:id/:reviewId/editreview" element={<EditReview />}/>

    </Routes>

  );
};

export default App;
