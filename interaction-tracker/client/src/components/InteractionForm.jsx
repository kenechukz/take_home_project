import { Button, Card, Select, TextInput, Textarea } from '@mantine/core'
import { useState } from 'react'
import { createInteraction } from '../api/interactions'

export default function InteractionForm() {
  const [userId, setUserId] = useState('')
  const [eventType, setEventType] = useState('click')
  const [metadataStr, setMetadataStr] = useState('')
  const [error, setError] = useState('')

  async function handleSubmit() {

    let metadata = null
    
    // Parse JSON if provided
    if (metadataStr.trim()) {
      try {
        metadata = JSON.parse(metadataStr)
        setError('')
      } catch (e) {
        setError('Invalid JSON format')
        return
      }
    }

    try{
      const response = await createInteraction({
        user_id: userId,
        event_type: eventType,
        metadata: metadata
      })

    // Only alert on success
    alert('Interaction created')
    } catch (error) {
      // Show error if request failed
      alert('Failed to create interaction')
    }
  }

  return (
    <Card shadow="sm">
      <TextInput
        label="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        required
        error={!userId && error === 'User ID is required' ? error : ''}
      />
      <Select
        label="Event Type"
        data={['click', 'page_view', 'form_submit']}
        value={eventType}
        onChange={setEventType}
        mt="sm"
        size="sm"
        required
      />
      <Textarea
        label="Metadata (JSON)"
        placeholder='{"key": "value"}'
        value={metadataStr}
        onChange={(e) => setMetadataStr(e.target.value)}
        mt="sm"
        minRows={3}
        error={error}
      />
      <Button 
        mt="md" 
        onClick={handleSubmit}
        disabled={!userId.trim() || !eventType}
      >
        Create Interaction
      </Button>
    </Card>
  )
}
