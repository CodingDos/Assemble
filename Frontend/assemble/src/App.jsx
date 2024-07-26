import { Route, Routes } from "react-router-dom"; 
import Landing from './Pages/Landing/Landing.jsx'
import Auth from './Pages/Auth/Auth.jsx'
import "./App.css";
import HackathonDetail from "./Pages/Hackathon/HackathonDetail.jsx";

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Landing />}/>
        <Route path='/auth' element={<Auth />}/>
        <Route path='/hackathon/:id' element={<HackathonDetail />} />
      </Routes>
    </>
  )
}

export default App;
