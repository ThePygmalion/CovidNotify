import tkinter as tk
from tkinter import messagebox
import requests
import threading
import time

class CovidApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 India Tracker")

        self.label = tk.Label(root, text="COVID-19 Cases in India", font=("Helvetica", 18))
        self.label.pack(pady=10)

        self.data_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.data_label.pack()

        self.update_button = tk.Button(root, text="Update Data", command=self.update_data)
        self.update_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

        self.update_data()

    def get_covid_data(self):
        url = "https://api.covid19india.org/data.json"
        response = requests.get(url)
        data = response.json()
        cases_data = data['cases_time_series']
        latest_data = cases_data[-1]
        confirmed = latest_data['totalconfirmed']
        recovered = latest_data['totalrecovered']
        deaths = latest_data['totaldeceased']
        return confirmed, recovered, deaths

    def update_data(self):
        confirmed, recovered, deaths = self.get_covid_data()
        self.data_label.config(text=f"Confirmed: {confirmed}\nRecovered: {recovered}\nDeaths: {deaths}")
        self.root.after(3600000, self.update_data)  # Update data every hour

def main():
    root = tk.Tk()
    app = CovidApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
