import { Container, Title, Stack, Center } from '@mantine/core'
import Stats from './components/Stats'
import InteractionForm from './components/InteractionForm'
import InteractionTable from './components/InteractionTable'

function App() {
  return (
    <Container size="lg">
      <Title mb="md" >Interaction Tracker</Title>
      <Stack spacing="xl">
        <Stats />
        <InteractionForm />
        <InteractionTable />
      </Stack>
    </Container>
  )
}

export default App
