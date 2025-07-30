import './SquadCard.css'

const EditIcon = () => (
  <svg
    width='20'
    height='20'
    viewBox='0 0 24 24'
    fill='none'
    stroke='currentColor'
    strokeWidth='2'
    strokeLinecap='round'
    strokeLinejoin='round'
  >
    <path d='M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7'></path>
    <path d='M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z'></path>
  </svg>
)

const DeleteIcon = ({ className = '' }) => (
  <svg
    className={className}
    width='20'
    height='20'
    viewBox='0 0 24 24'
    fill='none'
    stroke='currentColor'
    strokeWidth='2'
    strokeLinecap='round'
    strokeLinejoin='round'
  >
    <polyline points='3 6 5 6 21 6'></polyline>
    <path d='M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2'></path>
    <line
      x1='10'
      y1='11'
      x2='10'
      y2='17'
    ></line>
    <line
      x1='14'
      y1='11'
      x2='14'
      y2='17'
    ></line>
  </svg>
)

const Member = ({ member }) => (
  <li className='member-item'>
    <div className='member-info'>
      <div className='member-name'>{member.name}</div>
      <div className='member-role'>{member.role}</div>
    </div>
    <div className='member-details'>
      <span className='member-allocation'>{member.allocation}%</span>
      <button className='icon-btn'>
        <EditIcon />
      </button>
      <button className='icon-btn icon-btn--delete'>
        <DeleteIcon />
      </button>
    </div>
  </li>
)

const SquadCard = ({ squad }) => {
  console.log('SquadCard props:', squad)
  return (
    <div className='squad-card'>
      <div className='card-header'>
        <div className='card-header__info'>
          <h2 className='card-header__title'>{squad.name}</h2>
          <p className='card-header__subtitle'>{squad.description}</p>
        </div>
        <div className='card-header__actions'>
          <button className='icon-btn'>
            <EditIcon />
          </button>
          <button className='icon-btn icon-btn--delete'>
            <DeleteIcon />
          </button>
        </div>
      </div>

      <div className='team-members-section'>
        <div className='section-header'>
          <h3 className='section-title'>Team Members</h3>
          <button className='add-btn'>+ Add</button>
        </div>

        <ul className='member-list'>
          {/* TODO: replace with actual members from squad */}
          {squad.members.map((member, index) => (
            <Member
              member={member}
              key={index}
            />
          ))}
        </ul>
      </div>
    </div>
  )
}

export default SquadCard
