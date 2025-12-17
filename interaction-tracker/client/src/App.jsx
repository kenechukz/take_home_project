import { Container, Title, Stack, Center, Box } from '@mantine/core'
import Stats from './components/Stats'
import InteractionForm from './components/InteractionForm'
import InteractionTable from './components/InteractionTable'
import StatsTable from './components/StatsTable'

function App() {
  return (
    <Center h="200vh">
      <Container size="lg">
        <Title mb="md">Interaction Tracker</Title>
        <Stack spacing="xl">
          <InteractionForm />
          <h2>Interaction Summary Statistics</h2>
          <StatsTable />
          <Stats />
          <h2>Interaction Table</h2>
          <InteractionTable />
          
        </Stack>
      </Container>
    </Center>
  )
}

export default App
