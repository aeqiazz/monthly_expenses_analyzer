# ** TODO
# [ ] Remove spaces on categories
# [ ] Check if all amounts are positive
#       And if not, check if all amounts are negative, if all, then make them positive
#

import core.loader as loader

# import utils.validator as validator

# validator.validate_csv(loader.csv_file, ["date", "category", "amount", "description"])


# validator.validate_date(loader.csv_file, "date", "%Y-%m-%d")
def clean_csv():
    try:
        loader.df
        print(
            f"Successfully read data from {loader.csv_file}. Shape: {loader.df.shape}"
        )

        loader.df = loader.df.dropna()

        loader.df.to_csv(f"test_csvs/clean_{loader.filename}.csv", index=False)
        print(f"Successfully wrote data to 'clean_{loader.filename}.csv'")

    except FileNotFoundError:
        print(f"Error: The file {loader.csv_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
