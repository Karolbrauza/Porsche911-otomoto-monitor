# Porsche 911 Offers Monitor

## Project Description and Purpose

This project is a web scraping script designed to monitor available offers of Porsche 911 cars on the Polish car marketplace otomoto.pl. The script extracts data from the website, stores it in a CSV file, and runs periodically to update the data. Additionally, the project includes data analysis and visualization tools to identify trends and patterns in the offers, as well as a notification system to alert users when new listings are available.

## Setup and Run Instructions

1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the scraper script to fetch and store data:
   ```
   python scraper.py
   ```

4. Run the data analysis script to analyze and visualize the data:
   ```
   python analyze_data.py
   ```

5. Run the notification system script to monitor new listings and send notifications:
   ```
   python notification_system.py
   ```

## Usage Instructions and Examples

### Web Scraping Script

The web scraping script (`scraper.py`) fetches HTML content from otomoto.pl, parses it to extract Porsche 911 offers, and stores the data in a CSV file. The script runs periodically to update the data.

Example usage:
```
python scraper.py
```

### Data Analysis and Visualization

The data analysis script (`analyze_data.py`) loads the data from the CSV file, analyzes it to identify trends and patterns, and creates visualizations using Matplotlib and Plotly. The script also creates interactive dashboards using Dash.

Example usage:
```
python analyze_data.py
```

### Notification System

The notification system script (`notification_system.py`) monitors otomoto.pl for new Porsche 911 listings and sends email or SMS notifications to users based on their preferences.

Example usage:
```
python notification_system.py
```
