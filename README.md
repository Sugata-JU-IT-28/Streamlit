# Startup Funding Analysis App

A Streamlit-based data analysis app for exploring startup funding trends, startup-wise funding details, and investor-wise investment behavior using a cleaned startup funding dataset. The app provides three main modules: Overall Analysis, Startup Analysis, and Investor Analysis. [file:2][file:1]

## Features

- **Overall Analysis**
  - Displays total invested amount.
  - Shows maximum funding received by a startup.
  - Calculates average funding per startup.
  - Displays the total number of funded startups.
  - Provides month-over-month funding trend visualization with both total funding and funding count views. [file:2]

- **Startup Analysis**
  - Lets users select a startup from the sidebar.
  - Displays basic startup details such as name, industry, and city.
  - Shows the funding history table including funding round, investors, and date. [file:2]

- **Investor Analysis**
  - Lets users select an investor from the sidebar.
  - Shows the investor’s most recent investments.
  - Displays biggest investments by startup.
  - Visualizes sectors invested in.
  - Visualizes cities invested in.
  - Shows yearly investment trend. [file:2]

## Dataset

The application uses `startup_cleaned.csv`, which contains startup funding data with fields such as `date`, `startup`, `vertical`, `subvertical`, `city`, `investors`, `round`, and `amount`. [file:1]

## Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib 

## Project Structure

```bash
.
├── app-2.py
├── startup_cleaned.csv
└── README.md
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/Sugata-JU-IT-28/Streamlit.git
cd Streamlit
```

2. Install the required libraries:

```bash
pip install streamlit pandas matplotlib
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the local URL shown in the terminal, usually:

```bash
http://localhost:8501
```


## App Workflow

- The app loads the cleaned startup funding dataset.
- It preprocesses the `date` column and extracts `year` and `month`.
- Users can navigate from the sidebar to:
    - Overall Analysis
    - Startup Analysis
    - Investor Analysis 


## Example Insights You Can Explore

- Total capital invested across startups.
- Which startup received the highest funding.
- Funding patterns over time.
- Which sectors or cities attract specific investors.
- Complete funding history of any selected startup. 



