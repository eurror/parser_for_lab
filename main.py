from selenium import webdriver
from selenium.webdriver.common.by import By

from db import Appartment, Session
from utils import get_formatted_date

session = Session()
driver = webdriver.Chrome()
URL = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
driver.get(URL)

appartments = driver.find_elements(by=By.CLASS_NAME, value='search-item')

for a in appartments:
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
        price=price,
        currency=currency,
        location=location,
        date=date,
        image=image)
    session.add(appartment)
    session.commit()

session.close()
driver.quit()
