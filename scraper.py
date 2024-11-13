import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    offers = []
    for offer in soup.find_all('div', class_='offer-item'):
        title = offer.find('h2', class_='offer-title').text.strip()
        price = offer.find('span', class_='offer-price').text.strip()
        location = offer.find('span', class_='offer-location').text.strip()
        offers.append({'title': title, 'price': price, 'location': location})
    return offers

def store_data(data, filename='porsche_911_offers.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def job():
    url = 'https://www.otomoto.pl/osobowe/porsche/911'
    html_content = fetch_html(url)
    if html_content:
        offers = parse_html(html_content)
        store_data(offers)

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
