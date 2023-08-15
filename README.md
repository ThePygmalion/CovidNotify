# COVID-19 India Tracker App


The COVID-19 India Tracker App is a simple graphical user interface (GUI) application built using Python's `tkinter` library. It provides real-time updates on COVID-19 cases in India, displaying the total confirmed, recovered, and deceased cases. The data is fetched from the COVID-19 India API and updated periodically within the app.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [License](#license)

## Features

- Display real-time COVID-19 case statistics for India.
- Update data automatically every hour.
- Simple and intuitive graphical user interface.
- Quit button to close the application.

## Getting Started

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. Install the required dependencies by running the following command in your terminal or command prompt:

    ```bash
    pip install tk requests
    ```

3. Clone or download this repository to your local machine.

4. Open a terminal or command prompt and navigate to the directory where you've saved the repository files.

## Usage

1. Run the app by executing the following command in your terminal or command prompt:

    ```bash
    python covid_app.py
    ```

2. The app window will open, displaying the current COVID-19 case statistics for India. The data will automatically update every hour.

3. Click the "Update Data" button to manually refresh the data.

4. To quit the app, click the "Quit" button or simply close the app window.

## Customization

You can customize the app according to your preferences and requirements:

- Modify the UI layout and design using `tkinter` widgets and styling options.
- Change the data update interval (default is one hour) by modifying the `root.after` delay in the `update_data` method.
- Add additional features, such as regional case statistics, charts, or data visualization.

## Dependencies

- Python 3.x
- `tkinter` library (standard Python library for GUI)
- `requests` library (for making HTTP requests)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
