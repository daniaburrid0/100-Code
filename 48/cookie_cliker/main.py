from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import logging
from selenium.common.exceptions import NoSuchElementException

# Initialize logger
logging.basicConfig(level=logging.INFO)

# Constants
URL = 'https://orteil.dashnet.org/experiments/cookie/'
MONEY_ID = 'money'
COOKIE_ID = 'cookie'
COOKIE_PER_SEC_ID = 'cps'

ITEMS = {
    "TimeMachine": {"id": "buyTime machine", "xpath": '//*[@id="buyTime machine"]/b'},
    "Portal": {"id": "buyPortal", "xpath": '//*[@id="buyPortal"]/b'},
    "Lab": {"id": "buyAlchemy lab", "xpath": '//*[@id="buyAlchemy lab"]/b'},
    "Shipment": {"id": "buyShipment", "xpath": '//*[@id="buyShipment"]/b'},
    "Mine": {"id": "buyMine", "xpath": '//*[@id="buyMine"]/b'},
    "Factory": {"id": "buyFactory", "xpath": '//*[@id="buyFactory"]/b'},
    "Grandma": {"id": "buyGrandma", "xpath": '//*[@id="buyGrandma"]/b'},
    "Cursor": {"id": "buyCursor", "xpath": '//*[@id="buyCursor"]/b'}
}

def get_money_from_text(text: str) -> float:
    # Using regex for string manipulation
    money_str = re.findall(r'-([\d, ]+)', text)[0]
    return float(money_str.replace(',', '').replace(' ', ''))

def get_element(driver: webdriver.Chrome, by: str, value: str):
    try:
        return driver.find_element(by, value)
    except NoSuchElementException:
        logging.warning(f"Element not found: {value}")
        return None

def get_money(driver: webdriver.Chrome) -> float:
    money = get_element(driver, By.ID, MONEY_ID)
    if money:
        return float(money.text.replace(',', '').replace(' ', ''))
    return 0.0

def get_cookie_per_sec(driver: webdriver.Chrome) -> float:
    cookie_per_sec = get_element(driver, By.ID, COOKIE_PER_SEC_ID)
    return cookie_per_sec.text if cookie_per_sec else 0.0

def get_cost(driver: webdriver.Chrome, xpath: str) -> float:
    cost = get_element(driver, By.XPATH, xpath)
    return get_money_from_text(cost.text) if cost else 0.0

def buy_item(driver: webdriver.Chrome, item_id: str) -> None:
    item = get_element(driver, By.ID, item_id)
    if item:
        item.click()

def buy(driver: webdriver.Chrome) -> None:
    money = get_money(driver)
    for item_name, item_info in ITEMS.items():
        cost = get_cost(driver, item_info["xpath"])
        if money >= cost:
            buy_item(driver, item_info["id"])
            break

def main() -> None:
    with webdriver.Chrome() as driver:
        driver.get(URL)
        cookie = get_element(driver, By.ID, COOKIE_ID)
        
        timeout = time.time() + 5
        finish_time = time.time() + 60*5

        while time.time() < finish_time:
            if time.time() > timeout:
                timeout = time.time() + 5
                buy(driver)
            if cookie:
                cookie.click()
        
        logging.info("5 minutes passed")
        logging.info(get_cookie_per_sec(driver))
        input("Press Enter to close the window...")

if __name__ == "__main__":
    main()
