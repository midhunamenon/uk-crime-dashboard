# UK Police Force Crime Dashboard
This interactive dashboard visualises UK crime data from May 2024 to April 2025 using Plotly. The chart allows filtering by month and visualises crime types in each month
----
## Features
- Month-wise dropdown filtering
- Bar chart of crime types per month
- Modular code structure with reusable components
- Data cleaned and merged from 12 months of CSVs
----
## Folder Structure
<pre>
<code>```plaintext
policeforice-crime-dashboard/
├── assets/             # Main Dash app
    ├── style.css
├── components/         # Dash layout and charts
    ├── charts.py
    ├── filters.py
    ├── layout.py
    ├── maps.py
├── data/
│   ├── raw/            # Original monthly CSVs
│   └── processed/      # Combined cleaned data (not committed)
├── utils/              # Helper functions
    ├── crime_analysis.py
│   └── data_processing.py
├── venv/               # Virtual environment (ignored)
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
```</code>
</pre>

## Setup Instructions

### 1. Clone the repo
<pre>
```bash
git clone https://github.com/midhunamenon/uk-crime-dashboard.git
cd policeforice-crime-dashboard
</pre>

### 2. Create a virtual environment
<pre>
```bash
python3 -m venv venv
source venv/bin/activate
</pre>

### 3. Install required packages
<pre>
```bash
pip install -r requirements.txt
</pre>

### 4. Prepare the data
Place the 12 monthly CSV files into data/raw/, then run:
<pre>
```bash
python3 utils/data_processing.py  
</pre>
This will generate the combined dataset at data/processed/Combined_crime_data.csv. Note, this large file is ignored from Git and is generated locally

### 5. Running the App
<pre>
```bash
python3 app.py
</pre>

Then open the browser and navigate to: http://127.0.0.1:8050

## Development Approach
- Developed using feature branches for major dashboard components
- Committed in small, meaningful commits using Git
- Virtual environment used for clean dependency management
- .gitignore used to avoid pushing large datasets and system files

## Assessment criteria addressed
- Dashboard interactivity via dropdown
- Monthly data aggregation
- Cleaned and merged dataset
- Git workflow with feature branches
- Virtual environment setup and documentation

## Contact
Project by Midhuna Menon
GitHub repo: https://github.com/midhunamenon/uk-crime-dashboard



