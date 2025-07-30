type Member = {
  id: string
  name: string
  role: string
  allocation: number
}

type Squad = {
  id: string
  name: string
  description: string
  members: Member[]
}

type Tribe = {
  id: string
  name: string
  description: string
  squads: Squad[]
}

export type { Member, Squad, Tribe }
