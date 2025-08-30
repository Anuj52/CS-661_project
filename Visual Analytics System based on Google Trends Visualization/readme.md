# Visual Analytics System based on Google Trends Visualization

A web-based dashboard for exploring global Google Trends data (2004–2013) interactively. The system visualizes search interest by country, year, and category using multiple chart types and a word cloud.

---

## Table of Contents

- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Setup & Usage](#setup--usage)
- [API Endpoints](#api-endpoints)
- [Customization](#customization)
- [License](#license)

---

## Features

- **World Map (Choropleth):** Visualizes search interest geographically.
- **Pie Chart:** Shows distribution of search interest by category.
- **Bar Chart:** Displays search interest by category for a selected country.
- **Line Chart:** Shows trends over time for a selected category.
- **Word Cloud:** Visualizes most common search queries.

---

## Architecture Overview

- **Backend:**  
  - Built with Flask (Python).
  - Loads and filters Google Trends data from CSV.
  - Serves chart data via REST API endpoints.
  - Generates word cloud images dynamically.

- **Frontend:**  
  - HTML/JS dashboard (see `templates/index.html`).
  - Chart rendering handled by modular JS files (`static/`).
  - Fetches data from backend and updates visualizations interactively.

---

## Project Structure

```
Visual Analytics System based on Google Trends Visualization/
│
├── server.py
├── Updated_Final_Global_Google_Trends_2004_2013_FixedYears.csv
│
├── static/
│   ├── bar-chart.js
│   ├── line-chart.js
│   ├── main.js
│   ├── map-chart.js
│   ├── pie-chart.js
│   ├── wordcloud-chart.js
│   └── data/
│       └── geo.json
│
└── templates/
    └── index.html
```

- **server.py:** Flask backend, API logic, word cloud generation.
- **static/**: JS files for each chart type, main dashboard logic, geo data for map.
- **templates/index.html:** Main dashboard HTML template.
- **Updated_Final_Global_Google_Trends_2004_2013_FixedYears.csv:** Main dataset.

---

## Setup & Usage

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository**
   ```
   git clone <your-repo-url>
   cd "Visual Analytics System based on Google Trends Visualization"
   ```

2. **Install dependencies**
   ```
   pip install flask flask-cors pandas matplotlib wordcloud
   ```

3. **Run the server**
   ```
   python server.py
   ```

4. **Open the dashboard**
   - Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## API Endpoints

- `/`  
  Returns the dashboard homepage.

- `/api/options`  
  Returns available years, countries, and categories for dropdowns.

- `/fetchdata`  
  **POST**: Accepts filters (`year`, `country`, `category`) and returns data for all charts and word cloud.

- `/geo.json`  
  Serves geo data for the map.

---

## Customization

- **Dataset:**  
  Replace `Updated_Final_Global_Google_Trends_2004_2013_FixedYears.csv` with your own data (same format).

- **Charts:**  
  Edit JS files in `static/` to change chart types, colors, or interactivity.

- **Map:**  
  Update `static/data/geo.json` for different geo boundaries.

---

## License

This project is for educational