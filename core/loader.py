import pandas as pd

# filename = "expenses_mixed_errors"
filename = "invalid_structure"
csv_file = f"test_csvs/{filename}.csv"
# csv_file = "test_csvs/test.csv"
df = pd.read_csv(csv_file)


# Check if columns match expected columns
def check_columns(csv_file, expected_columns):
    try:
        df = pd.read_csv(csv_file)

        if list(df.columns) != expected_columns:
            print(
                f"Error: Expected columns {expected_columns}, but got {list(df.columns)}"
            )
            return False

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_file} does not exist.")
        return False
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
