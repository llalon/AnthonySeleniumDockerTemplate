import argparse

from selenium.webdriver import ChromeOptions
from seleniumrequests import Chrome


def main():
    print("Hello world!")

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    driver = get_driver()
    driver.get("https://www.google.com")
    print(driver.find_element_by_xpath("/html/body").text)
    driver.close()

def get_driver():
    chrome_options = ChromeOptions()

    chrome_options.add_argument("headless")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("disable-dev-shm-usage")
    chrome_options.add_argument("disable-gpu")

    driver = Chrome(options=chrome_options)

    return driver
        
