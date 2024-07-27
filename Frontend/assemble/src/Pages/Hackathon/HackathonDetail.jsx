import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import axios from "axios"
import Hackathon from "../../Components/Hackathon/Hackathon"
import Team from "../../Components/Team/Team"
import TeamModal from "../../Components/Team/TeamModal"

function HackathonDetail() {
  const [hackathonDetails, setHackathonDetails] = useState({})
  const [selectedTeam, setSelectedTeam] = useState(null)
  const {id} = useParams()

  //Function to render specific hackathon based on the ID
  useEffect(() => {
    const getHackathon = async() => {
      try {
        const response = axios.get(`hackathons/${id}`)
        console.log(response)
        setHackathonDetails(response)
      } catch (error) {
        console.error("Error fetching the hackathon", error)
      }
    }
    getHackathon()
  },[])
  

  return (
    <div>
      <main>
        <Hackathon hackathon={hackathonDetails} />
        {hackathonDetails.team?.map((team) => (
          <div key={team._id}>
            <Team team={team} onSelect={() => setSelectedTeam(team)}/>
          </div>
        ))}
        {selectedTeam && (
          <TeamModal team={selectedTeam} onClose={()=> setSelectedTeam(null)}/>
        )}
      </main>
    </div>
  )
}

export default HackathonDetail