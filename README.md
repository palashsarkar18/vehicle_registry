# Vehicle Registry Project

## Introduction

This project is a simple vehicle registry application built using Django and PostgreSQL. It provides functionality to upload vehicle data, search for vehicles, and display the data in a tabular format. The project includes basic unit and integration tests and uses vanilla JavaScript for the user interface.

## Scope of this Project

- **Unit and Integration Tests:** The project includes basic unit and integration tests using pytest.
- **User Interface:** The UI is built using vanilla JavaScript and HTML.
- **Functionality:** 
  - Upload vehicle data via JSON files.
  - Display vehicle data in a table with alternating row colors.
  - Search for vehicles based on make, model, year, and other attributes.

## How to Run the Project

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Steps to Run the Project

1. **Download the Repository and unzip it**

   ```
   cd vehicle_registry
   ```

2. **Set Up Environment Variables**
    Create a .env file in the project root with the following content:

    ```
    SECRET_KEY=your_secret_key
    DEBUG=on
    SECRET_KEY=secret-key
    DATABASE_NAME=db_name
    DATABASE_USER=db_user
    DATABASE_PASSWORD=db_password
    DATABASE_HOST=host
    DATABASE_PORT=port
    ```

3. **Build and Start the Docker Containers**
   ```
   docker-compose up --build
   ```

4. **Access the Application**
    Open your web browser and go to http://localhost:8000/. You should see the vehicle registry application.

5. **Run Tests**
    To run the tests, use the following command:
    ```
    docker-compose run test
    ```

## Additional Information

* **Database Initialization**: The `wait-for-it.sh` script ensures that the PostgreSQL service is up and running before starting the Django application.
* **Automatic Migrations**: The `entrypoint.sh` script handles database migrations before starting the Django server.

This setup ensures that the application is ready to use and that the tests can be run in an isolated environment.