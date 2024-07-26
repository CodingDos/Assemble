import PropTypes from 'prop-types';

function Team({team}) {
  return (
    <div>
      <main>
        <h1>{team.team_name}</h1>
        <p>Leader: {team.team_leader}</p>
        <ul>
          {team.members.map((member) => (
            <li key={member._id}>{member.username}</li>
          )) }
        </ul>
      </main>
    </div>
  )
}

Team.propTypes = {
  team: PropTypes.shape({
      team_name: PropTypes.string.isRequired,
      team_leader: PropTypes.string.isRequired,
      members:PropTypes.string.isRequired,
  })
}

export default Team