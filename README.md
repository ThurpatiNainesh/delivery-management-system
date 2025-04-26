# Django Delivery System .L3 Backend

## Overview

A minimal backend for automating order assignment to delivery agents, respecting daily working hour and distance constraints. Built with Django and Django REST Framework.

## Features

- **Models:** Warehouse, Agent, Order
- **REST API:** CRUD endpoints for all models
- **Allocation Command:** `allocate_orders` management command to assign orders automatically
- **Environment Configuration:** Manage secrets and database settings via `.env`

## Tech Stack

- Python 3.10+
- Django 4.2
- Django REST Framework 3.14
- PostgreSQL (or MySQL)
- python-dotenv for environment variables

## Getting Started

### Prerequisites

- Python 3.10 or newer
- PostgreSQL (or MySQL) server
- Git

### Installation

```bash
# Clone repository
git clone <REPO_URL> django_delivery_system
cd django_delivery_system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Copy the example environment file and update with your values:

```bash
cp .env.example .env
```

**.env**
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### Database Setup

```bash
python manage.py migrate
```

### Seeding Sample Data

Use Django admin or fixtures to create:

- **10** Warehouses
- **20** Agents per warehouse
- Up to **60** Orders per agent


## Running the Application

```bash
python manage.py runserver
```

API base URL: `http://localhost:8000/api/`

## Allocation Command

Each morning at a fixed time, run:

```bash
python manage.py allocate_orders
```

This command:

1. Selects all unassigned orders
2. Iterates through agents in a round-robin fashion
3. Assigns orders if agent’s daily order count < capacity

Customize compliance checks (work hours, distance) in `allocate_orders.py`.

## API Endpoints

| Endpoint              | Methods        | Description                   |
| --------------------- | -------------- | ----------------------------- |
| `/api/warehouses/`    | GET, POST      | List or create warehouses     |
| `/api/warehouses/{id}`| GET, PUT, DELETE | Retrieve, update, delete      |
| `/api/agents/`        | GET, POST      | List or create agents         |
| `/api/agents/{id}`    | GET, PUT, DELETE | Retrieve, update, delete      |
| `/api/orders/`        | GET, POST      | List or create orders         |
| `/api/orders/{id}`    | GET, PUT, DELETE | Retrieve, update, delete      |

## Testing

```bash
python manage.py test
```

## Deployment

For production, consider:

- **Gunicorn** + **Nginx**
- **Docker**: Write a `Dockerfile` and `docker-compose.yml`
- **CI/CD** pipelines (GitHub Actions / GitLab CI)

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/XYZ`)
3. Commit your changes (`git commit -m "Add XYZ feature"`)
4. Push (`git push origin feature/XYZ`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. Feel free to use and modify.

