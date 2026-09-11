# Ford GoBike Trip Data Analysis

An end-to-end project that cleans and explores Ford GoBike bike-share trip data, loads it into a database, and exposes it through two different apps — an interactive web dashboard and a desktop database viewer.

## Project Structure

| File | Purpose |
|---|---|
| `eda_report.ipynb` | Cleans the raw trip data, engineers features, and runs the full exploratory data analysis |
| `gobike_processed.csv` | Cleaned dataset produced by the notebook (input to the dashboard) |
| `dashboard.py` | Interactive Plotly Dash web dashboard for exploring trips, users, and stations |
| `Gobike_app.py` | PyQt5 desktop app for browsing the star-schema PostgreSQL database |

## Pipeline Overview

```
fordgobike-tripdataFor201902.csv
        │
        ▼
  eda_report.ipynb  (clean, engineer features, analyze, export)
        │
        ├──► gobike_processed.csv ──► dashboard.py (Dash web app)
        │
        └──► loaded into PostgreSQL star schema ──► Gobike_app.py (PyQt5 viewer)
```

## 1. EDA Notebook (`eda_report.ipynb`)

Loads the raw monthly trip export and walks through a full cleaning and analysis pipeline:

- **Load & inspect** — shape, dtypes, missing values, duplicates, schema sanity check
- **Clean** — fills missing gender as `"Unknown"`, leaves missing birth year as `NaN` (flagged via `birth_year_known`), caps duration outliers with the IQR method instead of dropping them, and drops the small number of rows missing station identity
- **Feature engineering** — derives `age`, `age_group` (Young / Adult / Senior / Unknown), and `duration_min`
- **Standardization** — normalizes casing/whitespace in categorical fields
- **Encoding & scaling** — produces a separate one-hot-encoded, scaled table for downstream modeling (the human-readable columns are kept for the charts)
- **Univariate, bivariate & multivariate analysis** — trip duration distribution, user type split, gender and age breakdowns, duration vs. user type/gender/age, and combined views
- **Time-based analysis** — trips by day of week, hour of day, and weekday vs. weekend (only runs if timestamps parse correctly)
- **Correlation overview** — heatmap of numeric features
- **Statistical tests** — Welch's t-test (duration: Subscriber vs. Customer) and a chi-square test (user type vs. gender)
- **Export** — writes the cleaned dataset to `gobike_processed.csv`

### Key Findings

- **Duration is right-skewed**: most trips last 3–15 minutes; ~10% were capped as outliers.
- **User mix**: ~85% Subscribers, ~15% Customers.
- **Demographics**: riders skew Male (~70%) and are concentrated in the Young/Adult age groups.
- **User type drives duration**: Customers ride noticeably longer than Subscribers (median ~14 vs. ~7 min), and the gap holds across every age group. A Welch's t-test confirms this difference is statistically significant.
- **Age has little effect**: duration is roughly flat across age groups and shows almost no correlation with age.
- **User type vs. gender**: nearly all female riders in the sample are Subscribers, but with only 15 Customer trips total and several expected cell counts under 5, the chi-square result here is reported for completeness rather than as a firm conclusion.

> **Note:** the sample analyzed is small (n ≈ 99 trips after cleaning), so findings — especially the gender/user-type association — should be treated as preliminary.

## 2. Interactive Dashboard (`dashboard.py`)

A Plotly Dash web app built on `gobike_processed.csv`.

**Features:**
- Filters for user type, gender, and age group
- KPI cards: total trips, average duration, unique bikes used, most popular station
- Charts: trips by user type (donut), by gender, by age group, top 10 start/end stations, and a trip duration histogram
- All charts and filters update together via a single callback

**Run it:**
```bash
pip install dash pandas plotly
python dashboard.py
```
Then open the local URL Dash prints in your terminal (default `http://127.0.0.1:8050`). Make sure `gobike_processed.csv` is in the same directory, or update `DATA_PATH` at the top of the script.

## 3. Database Viewer (`Gobike_app.py`)

A PyQt5 desktop app for browsing a star-schema version of the data in PostgreSQL (`fact_trips`, `dim_station`, `dim_user`).

**Requirements:**
```bash
pip install PyQt5 psycopg2-binary
```

**Configuration:** connection settings live in the `DB_CONFIG` dict near the top of the file (`host`, `dbname`, `user`, `password`, `port`) — update these to match your local PostgreSQL setup. Consider moving the password to an environment variable rather than hardcoding it in the script.

**Built-in queries** (selectable from a dropdown):
- All trips (joined with station and user details)
- Trip count by user type (with average duration)
- Trip count by gender
- Top 10 stations by trips started
- All stations

**Run it:**
```bash
python Gobike_app.py
```

## Requirements Summary

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn dash plotly PyQt5 psycopg2-binary
