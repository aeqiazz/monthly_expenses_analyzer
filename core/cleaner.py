# ** TODO
# [ ] Remove spaces on categories
# [ ] Check if all amounts are positive
#       And if not, check if all amounts are negative, if all, then make them positive
#
import numpy as np
import pandas as pd

import core.loader as loader
import utils.validator as validator


def clean_csv():
    try:
        loader.df
        print(
            f"Successfully read data from {loader.csv_file}. Shape: {loader.df.shape}"
        )

        loader.df = loader.df.dropna()

        # Not working right. It doesn't need to write csv if there's an error
        if not loader.check_columns(loader.csv_file, validator.expected_columns):
            print("Error: CSV columns do not match expected structure.")
            return
        else:
            print("CSV columns match expected structure.")
            loader.df.to_csv(f"test_csvs/clean_{loader.filename}.csv", index=False)
            print(f"Successfully wrote data to 'clean_{loader.filename}.csv'")

        # Trying to get rid off whitespaces (i gave up gonna do this later)
        loader.df["category"] = (
            loader.df["category"].str.strip().replace(r"\s+", " ", regex=True)
        )

        for col in loader.df.columns:
            if loader.df[col].dtype == "category":
                loader.df[col] = loader.df[col].str.strip()

    except FileNotFoundError:
        print(f"Error: The file {loader.csv_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
