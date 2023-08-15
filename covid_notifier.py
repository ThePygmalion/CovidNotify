import time
import requests
from plyer import notification

def get_covid_data():
    url = "https://api.covid19india.org/data.json"
    response = requests.get(url)
    data = response.json()
    cases_data = data['cases_time_series']
    latest_data = cases_data[-1]
    confirmed = latest_data['totalconfirmed']
    recovered = latest_data['totalrecovered']
    deaths = latest_data['totaldeceased']
    return confirmed, recovered, deaths

def display_notification(confirmed, recovered, deaths):
    title = "COVID-19 India Update"
    message = f"Confirmed: {confirmed}\nRecovered: {recovered}\nDeaths: {deaths}"
    notification.notify(
        title=title,
        message=message,
        app_name="COVID Notifier",
        timeout=10
    )

def main():
    while True:
        confirmed, recovered, deaths = get_covid_data()
        display_notification(confirmed, recovered, deaths)
        time.sleep(3600)  # Fetch data every hour

if __name__ == "__main__":
    main()
