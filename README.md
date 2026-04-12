# FastAPI Task Manager

Learning project using FastAPI and SQLAlchemy.

## Features

- Task CRUD
- User model
- Basic User → Task relationship
- Clean architecture (routers, services, schemas, models)

## Status

This project is paused at this stage as a learning checkpoint.

Next step:
- Focus on SQL fundamentals
- Improve relationships and queries


## New Feature

### Get tasks by user with optional filtering

GET /tasks/by-user/{user_id}?completed=true

- Returns all tasks for a specific user
- Optional filter by completion status
- Returns 404 if user does not exist