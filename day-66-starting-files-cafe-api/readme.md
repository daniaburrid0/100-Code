# Cafe Management API

## Project Description
This project is a Python application that utilizes Flask and SQLAlchemy to effectively manage cafes. It provides a variety of endpoints for operations like retrieving a random cafe, fetching a list of all cafes, searching for cafes based on location, adding new cafes, updating cafe coffee prices, and reporting cafes as closed.

## Installation

1. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Start the Flask Server**
    ```
    python main.py
    ```

2. **Accessing the API**
    - Open a web browser and navigate to `http://localhost:5000/` to access the homepage.

3. **API Endpoints**
    - `GET /random`: Fetches a random cafe from the database.
    - `GET /all`: Retrieves all cafes in the database, ordered by name.
    - `GET /search?loc={location}`: Searches for cafes in the database based on location.
    - `POST /add`: Adds a new cafe entry into the database.
    - `PATCH /update-price/{cafe_id}?new_price={new_price}`: Updates the coffee price for a specific cafe.
    - `DELETE /report-closed/{cafe_id}?api_key={api_key}`: Reports a cafe as closed and deletes its record from the database.

## API Documentation
The comprehensive API documentation can be accessed directly from the home page of the application. It provides a structured and detailed exposition of each API endpoint for a thorough understanding of the system's functionality.
