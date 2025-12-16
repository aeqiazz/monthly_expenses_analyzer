import pandas as pd

filename = "expenses_mixed_errors"
csv_file = f"test_csvs/{filename}.csv"
# csv_file = "test_csvs/test.csv"
df = pd.read_csv(csv_file)


# Check if columns match expected columns
def check_columns(csv_file, expected_columns):
    if list(df.columns) != expected_columns:
        print(f"Error: Expected columns {expected_columns}, but got {list(df.columns)}")
        return False
