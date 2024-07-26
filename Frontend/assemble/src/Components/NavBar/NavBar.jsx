import React from 'react'
import { useState } from 'react'
import { NavLink, useNavigate } from 'react-router-dom'
import { signOut } from '../../Services/services.js'

//login needs to route to auth.js
//LOGOUT will be handled here and navigate to auth

function NavBar() {
  const [loggedIn, setLoggedIn] = useState(false)

  let navigate = useNavigate()

  if(loggedIn){
    let current = sessionStorage.getItem('key')
    if(current){
      setLoggedIn(true)
    }
  }

  const handleLogout = async () => {
    try {
      if(!loggedIn){
        await signOut()
        setLoginState(false)
        navigate('/auth')
      }
    } catch (error) {
      console.error('Unable to logout ERROR:', error)
    }
  }
  

  return (
    <nav>
      <NavLink to='/'>Home</NavLink>
      {!loggedIn ? 
      <NavLink onClick={handleLogout}>Logout</NavLink> : 
      <NavLink to='/auth'>Login</NavLink>
      }
      <NavLink to='/profile'>Profile</NavLink>
      
    </nav>
  )
}

export default NavBar