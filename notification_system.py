import requests
import schedule
import time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

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

def monitor_new_listings(url, existing_offers):
    html_content = fetch_html(url)
    if html_content:
        new_offers = parse_html(html_content)
        for offer in new_offers:
            if offer not in existing_offers:
                send_notifications(offer)
        return new_offers
    return existing_offers

def send_email_notification(offer, user_email):
    message = Mail(
        from_email='your_email@example.com',
        to_emails=user_email,
        subject='New Porsche 911 Listing',
        html_content=f"New listing: {offer['title']} - {offer['price']} - {offer['location']}"
    )
    try:
        sg = SendGridAPIClient('your_sendgrid_api_key')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

def send_sms_notification(offer, user_phone):
    client = Client('your_twilio_account_sid', 'your_twilio_auth_token')
    message = client.messages.create(
        body=f"New listing: {offer['title']} - {offer['price']} - {offer['location']}",
        from_='+1234567890',
        to=user_phone
    )
    print(message.sid)

def send_notifications(offer):
    user_preferences = get_user_preferences()
    for user in user_preferences:
        if user['notification_type'] == 'email':
            send_email_notification(offer, user['contact'])
        elif user['notification_type'] == 'sms':
            send_sms_notification(offer, user['contact'])

def get_user_preferences():
    # This function should return a list of user preferences
    # Example:
    return [
        {'notification_type': 'email', 'contact': 'user1@example.com'},
        {'notification_type': 'sms', 'contact': '+1234567890'}
    ]

def job():
    url = 'https://www.otomoto.pl/osobowe/porsche/911'
    existing_offers = []
    existing_offers = monitor_new_listings(url, existing_offers)

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
