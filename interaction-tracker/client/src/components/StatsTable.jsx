import { Table, Card, Title, Stack } from '@mantine/core'
import { useEffect, useState } from 'react'
import { getStats } from '../api/interactions'

export default function StatsTable() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    getStats().then(setStats)
  }, [])

  if (!stats) return <div>Loading...</div>

  return (
    <Stack spacing="md">
      {/* Count by Event Type */}
      <Card shadow="sm">
        <Title order={4} mb="sm">Count by Event Type</Title>
        <Table>
          <thead>
            <tr>
              <th>Event Type</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            {stats.count_by_event_type.map((item) => (
              <tr key={item.event_type}>
                <td>{item.event_type}</td>
                <td>{item.count}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Card>

      {/* Count by User */}
      <Card shadow="sm">
        <Title order={4} mb="sm">Count by User</Title>
        <Table>
          <thead>
            <tr>
              <th>User ID</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            {stats.count_by_user.map((item) => (
              <tr key={item.user_id}>
                <td>{item.user_id}</td>
                <td>{item.count}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Card>
    </Stack>
  )
}












// export default function StatsTable() {
//   const [data, setData] = useState(null)

//   useEffect(() => {
//     getStats().then(setData)
//   }, [])

//   const rows = data.slice(1, -1).map((item) => (
//     <tr>
//       <td>{item.get("user_id")}</td>
//       <td>{i.event_type}</td>
//     </tr>
//   ))

//   return (
//     <Card shadow="sm">
//       <Table>
//         <thead>
//           <tr>
//             <th>Group</th>
//             <th>Count</th>
//           </tr>
//         </thead>
//         <tbody>{rows}</tbody>
//       </Table>
//     </Card>
//   )
// }
