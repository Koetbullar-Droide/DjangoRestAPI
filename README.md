# Django REST API with PostgreSQL and Docker

This is a Django project that provides a REST API, using PostgreSQL as the database, and is containerized using Docker and Docker Compose.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Accessing the Application](#accessing-the-application)
  - [Running Migrations](#running-migrations)
  - [Creating a Superuser](#creating-a-superuser)
  - [Accessing the PostgreSQL Database](#accessing-the-postgresql-database)
- [Common Commands](#common-commands)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Project Description

This project is a Django-based REST API that allows you to perform CRUD operations on a PostgreSQL database. The application is containerized using Docker, making it easy to deploy and manage.

## Installation

### Prerequisites

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)
- Git (optional, for cloning the repository): [Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Python

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject

### Usage
#### Running the Application
#### Development Environment
1.  Ensure that PostgreSQL is installed and running on your local machine.
2.  Create a .env file in the root directory of the project and add your environment variables:
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password

3.  Create a virtual environment and activate it:
    python3 -m venv venv
    source venv/bin/activate
4.  Install dependencies:
    pip install -r requirements.txt
5.  Apply migrations(You must have a postgres database locally running):
    python manage.py migrate
6.  Run the development server:
    python manage.py runserver

#### Dockerized Environment

1.  Build and start the containers:
    docker-compose up --build

#### Accessing the Application
-   Development Environment: Visit http://localhost:8000/ in your web browser.
-   Dockerized Environment: Visit http://localhost:8000/ in your web browser.

#### Running Migrations

-   Development Environment:
    python manage.py migrate
-   Dockerized Environment:
    docker-compose exec web python manage.py migrate

#### Creating a Superuser

-   Development Environment:
    python manage.py createsuperuser
-   Dockerized Environment:
    docker-compose exec web python manage.py createsuperuser

#### Accessing the PostgreSQL Database
-   Development Environment: Connect using your preferred PostgreSQL client to localhost on port 5432 with the provided credentials.
-   Dockerized Environment: Use the following command to access the PostgreSQL database:
    docker-compose exec db psql -U your_database_user -d your_database_name

### Common Commands
-   Build the containers:
    docker-compose build
-   Start the containers:
    docker-compose up
-   Stop the containers:
    docker-compose down
-   Run Django commands:
    docker-compose exec web python manage.py <command>






