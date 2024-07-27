import Modal from 'react-modal';
import PropTypes from 'prop-types';


function TeamModal({team, onClose}) {
  return (
    <div>
        <Modal isOpen={true} onRequestClose={onClose}>
            <main>
                <h1>{team.team_name}</h1>
                <p>Leader: {team.team_leader}</p>
                <ul>
                    {team.members.map((member) => (
                        <li key={member._id}>{member.username}</li>
                    )) }
                </ul>
                <button 
                    onClick={() => console.log('I Joined A Team')}
                >
                    Join Team
                </button>
                <button onClick={onClose}>Close</button>
            </main>
        </Modal>
    </div>
  )
}

TeamModal.propTypes = {
    team: PropTypes.shape({
        team_name: PropTypes.string.isRequired,
        team_leader: PropTypes.string.isRequired,
        members:PropTypes.string.isRequired,
    }),
    onClose: PropTypes.bool
  }

export default TeamModal