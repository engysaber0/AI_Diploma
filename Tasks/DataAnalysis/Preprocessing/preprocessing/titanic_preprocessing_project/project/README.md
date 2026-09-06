# Titanic Preprocessing Project

Simple preprocessing pipeline for the Titanic dataset using Python and pandas.

## What it does

- Reads the Titanic CSV file into a DataFrame, with error handling for missing/bad files
- Drops columns that aren't needed (column list comes from config, not hardcoded)
- Shows a small data-quality report (dtype, unique values, missing values per column)

## Project structure

```
project/
├── config/
│   ├── __init__.py
│   └── config.py          # data file path + columns to drop
├── data/
│   └── raw/
│       └── titanic.csv
├── preprocessing.py        # Read_data_file, Drop_unnecessary_features, Check_data_type
└── Main.py                 # runs the pipeline
```

## Requirements

- Python 3
- pandas

Install pandas if you don't have it:

```
pip install pandas
```

## How to run

```
cd project
python Main.py
```

You'll get a menu:

```
1. Drop columns (from config)
2. Check data types
3. Show current shape
4. Exit
```

Pick a number and press Enter. Repeat until you exit with 4.

## Changing the dataset

If you want to run this on a different dataset later, you don't touch
preprocessing.py at all. Just:

1. Put the new CSV in `data/raw/`
2. Update `DATA_FILE_PATH` and `COLUMNS_TO_DROP` in `config/config.py`

The functions in preprocessing.py have no idea they were built for Titanic,
they just work off whatever config gives them.
