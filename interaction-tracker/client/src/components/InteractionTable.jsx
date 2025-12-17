import { Table, Card, Group, TextInput, Select, Divider  } from '@mantine/core'
import { useEffect, useState } from 'react'
import { getInteractions } from '../api/interactions'

export default function InteractionTable() {
  const [data, setData] = useState([])
  const [userIdFilter, setUserIdFilter] = useState('')
  const [eventTypeFilter, setEventTypeFilter] = useState('')



  useEffect(() => {
    const params = {}
    if (userIdFilter) params.user_id = userIdFilter
    if (eventTypeFilter) params.event_type = eventTypeFilter
    getInteractions(params).then(setData)
  }, [userIdFilter, eventTypeFilter])

  const rows = data.map((i) => (
    <tr key={i.id}>
      <td>{i.user_id}</td>
      <td>{i.event_type}</td>
      <td>{new Date(i.created_at).toLocaleString()}</td>
      <td>{JSON.stringify(i.metadata)}</td>
    </tr>
  ))

  return (
    <Card shadow="sm">
      <Group mb="md">
        <TextInput 
          placeholder="Filter by User ID" 
          value={userIdFilter}
          onChange={(e) => setUserIdFilter(e.target.value)}
        />
        <Select
          placeholder="Filter by Event Type"
          data={['', 'click', 'page_view', 'form_submit']}
          value={eventTypeFilter}
          onChange={setEventTypeFilter}
        />
      </Group>
      <Divider my="md" />
      <Table>
        <thead>
          <tr>
            <th>User</th>
            <th>Event</th>
            <th>Time</th>
            <th>Metadata</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </Table>
    </Card>
  )
}
