# take_home_project

Here's the project.

## Database connection (if not using docker image)

In `interaction-tracker/server/prisma/schema.prisma`, specify your database provider and URL.

Example:

```prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
````

You will then need to run Prisma migrations to create your tables from the models and establish a connection with your database:

```bash
prisma migrate dev --name init
```

To begin using the Prisma Client in the backend, run:

```bash
prisma generate
```

## Running tests

From the `server` directory, run:

```bash
pytest
```

## Running the application

### Backend

** Docker method:

```bash
cd interaction-tracker/infra/docker
docker-compose up --build
```

** when you are ready to stop application run:

```bash
docker-compose down
```

** Note, it's recommended to run backend then frontend after

** Manual method:
Prequisite:
Set up db connection and migrate prisma schemas

Change into the server directory and start the backend server:

```bash
cd interaction-tracker/server
uvicorn src.main:app --reload
```

### Frontend

```bash
cd interaction-tracker/client
npm run dev
```

## Technologies Used

- Backend: FastAPI, Prisma, PostgreSQL
- Frontend: React, Mantine UI
- Testing: pytest
- Infrastructure: Docker, Docker Compose
