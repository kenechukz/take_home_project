# take_home_project

Here's the project.

## Database connection

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

Change into the server directory and start the application:

```bash
cd interaction-tracker/server
uvicorn src.main:app --reload
```
