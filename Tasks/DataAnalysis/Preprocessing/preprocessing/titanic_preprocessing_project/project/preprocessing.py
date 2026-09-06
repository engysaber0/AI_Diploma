import os
import pandas as pd


def Read_data_file(file_path):
    if not file_path:
        print("no path given")
        return None

    if not os.path.exists(file_path):
        print("file not found:", file_path)
        return None

    if os.path.isdir(file_path):
        print("that's a folder, not a file:", file_path)
        return None

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print("couldn't read the file -", e)
        return None

    if df.empty:
        print("warning: the dataframe came back empty")

    print("data loaded, shape =", df.shape)
    return df


def Drop_unnecessary_features(df, cols_to_drop):
    if df is None:
        print("no data to work with")
        return None

    if not cols_to_drop:
        return df

    cols_found = []
    for c in cols_to_drop:
        if c in df.columns:
            cols_found.append(c)
        else:
            print(f"column '{c}' not in the data, skipping it")

    df = df.drop(columns=cols_found)
    print("dropped", cols_found)
    print("shape now:", df.shape)
    return df


def Check_data_type(df):
    if df is None:
        print("no data to check")
        return None

    result = {}
    for col in df.columns:
        result[col] = {
            "dtype": df[col].dtype,
            "unique": df[col].nunique(),
            "nulls": df[col].isnull().sum(),
        }

    report = pd.DataFrame(result)
    return report
