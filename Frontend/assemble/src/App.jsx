import { Route, Routes } from "react-router-dom"; 
import Landing from './Pages/Landing/Landing.jsx'
import Auth from './Pages/Auth/Auth.jsx'
import "./App.css";

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Landing />}/>
        <Route path='/auth' element={<Auth />}/>
      </Routes>
    </>
  )
}

export default App;
