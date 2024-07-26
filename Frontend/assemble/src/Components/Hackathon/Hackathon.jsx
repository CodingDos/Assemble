import PropTypes from 'prop-types';

function Hackathon({hackathon}) {
  return (
    <div>
        <main>
          <h1>{hackathon.name}</h1>
          <p>{hackathon.description}</p>
          <hr />
          <time>Created on: {hackathon.created_date}</time>
          <time>Hackathon starts on: {hackathon.start_date}</time>
          <time>Hackathon ends on: {hackathon.end_date}</time>
        </main>
    </div>
  )
}

Hackathon.propTypes = {
    hackathon: PropTypes.shape({
        name: PropTypes.string.isRequired,
        description: PropTypes.string.isRequired,
        created_date:PropTypes.string.isRequired,
        start_date: PropTypes.string.isRequired,
        end_date: PropTypes.string.isRequired,
    })
}

export default Hackathon