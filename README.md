# take_home_project

Here's project

## Database connection

In interaction-tracker/server/prisma/schema.prisma specify your db and its url:
e.g.
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

## Running tests

From the server directory, run:
    pytest

## Running application

cd to interaction-tracker/server and run:
  uvicorn src.main:app --reload
