# Weather-Data-Dashboard
A Flask web application to fetch, store, and display weather data for multiple locations, using an Excel file as the database. Includes real-time weather fetching, historical tracking, and data visualization.

🔧 Features

- 🌍 Search and view current weather for any city
- ➕ Add new locations to track
- 📊 View weather history in a table
- 📈 Chart.js bar chart for latest temperatures
- ⬇️ Export data to CSV
- 💾 Excel-based data storage (no external database)

📁 Project Structure

weather-Data-Dashboard/
│
├── app.py 
├── requirements.txt 
├── README.md
│
├── templates/
│ ├── index.html 
│ ├── add_location.html 
│ └── history.html 
│
├── Data/
│ └── Data.xlsx
│
└── static/
└── style.css 

