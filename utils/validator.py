import pandas as pd

import core.loader as loader

expected_columns = ["date", "category", "amount", "description"]


def validate_csv(csv_file, expected_columns):
    try:
        loader.df

        # Check if csv is empty
        if loader.df.empty:
            print("Error: The CSV file is empty.")
            return False

        validate_date(loader.csv_file, "date", "%Y-%m-%d")

        print("CSV file is valid.")
        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_file} does not exist.")
        return False
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return False
    except Exception as e:
        print(f"An error ocured: {e}")
        return False


def validate_date(csv_file, date_column, date_format):
    loader.df

    # Attempt to convert the column to datetime using the specified format.
    # errors="coerce" will turn any invalid date strings into NaT (Not a Time)
    loader.df["date"] = pd.to_datetime(
        loader.df[date_column], format=date_format, errors="coerce"
    )
    # Check for invalid entries (NaT)
    invalid_dates = loader.df[loader.df["date"].isna() & loader.df[date_column].notna()]

    if invalid_dates.empty:
        print(f"All dates in column '{date_column}' are valid.")
    else:
        print(f"Found {len(invalid_dates)} invalid date(s) in column '{date_column}':")
        print(invalid_dates[[date_column, "date"]])


####def validate_amounts():
####    if not pd.api.types.is_numeric_dtype(loader.df["amount"]):
####        print("Error: 'amount' is not numeric")
####        return False
####    if loader.df["amount"] < 0:
####        print("Error: 'amount' must be a positive number")
####        return False
