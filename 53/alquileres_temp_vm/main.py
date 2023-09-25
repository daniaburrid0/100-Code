import os
import logging
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize logging for debugging and runtime information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration from an external JSON file for modularity and easier adjustments
with open("config.json", "r") as file:
    CONFIG = json.load(file)

# Retrieve configuration details from the loaded JSON
URL_ALQUILERES = CONFIG["URL_ALQUILERES"]
URL_FORM = CONFIG["URL_FORM"]
HEADERS = CONFIG["HEADERS"]
XPATHS = CONFIG["XPATHS"]
CSS_CLASSES = CONFIG["CSS_CLASSES"]

# Class for Selenium Web Scraper functionalities
class WebScraper:
    def __init__(self):
        # Initialize Selenium WebDriver
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    # Function to fill in the web form using Selenium
    def fill_form(self, listing: dict) -> None:
        self.driver.get(URL_FORM)
        try:
            # Fill in the form fields
            direction = self.wait.until(EC.element_to_be_clickable((By.XPATH, XPATHS["DIRECTION_FORM"])))
            direction.send_keys(listing['location'])
            precio = self.driver.find_element(By.XPATH, XPATHS["PRECIO_FORM"])
            precio.send_keys(listing['price'])
            link = self.driver.find_element(By.XPATH, XPATHS["LINK_FORM"])
            link.send_keys(listing['link'])
            submit = self.driver.find_element(By.XPATH, XPATHS["SUBMIT_FORM"])
            submit.click()
        except Exception as e:
            logging.error(f"An error occurred while filling the form: {e}")

    # Function to close the Selenium WebDriver instance
    def close(self):
        self.driver.close()

# Function to fetch and save the initial HTML page for scraping
def get_meli_html() -> None:
    files = os.listdir()
    create_file = input('Crear archivo meli.html? (y/n): ')

    # Check if HTML file exists, else fetch and save it
    if 'meli.html' not in files and create_file.lower() == 'y':
        response = requests.get(URL_ALQUILERES, headers=HEADERS)
        if response.status_code == 200:
            with open('meli.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
                logging.info(f"HTML file created successfully.")
        else:
            logging.error(f"Failed to retrieve HTML with status code: {response.status_code}")

# Function to extract elements from the HTML using BeautifulSoup
def parse_soup(soup: BeautifulSoup, css_class: str) -> list:
    elements = soup.find_all(class_=css_class)
    return elements

# Main function to execute the entire scraping and form-filling workflow
def main() -> None:
    get_meli_html()

    # Read HTML file and initialize BeautifulSoup parser
    with open('meli.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Scrape necessary data
    locations = [location.text for location in parse_soup(soup, CSS_CLASSES["CLASS_LOCATION"])]
    prices = [float(price.text.replace('.', '')) for price in parse_soup(soup, CSS_CLASSES["CLASS_PRICE"])]
    links = [link.find('a').get('href') for link in parse_soup(soup, CSS_CLASSES["CLASS_IMG_WRAPPER"])]

    # Prepare data for form-filling
    listings = [
        {
            'location': location,
            'price': price,
            'link': link
        } 
        for location, price, link in zip(locations, prices, links)
    ]

    # Initialize and use WebScraper class to fill in the form for each listing
    scraper = WebScraper()
    for listing in listings:
        scraper.fill_form(listing)
    scraper.close()

if __name__ == '__main__':
    main()
