from selenium import webdriver
from selenium.webdriver.common.by import By

from db import Appartment, Session
from utils import get_formatted_date


def get_appartment_details(a):
    title = a.find_element(By.CLASS_NAME, 'title').text
    price = a.find_element(By.CLASS_NAME, 'price').text
    currency = price[0]
    price = price[1:]
    location = a.find_element(
        By.CLASS_NAME,
        'location'
    ).find_element(
        By.TAG_NAME,
        'span'
    ).text
    date_posted = a.find_element(by=By.CLASS_NAME, value='date-posted').text
    image = a.find_element(
        By.CLASS_NAME,
        'image').find_element(
        By.TAG_NAME,
        'img').get_attribute('data-src')

    if "ago" in date_posted:
        date = get_formatted_date(date_posted)
    else:
        date = date_posted

    appartment = Appartment(
        title=title,
        currency=currency,
        price=price,
        date=date,
        location=location,
        image=image)

    return appartment


def parse_appartments():
    session = Session()
    driver = webdriver.Chrome()

    for i in range(1, 100):
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273'
        driver.get(url)
        appartments = driver.find_elements(
            by=By.CLASS_NAME, value='search-item')

        for a in appartments:
            appartment = get_appartment_details(a)
            session.add(appartment)
            session.commit()

    session.close()
    driver.quit()


if __name__ == "__main__":
    parse_appartments()
