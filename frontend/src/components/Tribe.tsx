import { useState } from 'react'
import type { Tribe } from '../types'

const Tribe = () => {
  const [tribes, setTribes] = useState<Tribe[]>([])

  return (
    <div className='p-6 space-y-6'>
      <h1 className='text-2xl font-bold'>Team Management</h1>

      {tribes.map(tribe => (
        <div
          key={tribe.id}
          className='bg-blue-600 text-white rounded-xl p-4'
        >
          <div className='flex justify-between items-center'>
            <div>
              <h2 className='text-xl font-semibold'>{tribe.name}</h2>
              <p className='text-sm'>{tribe.description}</p>
            </div>
            <button className='text-white hover:opacity-70'>✏️</button>
          </div>

          <div className='mt-4 bg-white rounded-xl p-4 space-y-4 text-black'>
            <h3 className='text-lg font-semibold'>Squads</h3>

            <div className='grid md:grid-cols-2 gap-4'>
              {tribe.squads.map(squad => (
                <div
                  key={squad.id}
                  className='border rounded-lg p-4 shadow-sm'
                >
                  <div className='flex justify-between items-center'>
                    <div>
                      <h4 className='font-semibold'>{squad.name}</h4>
                      <p className='text-sm text-gray-600'>
                        {squad.description}
                      </p>
                    </div>
                    <button className='text-gray-500 hover:text-gray-800'>
                      ✏️
                    </button>
                  </div>
                  {/* Members will go here later */}
                </div>
              ))}
              <button className='border border-dashed border-blue-400 rounded-lg p-4 text-blue-600 hover:bg-blue-50'>
                + Add Squad
              </button>
            </div>
          </div>
        </div>
      ))}

      <button className='bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700'>
        + Create Tribe
      </button>
    </div>
  )
}

export default Tribe
