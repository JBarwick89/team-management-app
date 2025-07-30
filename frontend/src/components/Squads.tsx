import { useEffect, useState } from 'react'
import SquadCard from './SquadCard'

const Squads = () => {
  const [squads, setSquads] = useState([])

  const fetchSquads = async () => {
    try {
      const response = await fetch('http://localhost:8000/squads')
      const data = await response.json()
      setSquads(data.squads)
    } catch (error) {
      console.error('Error fetching Squads', error)
    }
  }

  const addSquad = async (squadName: string) => {
    try {
      await fetch('http://localhost:8000/squads', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: squadName }),
      })
      fetchSquads() // Refresh the list after adding a squad
    } catch (error) {
      console.error('Error adding squad', error)
    }
  }

  useEffect(() => {
    fetchSquads()
  }, [])

  return (
    <div>
      <h2>Squads List</h2>
      <ul>
        {squads.map((squad, index) => (
          <SquadCard
            squad={squad}
            key={index}
          />
        ))}
      </ul>
    </div>
  )
}

export default Squads
