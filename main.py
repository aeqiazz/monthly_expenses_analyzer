import core.cleaner as cleaner
import core.loader as loader
import utils.validator as validator

expected_columns = ["date", "category", "amount", "description"]

loader.check_columns(loader.csv_file, expected_columns)

print(
    validator.validate_csv(
        loader.csv_file, ["date", "category", "amount", "description"]
    )
)
# print(loader.df)

# validator.validate_date(loader.csv_file, "date", "%Y-%m-%d")
print(validator.validate_date(loader.csv_file, "date", "%Y-%m-%d"))

cleaner.clean_csv()
