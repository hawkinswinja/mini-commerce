# Minicommerce 

This project is a full-stack application built on Django Rest Framework for backend, React for frontend amd Postgresql for backend. Docker Compose is used to orchestrate all the services, including the backend, frontend, database, and watchtower.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setting Up the Project](#setting-up-the-project)
- [Starting the Services](#starting-the-services)
- [Stopping the Services](#stopping-the-services)
- [Useful Commands](#useful-commands)
- [Local Setup](#local-setup)
- [Contributing](#contributing)

## Overview

This repository uses **Docker Compose** to manage multiple services in a containerized environment, ensuring consistency and ease of setup. The following services are included:
- **Backend**: Handles the API and core application logic.
- **Frontend**: User interface of the application.
- **Database**: Stores application data (e.g., PostgreSQL).
- **Redis** (optional): Caching layer.

## Prerequisites

Before you begin, make sure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- setup [google auth credentials](https://console.cloud.google.com/apis/credentials)
## Setting Up the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/hawkinswinja/minicommerce.git
   cd minicommerce
   ```
2. Create a `.env` file in the root directory and configure the necessary environment variables. You can use the provided [env.template](./backend/env.template) as a reference.


## Starting the Services

To start the services, run the following command:
```bash
   docker compose up
```
This will start all the services defined in the [docker compose file](./docker-compose.yaml) file.

## Stopping the Services

To stop the services, run:
```bash
docker compose down
```
This will stop and remove all the containers.

## Useful Commands

- To rebuild the services:
  ```bash
  docker compose up --build
  ```

- To view the logs of a specific service:
  ```bash
  docker compose logs <service_name>
  ```

- To run a command in a running container:
  ```bash
  docker compose exec <service_name> <command>
  ```

## Local Setup

For local development without Docker, follow these steps:

1. Set up the backend:
    - Navigate to the backend directory:
      ```bash
      cd backend
      ```
    - Follow the instructions in the [backend README](./backend/README.md) to set up and start the backend services.

2. Set up the frontend:
    - Navigate to the frontend directory:
      ```bash
      cd frontend
      ```
    - Follow the instructions in the [frontend README](./frontend/README.md) to set up and start the backend services.``

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add your message here"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

Thank you for contributing!

