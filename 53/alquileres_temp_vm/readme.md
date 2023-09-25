# Web Scraper and Form Filler for Real Estate Listings

## Overview

This Python script utilizes both `requests` and `selenium` for web scraping and form-filling functionalities. It is specifically targeted at gathering real estate information from a predefined URL (Villa Maria, Cordoba, Argentina) and populating a web form with the scraped details.

The project incorporates well-known Python libraries such as `BeautifulSoup` for HTML parsing and `logging` for runtime information and debugging.

## Prerequisites

### Dependencies
- Python 3.x
- Selenium
- BeautifulSoup
- requests

You can install these packages using pip:
```bash
pip install selenium beautifulsoup4 requests
```

### Selenium WebDriver

Ensure that the Selenium WebDriver is installed and properly configured for use with Google Chrome.

### Configuration File

A `config.json` file is used for maintaining constants and XPath selectors. Make sure to populate this file with the appropriate configurations.

## Code Structure

- **Imports and Logging Setup**: Necessary modules and logging configurations are loaded.

- **Configuration**: Constants and other settings are fetched from an external `config.json` file for modularity.

- **WebScraper Class**: A class encompassing the Selenium WebDriver functionalities for filling out a web form.

- **Helper Functions**: Functions like `get_meli_html()` and `parse_soup()` are utility functions performing specific tasks like fetching HTML and parsing HTML, respectively.

- **Main Function**: Orchestrates the workflow including HTML fetching, parsing, data scraping, and form filling.

### Functions

- `get_meli_html()`: Fetches and saves the initial HTML for scraping.
- `parse_soup(soup: BeautifulSoup, css_class: str)`: Extracts elements based on a CSS class from HTML content parsed by BeautifulSoup.
- `WebScraper.fill_form(listing: dict)`: Fills in the web form for each listing.
- `WebScraper.close()`: Closes the Selenium WebDriver instance.
- `main()`: Executes the entire program flow.

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies.
4. Run `python script_name.py`.

## Educational Goals Achieved

1. **Modularity**: Code is separated into functions and classes, enhancing readability and maintainability.
2. **Configuration Management**: Use of an external JSON file for configurations makes it easier to adapt the code for other scraping tasks.
3. **Best Practices**: Logging, error handling, and comments have been implemented.
4. **Technical Learning**: Exposure to web scraping and web automation with `requests`, `BeautifulSoup`, and `Selenium`.

This README aims to be comprehensive and educational, shedding light on the code architecture, functionality, and educational merits, aligned with your aspirations to improve your coding skills in Python.