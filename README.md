# Mini Commerce

This project aims to build a simple e-commerce application using Django Rest Framework for the backend.

## Features

- User authentication and authorization
- Product listing and details
- Order processing

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/hawkinswinja/mini-commerce.git
    ```
2. Navigate to the project directory:
    ```sh
    cd mini-commerce
    ```
3. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Apply migrations:
    ```sh
    python manage.py migrate
    ```
2. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```
3. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
