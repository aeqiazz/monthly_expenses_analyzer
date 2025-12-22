import core.cleaner as cleaner
import core.loader as loader
import utils.validator as validator

expected_columns = ["date", "category", "amount", "description"]

cleaner.clean_csv()

print(validator.validate_csv(loader.csv_file, expected_columns))
