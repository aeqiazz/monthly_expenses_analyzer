import pandas as pd


def validate_csv(csv_file, expected_columns):
    try:
        df = pd.read_csv(csv_file)

        # Check if csv is empty
        if df.empty:
            print("Error: The CSV file is empty.")
            return False

        # Check data types (example: ensuring 'amount' is numeric)
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            print("Error: 'amount' is not numeric")
            return False
        if df["amount"] < 0:
            print("Error: 'amount' must be a positive number")
            return False

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
    df = pd.read_csv(csv_file)

    # Attempt to convert the column to datetime using the specified format.
    # errors="coerce" will turn any invalid date strings into NaT (Not a Time)
    df["Valid_Date"] = pd.to_datetime(
        df[date_column], format=date_format, errors="coerce"
    )
    # Check for invalid entries (NaT)
    invalid_dates = df[df["Valid_Date"].isna() & df[date_column].notna()]

    if invalid_dates.empty:
        print(f"All dates in column '{date_column}' are valid.")
    else:
        print(f"Found {len(invalid_dates)} invalid date(s) in column '{date_column}':")
        print(invalid_dates[[date_column, "Valid_Date"]])
