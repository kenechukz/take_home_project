import { Card, Text, Group } from '@mantine/core'
import { useEffect, useState } from 'react'
import { getStats } from '../api/interactions'

export default function Stats() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    getStats().then(setStats)
  }, [])

  if (!stats) return <Text>Loading stats...</Text>

  return (
    <Card shadow="sm">
      <Group>
        <Text>Total Users: {stats.count}</Text>
        <Text>
        Most Active: {stats.most_active_user ? `${stats.most_active_user.user_id} (${stats.most_active_user.count})` : 'N/A'}
        </Text>
      </Group>
    </Card>
  )
}
