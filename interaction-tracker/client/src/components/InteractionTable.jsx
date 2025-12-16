import { Table, Card } from '@mantine/core'
import { useEffect, useState } from 'react'
import { getInteractions } from '../api/interactions'

export default function InteractionTable() {
  const [data, setData] = useState([])

  useEffect(() => {
    getInteractions().then(setData)
  }, [])

  const rows = data.map((i) => (
    <tr key={i.id}>
      <td>{i.user_id}</td>
      <td>{i.event_type}</td>
      <td>{new Date(i.created_at).toLocaleString()}</td>
    </tr>
  ))

  return (
    <Card shadow="sm">
      <Table>
        <thead>
          <tr>
            <th>User</th>
            <th>Event</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </Table>
    </Card>
  )
}
