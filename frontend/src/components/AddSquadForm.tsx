import { useState } from 'react'

const AddSquadForm = ({ addSquad }) => {
  const [squadName, setSquadName] = useState('')

  const handleSubmit = event => {
    event.preventDefault()
    if (squadName) {
      addSquad(squadName)
      setSquadName('')
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type='text'
        value={squadName}
        onChange={e => setSquadName(e.target.value)}
        placeholder='Enter squad name'
      />
      <button type='submit'>Add Squad</button>
    </form>
  )
}

export default AddSquadForm
