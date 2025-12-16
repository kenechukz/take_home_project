import { Button, Card, Select, TextInput } from '@mantine/core'
import { useState } from 'react'
import { createInteraction } from '../api/interactions'

export default function InteractionForm() {
  const [userId, setUserId] = useState('')
  const [eventType, setEventType] = useState('click')
  const [metaData, setMetaData] = useState({})

  async function handleSubmit() {
    await createInteraction({
      user_id: userId,
      event_type: eventType,
      metadata: metaData
    })
    alert('Interaction created')
  }

  return (
    <Card shadow="sm">
      <TextInput
        label="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />
      <Select
        label="Event Type"
        data={['click', 'page_view', 'form_submit']}
        value={eventType}
        onChange={setEventType}
        mt="sm"
        size="sm"
      />
      <TextInput
        label="Metadata"
        value={metaData}
        onChange={(e) => setMetaData(e.target.value)}
      />
      <Button mt="md" onClick={handleSubmit}>
        Create Interaction
      </Button>
    </Card>
  )
}
