import { useState } from "react"
import { useEffect } from "react"
import axios from 'axios'

function Landing() {

  const [hackathons, setHackathons] = useState([])

  // Function to get all hackathons and re-render the page as soon as a new hackathon is added.
  useEffect(() => {
    const allHackathons = async() => {
      try {
        const response = await axios.get('/hackathons')
        console.log(response)
        setHackathons(response)
      } catch (error) {
        console.error("Error fetching hackathon data", error)
      }
    }
    allHackathons()

  },[])

  return (
    <div>
      <h1>Hackathons Going On</h1>
      {/* {hackathons.map((hackathon) => (
        <div key={hackathon._id}>
          <h1>{hackathon.name}</h1>
          <h2>{hackathon.description}</h2>
        </div>
      ))} */}
    </div>
  )
}

export default Landing