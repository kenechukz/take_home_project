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
          <StatsTable />
          <Stats />
          <InteractionTable />
        </Stack>
      </Container>
    </Center>
  )
}

export default App
