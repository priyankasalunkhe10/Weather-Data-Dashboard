# Weather-Data-Dashboard
A Flask web application to fetch, store, and display weather data for multiple locations, using an Excel file as the database. Includes real-time weather fetching, historical tracking, and data visualization.

🔧 Features

- 🌍 Search and view current weather for any city
- ➕ Add new locations to track
- 📊 View weather history in a table
- 📈 Chart.js bar chart for latest temperatures
- ⬇️ Export data to CSV
- 💾 Excel-based data storage (no external database)

🖼️ Screenshots

Home Page->

![Screenshot_home png](https://github.com/user-attachments/assets/08221ac1-d95b-41b9-bf89-1547251235e3)

Get Weather->

![Screenshot_get_weather png](https://github.com/user-attachments/assets/f5231cc7-02ce-475c-b139-9bade06e4f1e)

Add Location->

![Screenshot_add_location png](https://github.com/user-attachments/assets/56daef49-cbbb-49b3-aa05-c42a2c09a930)

History->

![Screenshot_history png](https://github.com/user-attachments/assets/bd90d291-e0e8-4e1b-9c31-072e62a8af46)

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

